import os
import tempfile
import unittest
from uuid import UUID

import cimgraph.data_profile.cimhub_2023 as cim
from cimgraph.databases import XMLFile
from cimgraph.models import FeederModel


class TestXMLFile(unittest.TestCase):

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
        os.environ['CIMG_URL'] = 'http://localhost:8889/bigdata/namespace/kb/sparql'
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

        connection = XMLFile(filename='tests/test_models/ieee13.xml')
        self.assertIsInstance(connection, XMLFile, 'Connection should be an instance of XMLFile')
        self.assertEqual(connection.cim_profile, 'cimhub_2023', 'CIM profile mismatch')
        self.assertEqual(connection.namespace, 'http://iec.ch/TC57/CIM100#', 'Namespace mismatch')
        self.assertEqual(connection.iec61970_552, '552-NEW', 'IEC61970_552 mismatch')


    def test_get_feeder_model(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        initial_keys = len(network.graph.keys())
        self.assertEqual(initial_keys, 48)

    def test_get_all_line_data(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertEqual(len(line.Terminals),2)
        # check value of line 645646
        self.assertEqual(line.name, '645646')
        self.assertEqual(line.length, 91.44)

        # check phase C
        for phase in line.ACLineSegmentPhases:
            if phase.phase.value == 'C':
               break
        self.assertEqual(phase.name, '645646_C')
        self.assertEqual(phase.ACLineSegment, line)

    def test_units_disabled_raw_float(self):
        os.environ['CIMG_USE_UNITS'] = 'false'
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertIs(type(line.length), float)
        self.assertEqual(line.length, 91.44)

    def test_units_enabled_si_fallback(self):
        os.environ['CIMG_USE_UNITS'] = 'true'
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertIsInstance(line.length, cim.Length)
        self.assertEqual(float(line.length), 91.44)
        self.assertAlmostEqual(line.length.to('km'), 0.09144)

    def test_upload_round_trip_via_write_xml(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line_uuid = UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')
        line = network.graph[cim.ACLineSegment][line_uuid]
        original_name = line.name
        original_length = line.length

        tmp = tempfile.NamedTemporaryFile(suffix='.xml', delete=False)
        tmp.close()
        tmp_path = tmp.name
        try:
            network.connection.filename = tmp_path
            network.upload()

            database2 = XMLFile(filename=tmp_path)
            feeder2 = cim.Feeder(mRID=self.feeder_mrid)
            network2 = FeederModel(connection=database2, container=feeder2, distributed=False)
            line2 = network2.graph[cim.ACLineSegment][line_uuid]

            self.assertEqual(line2.name, original_name)
            self.assertEqual(line2.length, original_length)
        finally:
            os.unlink(tmp_path)


if __name__ == '__main__':
    unittest.main()
