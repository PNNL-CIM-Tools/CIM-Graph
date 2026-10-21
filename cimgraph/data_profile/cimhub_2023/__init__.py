"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim17.cimhub_2023``.
"""
import warnings

from cimprofiles.cim17.cimhub_2023 import *
from cimprofiles.cim17.cimhub_2023 import __all__

warnings.warn('cimgraph.data_profile.cimhub_2023 is deprecated; '
              'import cimprofiles.cim17.cimhub_2023 instead',
              DeprecationWarning, stacklevel=2)
