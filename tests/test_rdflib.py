import os
import unittest
from uuid import UUID

import cimprofiles.cim17.cimhub_2023 as cim
import pytest
from cimprofiles.identity import Identity, as_uuid

from cimgraph import utils
from cimgraph.core.attribute_utils import diff_attributes
from cimgraph.databases import RDFlibConnection, XMLFile
from cimgraph.models import FeederModel
from cimgraph.queries import sparql


class TestRDFlibConnection(unittest.TestCase):

    def setUp(self):
        # Backup environment variables
        self.original_env = {
            'CIMG_CIM_PROFILE': os.getenv('CIMG_CIM_PROFILE'),
            'CIMG_URL': os.getenv('CIMG_URL'),
            'CIMG_DATABASE': os.getenv('CIMG_DATABASE'),
            'CIMG_HOST': os.getenv('CIMG_HOST'),
            'CIMG_PORT': os.getenv('CIMG_PORT'),
            'CIMG_USERNAME': os.getenv('CIMG_USERNAME'),
            'CIMG_PASSWORD': os.getenv('CIMG_PASSWORD'),
            'CIMG_NAMESPACE': os.getenv('CIMG_NAMESPACE'),
            'CIMG_IEC61970_552': os.getenv('CIMG_IEC61970_552'),
            'CIMG_USE_UNITS': os.getenv('CIMG_USE_UNITS'),
        }

        # Set environment variables for testing
        os.environ['CIMG_CIM_PROFILE'] = 'cimhub_2023'
        os.environ['CIMG_NAMESPACE'] = 'http://iec.ch/TC57/CIM100#'
        os.environ['CIMG_IEC61970_552'] = '552-NEW'
        os.environ['CIMG_USE_UNITS'] = 'false'

        self.feeder_mrid = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'

    def tearDown(self):
        # Restore environment variables
        for key, value in self.original_env.items():
            if value is not None:
                os.environ[key] = value
            else:
                os.environ.pop(key, None)

    def test_xml_connection_with_env_vars(self):

        connection = RDFlibConnection(filename='tests/test_models/ieee13.xml')
        self.assertIsInstance(connection, RDFlibConnection, 'Connection should be an instance of RDFlibConnection')
        self.assertEqual(connection.cim_profile, 'cimhub_2023', 'CIM profile mismatch')
        self.assertEqual(connection.namespace, 'http://iec.ch/TC57/CIM100#', 'Namespace mismatch')
        self.assertEqual(connection.iec61970_552, '552-NEW', 'IEC61970_552 mismatch')

    def test_get_object(self):
        database = RDFlibConnection(filename='tests/test_models/ieee13.xml')
        feeder = database.get_object(mRID=self.feeder_mrid)
        expected_str = '{"@id": "49ad8e07-3bf9-a4e2-cb8f-c3722f837b62", "@type": "Feeder"}'
        self.assertEqual(feeder.__str__(), expected_str)

    def test_get_feeder_model(self):
        database = RDFlibConnection(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        initial_keys = len(network.graph.keys())
        self.assertEqual(initial_keys, 14)

    def test_get_all_line_data(self):
        database = RDFlibConnection(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertEqual(len(line.Terminals),2)
        utils.get_all_line_data(network)
        # check size of graph
        total_keys = len(network.graph.keys())
        # self.assertEqual(total_keys, 21)
        # check value of line 645646
        self.assertEqual(line.name, '645646')
        self.assertEqual(line.length, 91.44)

        # check phase C
        for phase in line.ACLineSegmentPhases:
            if phase.phase.value == 'C':
               break
        self.assertEqual(phase.name, '645646_C')
        self.assertEqual(phase.ACLineSegment, line)


LINE = '1d4e3b4a-6c6f-4f35-9a3e-0d7e5b1c2a11'
TERMINAL = '9c1f0a7e-2b3d-4e5f-8a6b-7c8d9e0f1a2b'
FEEDER = '5b0c3e8d-7a41-4f62-9d1e-3c2b1a0f9e8d'
# CGMES: underscore in rdf:ID and references, none in the mRID
CGMES_FEEDER = f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<cim:Feeder rdf:ID="_{FEEDER}">
  <cim:IdentifiedObject.mRID>{FEEDER}</cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>feeder</cim:IdentifiedObject.name>
</cim:Feeder>
<cim:ACLineSegment rdf:ID="_{LINE}">
  <cim:IdentifiedObject.mRID>{LINE}</cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>650632</cim:IdentifiedObject.name>
  <cim:Equipment.EquipmentContainer rdf:resource="#_{FEEDER}"/>
</cim:ACLineSegment>
<cim:Terminal rdf:ID="_{TERMINAL}">
  <cim:IdentifiedObject.mRID>{TERMINAL}</cim:IdentifiedObject.mRID>
  <cim:Terminal.ConductingEquipment rdf:resource="#_{LINE}"/>
</cim:Terminal>
</rdf:RDF>
'''


def _references(value) -> set | None:
    """The identifiers of a reference or list of references, which may be objects or, for
    objects outside the graph, identifier text. None if value is not references."""
    values = value if isinstance(value, list) else [value]
    identifiers = {item.identifier if isinstance(item, Identity) else as_uuid(item)
                   for item in values if isinstance(item, (Identity, str))}
    if not values or len(identifiers) != len(values) or None in identifiers:
        return None
    return identifiers


def _get_attributes_per_class(network: FeederModel) -> None:
    for cim_class in list(network.graph):
        network.get_all_attributes(cim_class)


def _differences_from_xml(filename: str, feeder_mrid: str,
                          load_data=_get_attributes_per_class) -> list[str]:
    """Every object RDFlibConnection reads for the feeder, after load_data(network), and its
    attributes, compared to what XMLFile reads from the same file."""
    connection = RDFlibConnection(filename=filename)
    network = FeederModel(connection=connection, container=cim.Feeder(mRID=feeder_mrid),
                          distributed=False)
    load_data(network)
    xml_network = FeederModel(connection=XMLFile(filename=filename),
                              container=cim.Feeder(mRID=feeder_mrid), distributed=False)

    assert sum(len(objects) for objects in network.graph.values()) > 1
    differences = []
    for cim_class, objects in network.graph.items():
        for identifier, obj in objects.items():
            xml_obj = xml_network.graph.get(cim_class, {}).get(identifier)
            if xml_obj is None:
                differences.append(f'{cim_class.__name__} {identifier} is not in {filename}')
                continue
            for attribute, (value, xml_value) in diff_attributes(obj, xml_obj).items():
                if _references(value) is not None and _references(value) == _references(xml_value):
                    continue
                differences.append(f'{cim_class.__name__}.{attribute}: {value!r} != {xml_value!r}')
    return differences


@pytest.fixture
def legacy_env(monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    monkeypatch.setenv('CIMG_NAMESPACE', 'http://iec.ch/TC57/CIM100#')
    monkeypatch.setenv('CIMG_USE_UNITS', 'false')
    return monkeypatch


def test_legacy_rdf_ids_read_the_objects_xml_reads(legacy_env):
    legacy_env.setenv('CIMG_IEC61970_552', '552-LEGACY')
    assert _differences_from_xml('tests/test_models/maple10nodebreaker.xml',
                                 '_9E985101-27AD-4FE4-B36A-EBECC98CDFA1') == []


def test_get_all_data_reads_objects_found_after_their_class(legacy_env):
    # Objects reached later through other classes (e.g. Locations, other Feeders) must be
    # fetched too, not only the ones present when their class was first fetched. Compares
    # names only: maple10 repeats ACLineSegment.b0ch, and several nodes share one
    # OperationalLimitSet, so the readers legitimately differ on those attributes.
    legacy_env.setenv('CIMG_IEC61970_552', '552-LEGACY')
    filename = 'tests/test_models/maple10nodebreaker.xml'
    feeder = cim.Feeder(mRID='_9E985101-27AD-4FE4-B36A-EBECC98CDFA1')
    network = FeederModel(connection=RDFlibConnection(filename=filename), container=feeder,
                          distributed=False)
    utils.get_all_data(network)
    xml_network = FeederModel(connection=XMLFile(filename=filename),
                              container=cim.Feeder(mRID=feeder.mRID), distributed=False)

    unnamed = [f'{cim_class.__name__} {identifier}'
               for cim_class, objects in network.graph.items()
               for identifier, obj in objects.items()
               if getattr(obj, 'name', None)
               != getattr(xml_network.graph.get(cim_class, {}).get(identifier), 'name', None)]
    assert unnamed == []


def test_cgmes_rdf_ids_read_the_objects_xml_reads(legacy_env, tmp_path):
    legacy_env.setenv('CIMG_IEC61970_552', 'CGMES')
    filename = tmp_path / 'cgmes.xml'
    filename.write_text(CGMES_FEEDER, encoding='utf-8')
    assert _differences_from_xml(str(filename), FEEDER) == []


if __name__ == '__main__':
    unittest.main()
