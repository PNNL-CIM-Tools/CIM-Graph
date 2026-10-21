"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim17.cgmes_3_0_0.short_circuit``.
"""
import warnings

from cimprofiles.cim17.cgmes_3_0_0.short_circuit import *
from cimprofiles.cim17.cgmes_3_0_0.short_circuit import __all__

warnings.warn('cimgraph.data_profile.cgmes_3_0_0.short_circuit is deprecated; '
              'import cimprofiles.cim17.cgmes_3_0_0.short_circuit instead',
              DeprecationWarning, stacklevel=2)
