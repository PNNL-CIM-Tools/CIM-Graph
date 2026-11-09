"""Regression tests for the WS1 security fixes (docs/development/RELEASE_1_0_PLAN.md)."""
import cimprofiles.cim17.cimhub_2023 as cim
import pytest

from cimgraph.core.validation import validate_attribute, validate_identifier
from cimgraph.queries import cypher, sparql

SPARQL_BREAKOUT = 'x"} } UNION { ?a ?b ?c } #'
CYPHER_BREAKOUT = 'x" OR 1=1 WITH n MATCH (m) DETACH DELETE m //'
ATTRIBUTE_BREAKOUT = 'IdentifiedObject.name`]-(m) DETACH DELETE m //'


# 1.1 Query injection

@pytest.mark.parametrize('identifier', [
    '49ad8e07-3bf9-a4e2-cb8f-c3722f837b62',
    '_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62',
    '_LINE_650632',
    'line.650-632',
])
def test_valid_identifiers_pass(identifier):
    assert validate_identifier(identifier) == identifier


@pytest.mark.parametrize('identifier', [SPARQL_BREAKOUT, CYPHER_BREAKOUT, 'a b', '', 'a\nb', None])
def test_invalid_identifiers_raise(identifier):
    with pytest.raises(ValueError):
        validate_identifier(identifier)


@pytest.mark.parametrize('attribute', ['name', 'IdentifiedObject.name', 'ACLineSegment.r0'])
def test_valid_attributes_pass(attribute):
    assert validate_attribute(attribute) == attribute


@pytest.mark.parametrize('attribute', [ATTRIBUTE_BREAKOUT, 'a.b.c', '1name', 'name "x"', ''])
def test_invalid_attributes_raise(attribute):
    with pytest.raises(ValueError):
        validate_attribute(attribute)


def test_get_object_builders_reject_breakout():
    with pytest.raises(ValueError):
        sparql.get_object_sparql(SPARQL_BREAKOUT)
    with pytest.raises(ValueError):
        cypher.get_object_cypher(CYPHER_BREAKOUT)
    assert '"_LINE_650632"' in sparql.get_object_sparql('_LINE_650632')
    assert '_LINE_650632"' in cypher.get_object_cypher('_LINE_650632')


def test_get_triple_builders_reject_breakout():
    line = cim.ACLineSegment()
    with pytest.raises(ValueError):
        sparql.get_triple_sparql(line, ATTRIBUTE_BREAKOUT)
    with pytest.raises(ValueError):
        cypher.get_triple_cypher(line, ATTRIBUTE_BREAKOUT)
    assert 'cim:IdentifiedObject.name' in sparql.get_triple_sparql(line, 'IdentifiedObject.name')


def test_node_list_builder_rejects_breakout():
    with pytest.raises(ValueError):
        sparql.get_all_nodes_from_list(['_LINE_650632', SPARQL_BREAKOUT], 'http://iec.ch/TC57/CIM100#')


# 1.2 Incremental builder trusts message contents

def _message(forward=None, reverse=None):
    from collections import defaultdict
    return {'forwardDifferences': defaultdict(dict, forward or {}),
            'reverseDifferences': defaultdict(dict, reverse or {})}


def _breaker_model(monkeypatch, name='B1'):
    from cimgraph.core import get_cim_profile
    from cimgraph.models import FeederModel
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    get_cim_profile.cache_clear()
    network = FeederModel(connection=None, container=cim.Feeder(name='fdr'), distributed=False)
    breaker = cim.Breaker(name=name, normalOpen=False)
    network.add_to_graph(breaker)
    return network, breaker


def test_unknown_mrid_differences_are_not_applied_to_previous_object(monkeypatch):
    from uuid import uuid4

    from cimgraph.models.incremental_builder import apply_incremental
    network, breaker = _breaker_model(monkeypatch)
    message = _message(forward={
        breaker.uri(): {'IdentifiedObject.name': 'B2'},
        str(uuid4()): {'IdentifiedObject.name': 'evil'},
    })
    with pytest.raises(ValueError, match='not in the model'):
        apply_incremental(network, message)
    assert breaker.name == 'B1'  # nothing is applied when any difference does not fit


def test_values_are_converted_and_bad_differences_rejected(monkeypatch):
    from cimgraph.models.incremental_builder import apply_incremental
    network, breaker = _breaker_model(monkeypatch)
    message = _message(forward={breaker.uri(): {'Switch.normalOpen': 'true'}})
    assert apply_incremental(network, message) == [breaker]
    assert breaker.normalOpen is True

    for bad in ({'Switch.notAField': 'x'}, {'Switch.normalOpen': 'maybe'},
                {'ACLineSegment.name': 'x'}, {'Switch.__class__': 'x'}):
        with pytest.raises(ValueError):
            apply_incremental(network, _message(forward={breaker.uri(): bad}))
    assert breaker.normalOpen is True and type(breaker) is cim.Breaker


