"""Header vocabulary terms (dct:issued, dcat:version, adms:versionNotes, eumd:processType) are
written and read by their bare names, on the md:Model children of the cim18v17 metadata
profile. md: terms keep their class (md:Model.modelingAuthoritySet). A reference to a resource
outside the model (a licence, a process) is kept as its IRI. A part file's md:FullModel or
dcat:Dataset header is never read as an object, though the profile declares both classes."""
import json
from collections import defaultdict
from types import SimpleNamespace

import pytest

from cimgraph.core import get_cim_profile
from cimgraph.core.serialization import object_to_json_ld, profile_namespaces
from cimgraph.databases import JSONLDFile, XMLFile
from cimgraph.databases.fileparsers.metadata import is_header_type
from cimgraph.utils.write_json import write_json_ld
from cimgraph.utils.write_xml import write_graph_xml

PROFILE = 'cimprofiles.cim18.cim18v17.metadata'
cim = pytest.importorskip(PROFILE)
pytestmark = pytest.mark.skipif(
    'versionNotes' not in getattr(getattr(cim, 'Model', None), '__dataclass_fields__', {}),
    reason='cim-profiles has no adms:versionNotes on md:Model yet (0.2.0a11 has)')

LICENSE = 'https://creativecommons.org/licenses/by/4.0/'
PROCESS = 'https://gridkitchen.pnnl.gov/process/IGM'
EQUIPMENT_PROFILE = 'http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0'
MD = 'http://iec.ch/TC57/61970-552/ModelDescription/1#'


@pytest.fixture
def assembly(monkeypatch):
    """An assembly of a frame model and the boundary model it requires, with every header
    term set, as Grid Kitchen's assembly.xml holds them; and the graph of it."""
    monkeypatch.setenv('CIMG_CIM_PROFILE', PROFILE)
    monkeypatch.setenv('CIMG_IEC61970_552', '552-NEW')
    get_cim_profile.cache_clear()
    frame = cim.Frame(name='feeder')
    boundary = cim.BoundaryModel(description='Supply boundary', version='1.0.0')
    area = cim.FrameModel(description='Distribution area', version='1.0.0', issued='2026-11-19T17:00:00Z',
                          versionNotes='First version.', modelingAuthoritySet='https://example.org/authority',
                          spatial=frame, RepresentedFrame=frame, requires=[boundary], license=LICENSE,
                          processType=PROCESS, conformsTo=[EQUIPMENT_PROFILE])
    package = cim.GridAssembly(description='package', version='1.0.0', GridModelParts=[area, boundary])
    graph = defaultdict(dict)
    for obj in (frame, boundary, area, package):
        graph[type(obj)][obj.identifier] = obj
    yield SimpleNamespace(frame=frame, boundary=boundary, area=area, package=package, graph=graph)
    get_cim_profile.cache_clear()


def _assert_read_back(assembly, graph):
    area = graph[cim.FrameModel][assembly.area.identifier]
    for attribute in ('description', 'version', 'issued', 'versionNotes', 'modelingAuthoritySet',
                      'license', 'processType', 'conformsTo'):
        assert getattr(area, attribute) == getattr(assembly.area, attribute), attribute
    assert area.spatial is area.RepresentedFrame is graph[cim.Frame][assembly.frame.identifier]
    assert area.requires == [graph[cim.BoundaryModel][assembly.boundary.identifier]]
    package = graph[cim.GridAssembly][assembly.package.identifier]
    assert set(package.GridModelParts) == {area, *area.requires}
    # The md:FullModel header write_graph_xml writes is not an object
    assert cim.FullModel not in graph


