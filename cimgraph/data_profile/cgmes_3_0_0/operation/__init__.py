"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cgmes_3_0_0.operation``.
"""
import warnings

from cimprofiles.cgmes_3_0_0.operation import *
from cimprofiles.cgmes_3_0_0.operation import __all__

warnings.warn('cimgraph.data_profile.cgmes_3_0_0.operation is deprecated; '
              'import cimprofiles.cgmes_3_0_0.operation instead',
              DeprecationWarning, stacklevel=2)
