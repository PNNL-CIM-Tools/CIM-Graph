import os
import unittest
from uuid import UUID

import cimgraph.data_profile.cimhub_2023 as cim
from cimgraph import utils
from cimgraph.databases import Neo4jConnection
from cimgraph.models import FeederModel
from cimgraph.queries import cypher


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
        os.environ['CIMG_URL'] = 'neo4j://localhost:7687'
        os.environ['CIMG_DATABASE'] = 'neo4j'
        os.environ['CIMG_HOST'] = 'localhost'
        os.environ['CIMG_PORT'] = '7687'
        os.environ['CIMG_USERNAME'] = 'neo4j'
        os.environ['CIMG_PASSWORD'] = 'test1234'
        os.environ['CIMG_NAMESPACE'] = 'http://iec.ch/TC57/CIM100#'
        os.environ['CIMG_IEC61970_301'] = '8'
        os.environ['CIMG_USE_UNITS'] = 'False'
        self.feeder_mrid = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'

    def tearDown(self):
        # Restore environment variables
        for key, value in self.original_env.items():
            if value is not None:
                os.environ[key] = value
            else:
                os.environ.pop(key, None)

    def test_blazegraph_connection_with_env_vars(self):

        connection = Neo4jConnection()
        self.assertIsInstance(connection, Neo4jConnection, 'Connection should be an instance of Neo4jConnection')
        self.assertEqual(connection.cim_profile, 'cimhub_2023', 'CIM profile mismatch')
        self.assertEqual(connection.url, 'neo4j://localhost:7687', 'URL mismatch')
        self.assertEqual(connection.namespace, 'http://iec.ch/TC57/CIM100#', 'Namespace mismatch')
        self.assertEqual(connection.iec61970_301, 8, 'IEC61970_301 mismatch')

    def test_get_object_cypher(self):
        """Test get_object_sparql to retrieve object from mrid"""

        query = cypher.get_object_cypher(mRID=self.feeder_mrid)
        expected_str = '\nMATCH(n)\nWHERE n.uri = "urn:uuid:49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"\nRETURN DISTINCT n.uri as identifier,\nlabels(n)[1] as class'
        self.assertEqual(query, expected_str)

    def test_get_object(self):
        database = Neo4jConnection()
        feeder = database.get_object(mRID=self.feeder_mrid)
        expected_str = '{"@id": "49ad8e07-3bf9-a4e2-cb8f-c3722f837b62", "@type": "Feeder"}'
        self.assertEqual(feeder.__str__(), expected_str)
        database.disconnect()

    def test_get_nodes_sparql(self):
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        query = cypher.get_all_nodes_from_container(feeder)
        expected_str = 'MATCH (container:Feeder)\nWHERE container.uri = "urn:uuid:49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"\nMATCH (eq) - [:`Equipment.EquipmentContainer`] - (container)\nOPTIONAL MATCH (cnode) - [:`Terminal.ConnectivityNode`] - (term:Terminal) - [:`Terminal.ConductingEquipment`] -> (eq)\nRETURN DISTINCT\nREPLACE(cnode.uri, "urn:uuid:", "") as ConnectivityNode,\nREPLACE(term.uri, "urn:uuid:", "") as Terminal,\nREPLACE(eq.uri, "urn:uuid:", "") as eq_id,\nLABELS(eq)[1] as eq_class'
        self.assertEqual(query, expected_str)

    def test_get_feeder_model(self):
        database = Neo4jConnection()
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        initial_keys = len(network.graph.keys())
        self.assertEqual(initial_keys, 13)
        database.disconnect()


    def test_get_all_line_data(self):
        database = Neo4jConnection()
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
        database.disconnect()



if __name__ == '__main__':
    unittest.main()
