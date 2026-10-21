"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18gmdm.location``.
"""
import warnings

from cimprofiles.cim18gmdm.location import *
from cimprofiles.cim18gmdm.location import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm.location is deprecated; '
              'import cimprofiles.cim18gmdm.location instead',
              DeprecationWarning, stacklevel=2)
