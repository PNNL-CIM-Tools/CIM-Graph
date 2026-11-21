"""CIMG_ALLOW_UNDEFINED_ATTRIBUTES=true keeps properties the profile does not define, as text."""
import json
from pathlib import Path
from uuid import UUID

import cimprofiles.cim17.cimhub_2023 as cim
import pytest

from cimgraph.core import get_cim_profile
from cimgraph.databases import JSONLDFile, RDFlibConnection, XMLFile
from cimgraph.models import FeederModel

FEEDER = '5b0c3e8d-7a41-4f62-9d1e-3c2b1a0f9e8d'
LINE = '1d4e3b4a-6c6f-4f35-9a3e-0d7e5b1c2a11'
TERMINAL = '9c1f0a7e-2b3d-4e5f-8a6b-7c8d9e0f1a2b'
LINE_XML = f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<cim:Feeder rdf:about="urn:uuid:{FEEDER}">
  <cim:IdentifiedObject.name>feeder</cim:IdentifiedObject.name>
</cim:Feeder>
<cim:ACLineSegment rdf:about="urn:uuid:{LINE}">
  <cim:IdentifiedObject.name>650632</cim:IdentifiedObject.name>
  <cim:Equipment.EquipmentContainer rdf:resource="urn:uuid:{FEEDER}"/>
  <cim:ACLineSegment.vendorRating>42.5</cim:ACLineSegment.vendorRating>
  <cim:ACLineSegment.vendorTag>a</cim:ACLineSegment.vendorTag>
  <cim:ACLineSegment.vendorTag>b</cim:ACLineSegment.vendorTag>
  <cim:ACLineSegment.vendorPhases rdf:resource="http://iec.ch/TC57/CIM100#PhaseCode.ABC"/>
  <cim:ACLineSegment.VendorTerminal rdf:resource="urn:uuid:{TERMINAL}"/>
</cim:ACLineSegment>
<cim:Terminal rdf:about="urn:uuid:{TERMINAL}">
  <cim:Terminal.ConductingEquipment rdf:resource="urn:uuid:{LINE}"/>
</cim:Terminal>
</rdf:RDF>
'''


@pytest.fixture
def line_file(tmp_path, monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    monkeypatch.setenv('CIMG_IEC61970_552', '552-NEW')
    monkeypatch.setenv('CIMG_USE_UNITS', 'false')
    get_cim_profile.cache_clear()
    filename = tmp_path / 'line.xml'
    filename.write_text(LINE_XML, encoding='utf-8')
    yield str(filename)
    get_cim_profile.cache_clear()


def _line(connection) -> object:
    network = FeederModel(connection=connection, container=cim.Feeder(mRID=FEEDER),
                          distributed=False)
    network.get_all_edges(cim.ACLineSegment)
    return network.graph[cim.ACLineSegment][UUID(LINE)]


def test_undefined_properties_are_dropped_by_default(line_file):
    line = _line(XMLFile(line_file))
    assert not hasattr(line, 'vendorRating')


@pytest.mark.parametrize('connection_class', [XMLFile, RDFlibConnection])
def test_undefined_properties_are_kept_as_text(line_file, monkeypatch, connection_class):
    monkeypatch.setenv('CIMG_ALLOW_UNDEFINED_ATTRIBUTES', 'true')
    line = _line(connection_class(line_file))

    assert line.vendorRating == '42.5'
    assert sorted(line.vendorTag) == ['a', 'b']
    assert line.vendorPhases.endswith('PhaseCode.ABC')
    assert line.VendorTerminal.lower().endswith(TERMINAL)
    assert line.name == '650632'    # defined properties are read as usual


def test_undefined_jsonld_properties_are_kept_as_text(line_file, monkeypatch, tmp_path):
    monkeypatch.setenv('CIMG_ALLOW_UNDEFINED_ATTRIBUTES', 'true')
    source = json.loads((Path(__file__).parent / 'test_models' / 'ieee13.jsonld').read_text())
    line_node = next(node for node in source['@graph']
                     if node.get('@type') == 'cim:ACLineSegment')
    line_node['cim:ACLineSegment.vendorRating'] = '42.5'
    line_node['cim:ACLineSegment.VendorTerminal'] = {'@id': f'urn:uuid:{TERMINAL}'}
    filename = tmp_path / 'ieee13.jsonld'
    filename.write_text(json.dumps(source), encoding='utf-8')

    network = FeederModel(connection=JSONLDFile(str(filename)),
                          container=cim.Feeder(mRID='49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'),
                          distributed=False)
    lines = [line for line in network.graph[cim.ACLineSegment].values()
             if hasattr(line, 'vendorRating')]

    assert len(lines) == 1
    assert lines[0].vendorRating == '42.5'
    assert lines[0].VendorTerminal == f'urn:uuid:{TERMINAL}'
