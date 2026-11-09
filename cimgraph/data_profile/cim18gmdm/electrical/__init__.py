"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18.cim18gmdm.electrical``.
"""
import warnings

from cimprofiles.cim18.cim18gmdm.electrical import *
from cimprofiles.cim18.cim18gmdm.electrical import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm.electrical is deprecated; '
              'import cimprofiles.cim18.cim18gmdm.electrical instead',
              DeprecationWarning, stacklevel=2)
