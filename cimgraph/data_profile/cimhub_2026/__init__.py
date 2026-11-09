"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18.cimhub_2026``.
"""
import warnings

from cimprofiles.cim18.cimhub_2026 import *
from cimprofiles.cim18.cimhub_2026 import __all__

warnings.warn('cimgraph.data_profile.cimhub_2026 is deprecated; '
              'import cimprofiles.cim18.cimhub_2026 instead',
              DeprecationWarning, stacklevel=2)
