"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cgmes_3_0_0.steady_state_hypothesis``.
"""
import warnings

from cimprofiles.cgmes_3_0_0.steady_state_hypothesis import *
from cimprofiles.cgmes_3_0_0.steady_state_hypothesis import __all__

warnings.warn('cimgraph.data_profile.cgmes_3_0_0.steady_state_hypothesis is deprecated; '
              'import cimprofiles.cgmes_3_0_0.steady_state_hypothesis instead',
              DeprecationWarning, stacklevel=2)
