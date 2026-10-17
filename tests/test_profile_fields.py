from pathlib import Path

from cimgraph.data_profile.dedupe_profile_fields import PROFILE_ROOT, find_duplicates


def test_profiles_have_no_duplicate_fields():
    """Duplicate field definitions silently keep the last one (often serialize=False).
    Run cimgraph/data_profile/dedupe_profile_fields.py after regenerating profiles."""
    duplicates = []
    for path in sorted(Path(PROFILE_ROOT).rglob('*.py')):
        for dup in find_duplicates(path.read_text(encoding='utf-8')):
            duplicates.append(f"{path.relative_to(PROFILE_ROOT)} {dup['class']}.{dup['field']}")
    assert duplicates == []


def test_find_duplicates_prefers_serialized_definition():
    source = '''
class RatioTapChanger:
    TransformerEnd: Optional[TransformerEnd] = field(
        default=None,
        metadata={'inverse': 'TransformerEnd.RatioTapChanger', 'serialize': True})
    """own reference"""

    TransformerEnd: Optional[TransformerEnd] = field(
        default=None,
        metadata={'inverse': 'TransformerEnd.AdditionalRatioTapChanger', 'serialize': False})
    """inverse of a different association"""
'''
    (dup,) = find_duplicates(source)
    assert dup['kind'] == 'UML conflict'
    assert dup['keep']['serialize'] is True
    assert dup['drop'][0]['inverse'] == 'TransformerEnd.AdditionalRatioTapChanger'
