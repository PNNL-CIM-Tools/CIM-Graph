"""Unit tests for cimgraph.utils.mermaid class-diagram generation."""
import cimgraph.data_profile.cim17v40 as cim
from cimgraph import utils


def test_class_diagram_default_shows_reverse_associations():
    """Default (serialize_only=False) renders both forward and reverse associations."""
    out = utils.get_mermaid([cim.ACLineSegment, cim.ACLineSegmentPhase])

    # Forward attribute lines on ACLineSegment (structural attributes only — not associations)
    assert '+ r: float | Resistance' in out
    assert '+ x: float | Reactance' in out
    assert '+ b0ch: float | Susceptance' in out

    # ACLineSegment must NOT list associations as attribute lines
    assert '+ LineJumpingAction' not in out
    assert '+ PerLengthImpedance' not in out
    assert '+ WireSpacingInfo' not in out

    # ACLineSegmentPhase must NOT list its reverse-to-parent as an attribute line
    assert '+ ACLineSegment: ACLineSegment' not in out
    assert '+ WireInfo: WireInfo' not in out

    # Both association arrows present
    assert 'ACLineSegment --> "0..*" ACLineSegmentPhase : ACLineSegmentPhases' in out
    assert 'ACLineSegmentPhase --> "0..1" ACLineSegment : ACLineSegment' in out

    # Enum attribute rendered with enum: prefix
    assert '+ phase: enum:SinglePhaseKind' in out


def test_class_diagram_serialize_only_hides_reverse_ends():
    """serialize_only=True hides associations with metadata['serialize'] == False."""
    out = utils.get_mermaid(
        [cim.ACLineSegment, cim.ACLineSegmentPhase],
        serialize_only=True,
    )

    # Determine which end is the XML-roundtrippable one for this profile build
    forward_acls_phases = cim.ACLineSegment.__dataclass_fields__[
        'ACLineSegmentPhases'
    ].metadata.get('serialize', True)
    forward_phase_to_acls = cim.ACLineSegmentPhase.__dataclass_fields__[
        'ACLineSegment'
    ].metadata.get('serialize', True)

    if forward_acls_phases:
        assert 'ACLineSegment --> "0..*" ACLineSegmentPhase : ACLineSegmentPhases' in out
    else:
        assert 'ACLineSegmentPhases' not in out

    if forward_phase_to_acls:
        assert 'ACLineSegmentPhase --> "0..1" ACLineSegment : ACLineSegment' in out
    else:
        # Reverse-only side should be suppressed
        assert 'ACLineSegmentPhase --> "0..1" ACLineSegment' not in out

    # At least one direction must survive, otherwise the test setup is wrong
    assert forward_acls_phases or forward_phase_to_acls


def test_single_class_has_header_and_no_inherited_by_default():
    """Single-class diagram emits a classDiagram block with a class header."""
    out = utils.get_mermaid(cim.ACLineSegmentPhase)
    assert 'classDiagram' in out
    assert 'class ACLineSegmentPhase{' in out
    # Default show_inherited=False → don't list parent fields as attribute lines
    assert '+ mRID' not in out
