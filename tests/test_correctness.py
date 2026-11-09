"""Regression tests for the WS2 data-loss and correctness fixes (docs/development/RELEASE_1_0_PLAN.md)."""
import json
from xml.etree.ElementTree import ParseError

import pytest

import cimprofiles.cim17.cimhub_2023 as cim
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

def test_get_all_edges_runs_every_batch_once():
    connection = _RecordingEndpoint()
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
    lines = sorted((network.create(cim.ACLineSegment, name=name) for name in ('a', 'b')),
                   key=lambda line: line.uri())

    assert network.next(cim.ACLineSegment) is lines[0]  # next() without first() starts over
    assert network.next(cim.ACLineSegment) is lines[1]
    assert network.next(cim.ACLineSegment) is None
    assert network.first(cim.ACLineSegment) is lines[0]


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
