"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim17.cim17v40``.
"""
import warnings

from cimprofiles.cim17.cim17v40 import *
from cimprofiles.cim17.cim17v40 import __all__

warnings.warn('cimgraph.data_profile.cim17v40 is deprecated; '
              'import cimprofiles.cim17.cim17v40 instead',
              DeprecationWarning, stacklevel=2)