def test_rdf_xml_writes_and_reads_bare_header_terms(assembly, tmp_path):
    filename = tmp_path / 'assembly.xml'
    write_graph_xml(assembly.graph, str(filename))
    text = filename.read_text()

    assert '<md:FullModel ' in text
    for element in (f'<dct:identifier>{assembly.area.uri()}</dct:identifier>',
                    '<dct:description>Distribution area</dct:description>',
                    '<dcat:version>1.0.0</dcat:version>',
                    '<dct:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">'
                    '2026-11-19T17:00:00Z</dct:issued>',
                    '<adms:versionNotes>First version.</adms:versionNotes>',
                    '<md:Model.modelingAuthoritySet>https://example.org/authority</md:Model.modelingAuthoritySet>',
                    f'<dct:requires rdf:resource="urn:uuid:{assembly.boundary.uri()}"/>',
                    f'<dct:spatial rdf:resource="urn:uuid:{assembly.frame.uri()}"/>',
                    # External IRIs are written as they are, without the urn:uuid: prefix
                    f'<dct:license rdf:resource="{LICENSE}"/>',
                    f'<eumd:processType rdf:resource="{PROCESS}"/>',
                    f'<dct:conformsTo rdf:resource="{EQUIPMENT_PROFILE}"/>'):
        assert element in text
    assert 'Model.versionNotes' not in text and 'Model.processType' not in text
    assert 'Identity.identifier' not in text.split('<gad:FrameModel ')[1].split('</gad:FrameModel>')[0]

    _assert_read_back(assembly, XMLFile(str(filename)).create_new_graph(container=None))


def test_json_ld_writes_and_reads_bare_header_terms(assembly, tmp_path):
    namespaces = profile_namespaces(assembly.graph)
    node = object_to_json_ld(assembly.area, namespaces)
    assert {'dct:description', 'dcat:version', 'dct:issued', 'adms:versionNotes', 'eumd:processType',
            'md:Model.modelingAuthoritySet', 'dct:requires', 'dct:spatial'} <= set(node)
    assert (node['dct:license'], node['eumd:processType']) == (LICENSE, PROCESS)

    filename = tmp_path / 'assembly.jsonld'
    nodes = [object_to_json_ld(obj, namespaces) for objects in assembly.graph.values() for obj in objects.values()]
    filename.write_text(json.dumps({'@context': namespaces, '@graph': nodes}), encoding='utf-8')

    _assert_read_back(assembly, JSONLDFile(str(filename)).create_new_graph(container=None))


def test_a_dataset_header_is_not_an_object(assembly, tmp_path):
    header = {'dcat:isVersionOf': {'@id': 'https://example.org/model/assembly'}, 'dct:license': {'@id': LICENSE}}
    xml_file, json_file = tmp_path / 'assembly.xml', tmp_path / 'assembly.jsonld'
    write_graph_xml(assembly.graph, str(xml_file), header=header, profile=cim)
    write_json_ld(SimpleNamespace(graph=assembly.graph, cim=cim), str(json_file), header=header)
    assert '<dcat:Dataset ' in xml_file.read_text()

    for connection in (XMLFile(str(xml_file)), JSONLDFile(str(json_file))):
        graph = connection.create_new_graph(container=None)
        assert cim.Dataset not in graph and cim.FullModel not in graph
        assert graph[cim.FrameModel][assembly.area.identifier].processType == PROCESS
        (model_header,) = connection.model_headers
        assert model_header.created is not None


@pytest.mark.parametrize('namespace, local, header', [
    (MD, 'FullModel', True),                                       # declared by the profile
    ('http://www.w3.org/ns/dcat#', 'Dataset', True),               # declared by the profile
    ('http://iec.ch/TC57/CIM100#', 'ModelAuthority', True),        # cimgraph's header element
    ('http://gridappsd.org/CIM/extension#', 'ModelAuthority', False),
    ('http://purl.org/dc/terms/', 'PeriodOfTime', False),
    ('http://gridappsd.org/CIM/extension#', 'GridAssembly', False),  # a FullModel, under its own type
])
def test_header_types(namespace, local, header):
    assert is_header_type(cim, namespace, local) is header
