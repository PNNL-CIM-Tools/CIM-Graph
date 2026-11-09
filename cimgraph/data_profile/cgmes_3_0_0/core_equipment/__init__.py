"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim17.cgmes_3_0_0.core_equipment``.
"""
import warnings

from cimprofiles.cim17.cgmes_3_0_0.core_equipment import *
from cimprofiles.cim17.cgmes_3_0_0.core_equipment import __all__

warnings.warn('cimgraph.data_profile.cgmes_3_0_0.core_equipment is deprecated; '
              'import cimprofiles.cim17.cgmes_3_0_0.core_equipment instead',
              DeprecationWarning, stacklevel=2)
