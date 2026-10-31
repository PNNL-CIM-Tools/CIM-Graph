import os
import tempfile
import unittest

os.environ['CIMG_CIM_PROFILE'] = 'cimhub_2026'

import cimprofiles.cim18.cimhub_2026 as cim
from cimgraph.databases import XMLFile, add_object_to_graph
from cimgraph.models import BusBranchModel


def new_network() -> BusBranchModel:
    connection = XMLFile(filename=tempfile.mktemp(suffix='.xml'))
    return BusBranchModel(connection=connection, container=cim.Feeder(mRID='fdr_1'),
                          distributed=False)


class TestMRIDIndex(unittest.TestCase):

    def test_find_by_mrid_returns_added_object(self):
        network = new_network()
        bus = cim.ConnectivityNode(mRID='bus_650', name='650')
        network.add_to_graph(bus)
        self.assertIs(network.find_by_mRID('bus_650'), bus)

    def test_find_by_mrid_misses_return_none(self):
        self.assertIsNone(new_network().find_by_mRID('bus_650'))

    def test_mrid_is_unique_across_classes(self):
        # CIM 18: the mRID is unique within the model, not within a class
        network = new_network()
        network.add_to_graph(cim.ConnectivityNode(mRID='671'))
        with self.assertRaisesRegex(ValueError, "mRID '671' .* already used by ConnectivityNode"):
            network.add_to_graph(cim.EnergyConsumer(mRID='671'))
        self.assertEqual(network.list_identities()[-1]['class'], 'ConnectivityNode')

    def test_readding_the_same_object_is_a_no_op(self):
        network = new_network()
        bus = cim.ConnectivityNode(mRID='bus_650')
        network.add_to_graph(bus)
        network.add_to_graph(bus)
        self.assertIs(network.find_by_mRID('bus_650'), bus)

    def test_objects_put_in_the_graph_directly_are_indexed(self):
        # Readers and queries write into network.graph without add_to_graph
        network = new_network()
        network.find_by_mRID('anything')
        bus = cim.ConnectivityNode(mRID='bus_650')
        add_object_to_graph(network.graph, bus)
        self.assertIs(network.find_by_mRID('bus_650'), bus)

    def test_deleted_object_is_not_found(self):
        network = new_network()
        bus = cim.ConnectivityNode(mRID='bus_650')
        network.add_to_graph(bus)
        network.delete(bus)
        self.assertIsNone(network.find_by_mRID('bus_650'))
        replacement = cim.ConnectivityNode(mRID='bus_650', name='new')
        network.add_to_graph(replacement)
        self.assertIs(network.find_by_mRID('bus_650'), replacement)

    def test_list_identities(self):
        network = new_network()
        bus = cim.ConnectivityNode(mRID='bus_650', name='650')
        network.add_to_graph(bus)
        self.assertIn({'identifier': str(bus.identifier), 'mRID': 'bus_650', 'name': '650',
                       'class': 'ConnectivityNode'}, network.list_identities())


if __name__ == '__main__':
    unittest.main()