def test_read_incremental_keeps_full_uuid(tmp_path):
    from cimgraph.models.incremental_builder import read_incremental_xml
    uri = '7ea8f6d8-0e1d-4c43-a3e4-2a0e0c0a000d'
    path = tmp_path / 'diff.xml'
    path.write_text(f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:cim="http://iec.ch/TC57/CIM100#"
    xmlns:dm="http://iec.ch/2002/schema/CIM_difference_model#">
<dm:DifferenceModel>
  <dm:forwardDifferences rdf:parseType="Statements">
    <rdf:Description rdf:about="urn:uuid:{uri}">
      <cim:IdentifiedObject.name>B2</cim:IdentifiedObject.name>
    </rdf:Description>
  </dm:forwardDifferences>
</dm:DifferenceModel>
</rdf:RDF>
''')
    assert list(read_incremental_xml(str(path))['forwardDifferences']) == [uri]


# 1.3 Path traversal in 557 metadata

@pytest.mark.parametrize('access_url', ['../secret.xml', '..\\secret.xml', 'parts/../../secret.xml'])
def test_metadata_access_url_cannot_leave_metadata_dir(tmp_path, access_url):
    from cimgraph.databases.fileparsers.metadata import (Distribution, MetadataGraph,
                                                         resolve_part_paths)
    (tmp_path / 'secret.xml').write_text('<rdf:RDF/>')  # exists, so only containment can stop it
    package = tmp_path / 'package'
    package.mkdir()
    meta = MetadataGraph(distributions=[Distribution(uuid='d1', access_url=access_url)])
    with pytest.raises(ValueError, match='outside'):
        resolve_part_paths(meta, package)


# 1.4 eval() on caller-supplied mermaid paths

def _line_with_node():
    line = cim.ACLineSegment(name='L1')
    node = cim.ConnectivityNode(name='N1')
    terminal = cim.Terminal(name='T1', ConductingEquipment=line, ConnectivityNode=node)
    line.Terminals.append(terminal)
    return line, node


def test_mermaid_object_path_follows_indexes():
    from cimgraph.utils import get_mermaid_path
    line, node = _line_with_node()
    for path in ('Terminals[0].ConnectivityNode', ['Terminals', '[0]', 'ConnectivityNode']):
        assert node.uri().split('-')[0] in get_mermaid_path(line, path)


def test_mermaid_class_path_follows_subclasses():
    from cimgraph.utils import get_mermaid_path
    first_subclass = cim.ConductingEquipment.__subclasses__()[0]
    diagram = get_mermaid_path(cim.ConductingEquipment, '__subclasses__()[0]')
    assert f'ConductingEquipment <|-- {first_subclass.__name__}' in diagram


@pytest.mark.parametrize('path', [
    'Terminals[0].__class__.__init__.__globals__',
    "Terminals[__import__('os').system('echo pwned')]",
    ['Terminals', "[0];__import__('os')"],
    'notAField',
])
def test_mermaid_object_path_rejects_code(path):
    from cimgraph.utils import get_mermaid_path
    line, _ = _line_with_node()
    with pytest.raises(ValueError):
        get_mermaid_path(line, path)


def test_mermaid_class_path_rejects_code():
    from cimgraph.utils import get_mermaid_path
    with pytest.raises(ValueError):
        get_mermaid_path(cim.ConductingEquipment, '__subclasses__()[0].__init__.__globals__')


# 1.5 Serializer escaping

SPARQL_UPDATE_BREAKOUT = 'x> . } ; DROP ALL ; INSERT DATA { <y'


def test_sparql_rejects_reference_breakout():
    from cimgraph.core.serialization import object_to_sparql_triples
    terminal = cim.Terminal(ConductingEquipment=SPARQL_UPDATE_BREAKOUT)
    with pytest.raises(ValueError):
        object_to_sparql_triples(terminal)


def test_sparql_literal_escapes_newlines_and_quotes():
    from cimgraph.core.serialization import _sparql_literal
    assert _sparql_literal('a"b\nc\rd\\e') == '"a\\"b\\nc\\rd\\\\e"'


def test_xml_reference_is_escaped_or_rejected():
    from cimgraph.core.attribute_utils import Property
    from cimgraph.core.serialization import property_to_xml
    namespaces = {'cim': 'http://iec.ch/TC57/CIM100#'}

    def reference(value):
        prop = Property('Terminal.ConductingEquipment', namespaces['cim'], 'reference', value)
        return property_to_xml(prop, namespaces, '#')

    with pytest.raises(ValueError):
        reference('x"/><cim:Evil rdf:about="y')
    assert 'rdf:resource="#http://example.com/a?b=1&amp;c=2"' in reference(
        'http://example.com/a?b=1&c=2')


# 1.6 Enum lookup by an unchecked name from the data

def test_profile_enum_only_returns_profile_enumerations():
    from types import SimpleNamespace

    from cimgraph.databases import ConnectionInterface
    connection = SimpleNamespace(cim=cim)
    assert ConnectionInterface.profile_enum(connection, 'PhaseCode', 'ABC') is cim.PhaseCode.ABC
    for class_name in ('ACLineSegment', 'field', 'UUID', 'NotAClass'):
        assert ConnectionInterface.profile_enum(connection, class_name, 'x') is None
    with pytest.raises(ValueError):
        ConnectionInterface.profile_enum(connection, 'PhaseCode', 'not-a-phase')


def test_xml_enum_reference_cannot_instantiate_classes(tmp_path, monkeypatch):
    from cimgraph.core import get_cim_profile
    from cimgraph.databases import XMLFile
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    get_cim_profile.cache_clear()
    path = tmp_path / 'enums.xml'
    ns = 'http://iec.ch/TC57/CIM100#'
    path.write_text(f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="{ns}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<cim:ACLineSegmentPhase rdf:about="urn:uuid:5b3b9c4e-0d5a-4a43-9a3c-1f0c3d7e8a01">
  <cim:ACLineSegmentPhase.phase rdf:resource="{ns}SinglePhaseKind.A"/>
</cim:ACLineSegmentPhase>
<cim:ACLineSegmentPhase rdf:about="urn:uuid:5b3b9c4e-0d5a-4a43-9a3c-1f0c3d7e8a02">
  <cim:ACLineSegmentPhase.phase rdf:resource="{ns}ACLineSegment.evil"/>
</cim:ACLineSegmentPhase>
</rdf:RDF>
''')
    graph = XMLFile(filename=str(path)).create_new_graph(container=None)
    phases = sorted(graph[cim.ACLineSegmentPhase].values(), key=lambda phase: phase.uri())
    assert phases[0].phase is cim.SinglePhaseKind.A
    assert phases[1].phase is None
    assert not graph.get(cim.ACLineSegment)
    get_cim_profile.cache_clear()


