"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.rc4_2021``.
"""
import warnings

from cimprofiles.rc4_2021 import *
from cimprofiles.rc4_2021 import __all__

warnings.warn('cimgraph.data_profile.rc4_2021 is deprecated; '
              'import cimprofiles.rc4_2021 instead',
              DeprecationWarning, stacklevel=2)
