"""
Deprecated in cim-graph 0.6, removed in 1.0. Use ``cimprofiles.cim18.cim18gmdm.diagram``.
"""
import warnings

from cimprofiles.cim18.cim18gmdm.diagram import *
from cimprofiles.cim18.cim18gmdm.diagram import __all__

warnings.warn('cimgraph.data_profile.cim18gmdm.diagram is deprecated; '
              'import cimprofiles.cim18.cim18gmdm.diagram instead',
              DeprecationWarning, stacklevel=2)
