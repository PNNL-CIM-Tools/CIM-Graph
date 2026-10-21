"""cim-graph 0.6 compatibility with the profiles moved to cimprofiles.

Old import paths must give the same objects as the new ones, not copies:
a second Identity, pint registry or merged module would break isinstance
checks, unit arithmetic and graph-key lookups without raising.
"""
import importlib
import sys
import warnings

import pytest

import cimprofiles.identity
import cimprofiles.units.units
from cimgraph.core import get_cim_profile, set_model_scope


def test_identity_and_units_are_aliased_not_copied():
    import cimgraph.data_profile.identity as old_identity
    import cimgraph.data_profile.units.units as old_units

    assert old_identity is cimprofiles.identity
    assert old_units is cimprofiles.units.units
    assert old_units.ureg is cimprofiles.units.units.ureg


def test_module_state_is_shared_through_the_alias(monkeypatch):
    import cimgraph.data_profile.identity as old_identity
    import cimprofiles.cimhub_2026 as cim

    monkeypatch.setattr(old_identity, 'ARCHIVE_JSON_LD', False)
    assert cimprofiles.identity.ARCHIVE_JSON_LD is False
    assert cim.Terminal().__json_ld__ is None


def test_profile_shim_reexports_the_same_classes_with_a_warning():
    import cimprofiles.cim18gmdm.connectivity as new

    for name in [n for n in sys.modules if n.startswith('cimgraph.data_profile.cim18gmdm')]:
        del sys.modules[name]
    # The parent package shim (cim18gmdm) warns too, so capture all and look for ours.
    with pytest.warns(DeprecationWarning) as records:
        old = importlib.import_module('cimgraph.data_profile.cim18gmdm.connectivity')

    assert any('import cimprofiles.cim18gmdm.connectivity' in str(r.message) for r in records)
    assert old.__all__ == new.__all__
    assert old.ACLineSegment is new.ACLineSegment
    assert issubclass(old.ACLineSegment, cimprofiles.identity.Identity)


def test_legacy_profile_prefix_gives_the_same_merged_module(monkeypatch):
    parts = ('cim18gmdm.connectivity', 'cim18gmdm.electrical')

    monkeypatch.setenv('CIMG_CIM_PROFILE', ','.join('cimprofiles.' + p for p in parts))
    get_cim_profile.cache_clear()
    _, new_merged = get_cim_profile()

    monkeypatch.setenv('CIMG_CIM_PROFILE', ','.join('cimgraph.data_profile.' + p for p in parts))
    get_cim_profile.cache_clear()
    with pytest.warns(DeprecationWarning, match='cimgraph.data_profile'):
        _, old_merged = get_cim_profile()
    get_cim_profile.cache_clear()

    assert old_merged is new_merged


def test_bare_profile_name_resolves_to_cimprofiles(monkeypatch):
    import cimprofiles.cimhub_2026

    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2026')
    get_cim_profile.cache_clear()
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        _, cim = get_cim_profile()
    get_cim_profile.cache_clear()

    assert cim is cimprofiles.cimhub_2026


def test_set_model_scope_reaches_identity(monkeypatch):
    import cimprofiles.cimhub_2026 as cim

    monkeypatch.delenv('CIMG_MODEL_AUTHORITY', raising=False)
    monkeypatch.delenv('CIMG_MODEL_NAME', raising=False)
    set_model_scope('authority_a', 'model_1')
    first = cim.Feeder(name='feeder').identifier
    set_model_scope('authority_b', 'model_1')
    second = cim.Feeder(name='feeder').identifier
    set_model_scope('authority_a', 'model_1')

    assert first != second
    assert cim.Feeder(name='feeder').identifier == first


def test_missing_driver_names_the_extra(monkeypatch):
    import cimgraph.databases

    monkeypatch.delitem(sys.modules, 'cimgraph.databases.neo4j', raising=False)
    monkeypatch.delitem(sys.modules, 'cimgraph.databases.neo4j.neo4j', raising=False)
    monkeypatch.setitem(sys.modules, 'neo4j', None)    # makes `import neo4j` fail

    with pytest.raises(ImportError, match=r'pip install "cim-graph\[neo4j\]"'):
        cimgraph.databases.Neo4jConnection


def test_unknown_databases_attribute_is_an_attribute_error():
    import cimgraph.databases

    with pytest.raises(AttributeError):
        cimgraph.databases.NoSuchConnection