# 1.7 Credentials

@pytest.mark.parametrize('variable, getter_name', [('CIMG_USERNAME', 'get_username'),
                                                   ('CIMG_PASSWORD', 'get_password')])
def test_missing_credentials_raise_instead_of_defaulting(monkeypatch, variable, getter_name):
    import cimgraph.core.env_vars as env_vars
    getter = getattr(env_vars, getter_name)
    monkeypatch.delenv(variable, raising=False)
    getter.cache_clear()
    with pytest.raises(ValueError, match=variable):
        getter()
    monkeypatch.setenv(variable, 'from-env')
    getter.cache_clear()
    assert getter() == 'from-env'
    getter.cache_clear()


def test_gridappsd_credentials_are_not_written_to_environment(monkeypatch):
    import os

    pytest.importorskip('gridappsd')
    import cimgraph.databases.gridappsd.gridappsd as gridappsd_module
    from cimgraph.core import get_cim_profile

    captured = {}

    class FakeGridAPPSD:
        def __init__(self, **kwargs):
            captured.update(kwargs)

    for variable, value in (('CIMG_CIM_PROFILE', 'cimhub_2023'), ('CIMG_HOST', 'platform'),
                            ('CIMG_PORT', '61613'), ('CIMG_USERNAME', 'user'),
                            ('CIMG_PASSWORD', 's3cret')):
        monkeypatch.setenv(variable, value)
    monkeypatch.delenv('GRIDAPPSD_PASSWORD', raising=False)
    monkeypatch.setattr(gridappsd_module, 'GridAPPSD', FakeGridAPPSD)
    get_cim_profile.cache_clear()

    gridappsd_module.GridappsdConnection().connect()

    assert captured == {'address': ('platform', '61613'), 'username': 'user', 'password': 's3cret'}
    assert 'GRIDAPPSD_PASSWORD' not in os.environ
    get_cim_profile.cache_clear()


# 1.9 rdflib parse

@pytest.mark.parametrize('filename', ['https://example.com/model.jsonld', 'missing.xml'])
def test_rdflib_connection_only_reads_local_files(filename, monkeypatch):
    pytest.importorskip('rdflib')
    from cimgraph.core import get_cim_profile
    from cimgraph.databases import RDFlibConnection
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    get_cim_profile.cache_clear()
    with pytest.raises(FileNotFoundError):
        RDFlibConnection(filename=filename)
    get_cim_profile.cache_clear()
