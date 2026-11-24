"""Moved to :mod:`cimgraph.updaters.incremental_builder`; this import path is removed in the next release."""
import warnings

from cimgraph.updaters.incremental_builder import *
from cimgraph.updaters.incremental_builder import __all__  # noqa: F401

warnings.warn('cimgraph.models.incremental_builder moved to cimgraph.updaters.incremental_builder',
              DeprecationWarning, stacklevel=2)
