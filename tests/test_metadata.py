"""Tests for the package metadata reader (ENTSO-E DCAT layout, and the earlier 557 sketch) and XMLFile wiring."""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from cimgraph.databases.fileparsers.metadata import (Distribution, MetadataGraph, parse_metadata,
                                                     resolve_part_paths)

_MODELS = Path(__file__).parent / 'test_models'
_METADATA = _MODELS / 'ieee13_metadata.cimx'      # the earlier 557 sketch's vocabulary
_MANIFEST = _MODELS / 'ieee13_manifest.xml'       # ENTSO-E layout, cim18v17 metadata classes
_UUID = 'urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000'
RDF_XML = 'https://www.iana.org/assignments/media-types/application/rdf+xml'


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


def test_resolve_part_paths_skips_external_urls():
    meta = MetadataGraph(distributions=[
        Distribution(uuid='x', access_url='https://example.com/remote_EQ.xml', media_type=RDF_XML),
        Distribution(uuid='y', access_url='ieee13.xml', media_type=RDF_XML),
    ])
    assert [p.name for p in resolve_part_paths(meta, _MODELS)] == ['ieee13.xml']


def test_parse_entsoe_manifest():
    meta = parse_metadata(_MANIFEST)

    assert meta.catalog_uuid == _UUID + '100'
    frame, boundary = meta.datasets
    assert frame.types == ['Dataset', 'FrameModel'] and boundary.types == ['Dataset', 'BoundaryModel']
    assert (frame.identifier, frame.title, frame.issued, frame.version) == (
        '7b1e0c2a-1d3f-4b6e-9a51-000000000101', 'IEEE 13 feeder', '2026-11-16T00:00:00Z', '1.0.0')
    assert frame.spatial == _UUID + '110' and frame.requires == [_UUID + '102']
    assert frame.cim_properties == {'FrameModel.represents': [_UUID + '110'],
                                    'FrameModel.perimeter': [_UUID + '102']}
    assert [(r.cim_class, r.cim_properties) for r in meta.grid_resources] == [
        ('Frame', {'Frame.connectsTo': [_UUID + '111']}), ('Boundary', {'Boundary.separates': [_UUID + '110']})]

    eq = meta.distributions[0]
    assert (eq.access_url, eq.media_type, eq.byte_size) == ('file://ieee13.xml', RDF_XML, 293948)
    assert eq.checksum == 'a4e2b3d3bcdfc88d07252f0f00a8935f2cb1e8cb0bc3c9bdc399d35635a79ca7'
    assert eq.checksum_algorithm == 'http://spdx.org/rdf/terms#checksumAlgorithm_sha256'
    assert eq.conforms_to == ['urn:iso:std:iec:61970-552:2016']
    # dcat:distribution on the dataset links every file to it
    assert {d.dataset_uuid for d in meta.distributions} == {frame.uuid}


def test_resolve_part_paths_loads_only_rdf_xml_parts():
    """file:// package paths and relative IRIs; the JSON-LD and .cimtbl files are skipped."""
    paths = resolve_part_paths(parse_metadata(_MANIFEST), _MANIFEST.parent)
    assert [p.name for p in paths] == ['ieee13.xml', 'ieee13_assets.xml']


def test_file_url_first_segment_is_a_directory(tmp_path):
    """file://BoundaryData/EQBD.xml, as the ENTSO-E specification writes it: BoundaryData is not a host."""
    (tmp_path / 'BoundaryData').mkdir()
    (tmp_path / 'BoundaryData' / 'EQBD.xml').write_text('<rdf:RDF/>')
    meta = MetadataGraph(distributions=[
        Distribution(uuid='d', access_url='file://BoundaryData/EQBD.xml', media_type='application/rdf+xml')])
    assert resolve_part_paths(meta, tmp_path) == [(tmp_path / 'BoundaryData' / 'EQBD.xml').resolve()]


def test_metadata_without_local_rdf_xml_parts_fails():
    """XMLFile(metadata=...) must not load an empty graph silently."""
    meta = MetadataGraph(distributions=[
        Distribution(uuid='x', access_url='https://example.com/remote_EQ.xml', media_type=RDF_XML),
        Distribution(uuid='y', access_url='ieee13.jsonld', media_type='application/ld+json')])
    with pytest.raises(ValueError, match='no local RDF/XML file'):
        resolve_part_paths(meta, _MODELS)
    with pytest.raises(ValueError, match='no local RDF/XML file'):
        resolve_part_paths(MetadataGraph(), _MODELS)


def test_rdf_xml_part_without_access_url_fails():
    meta = MetadataGraph(distributions=[Distribution(uuid='d', media_type=RDF_XML)])
    with pytest.raises(ValueError, match='has no accessURL'):
        resolve_part_paths(meta, _MODELS)


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


def test_xmlfile_entsoe_manifest_loads_its_rdf_xml_parts(cim_profile_env):
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel

    file = XMLFile(metadata=str(_MANIFEST))
    assert len(file.metadata_graph.distributions) == 4
    network = FeederModel(container=None, connection=file)
    type_names = {c.__name__ for c in network.graph}
    assert {'Breaker', 'OverheadWireInfo'} <= type_names
