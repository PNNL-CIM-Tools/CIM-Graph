import os
import unittest

os.environ['CIMG_CIM_PROFILE'] = 'cim18v17'

import cimprofiles.cim18.cim18v17 as cim
from cimgraph.core import get_system_mva_base
from cimgraph.models import BusBranchModel, FeederModel, NodeBreakerModel


class TestSystemBases(unittest.TestCase):

    def tearDown(self):
        os.environ.pop('CIMG_SYSTEM_MVA_BASE', None)
        get_system_mva_base.cache_clear()

    def test_defaults_are_100_mva_and_60_hz(self):
        os.environ.pop('CIMG_SYSTEM_MVA_BASE', None)
        get_system_mva_base.cache_clear()
        for model_class in (FeederModel, BusBranchModel, NodeBreakerModel):
            network = model_class(container=None, connection=None)
            self.assertEqual(network.base_power.to('VA'), 100e6)
            self.assertEqual(network.base_frequency.to('Hz'), 60)

    def test_env_var_sets_default_base_power(self):
        os.environ['CIMG_SYSTEM_MVA_BASE'] = '10'
        get_system_mva_base.cache_clear()
        network = FeederModel(container=None, connection=None)
        self.assertEqual(network.base_power.to('MVA'), 10)

    def test_explicit_bases_are_kept(self):
        network = FeederModel(container=None, connection=None,
                              base_power=cim.ApparentPower(1, 'MVA'), base_frequency=cim.Frequency(50, 'Hz'))
        self.assertEqual(network.base_power.to('VA'), 1e6)
        self.assertEqual(network.base_frequency.to('Hz'), 50)
