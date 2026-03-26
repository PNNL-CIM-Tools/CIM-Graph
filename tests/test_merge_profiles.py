"""Tests for runtime CIM profile merging."""
from __future__ import annotations

import dataclasses
import importlib
import os
import sys
import textwrap
from dataclasses import fields, is_dataclass
from enum import Enum
from pathlib import Path

import pytest


def test_merge_two_profiles():
    """Merge connectivity + electrical and check the result has a unified __all__."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)

    # __all__ should be the union
    conn_names = set(connectivity.__all__)
    elec_names = set(electrical.__all__)
    merged_names = set(merged.__all__)
    assert conn_names.issubset(merged_names)
    assert elec_names.issubset(merged_names)


def test_merged_acline_segment_has_union_of_fields():
    """ACLineSegment should have fields from both connectivity and electrical."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    MergedACLineSegment = getattr(merged, 'ACLineSegment')
    assert is_dataclass(MergedACLineSegment)

    field_names = {f.name for f in fields(MergedACLineSegment)}
    # From connectivity
    assert 'ACLineSegmentPhases' in field_names
    # From electrical
    assert 'PerLengthImpedance' in field_names


def test_merged_conductor_has_length_field():
    """Conductor should gain the 'length' field from electrical."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    MergedConductor = getattr(merged, 'Conductor')
    assert is_dataclass(MergedConductor)

    field_names = {f.name for f in fields(MergedConductor)}
    assert 'length' in field_names


def test_merged_class_inherits_from_merged_parent():
    """ACLineSegment should be a subclass of the merged Conductor, not the original."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    MergedACLineSegment = getattr(merged, 'ACLineSegment')
    MergedConductor = getattr(merged, 'Conductor')

    assert issubclass(MergedACLineSegment, MergedConductor)


def test_non_overlapping_classes_present():
    """Classes unique to one profile should still appear in the merged module."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)

    # ConnectivityNode is in connectivity but not electrical
    assert 'ConnectivityNode' in merged.__all__
    assert hasattr(merged, 'ConnectivityNode')

    # PerLengthPhaseImpedance is in electrical but not connectivity
    assert 'PerLengthPhaseImpedance' in merged.__all__
    assert hasattr(merged, 'PerLengthPhaseImpedance')


def test_enums_preserved():
    """Enums like PhaseCode should be present and functional."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    PhaseCode = getattr(merged, 'PhaseCode')
    assert issubclass(PhaseCode, Enum)


def test_field_metadata_preserved():
    """Field metadata (namespace, serialize, inverse, etc.) should survive the merge."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    MergedACLineSegment = getattr(merged, 'ACLineSegment')

    # Check metadata on a field from electrical
    pli_field = MergedACLineSegment.__dataclass_fields__['PerLengthImpedance']
    assert 'namespace' in pli_field.metadata
    assert 'serialize' in pli_field.metadata
    assert 'inverse' in pli_field.metadata

    # Check metadata on a field from connectivity
    phases_field = MergedACLineSegment.__dataclass_fields__['ACLineSegmentPhases']
    assert 'namespace' in phases_field.metadata
    assert 'inverse' in phases_field.metadata


def test_merged_class_is_instantiable():
    """Merged dataclasses should be instantiable with default values."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    MergedACLineSegment = getattr(merged, 'ACLineSegment')

    obj = MergedACLineSegment(identifier='test-uuid-1234')
    assert obj.identifier is not None
    assert obj.ACLineSegmentPhases == []
    assert obj.PerLengthImpedance is None


def test_stereotype_preserved():
    """Classes with __stereotype__ should retain it after merging."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical)
    MergedACLineSegment = getattr(merged, 'ACLineSegment')
    assert hasattr(MergedACLineSegment, '__stereotype__')


def test_merge_requires_two_modules():
    """merge_profiles should raise ValueError with fewer than 2 modules."""
    from cimgraph.data_profile.cim18gmdm import connectivity
    from cimgraph.data_profile.merge import merge_profiles

    with pytest.raises(ValueError):
        merge_profiles(connectivity)


def test_merge_three_profiles():
    """Merging three sub-profiles should work."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical, location
    from cimgraph.data_profile.merge import merge_profiles

    merged = merge_profiles(connectivity, electrical, location)

    # All three should contribute classes
    conn_names = set(connectivity.__all__)
    elec_names = set(electrical.__all__)
    loc_names = set(location.__all__)
    merged_names = set(merged.__all__)

    assert conn_names.issubset(merged_names)
    assert elec_names.issubset(merged_names)
    assert loc_names.issubset(merged_names)


