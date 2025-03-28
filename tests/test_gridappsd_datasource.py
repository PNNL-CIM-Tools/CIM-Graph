import os
import unittest

from cimgraph.databases.gridappsd import GridappsdConnection


class TestGridappsdDatasource(unittest.TestCase):

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
        os.environ['CIMG_DATABASE'] = 'powergridmodel'
        os.environ['CIMG_HOST'] = 'localhost'
        os.environ['CIMG_PORT'] = '61613'
        os.environ['CIMG_USERNAME'] = 'test_app_user'
        os.environ['CIMG_PASSWORD'] = '4Test'
        os.environ['CIMG_NAMESPACE'] = 'http://iec.ch/TC57/CIM100#'
        os.environ['CIMG_IEC61970_301'] = '8'
        os.environ['CIMG_USE_UNITS'] = 'False'

    def tearDown(self):
        # Restore environment variables
        for key, value in self.original_env.items():
            if value is not None:
                os.environ[key] = value
            else:
                os.environ.pop(key, None)

    def test_get_gridappsds_connection_with_env_vars(self):

        connection = GridappsdConnection()
        self.assertIsInstance(connection, GridappsdConnection, 'Connection should be an instance of GridappsdConnection')
        self.assertEqual(connection.cim_profile, 'cimhub_2023', 'CIM profile mismatch')
        self.assertEqual(connection.url, 'http://localhost:8889/bigdata/namespace/kb/sparql', 'URL mismatch')
        self.assertEqual(connection.database, 'powergridmodel', 'Database mismatch')
        self.assertEqual(connection.host, 'localhost', 'Host mismatch')
        self.assertEqual(connection.port, 61613, 'Port mismatch')
        self.assertEqual(connection.username, 'test_app_user', 'Username mismatch')
        self.assertEqual(connection.password, '4Test', 'Password mismatch')
        self.assertEqual(connection.namespace, 'http://iec.ch/TC57/CIM100#', 'Namespace mismatch')
        self.assertEqual(connection.iec61970_301, 8, 'IEC61970_301 mismatch')
        self.assertFalse(connection.use_units, 'USE_UNITS mismatch')

    def test_connection_established(self):
        # Overwrite for this test the profile.
        import cimgraph.data_profile.cim17v40 as cim
        from cimgraph.models import FeederModel
        os.environ['CIMG_CIM_PROFILE'] = 'cim17v40'

        # Hard coded feader id
        feeder_mrid = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'
        #eeder = cim.Feeder(mRID = feeder_mrid)
        connection = GridappsdConnection()
        feeder = connection.get_object(mRID=feeder_mrid)
        assert feeder, 'Feeder object.'
        assert connection.gapps.connected, "Couldn't connect"
        network = FeederModel(connection=connection, container=feeder, distributed=False)
        #network = FeederModel(connection=connection, container=feeder, distributed=False)

        connection.disconnect()


if __name__ == '__main__':
    unittest.main()
