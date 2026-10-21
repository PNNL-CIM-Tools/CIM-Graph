"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18.cim18gad``.
"""
import warnings

from cimprofiles.cim18.cim18gad import *
from cimprofiles.cim18.cim18gad import __all__

warnings.warn('cimgraph.data_profile.cim18gad is deprecated; '
              'import cimprofiles.cim18.cim18gad instead',
              DeprecationWarning, stacklevel=2)
