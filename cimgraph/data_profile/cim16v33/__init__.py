"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim16.cim16v33``.
"""
import warnings

from cimprofiles.cim16.cim16v33 import *
from cimprofiles.cim16.cim16v33 import __all__

warnings.warn('cimgraph.data_profile.cim16v33 is deprecated; '
              'import cimprofiles.cim16.cim16v33 instead',
              DeprecationWarning, stacklevel=2)