# ── Type-stub generation tests ─────────────────────────────────────────


def test_generate_type_stubs_creates_file(tmp_path):
    """generate_type_stubs writes a .py file that can be imported."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import generate_type_stubs

    out = tmp_path / 'cim_stubs.py'
    generate_type_stubs(connectivity, electrical, output_path=str(out))

    assert out.exists()
    content = out.read_text()
    assert 'from __future__ import annotations' in content
    assert '__all__' in content


def test_generate_type_stubs_has_all_names(tmp_path):
    """__all__ in the stub file should match merge_profiles output."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import generate_type_stubs, merge_profiles

    out = tmp_path / 'cim_stubs.py'
    generate_type_stubs(connectivity, electrical, output_path=str(out))

    merged = merge_profiles(connectivity, electrical)

    # Import the generated stub module
    sys.path.insert(0, str(tmp_path))
    try:
        stub_mod = importlib.import_module('cim_stubs')
        assert set(stub_mod.__all__) == set(merged.__all__)
    finally:
        sys.path.pop(0)
        sys.modules.pop('cim_stubs', None)


def test_generate_type_stubs_overlapping_classes(tmp_path):
    """Overlapping dataclasses should use multi-inheritance stub pattern."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import generate_type_stubs

    out = tmp_path / 'cim_stubs.py'
    generate_type_stubs(connectivity, electrical, output_path=str(out))

    content = out.read_text()
    # ACLineSegment is in both profiles — should be a multi-inherit class
    assert 'class ACLineSegment(' in content
    assert '_p0_ACLineSegment' in content
    assert '_p1_ACLineSegment' in content
    assert 'type: ignore[misc]' in content


def test_generate_type_stubs_non_overlapping_reexported(tmp_path):
    """Non-overlapping classes should be simple re-exports."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import generate_type_stubs

    out = tmp_path / 'cim_stubs.py'
    generate_type_stubs(connectivity, electrical, output_path=str(out))

    content = out.read_text()
    # ConnectivityNode is only in connectivity — should be a re-export
    assert 'import ConnectivityNode as ConnectivityNode' in content


def test_generate_type_stubs_importable(tmp_path):
    """The generated stub file should be importable without errors."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical
    from cimgraph.data_profile.merge import generate_type_stubs

    out = tmp_path / 'cim_stubs_import.py'
    generate_type_stubs(connectivity, electrical, output_path=str(out))

    sys.path.insert(0, str(tmp_path))
    try:
        stub_mod = importlib.import_module('cim_stubs_import')
        # Should have ACLineSegment as a class
        assert hasattr(stub_mod, 'ACLineSegment')
        assert isinstance(stub_mod.ACLineSegment, type)
        # Should have ConnectivityNode re-exported
        assert hasattr(stub_mod, 'ConnectivityNode')
    finally:
        sys.path.pop(0)
        sys.modules.pop('cim_stubs_import', None)


def test_generate_type_stubs_requires_two_modules():
    """generate_type_stubs should raise ValueError with fewer than 2 modules."""
    from cimgraph.data_profile.cim18gmdm import connectivity
    from cimgraph.data_profile.merge import generate_type_stubs

    with pytest.raises(ValueError):
        generate_type_stubs(connectivity, output_path='/dev/null')


def test_generate_type_stubs_three_profiles(tmp_path):
    """Stub generation should work with three profiles."""
    from cimgraph.data_profile.cim18gmdm import connectivity, electrical, location
    from cimgraph.data_profile.merge import generate_type_stubs

    out = tmp_path / 'cim_stubs_three.py'
    generate_type_stubs(connectivity, electrical, location, output_path=str(out))

    content = out.read_text()
    # ACLineSegment is in all three — should reference _p0, _p1, _p2
    assert '_p0_ACLineSegment' in content
    assert '_p1_ACLineSegment' in content
    assert '_p2_ACLineSegment' in content
