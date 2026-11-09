"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18.cim18gmdm.asset``.
"""
import warnings

from cimprofiles.cim18.cim18gmdm.asset import *
from cimprofiles.cim18.cim18gmdm.asset import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm.asset is deprecated; '
              'import cimprofiles.cim18.cim18gmdm.asset instead',
              DeprecationWarning, stacklevel=2)
