"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cgmes_3_0_0.state_variables``.
"""
import warnings

from cimprofiles.cgmes_3_0_0.state_variables import *
from cimprofiles.cgmes_3_0_0.state_variables import __all__

warnings.warn('cimgraph.data_profile.cgmes_3_0_0.state_variables is deprecated; '
              'import cimprofiles.cgmes_3_0_0.state_variables instead',
              DeprecationWarning, stacklevel=2)
