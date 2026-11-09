"""Regression tests for the WS2 data-loss and correctness fixes (docs/development/RELEASE_1_0_PLAN.md)."""
import json
from uuid import UUID
from xml.etree.ElementTree import ParseError

import cimprofiles.cim17.cimhub_2023 as cim
import pytest

from cimgraph.core import get_cim_profile
from cimgraph.databases import JSONLDFile, XMLFile
from cimgraph.databases.sparql_endpoint import SPARQLEndpointConnection
from cimgraph.models import DistributedArea, FeederModel

NS = 'http://iec.ch/TC57/CIM100#'
RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
LINE_ID = '5b3b9c4e-0d5a-4a43-9a3c-1f0c3d7e8a01'
TERMINAL_ID = '5b3b9c4e-0d5a-4a43-9a3c-1f0c3d7e8a02'


@pytest.fixture(autouse=True)
def profile(monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    monkeypatch.setenv('CIMG_NAMESPACE', NS)
    get_cim_profile.cache_clear()
    yield
    get_cim_profile.cache_clear()


def _network() -> FeederModel:
    return FeederModel(connection=None, container=cim.Feeder(name='fdr'), distributed=False)


def _write_xml(path, body: str) -> str:
    path.write_text(f'<?xml version="1.0" encoding="utf-8"?>\n'
                    f'<rdf:RDF xmlns:cim="{NS}" xmlns:rdf="{RDF}">\n{body}</rdf:RDF>\n')
    return str(path)


def _write_json_ld(path, nodes: list[dict]) -> str:
    path.write_text(json.dumps({'@context': {'cim': NS, 'xsd': 'http://www.w3.org/2001/XMLSchema#'},
                                '@graph': nodes}))
    return str(path)


class _RecordingEndpoint(SPARQLEndpointConnection):
    """A SPARQL endpoint that records its queries and returns no results."""

    def __init__(self):
        super().__init__()
        self.queries = []

    def _setup_connection(self):
        self.connection_obj = object()

    def _execute_raw_query(self, query_message):
        self.queries.append(query_message)
        return {'results': {'bindings': []}}

    def _parse_result_field(self, result, field_name):
        return result.get(field_name)

    def _update_raw(self, update_message):
        raise NotImplementedError


# 2.1 GraphDB updates

def test_graphdb_update_is_sent_to_the_statements_endpoint(monkeypatch):
    pytest.importorskip('SPARQLWrapper')
    import cimgraph.databases.graphdb.graphdb as graphdb_module
    sent = []

    class FakeSPARQLWrapper:
        def __init__(self, url):
            self.url = url

        def setQuery(self, query):
            self.query_text = query

        def setMethod(self, method):
            pass

        def setReturnFormat(self, return_format):
            pass

        def query(self):
            sent.append((self.url, self.query_text))
            return 'ok'

    monkeypatch.setattr(graphdb_module, 'SPARQLWrapper', FakeSPARQLWrapper)
    monkeypatch.setenv('CIMG_URL', 'http://localhost:7200/repositories/cim')
    connection = graphdb_module.GraphDBConnection()

    connection.update('INSERT DATA { }')

    assert sent == [('http://localhost:7200/repositories/cim/statements', 'INSERT DATA { }')]


# 2.2 get_all_edges batches

def test_get_all_edges_runs_every_batch_once_in_parallel():
    import threading
    both_running = threading.Barrier(2, timeout=5)

    class OverlappingEndpoint(_RecordingEndpoint):
        def _execute_raw_query(self, query_message):
            if len(self.queries) < 2:
                self.queries.append(query_message)
                both_running.wait()  # raises BrokenBarrierError unless two batches overlap
                return {'results': {'bindings': []}}
            return super()._execute_raw_query(query_message)

    connection = OverlappingEndpoint()
    lines = [cim.ACLineSegment(name=f'line {index}') for index in range(250)]
    graph = {cim.ACLineSegment: {line.identifier: line for line in lines}}

    connection.get_all_edges(graph, cim.ACLineSegment)

    assert len(connection.queries) == 3
    for line in lines:
        assert sum(line.uri() in query for query in connection.queries) == 1


# 2.3 and 2.15 DistributedArea

def test_topology_message_keeps_unaddressable_equipment():
    feeder = cim.Feeder(name='fdr')
    breaker, line = cim.Breaker(name='brk'), cim.ACLineSegment(name='line')
    area = DistributedArea(container=feeder, connection=_RecordingEndpoint())

    area.build_from_topo_message({
        '@id': feeder.uri(), '@type': 'Feeder',
        'AddressableEquipment': [{'@id': breaker.uri(), '@type': 'Breaker'}],
        'UnaddressableEquipment': [{'@id': line.uri(), '@type': 'ACLineSegment'}],
        'Measurements': [],
    })

    assert area.graph[cim.ACLineSegment][line.identifier].EquipmentContainer is feeder
    assert area.graph[cim.Breaker][breaker.identifier].EquipmentContainer is feeder
    assert area.incrementals == {'forwardDifferences': {}, 'reverseDifferences': {}}


# 2.4 modify validates

def test_modify_validates_and_converts_values():
    network = _network()
    line = network.create(cim.ACLineSegment, name='line')
    terminal = network.create(cim.Terminal, name='t1')

    with pytest.raises(TypeError):
        network.modify(line, 'length', 'not-a-number')
    with pytest.raises(TypeError):
        network.modify(line, 'name', 5)

    network.modify(line, 'length', '12.5')
    assert line.length == 12.5
    network.modify(line, 'length', cim.Length(1, 'km'))
    assert line.length.to('m') == 1000
    network.modify(terminal, 'ConductingEquipment', line)  # a subclass of ConductingEquipment
    network.modify(line, 'description', None)


# 2.6 incremental builder

def test_incrementals_record_references_and_unit_values(tmp_path):
    from cimgraph.models.incremental_builder import read_incremental_xml
    network = _network()
    line = network.create(cim.ACLineSegment, name='line')
    terminal = network.create(cim.Terminal, name='t1')

    network.modify(terminal, 'ConductingEquipment', line)  # the old value is None
    network.modify(line, 'length', cim.Length(10, 'm'))  # an unhashable value
    path = str(tmp_path / 'changes.xml')
    network.write_all_incrementals(path)

    reverse = network.incrementals['reverseDifferences']
    assert network.incrementals['forwardDifferences'][cim.Terminal][terminal.uri()][
        'ConductingEquipment'] == line.uri()
    assert reverse[cim.Terminal][terminal.uri()]['ConductingEquipment'] is None
    assert read_incremental_xml(path)['forwardDifferences'][line.uri()][
        'Conductor.length'] == '10.0'


# 2.7 file parsers fail loudly

def test_xml_file_errors_raise(tmp_path):
    with pytest.raises(FileNotFoundError):
        XMLFile(filename=str(tmp_path / 'missing.xml'))
    malformed = tmp_path / 'malformed.xml'
    malformed.write_text('<rdf:RDF><unclosed>')
    with pytest.raises(ParseError):
        XMLFile(filename=str(malformed))


def test_json_ld_file_errors_raise(tmp_path):
    with pytest.raises(FileNotFoundError):
        JSONLDFile(filename=str(tmp_path / 'missing.jsonld'))
    malformed = tmp_path / 'malformed.jsonld'
    malformed.write_text('{"@graph": [')
    with pytest.raises(json.JSONDecodeError):
        JSONLDFile(filename=str(malformed))


# 2.8 rdf:about="#_..." references

def test_xml_references_resolve_in_any_identifier_style(tmp_path):
    path = _write_xml(tmp_path / 'styles.xml', f'''
<cim:ACLineSegment rdf:ID="_{LINE_ID.upper()}"><cim:IdentifiedObject.name>uuid line</cim:IdentifiedObject.name></cim:ACLineSegment>
<cim:Terminal rdf:about="#_{TERMINAL_ID}"><cim:Terminal.ConductingEquipment rdf:resource="urn:uuid:{LINE_ID}"/></cim:Terminal>
<cim:ACLineSegment rdf:ID="_LINE_1"><cim:IdentifiedObject.name>legacy line</cim:IdentifiedObject.name></cim:ACLineSegment>
<cim:Terminal rdf:about="#_T_1"><cim:Terminal.ConductingEquipment rdf:resource="#_LINE_1"/></cim:Terminal>
''')
    graph = XMLFile(filename=path).create_new_graph(container=None)

    terminals = {terminal.ConductingEquipment.name: terminal
                 for terminal in graph[cim.Terminal].values()}
    assert set(terminals) == {'uuid line', 'legacy line'}
    for terminal in terminals.values():
        assert terminal.ConductingEquipment.Terminals == [terminal]


# 2.9 and 2.10 JSON-LD values and file lists

def test_json_ld_round_trips_names_timestamps_and_enums(tmp_path):
    from cimgraph.utils import write_json_ld
    network = _network()
    line = network.create(cim.ACLineSegment, name='Line 1: 12.47kV',
                          description='2024-05-01T12:30:00.5Z')
    network.create(cim.ACLineSegmentPhase, name='phase', ACLineSegment=line,
                   phase=cim.SinglePhaseKind.A)
    path = str(tmp_path / 'model.jsonld')
    write_json_ld(network, path)

    graph = JSONLDFile(filename=path).create_new_graph(container=None)

    read_line = graph[cim.ACLineSegment][line.identifier]
    assert read_line.name == 'Line 1: 12.47kV'
    assert read_line.description == '2024-05-01T12:30:00.5Z'
    assert read_line.ACLineSegmentPhases[0].phase is cim.SinglePhaseKind.A


def test_json_ld_typed_literals(tmp_path, monkeypatch):
    monkeypatch.setenv('CIMG_USE_UNITS', 'true')
    path = _write_json_ld(tmp_path / 'typed.jsonld', [
        {'@id': f'urn:uuid:{LINE_ID}', '@type': 'cim:ACLineSegment',
         'cim:Conductor.length': {'@value': '2.5', '@type': 'cim:Length.km'},
         'cim:ACLineSegment.r': {'@value': 0.5, '@type': 'xsd:float'}},
    ])

    line = next(iter(JSONLDFile(filename=path).create_new_graph(container=None)[cim.ACLineSegment].values()))

    assert line.length.to('m') == 2500
    assert float(line.r) == 0.5


def test_json_ld_reads_a_list_of_files(tmp_path):
    lines = _write_json_ld(tmp_path / 'lines.jsonld', [
        {'@id': f'urn:uuid:{LINE_ID}', '@type': 'cim:ACLineSegment'}])
    terminals = _write_json_ld(tmp_path / 'terminals.jsonld', [
        {'@id': f'urn:uuid:{TERMINAL_ID}', '@type': 'cim:Terminal',
         'cim:Terminal.ConductingEquipment': {'@id': f'urn:uuid:{LINE_ID}'}}])

    graph = JSONLDFile(filename=[lines, terminals]).create_new_graph(container=None)

    terminal = next(iter(graph[cim.Terminal].values()))
    assert terminal.ConductingEquipment.Terminals == [terminal]


# 2.15 GraphModel small bugs

def test_from_incremental_rejects_other_file_types():
    with pytest.raises(ValueError, match='.xml'):
        _network().from_incremental('changes.json')


def test_find_by_attribute_matches_whole_values():
    network = _network()
    line_1 = network.create(cim.ACLineSegment, name='L1')
    network.create(cim.ACLineSegment, name='L10')

    assert network.find_by_attribute(cim.ACLineSegment, 'name', 'L1') == [line_1]


def test_first_and_next_iterate_and_end_with_none():
    network = _network()
    assert network.first(cim.Breaker) is None
    lines = sorted((network.create(cim.ACLineSegment, name=name) for name in ('a', 'b', 'c')),
                   key=lambda line: line.uri())

    assert network.next(cim.ACLineSegment) is lines[0]  # next() without first() starts over
    network.delete(lines[1])
    assert network.next(cim.ACLineSegment) is lines[2]  # the deleted object is skipped
    assert network.next(cim.ACLineSegment) is None
    assert network.next(cim.ACLineSegment) is lines[0]  # after None, next() starts over
    assert network.first(cim.ACLineSegment) is lines[0]


def test_model_internal_state_is_not_a_constructor_argument():
    with pytest.raises(TypeError):
        FeederModel(connection=None, container=cim.Feeder(name='fdr'), _class_iter={})
    assert '_mrid_index' not in repr(_network())


# 2.16 inverse associations

def test_create_modify_and_delete_keep_inverse_associations():
    network = _network()
    line_1 = network.create(cim.ACLineSegment, name='line 1')
    line_2 = network.create(cim.ACLineSegment, name='line 2')

    terminal = network.create(cim.Terminal, name='t1', ConductingEquipment=line_1)
    assert line_1.Terminals == [terminal]

    network.modify(terminal, 'ConductingEquipment', line_2)
    assert line_1.Terminals == [] and line_2.Terminals == [terminal]

    line_3 = network.create(cim.ACLineSegment, name='line 3', Terminals=[terminal])
    assert terminal.ConductingEquipment is line_3 and line_2.Terminals == []

    network.delete(terminal)
    assert line_3.Terminals == []
    assert terminal.identifier not in network.graph[cim.Terminal]


# Issue #159: get_all_attributes writes associations as references

def _edge_binding(identifier, attribute, edge_id, edge_class, value=None):
    return {'identifier': identifier, 'attribute': attribute, 'value': value or edge_id,
            'edge': json.dumps({'@id': edge_id, '@type': edge_class})}


def test_get_all_attributes_sets_references_without_adding_objects():
    from cimprofiles.identity import read_identifier

    from cimgraph.core.serialization import object_to_xml
    connection = _RecordingEndpoint()
    location = cim.Location(name='loc')
    line = cim.ACLineSegment(name='line')
    terminal = cim.Terminal(name='t1')
    graph = {cim.ACLineSegment: {line.identifier: line}, cim.Location: {location.identifier: location}}
    output = {'results': {'bindings': [
        _edge_binding(line.uri(), 'ConductingEquipment.BaseVoltage', LINE_ID.upper(), 'BaseVoltage'),
        _edge_binding(line.uri(), 'PowerSystemResource.Location', location.uri(), 'Location'),
        _edge_binding(line.uri(), 'ConductingEquipment.Terminals', terminal.uri(), 'Terminal'),
        _edge_binding(line.uri(), 'ACLineSegment.PerLengthImpedance', '_IMP_1', 'PerLengthPhaseImpedance'),
    ]}}

    connection.edge_query_parser(output, graph, cim.ACLineSegment, expand_graph=False)

    assert set(graph) == {cim.ACLineSegment, cim.Location}
    assert line.BaseVoltage == LINE_ID.upper()
    assert line.Location is location  # already in the graph, so linked
    assert line.Terminals == [terminal.uri()]
    assert line.PerLengthImpedance == str(read_identifier('PerLengthPhaseImpedance', '_IMP_1'))
    xml = object_to_xml(line)
    assert f'<cim:ConductingEquipment.BaseVoltage rdf:resource="urn:uuid:{LINE_ID.upper()}"/>' in xml
    assert f'rdf:resource="urn:uuid:{line.PerLengthImpedance}"' in xml


def test_attribute_queries_name_extension_classes():
    from cimgraph.queries import sparql
    line = cim.ACLineSegment(name='line')
    query = sparql.get_all_attributes_sparql({cim.ACLineSegment: {line.identifier: line}},
                                             cim.ACLineSegment, [line.identifier])
    assert '?edge' in query and 'strafter(str(?classraw),"#")' in query


# Issue #160: enumerations in extension namespaces

def test_enum_iris_are_matched_to_the_enumeration_namespace(monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2026')
    monkeypatch.setenv('CIMG_NAMESPACE', 'http://cim.ucaiug.io/CIM101/draft#')
    get_cim_profile.cache_clear()
    import cimprofiles.cim18.cimhub_2026 as cim18
    connection = _RecordingEndpoint()
    gad = 'http://gridappsd.org/CIM/extension#'

    assert connection.enum_from_iri(f'{gad}BatteryTypeKind.leadAcid') is cim18.BatteryTypeKind.leadAcid
    assert connection.enum_from_iri(f'<{gad}BatteryTypeKind.leadAcid>') is cim18.BatteryTypeKind.leadAcid
    phase = next(iter(cim18.PhaseCode))
    assert connection.enum_from_iri(f'{phase.__namespace__}PhaseCode.{phase.value}') is phase
    assert connection.enum_from_iri(f'http://cim.ucaiug.io/CIM101/draft#PhaseCode.{phase.value}') is phase
    for not_an_enum in (f'http://example.com/other#BatteryTypeKind.leadAcid', f'{gad}ACLineSegment.r',
                        'Line 1: 12.47kV', '12.5', '2024-05-01T12:30:00.5Z'):
        assert connection.enum_from_iri(not_an_enum) is None

    battery = cim18.BatteryInfo(name='battery')
    graph = {cim18.BatteryInfo: {battery.identifier: battery}}
    connection.edge_query_parser({'results': {'bindings': [
        {'identifier': battery.uri(), 'attribute': 'BatteryInfo.batteryType',
         'value': f'{gad}BatteryTypeKind.leadAcid'}]}}, graph, cim18.BatteryInfo)
    assert battery.batteryType is cim18.BatteryTypeKind.leadAcid


def test_rdflib_get_all_attributes_keeps_the_graph_and_its_links(monkeypatch):
    pytest.importorskip('rdflib')
    from cimgraph.databases import RDFlibConnection
    monkeypatch.setenv('CIMG_IEC61970_552', '552-NEW')
    monkeypatch.setenv('CIMG_USE_UNITS', 'false')
    connection = RDFlibConnection(filename='tests/test_models/ieee13.xml')
    network = FeederModel(connection=connection, distributed=False,
                          container=cim.Feeder(mRID='49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'))
    sizes = {cim_class: len(objects) for cim_class, objects in network.graph.items()}

    network.get_all_attributes(cim.ACLineSegment)
    network.get_all_attributes(cim.Terminal)

    assert {cim_class: len(objects) for cim_class, objects in network.graph.items()} == sizes
    line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
    assert line.name == '645646' and isinstance(line.Location, str)
    assert all(isinstance(terminal.ConductingEquipment, cim.ConductingEquipment)
               for terminal in network.graph[cim.Terminal].values())


# Issue #155: delete

def test_delete_removes_every_point_of_a_location(tmp_path):
    from cimgraph.utils import create_object
    points = ''.join(f'<cim:PositionPoint rdf:ID="_PP_{index}"><cim:PositionPoint.Location '
                     f'rdf:resource="#_LOC_1"/></cim:PositionPoint>\n' for index in range(3))
    path = _write_xml(tmp_path / 'points.xml', '''
<cim:Location rdf:ID="_LOC_1"><cim:IdentifiedObject.name>loc</cim:IdentifiedObject.name></cim:Location>
''' + points)
    network = FeederModel(connection=XMLFile(filename=path), container=cim.Feeder(name='fdr'),
                          distributed=False)
    location = network.first(cim.Location)
    created = create_object(cim.PositionPoint, '_PP_9', network.graph)  # a non-UUID ID

    for point in location.PositionPoints:  # delete must not make this loop skip points
        network.delete(point)
    network.delete(created)

    assert network.graph[cim.PositionPoint] == {} and location.PositionPoints == []


def test_delete_rejects_classes_and_objects_not_in_the_graph():
    network = _network()
    with pytest.raises(TypeError):
        network.delete(cim.PositionPoint)
    with pytest.raises(ValueError, match='not in the graph'):
        network.delete(cim.PositionPoint())


# CIM difference writers

def _read_differences(network, tmp_path, write=None):
    from cimgraph.models.incremental_builder import read_incremental_xml
    path = str(tmp_path / 'changes.xml')
    (write or network.write_all_incrementals)(path)
    return read_incremental_xml(path), open(path).read()


def test_differences_of_created_and_deleted_objects(tmp_path):
    network = _network()
    line = network.create(cim.ACLineSegment, name='line')
    old_terminal = network.create(cim.Terminal, name='old', ConductingEquipment=line)
    network.incrementals = {'forwardDifferences': {}, 'reverseDifferences': {}}  # as if loaded

    terminal = network.create(cim.Terminal, name='new', ConductingEquipment=line)
    network.delete(old_terminal)
    temporary = network.create(cim.Breaker, name='temporary')
    network.delete(temporary)  # created and deleted: no difference
    differences, xml = _read_differences(network, tmp_path)

    assert differences['forwardDifferences'][terminal.uri()] == {
        'rdf:type': 'Terminal', 'IdentifiedObject.name': 'new',
        'IdentifiedObject.mRID': terminal.mRID,
        'Terminal.ConductingEquipment': f'urn:uuid:{line.uri()}'}
    assert differences['reverseDifferences'][old_terminal.uri()]['rdf:type'] == 'Terminal'
    assert set(differences['forwardDifferences']) == {terminal.uri()}
    assert set(differences['reverseDifferences']) == {old_terminal.uri()}
    assert f'<cim:Terminal rdf:about="urn:uuid:{terminal.uri()}">' in xml
    assert temporary.uri() not in xml


def test_deleting_a_referenced_object_removes_the_references(tmp_path):
    network = _network()
    line = network.create(cim.ACLineSegment, name='line')
    terminal = network.create(cim.Terminal, name='t1', ConductingEquipment=line)
    network.incrementals = {'forwardDifferences': {}, 'reverseDifferences': {}}

    network.delete(line)
    differences, _ = _read_differences(network, tmp_path)

    assert terminal.ConductingEquipment is None
    assert differences['reverseDifferences'][terminal.uri()] == {
        'Terminal.ConductingEquipment': f'urn:uuid:{line.uri()}'}
    assert differences['reverseDifferences'][line.uri()]['rdf:type'] == 'ACLineSegment'
    assert differences['forwardDifferences'] == {}


def test_modify_records_the_serialized_end_and_cancels_changes_back(tmp_path):
    network = _network()
    line_1 = network.create(cim.ACLineSegment, name='line 1')
    line_2 = network.create(cim.ACLineSegment, name='line 2')
    breaker = network.create(cim.Breaker, name='brk', open=False)
    terminal = network.create(cim.Terminal, name='t1', ConductingEquipment=line_1)
    network.incrementals = {'forwardDifferences': {}, 'reverseDifferences': {}}

    network.modify(breaker, 'open', True)
    network.modify(breaker, 'open', False)  # back to the original value: no difference
    network.modify(line_2, 'Terminals', [terminal])  # written from Terminal.ConductingEquipment
    differences, _ = _read_differences(network, tmp_path)

    assert differences['forwardDifferences'] == {
        terminal.uri(): {'Terminal.ConductingEquipment': f'urn:uuid:{line_2.uri()}'}}
    assert differences['reverseDifferences'] == {
        terminal.uri(): {'Terminal.ConductingEquipment': f'urn:uuid:{line_1.uri()}'}}


def test_incremental_file_holds_every_change_so_far(tmp_path):
    network = _network()
    line = network.create(cim.ACLineSegment, name='line', length=cim.Length(5, 'm'))
    path = str(tmp_path / 'changes.xml')

    network.modify(line, 'length', cim.Length(10, 'm'), incremental_file=path)

    from cimgraph.models.incremental_builder import read_incremental_xml
    differences = read_incremental_xml(path)
    assert differences['forwardDifferences'][line.uri()]['rdf:type'] == 'ACLineSegment'
    assert differences['forwardDifferences'][line.uri()]['Conductor.length'] == '10.0'


def test_list_differences_write_only_added_and_removed_items(tmp_path):
    network = _network()
    ends = [network.create(cim.TransformerEnd, name=f'end {index}') for index in range(3)]
    mesh = network.create(cim.TransformerMeshImpedance, name='mesh', ToTransformerEnd=ends[:2])
    network.incrementals = {'forwardDifferences': {}, 'reverseDifferences': {}}

    network.modify(mesh, 'ToTransformerEnd', [ends[1], ends[2]])
    differences, _ = _read_differences(network, tmp_path)

    assert differences['forwardDifferences'][mesh.uri()] == {
        'TransformerMeshImpedance.ToTransformerEnd': f'urn:uuid:{ends[2].uri()}'}
    assert differences['reverseDifferences'][mesh.uri()] == {
        'TransformerMeshImpedance.ToTransformerEnd': f'urn:uuid:{ends[0].uri()}'}


_BASE_MODEL = '''
<cim:ACLineSegment rdf:ID="_L1"><cim:IdentifiedObject.name>L1</cim:IdentifiedObject.name><cim:Conductor.length>5</cim:Conductor.length></cim:ACLineSegment>
<cim:ACLineSegment rdf:ID="_L2"><cim:IdentifiedObject.name>L2</cim:IdentifiedObject.name></cim:ACLineSegment>
<cim:Terminal rdf:ID="_T1"><cim:IdentifiedObject.name>T1</cim:IdentifiedObject.name><cim:Terminal.ConductingEquipment rdf:resource="#_L1"/></cim:Terminal>
<cim:Breaker rdf:ID="_B1"><cim:IdentifiedObject.name>B1</cim:IdentifiedObject.name><cim:Switch.open>false</cim:Switch.open></cim:Breaker>
<cim:Location rdf:ID="_LOC"><cim:IdentifiedObject.name>loc</cim:IdentifiedObject.name></cim:Location>
<cim:PositionPoint rdf:ID="_PP1"><cim:PositionPoint.Location rdf:resource="#_LOC"/><cim:PositionPoint.sequenceNumber>1</cim:PositionPoint.sequenceNumber></cim:PositionPoint>
<cim:PositionPoint rdf:ID="_PP2"><cim:PositionPoint.Location rdf:resource="#_LOC"/><cim:PositionPoint.sequenceNumber>2</cim:PositionPoint.sequenceNumber></cim:PositionPoint>
'''


def _load(path) -> FeederModel:
    return FeederModel(connection=XMLFile(filename=path), container=cim.Feeder(name='fdr'),
                       distributed=False)


def _by_name(network, cim_class, name):
    return network.find_by_attribute(cim_class, 'name', name)[0]


def test_from_incremental_repeats_the_changes_of_another_model(tmp_path, monkeypatch):
    from cimgraph.core.attribute_utils import diff_attributes
    monkeypatch.setenv('CIMG_USE_UNITS', 'true')
    base = _write_xml(tmp_path / 'base.xml', _BASE_MODEL)
    edited = _load(base)
    line_1, line_2 = _by_name(edited, cim.ACLineSegment, 'L1'), _by_name(edited, cim.ACLineSegment, 'L2')
    edited.create(cim.Terminal, name='T2', sequenceNumber=2, ConductingEquipment=line_2)
    edited.create(cim.ACLineSegmentPhase, name='L2a', phase=cim.SinglePhaseKind.A, ACLineSegment=line_2)
    edited.modify(_by_name(edited, cim.Breaker, 'B1'), 'open', True)
    edited.modify(line_2, 'length', cim.Length(10, 'm'))
    edited.modify(_by_name(edited, cim.Terminal, 'T1'), 'ConductingEquipment', line_2)
    edited.delete(line_1)
    edited.delete(edited.graph[cim.PositionPoint][next(iter(edited.graph[cim.PositionPoint]))])
    edited.delete(_by_name(edited, cim.Location, 'loc'))  # the other point keeps no Location
    path = str(tmp_path / 'changes.xml')
    edited.write_all_incrementals(path)

    applied = _load(base)
    changed = applied.from_incremental(path)

    assert {type(obj).__name__ for obj in changed} >= {'Terminal', 'ACLineSegmentPhase', 'Breaker'}
    assert applied.incrementals == edited.incrementals
    assert {cim_class: set(objects) for cim_class, objects in applied.graph.items() if objects} == \
           {cim_class: set(objects) for cim_class, objects in edited.graph.items() if objects}
    for cim_class, objects in edited.graph.items():
        for identifier, obj in objects.items():
            assert diff_attributes(obj, applied.graph[cim_class][identifier]) == {}
    assert _by_name(applied, cim.ACLineSegment, 'L2').length.to('m') == 10


def test_from_incremental_changes_nothing_if_a_difference_does_not_fit(tmp_path):
    base = _write_xml(tmp_path / 'base.xml', _BASE_MODEL)
    edited = _load(base)
    edited.create(cim.Terminal, name='T2')
    edited.modify(_by_name(edited, cim.Breaker, 'B1'), 'open', True)
    path = str(tmp_path / 'changes.xml')
    edited.write_all_incrementals(path)
    text = open(path).read().replace('<cim:Switch.open>true', '<cim:Switch.open>maybe')
    open(path, 'w').write(text)

    applied = _load(base)
    with pytest.raises(ValueError, match="open value 'maybe'"):
        applied.from_incremental(path)

    assert applied.incrementals == {'forwardDifferences': {}, 'reverseDifferences': {}}
    assert len(applied.graph[cim.Terminal]) == 1
