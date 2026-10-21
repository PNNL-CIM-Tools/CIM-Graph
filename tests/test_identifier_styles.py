"""Identifier formatting per IEC 61970-552 style, checked by reading a file and writing it back.

Every rdf:ID/rdf:about, rdf:resource and mRID written must be a string that was in the
source file: downstream tools and databases compare these as exact strings.
"""
import re
from pathlib import Path

import pytest

from cimgraph.core import get_cim_profile, get_iec61970_552
from cimgraph.databases import XMLFile
from cimgraph.models import FeederModel
from cimgraph.utils import write_xml

TEST_MODELS = Path(__file__).parent / 'test_models'

ID_PATTERN = re.compile(r'rdf:(?:ID|about)="([^"]*)"')
REFERENCE_PATTERN = re.compile(r'rdf:resource="([^"#]*#?[^"]*)"')
MRID_PATTERN = re.compile(r'<cim:IdentifiedObject\.mRID>([^<]*)<')

LINE = '1D4E3B4A-6C6F-4F35-9A3E-0D7E5B1C2A11'
TERMINAL = '9c1f0a7e-2b3d-4e5f-8a6b-7c8d9e0f1a2b'


def _rdf(objects: str) -> str:
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#" '
            'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
            f'{objects}</rdf:RDF>\n')


# 552-LEGACY with mixed case, as in GridAPPS-D: uppercase equipment, lowercase terminal
MIXED_CASE_LEGACY = _rdf(f'''<cim:ACLineSegment rdf:ID="_{LINE}">
  <cim:IdentifiedObject.mRID>_{LINE}</cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>650632</cim:IdentifiedObject.name>
</cim:ACLineSegment>
<cim:Terminal rdf:ID="_{TERMINAL}">
  <cim:IdentifiedObject.mRID>_{TERMINAL}</cim:IdentifiedObject.mRID>
  <cim:Terminal.ConductingEquipment rdf:resource="#_{LINE}"/>
</cim:Terminal>
''')

# CGMES: underscore in rdf:ID and references, none in the mRID
CGMES = _rdf(f'''<cim:ACLineSegment rdf:ID="_{LINE.lower()}">
  <cim:IdentifiedObject.mRID>{LINE.lower()}</cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>650632</cim:IdentifiedObject.name>
</cim:ACLineSegment>
<cim:Terminal rdf:ID="_{TERMINAL}">
  <cim:IdentifiedObject.mRID>{TERMINAL}</cim:IdentifiedObject.mRID>
  <cim:Terminal.ConductingEquipment rdf:resource="#_{LINE.lower()}"/>
</cim:Terminal>
''')


@pytest.fixture
def use_style(monkeypatch):
    def use(style: str) -> None:
        monkeypatch.setenv('CIMG_IEC61970_552', style)
        monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
        get_iec61970_552.cache_clear()
        get_cim_profile.cache_clear()
    yield use
    get_iec61970_552.cache_clear()
    get_cim_profile.cache_clear()


def _identifier_strings(text: str) -> tuple[set, set, set]:
    references = {r for r in REFERENCE_PATTERN.findall(text) if not r.startswith('http')}
    return set(ID_PATTERN.findall(text)), references, set(MRID_PATTERN.findall(text))


def _write_back(source: Path, tmp_path: Path) -> str:
    network = FeederModel(container=None, connection=XMLFile(filename=str(source)))
    out = tmp_path / 'round_trip.xml'
    write_xml(network, str(out), write_model_header=False)
    return out.read_text(encoding='utf-8')


def _assert_written_strings_come_from(source_text: str, written_text: str) -> None:
    source_ids, source_references, source_mrids = _identifier_strings(source_text)
    written_ids, written_references, written_mrids = _identifier_strings(written_text)
    # The writer also emits association ends the source left out, so a reference may
    # point at any source object, spelled as the source spells references to it
    referable = source_references | {i if i.startswith('urn:uuid:') else '#' + i
                                     for i in source_ids}
    assert written_ids, 'nothing was written'
    assert written_ids <= source_ids, sorted(written_ids - source_ids)[:5]
    assert written_references <= referable, sorted(written_references - referable)[:5]
    assert written_mrids <= source_mrids, sorted(written_mrids - source_mrids)[:5]


@pytest.mark.parametrize('fixture, style', [
    ('IEEE123.xml', '552-LEGACY'),
    ('maple10nodebreaker.xml', '552-LEGACY'),
    ('ieee13.xml', '552-NEW'),
    ('IEEE118_CIM.xml', '552-NEW'),
])
def test_fixture_round_trip_keeps_identifier_strings(fixture, style, use_style, tmp_path):
    use_style(style)
    source = TEST_MODELS / fixture
    _assert_written_strings_come_from(source.read_text(encoding='utf-8'),
                                      _write_back(source, tmp_path))


@pytest.mark.parametrize('text, style', [(MIXED_CASE_LEGACY, '552-LEGACY'), (CGMES, 'CGMES')],
                         ids=['mixed-case-legacy', 'cgmes'])
def test_synthetic_round_trip_keeps_identifier_strings(text, style, use_style, tmp_path):
    use_style(style)
    source = tmp_path / 'source.xml'
    source.write_text(text, encoding='utf-8')
    written = _write_back(source, tmp_path)

    _assert_written_strings_come_from(text, written)
    assert f'rdf:ID="_{LINE if style == "552-LEGACY" else LINE.lower()}"' in written
    assert f'rdf:ID="_{TERMINAL}"' in written


def test_legacy_file_written_as_552_new_has_no_underscores(use_style, tmp_path):
    use_style('552-NEW')
    written = _write_back(TEST_MODELS / 'IEEE123.xml', tmp_path)

    assert 'urn:uuid:_' not in written
    ids, references, mrids = _identifier_strings(written)
    assert all(i.startswith('urn:uuid:') for i in ids)
    assert not [m for m in mrids if m.startswith('_')]


def test_unknown_style_is_rejected(monkeypatch):
    monkeypatch.setenv('CIMG_IEC61970_552', '552-OLD')
    get_iec61970_552.cache_clear()
    with pytest.raises(ValueError, match="'552-NEW', '552-LEGACY', 'CGMES'"):
        get_iec61970_552()
    get_iec61970_552.cache_clear()
