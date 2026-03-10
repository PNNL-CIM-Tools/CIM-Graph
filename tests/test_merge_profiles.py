"""Tests for runtime CIM profile merging."""
from __future__ import annotations

import dataclasses
from dataclasses import fields, is_dataclass
from enum import Enum

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
