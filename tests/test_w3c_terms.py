"""W3C vocabulary terms (dct:issued, dcat:startDate) are written and read by their bare names,
and «compound» fields (dct:temporal -> dct:PeriodOfTime) as references to their own resources."""
import json
from collections import defaultdict

import pytest

from cimgraph.core import get_cim_profile
from cimgraph.core.serialization import object_to_json_ld, profile_namespaces
from cimgraph.databases import JSONLDFile, XMLFile
from cimgraph.utils.write_xml import write_graph_xml

PROFILE = 'cimprofiles.cim18.cim18v17.metadata'
cim = pytest.importorskip(PROFILE)
pytestmark = pytest.mark.skipif('issued' not in cim.GridDataset.__dataclass_fields__,
                                reason='cim-profiles has no dct:issued on GridDataset yet')


@pytest.fixture
def dataset(monkeypatch):
    """A FrameModel (a GridDataset) with every W3C term set, and the graph of it."""
    monkeypatch.setenv('CIMG_CIM_PROFILE', PROFILE)
    monkeypatch.setenv('CIMG_IEC61970_552', '552-NEW')
    get_cim_profile.cache_clear()
    model = cim.FrameModel(name='frame')
    model.issued = '2026-11-01T00:00:00Z'
    model.temporal = cim.PeriodOfTime(startDate='2026-01-01T00:00:00Z', endDate='2027-01-01T00:00:00Z')
    model.creator = cim.Agent(name='author')
    model.conformsTo = [cim.Standard()]
    graph = defaultdict(dict)
    for obj in (model, model.temporal, model.creator, *model.conformsTo):
        graph[type(obj)][obj.identifier] = obj
    yield model, graph
    get_cim_profile.cache_clear()


def _read_back(model, graph):
    return graph[cim.FrameModel][model.identifier]


def _assert_same(model, read):
    assert read.issued == model.issued
    assert read.temporal.startDate == model.temporal.startDate
    assert read.temporal.endDate == model.temporal.endDate
    assert read.creator.name == 'author'
    assert [standard.identifier for standard in read.conformsTo] == [model.conformsTo[0].identifier]


def test_rdf_xml_writes_bare_typed_w3c_terms(dataset, tmp_path):
    model, graph = dataset
    filename = tmp_path / 'frame.xml'
    write_graph_xml(graph, str(filename))
    text = filename.read_text()

    assert 'xmlns:dct="http://purl.org/dc/terms/"' in text
    assert ('<dct:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">'
            '2026-11-01T00:00:00Z</dct:issued>') in text
    assert f'<dct:temporal rdf:resource="urn:uuid:{model.temporal.uri()}"/>' in text
    assert f'<dct:PeriodOfTime rdf:about="urn:uuid:{model.temporal.uri()}">' in text
    assert '<dcat:startDate rdf:datatype=' in text
    assert '<dct:conformsTo ' in text and '<dct:creator ' in text
    assert 'GridDataset.' not in text
    assert '<cim:IdentifiedObject.name>frame</cim:IdentifiedObject.name>' in text

    _assert_same(model, _read_back(model, XMLFile(str(filename)).create_new_graph(container=None)))


def test_json_ld_writes_and_reads_bare_w3c_terms(dataset, tmp_path):
    model, graph = dataset
    namespaces = profile_namespaces(graph)
    node = object_to_json_ld(model, namespaces)
    assert {'dct:issued', 'dct:temporal', 'dct:conformsTo', 'dct:creator'} <= set(node)
    assert 'dcat:startDate' in object_to_json_ld(model.temporal, namespaces)

    filename = tmp_path / 'frame.jsonld'
    nodes = [object_to_json_ld(obj, namespaces) for objects in graph.values() for obj in objects.values()]
    filename.write_text(json.dumps({'@context': namespaces, '@graph': nodes}), encoding='utf-8')

    _assert_same(model, _read_back(model, JSONLDFile(str(filename)).create_new_graph(container=None)))
