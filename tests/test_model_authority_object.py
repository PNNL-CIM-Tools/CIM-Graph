"""A ModelAuthority the profile declares (gad:ModelAuthority in the cim18v17 metadata profile)
is an object of the file, as in a Grid Kitchen assembly.xml; the 552 header
md:FullModel / cim:ModelAuthority of a CIMXML file stays header."""
import json

import pytest

from cimgraph.core import get_cim_profile
from cimgraph.databases import JSONLDFile, XMLFile

PROFILE = 'cimprofiles.cim18.cim18v17.metadata'
cim = pytest.importorskip(PROFILE)
pytestmark = pytest.mark.skipif('ModelAuthority' not in cim.__all__,
                                reason='cim-profiles has no gad:ModelAuthority yet')

GAD = 'http://gridappsd.org/CIM/extension#'
CIM = 'http://cim.ucaiug.io/cim101/draft#'
AUTHORITY = 'https://example.org/authority'
MODEL = '3b8f2a1c-5d4e-4f6a-9b7c-8d9e0f1a2b3c'
FRAME = '7c6d5e4f-3a2b-4c1d-8e9f-0a1b2c3d4e5f'
ASSEMBLY_XML = f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="{CIM}" xmlns:gad="{GAD}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<gad:ModelAuthority rdf:about="{AUTHORITY}">
  <cim:IdentifiedObject.name>example authority</cim:IdentifiedObject.name>
</gad:ModelAuthority>
<gad:FrameModel rdf:about="urn:uuid:{MODEL}">
  <gad:GridModel.ModelAuthority rdf:resource="{AUTHORITY}"/>
</gad:FrameModel>
<gad:Frame rdf:about="urn:uuid:{FRAME}">
  <gad:Frame.ModelAuthority rdf:resource="{AUTHORITY}"/>
</gad:Frame>
</rdf:RDF>
'''


@pytest.fixture(autouse=True)
def metadata_profile(monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', PROFILE)
    monkeypatch.setenv('CIMG_IEC61970_552', '552-NEW')
    get_cim_profile.cache_clear()
    yield
    get_cim_profile.cache_clear()


def _assert_links_resolve(graph):
    [authority] = graph[cim.ModelAuthority].values()
    model = next(iter(graph[cim.FrameModel].values()))
    frame = next(iter(graph[cim.Frame].values()))
    assert authority.name == 'example authority'
    assert model.ModelAuthority is authority
    assert frame.ModelAuthority is authority
    assert authority.GridModels == [model] and authority.ModeledFrames == [frame]


def test_rdf_xml_reads_a_profile_model_authority_as_an_object(tmp_path):
    filename = tmp_path / 'assembly.xml'
    filename.write_text(ASSEMBLY_XML, encoding='utf-8')
    connection = XMLFile(str(filename))
    graph = connection.create_new_graph(container=None)

    _assert_links_resolve(graph)
    assert connection.model_headers[0].authority is None    # an object, not the file's header


def test_json_ld_reads_a_profile_model_authority_as_an_object(tmp_path):
    document = {'@context': {'cim': CIM, 'gad': GAD}, '@graph': [
        {'@id': AUTHORITY, '@type': 'gad:ModelAuthority', 'cim:IdentifiedObject.name': 'example authority'},
        {'@id': f'urn:uuid:{MODEL}', '@type': 'gad:FrameModel',
         'gad:GridModel.ModelAuthority': {'@id': AUTHORITY}},
        {'@id': f'urn:uuid:{FRAME}', '@type': 'gad:Frame', 'gad:Frame.ModelAuthority': {'@id': AUTHORITY}},
    ]}
    filename = tmp_path / 'assembly.jsonld'
    filename.write_text(json.dumps(document), encoding='utf-8')

    _assert_links_resolve(JSONLDFile(str(filename)).create_new_graph(container=None))
