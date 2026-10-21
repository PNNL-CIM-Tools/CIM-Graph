"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18gmdm.connectivity``.
"""
import warnings

from cimprofiles.cim18gmdm.connectivity import *
from cimprofiles.cim18gmdm.connectivity import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm.connectivity is deprecated; '
              'import cimprofiles.cim18gmdm.connectivity instead',
              DeprecationWarning, stacklevel=2)
