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


class TestBasePowerFromGraph(unittest.TestCase):
    """A model's BasePower (PSS/E SBASE, MATPOWER baseMVA) is its system base:
    reading a CIM XML file with one must not leave base_power at 100 MVA."""

    def _write_model(self, *base_powers):
        import tempfile

        from cimgraph.utils import write_xml
        network = NodeBreakerModel(container=None, connection=None, distributed=False,
                                   base_power=base_powers[0].basePower)
        for base_power in base_powers:
            network.add_to_graph(base_power)
        path = os.path.join(tempfile.mkdtemp(), 'model.xml')
        write_xml(network, path)
        return path

    def test_xml_base_power_sets_the_system_base(self):
        from cimgraph.databases import XMLFile
        path = self._write_model(cim.BasePower(mRID='sbase', basePower=cim.ApparentPower(50, 'MVA')))
        for model_class in (FeederModel, BusBranchModel, NodeBreakerModel):
            network = model_class(container=None, connection=XMLFile(path), distributed=False)
            self.assertAlmostEqual(network.base_power.to('MVA'), 50)

    def test_in_memory_graph_base_power_sets_the_system_base(self):
        graph = {cim.BasePower: {}}
        base_power = cim.BasePower(mRID='sbase', basePower=cim.ApparentPower(50, 'MVA'))
        graph[cim.BasePower][base_power.identifier] = base_power
        network = FeederModel(container=None, connection=None, graph=graph)
        self.assertAlmostEqual(network.base_power.to('MVA'), 50)

    def test_disagreeing_base_powers_raise(self):
        from cimgraph.databases import XMLFile
        path = self._write_model(cim.BasePower(mRID='sbase', basePower=cim.ApparentPower(50, 'MVA')),
                                 cim.BasePower(mRID='sbase_100', basePower=cim.ApparentPower(100, 'MVA')))
        with self.assertRaisesRegex(ValueError, 'disagrees with the model'):
            FeederModel(container=None, connection=XMLFile(path), distributed=False)
        with self.assertRaisesRegex(ValueError, 'disagrees with the model'):
            FeederModel(container=None, connection=XMLFile(self._write_model(
                cim.BasePower(mRID='sbase', basePower=cim.ApparentPower(50, 'MVA')))),
                distributed=False, base_power=cim.ApparentPower(100, 'MVA'))


class TestBaseFrequencyFromGraph(unittest.TestCase):
    """A model's BaseFrequency (a 50 Hz deck's) is its system frequency: it must
    not be left at the 60 Hz default (UPSTREAM_REQUESTS U14 in CIMHub)."""

    @staticmethod
    def _graph(*hertz):
        frequencies = [cim.BaseFrequency(mRID=f'bf_{i}', frequency=cim.Frequency(f, 'Hz')) for i, f in enumerate(hertz)]
        return {cim.BaseFrequency: {bf.identifier: bf for bf in frequencies}}

    def test_graph_base_frequency_sets_the_system_frequency(self):
        for model_class in (FeederModel, BusBranchModel, NodeBreakerModel):
            network = model_class(container=None, connection=None, graph=self._graph(50))
            self.assertEqual(network.base_frequency.to('Hz'), 50)

    def test_xml_base_frequency_sets_the_system_frequency(self):
        import tempfile

        from cimgraph.databases import XMLFile
        from cimgraph.utils import write_xml
        source = NodeBreakerModel(container=None, connection=None, distributed=False, graph=self._graph(50))
        path = os.path.join(tempfile.mkdtemp(), 'model.xml')
        write_xml(source, path)
        network = FeederModel(container=None, connection=XMLFile(path), distributed=False)
        self.assertEqual(network.base_frequency.to('Hz'), 50)

    def test_disagreeing_base_frequencies_raise(self):
        with self.assertRaisesRegex(ValueError, "BaseFrequency 'bf_1'.*disagrees with the model"):
            FeederModel(container=None, connection=None, graph=self._graph(50, 60))
        with self.assertRaisesRegex(ValueError, 'disagrees with the model'):
            FeederModel(container=None, connection=None, graph=self._graph(50),
                        base_frequency=cim.Frequency(60, 'Hz'))

    def test_explicit_base_frequency_agreeing_with_the_graph_is_kept(self):
        network = FeederModel(container=None, connection=None, graph=self._graph(50),
                              base_frequency=cim.Frequency(50, 'Hz'))
        self.assertEqual(network.base_frequency.to('Hz'), 50)
