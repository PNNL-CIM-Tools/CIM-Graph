import os
import unittest
import cimgraph.data_profile.cimhub_2023 as cim
from cimgraph.databases import BlazegraphConnection
from cimgraph.queries import sparql
from cimgraph.models import FeederModel
from cimgraph import utils
from uuid import UUID

class TestBlazegraphSETO(unittest.TestCase):

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
            'CIMG_IEC61970_301': os.getenv('CIMG_IEC61970_301'),
            'CIMG_USE_UNITS': os.getenv('CIMG_USE_UNITS'),
        }

        # Set environment variables for testing
        os.environ['CIMG_CIM_PROFILE'] = 'cimhub_2023'
        os.environ['CIMG_URL'] = 'http://localhost:8889/bigdata/namespace/kb/sparql'
        os.environ['CIMG_NAMESPACE'] = 'http://iec.ch/TC57/CIM100#'
        os.environ['CIMG_IEC61970_301'] = '8'
        os.environ['CIMG_USE_UNITS'] = 'false'

        self.feeder_mrid = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'

    def tearDown(self):
        # Restore environment variables
        for key, value in self.original_env.items():
            if value is not None:
                os.environ[key] = value
            else:
                os.environ.pop(key, None)

    def test_blazegraph_connection_with_env_vars(self):

        connection = BlazegraphConnection()
        self.assertIsInstance(connection, BlazegraphConnection, 'Connection should be an instance of BlazegraphConnection')
        self.assertEqual(connection.cim_profile, 'cimhub_2023', 'CIM profile mismatch')
        self.assertEqual(connection.url, 'http://localhost:8889/bigdata/namespace/kb/sparql', 'URL mismatch')
        self.assertEqual(connection.namespace, 'http://iec.ch/TC57/CIM100#', 'Namespace mismatch')
        self.assertEqual(connection.iec61970_301, 8, 'IEC61970_301 mismatch')

    def test_get_object_sparql(self):
        """Test get_object_sparql to retrieve object from mrid"""

        query = sparql.get_object_sparql(mRID=self.feeder_mrid)
        expected_str = '\n        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n        PREFIX cim:  <http://iec.ch/TC57/CIM100#>\n        SELECT DISTINCT ?identifier ?obj_class\n        WHERE {\n          \n    VALUES ?identifier {"49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"}\n        bind(iri(concat("urn:uuid:", ?identifier)) as ?eq)\n\n        ?eq a ?classraw.\n        bind(strafter(str(?classraw),"http://iec.ch/TC57/CIM100#") as ?obj_class)\n        }\n        ORDER by  ?identifier\n        '
        self.assertEqual(query, expected_str)
        
    def test_get_object(self):
        database = BlazegraphConnection()
        feeder = database.get_object(mRID=self.feeder_mrid)
        expected_str = '{"@id": "49ad8e07-3bf9-a4e2-cb8f-c3722f837b62", "@type": "Feeder"}'
        self.assertEqual(feeder.__str__(), expected_str)

    def test_get_nodes_sparql(self):
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        query = sparql.get_all_nodes_from_container(feeder)
        expected_str = '\n        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n        PREFIX cim:  <http://iec.ch/TC57/CIM100#>\n        SELECT DISTINCT ?ConnectivityNode ?Terminal ?Equipment\n        WHERE {\n          \n        VALUES ?identifier {"49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"}\n        bind(iri(concat("urn:uuid:", ?identifier)) as ?c).\n             {\n\n        ?node cim:ConnectivityNode.ConnectivityNodeContainer ?c.\n        ?t cim:Terminal.ConnectivityNode ?node.\n        ?t cim:Terminal.ConductingEquipment ?eq.\n        ?eq a ?eq_cls.\n\n        bind(strafter(str(?node),"urn:uuid:") as ?ConnectivityNode).\n        bind(strafter(str(?t),"urn:uuid:") as ?Terminal).\n        bind(strafter(str(?eq),"urn:uuid:") as ?eq_id).\n\n        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"http://iec.ch/TC57/CIM100#"), "\\"}") as ?Equipment)\n        }\n        \n        UNION\n        {\n        {?eq cim:Equipment.EquipmentContainer ?c.}\n        UNION\n        {?eq cim:Equipment.AdditionalEquipmentContainer ?c.}\n        OPTIONAL {\n            ?t cim:Terminal.ConductingEquipment ?eq.\n            ?t cim:Terminal.ConnectivityNode ?node.\n            }\n        ?eq a ?eq_cls.\n\n        bind(strafter(str(?node),"urn:uuid:") as ?ConnectivityNode).\n        bind(strafter(str(?t),"urn:uuid:") as ?Terminal).\n        bind(strafter(str(?eq),"urn:uuid:") as ?eq_id).\n\n        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"http://iec.ch/TC57/CIM100#"), "\\"}") as ?Equipment)\n        }\n        }\n        ORDER by ?ConnectivityNode\n        '
        self.assertEqual(query, expected_str)

    def test_get_feeder_model(self):
        database = BlazegraphConnection()
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        initial_keys = len(network.graph.keys())
        self.assertEqual(initial_keys, 14)

    def test_get_all_line_data(self):
        database = BlazegraphConnection()
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertEqual(len(line.Terminals),2)
        utils.get_all_line_data(network)
        # check size of graph
        total_keys = len(network.graph.keys())
        self.assertEqual(total_keys, 21)
        # check value of line 645646
        self.assertEqual(line.name, '645646')
        self.assertEqual(line.length, 91.44)
        
        # check phase C
        for phase in line.ACLineSegmentPhases:
            if phase.phase.value == 'C':
               break
        self.assertEqual(phase.name, '645646_C')
        self.assertEqual(phase.ACLineSegment, line)
        

if __name__ == '__main__':
    unittest.main()