"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18.cim18gmdm.canonical``.
"""
import warnings

from cimprofiles.cim18.cim18gmdm.canonical import *
from cimprofiles.cim18.cim18gmdm.canonical import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm.canonical is deprecated; '
              'import cimprofiles.cim18.cim18gmdm.canonical instead',
              DeprecationWarning, stacklevel=2)
