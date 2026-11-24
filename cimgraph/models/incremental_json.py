"""Moved to :mod:`cimgraph.updaters.incremental_json`; this import path is removed in the next release."""
import warnings

from cimgraph.updaters.incremental_json import *
from cimgraph.updaters.incremental_json import __all__  # noqa: F401

warnings.warn('cimgraph.models.incremental_json moved to cimgraph.updaters.incremental_json',
              DeprecationWarning, stacklevel=2)
