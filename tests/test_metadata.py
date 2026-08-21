"""Tests for the IEC 61970-552/-557 metadata-graph reader and XMLFile wiring."""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from cimgraph.databases.fileparsers.metadata import parse_metadata, resolve_part_paths

_MODELS = Path(__file__).parent / 'test_models'
_METADATA = _MODELS / 'ieee13_metadata.cimx'


# ── reader ──────────────────────────────────────────────────────────────


def test_parse_metadata_reads_distributions():
    meta = parse_metadata(_METADATA)

    assert meta.full_model_uuid == 'urn:uuid:00000000-0000-0000-0000-00000000ieee13'
    assert len(meta.distributions) == 2

    urls = {d.access_url for d in meta.distributions}
    assert urls == {'ieee13.xml', 'ieee13_assets.xml'}

    # conformsTo is carried verbatim as an opaque profile IRI.
    eq = next(d for d in meta.distributions if d.access_url == 'ieee13.xml')
    assert eq.conforms_to == [
        'https://github.com/PNNL-CIM-Tools/CIM-Graph/profiles/equipment/v1'
    ]


def test_parse_metadata_accepts_bytes():
    meta = parse_metadata(_METADATA.read_bytes())
    assert len(meta.distributions) == 2


def test_resolve_part_paths_relative_to_metadata_dir():
    meta = parse_metadata(_METADATA)
    paths = resolve_part_paths(meta, _METADATA.parent)

    assert [p.name for p in paths] == ['ieee13.xml', 'ieee13_assets.xml']
    assert all(p.exists() for p in paths)


def test_resolve_part_paths_missing_file_fails_fast(tmp_path):
    meta = parse_metadata(_METADATA)
    with pytest.raises(FileNotFoundError):
        # Resolving against an empty dir: the part files are not there.
        resolve_part_paths(meta, tmp_path)


def test_resolve_part_paths_skips_external_urls(caplog):
    from cimgraph.databases.fileparsers.metadata import Distribution, MetadataGraph
    meta = MetadataGraph(distributions=[
        Distribution(uuid='x', access_url='https://example.com/remote_EQ.xml'),
    ])
    paths = resolve_part_paths(meta, _MODELS)
    assert paths == []


# ── XMLFile integration ─────────────────────────────────────────────────


@pytest.fixture
def cim_profile_env():
    original = os.getenv('CIMG_CIM_PROFILE')
    os.environ['CIMG_CIM_PROFILE'] = 'cimhub_2023'
    yield
    if original is not None:
        os.environ['CIMG_CIM_PROFILE'] = original
    else:
        os.environ.pop('CIMG_CIM_PROFILE', None)


def test_xmlfile_metadata_loads_all_parts_into_one_graph(cim_profile_env):
    """XMLFile(metadata=...) loads every referenced part into one graph."""
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel

    file = XMLFile(metadata=str(_METADATA))

    # The metadata graph is exposed for provenance / profile hints.
    assert file.metadata_graph is not None
    assert len(file.metadata_graph.distributions) == 2

    network = FeederModel(container=None, connection=file)
    type_names = {c.__name__ for c in network.graph}

    # Breaker is only in the equipment part; OverheadWireInfo only in assets.
    # Both present => both files accumulated into the one graph.
    assert 'Breaker' in type_names
    assert 'OverheadWireInfo' in type_names


def test_xmlfile_single_filename_still_works(cim_profile_env):
    """The metadata path must not regress plain single-file reads."""
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel

    file = XMLFile(filename=str(_MODELS / 'ieee13.xml'))
    assert file.metadata_graph is None
    network = FeederModel(container=None, connection=file)
    assert len(network.graph) > 0
