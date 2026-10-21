"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18gmdm``.
"""
import warnings

from cimprofiles.cim18gmdm import *
from cimprofiles.cim18gmdm import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm is deprecated; '
              'import cimprofiles.cim18gmdm instead',
              DeprecationWarning, stacklevel=2)
