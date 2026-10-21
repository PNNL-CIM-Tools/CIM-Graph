"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim17.cgmes_3_0_0.equipment_boundary``.
"""
import warnings

from cimprofiles.cim17.cgmes_3_0_0.equipment_boundary import *
from cimprofiles.cim17.cgmes_3_0_0.equipment_boundary import __all__

warnings.warn('cimgraph.data_profile.cgmes_3_0_0.equipment_boundary is deprecated; '
              'import cimprofiles.cim17.cgmes_3_0_0.equipment_boundary instead',
              DeprecationWarning, stacklevel=2)
