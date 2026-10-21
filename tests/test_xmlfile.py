import json
import os
import tempfile
import unittest
from uuid import NAMESPACE_URL, UUID, uuid4, uuid5

import cimprofiles.cimhub_2023 as cim
from cimgraph.core import get_model_authority, get_model_name, set_model_scope
from cimgraph.databases import XMLFile
from cimgraph.models import FeederModel
from cimgraph.utils import write_json_ld, write_xml


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
            'CIMG_MODEL_AUTHORITY': os.getenv('CIMG_MODEL_AUTHORITY'),
            'CIMG_MODEL_NAME': os.getenv('CIMG_MODEL_NAME'),
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

    def test_writers_include_model_header(self):
        os.environ['CIMG_MODEL_AUTHORITY'] = 'pnnl'
        os.environ['CIMG_MODEL_NAME'] = 'ieee13'
        get_model_authority.cache_clear()
        get_model_name.cache_clear()
        self.addCleanup(get_model_name.cache_clear)
        self.addCleanup(get_model_authority.cache_clear)
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            xml_path = os.path.join(tmp_dir, 'out.xml')
            json_path = os.path.join(tmp_dir, 'out.jsonld')
            write_xml(network, xml_path)
            write_json_ld(network, json_path)

            with open(xml_path, encoding='utf-8') as f:
                xml_text = f.read()
            self.assertIn('<md:FullModel rdf:about="urn:uuid:', xml_text)
            self.assertIn('<md:Model.modelingAuthoritySet>pnnl</md:Model.modelingAuthoritySet>', xml_text)
            self.assertIn('<md:Model.description>ieee13</md:Model.description>', xml_text)
            self.assertIn('<cim:ModelAuthority rdf:about="urn:uuid:', xml_text)

            with open(json_path, encoding='utf-8') as f:
                graph = json.load(f)['@graph']
            types = [node['@type'] for node in graph]
            self.assertIn('md:FullModel', types)
            self.assertIn('cim:ModelAuthority', types)

    def _use_model_scope(self, authority, model_name):
        set_model_scope(authority, model_name)
        self.addCleanup(get_model_name.cache_clear)
        self.addCleanup(get_model_authority.cache_clear)

    def test_reader_restores_model_header(self):
        self._use_model_scope('pnnl', 'ieee13')
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        network = FeederModel(connection=database, container=cim.Feeder(mRID=self.feeder_mrid),
                              distributed=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            xml_path = os.path.join(tmp_dir, 'out.xml')
            write_xml(network, xml_path)

            self._use_model_scope('someone_else', '')
            reread = XMLFile(filename=xml_path)
            reread.create_new_graph(container=None)

        header = reread.model_headers[0]
        self.assertEqual(header.authority, 'pnnl')
        self.assertEqual(header.description, 'ieee13')
        self.assertEqual(header.authority_uuid, str(uuid5(NAMESPACE_URL, 'pnnl')))
        self.assertIsNotNone(header.full_model_uuid)
        self.assertEqual((get_model_authority(), get_model_name()), ('pnnl', 'ieee13'))
        class_names = {cim_class.__name__ for cim_class in reread.graph}
        self.assertNotIn('FullModel', class_names)
        self.assertNotIn('ModelAuthority', class_names)

    def test_headerless_file_keeps_model_scope(self):
        self._use_model_scope('pnnl', 'ieee13')
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        database.create_new_graph(container=None)
        self.assertIsNone(database.model_headers[0].authority)
        self.assertEqual((get_model_authority(), get_model_name()), ('pnnl', 'ieee13'))

    def test_each_part_seeds_with_its_own_authority(self):
        def part(authority, line_id):
            return f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#"
    xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<md:FullModel rdf:about="urn:uuid:{uuid4()}">
  <md:Model.description>feeder_1</md:Model.description>
  <md:Model.modelingAuthoritySet>{authority}</md:Model.modelingAuthoritySet>
</md:FullModel>
<cim:ACLineSegment rdf:ID="{line_id}">
  <cim:IdentifiedObject.name>{line_id}</cim:IdentifiedObject.name>
</cim:ACLineSegment>
</rdf:RDF>
'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = []
            for authority, line_id in (('utility_a', 'LINE_A'), ('utility_b', 'LINE_B')):
                path = os.path.join(tmp_dir, f'{authority}.xml')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(part(authority, line_id))
                paths.append(path)
            database = XMLFile(filename=paths)
            self.addCleanup(get_model_name.cache_clear)
            self.addCleanup(get_model_authority.cache_clear)
            graph = database.create_new_graph(container=None)

        lines = {line.name: line.identifier for line in graph[cim.ACLineSegment].values()}
        for authority, line_id in (('utility_a', 'LINE_A'), ('utility_b', 'LINE_B')):
            set_model_scope(authority, 'feeder_1')
            self.assertEqual(lines[line_id], cim.ACLineSegment(identifier=line_id).identifier)


if __name__ == '__main__':
    unittest.main()
