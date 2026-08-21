"""Read an IEC 61970-552/-557 model-metadata graph (bare RDF/XML).

A 557 model is split across several RDF/XML parts (EQ, SSH, TP, boundary, ...)
that together describe one network.  The *metadata graph* ties them together:
an ``<rdf:RDF>`` document listing each part as a ``dcat:Distribution`` (with an
``accessURL``, ``checksum``, ``mediaType`` and ``conformsTo`` profile IRIs),
plus ``md:FullModel`` / ``cim:BoundaryModel`` / ``cim:GridDataset`` nodes.

This module reads that bare graph (NOT the OPC ZIP ``.cimx`` container — that
is handled upstream in cimloader).  ``XMLFile`` uses :func:`resolve_part_paths`
to turn the distributions into a list of local files and load them all into one
in-memory graph.

The parse mirrors cimloader's ``downloaders/opc.py::parse_business_metadata`` so
the two can converge on this (lower-layer) implementation later — but it is kept
dependency-free here on purpose.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

from defusedxml.ElementTree import fromstring, parse

_log = logging.getLogger(__name__)

# Namespace URIs for the 552 ModelDescription/3 metadata serialization.
_NS = {
    'rdf':     'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'md':      'http://iec.ch/TC57/61970-552/ModelDescription/3#',
    'cim':     'http://cim.ucaiug.io/ns#',
    'dcat':    'http://www.w3.org/ns/dcat#',
    'dcterms': 'http://purl.org/dc/terms/',
    'spdx':    'http://spdx.org/rdf/terms#',
}


def _tag(prefix: str, local: str) -> str:
    return f'{{{_NS[prefix]}}}{local}'


def _about(el) -> str:
    return el.attrib.get(_tag('rdf', 'about'), '')


def _resource(el) -> str:
    return el.attrib.get(_tag('rdf', 'resource'), '')


@dataclass
class Distribution:
    """One ``dcat:Distribution`` — a physical part file of the model.

    ``conforms_to`` holds the profile IRIs verbatim; they are opaque profile
    identifiers (compared for equality, never dereferenced).
    """

    uuid: str
    access_url: str | None = None
    media_type: str | None = None
    checksum: str | None = None
    byte_size: str | None = None
    conforms_to: list[str] = field(default_factory=list)
    dataset_uuid: str | None = None


@dataclass
class MetadataGraph:
    """Parsed 552 metadata graph: the model identity, its parts, and datasets."""

    full_model_uuid: str | None = None
    distributions: list[Distribution] = field(default_factory=list)
    datasets: list[dict] = field(default_factory=list)


def parse_metadata(source: str | Path | bytes) -> MetadataGraph:
    """Parse a bare 552 metadata RDF/XML graph.

    Args:
        source: path to the metadata file, or its raw XML bytes.

    Returns:
        A :class:`MetadataGraph` with the FullModel identity, the list of
        distributions (parts), and the dataset nodes.
    """
    if isinstance(source, bytes):
        root = fromstring(source)
    else:
        root = parse(str(source)).getroot()

    meta = MetadataGraph()

    for el in root:
        tag = el.tag

        if tag == _tag('md', 'FullModel'):
            meta.full_model_uuid = _about(el)

        elif tag == _tag('dcat', 'Distribution'):
            dist = Distribution(uuid=_about(el))
            for child in el:
                ctag = child.tag
                if ctag == _tag('dcat', 'Distribution.accessURL'):
                    dist.access_url = (child.text or '').strip()
                elif ctag == _tag('dcat', 'Distribution.byteSize'):
                    dist.byte_size = (child.text or '').strip()
                elif ctag == _tag('dcat', 'Distribution.mediaType'):
                    dist.media_type = (child.text or '').strip()
                elif ctag == _tag('spdx', 'Distribution.checksum'):
                    dist.checksum = (child.text or '').strip()
                elif ctag == _tag('dcterms', 'Distribution.conformsTo'):
                    dist.conforms_to.append(_resource(child))
                elif ctag == _tag('dcat', 'Distribution.DataSet'):
                    dist.dataset_uuid = _resource(child)
            meta.distributions.append(dist)

        elif tag in (_tag('cim', 'BoundaryModel'), _tag('cim', 'GridDataset')):
            ds: dict = {'uuid': _about(el), 'contains': []}
            for child in el:
                ctag = child.tag
                if ctag == _tag('dcterms', 'MetaThing.title'):
                    ds['title'] = (child.text or '').strip()
                elif ctag == _tag('dcterms', 'Distribution.issued'):
                    ds['issued'] = (child.text or '').strip()
                elif ctag == _tag('cim', 'GridDataset.profileType'):
                    ds['profile_type'] = (child.text or '').strip()
                elif ctag == _tag('cim', 'BoundaryModel.Defines'):
                    ds['defines_uuid'] = _resource(child)
                elif ctag == _tag('cim', 'GridDataset.Contains'):
                    ds['contains'].append(_resource(child))
            meta.datasets.append(ds)

    return meta


def resolve_part_paths(meta: MetadataGraph, base_dir: str | Path) -> list[Path]:
    """Resolve each distribution's ``accessURL`` to a local part file.

    Part files sit beside the metadata file (the 557 package convention), so
    each ``accessURL`` is resolved relative to *base_dir* — the directory of the
    metadata file.  ``accessURL`` may use Windows-style separators
    (``\\contents\\Foo_EQ.xml``); they are normalized.

    External ``http(s)://`` URLs are skipped with a warning — network fetch is
    out of scope here (that belongs to cimloader's downloader).

    Args:
        meta: a parsed :class:`MetadataGraph`.
        base_dir: directory the metadata file lives in.

    Returns:
        Existing local part paths, in distribution order.

    Raises:
        FileNotFoundError: if a resolved local part file does not exist.
    """
    base = Path(base_dir)
    paths: list[Path] = []

    for dist in meta.distributions:
        url = dist.access_url
        if not url:
            _log.warning('Distribution %s has no accessURL; skipping', dist.uuid)
            continue

        if url.lower().startswith(('http://', 'https://')):
            _log.warning(
                'Distribution %s accessURL %r is external; network fetch is not '
                'supported here. Skipping.', dist.uuid, url,
            )
            continue

        # Normalize Windows separators and strip any leading slashes so the URL
        # resolves relative to the metadata file's directory.
        relative = url.replace('\\', '/').lstrip('/')
        part_path = (base / relative).resolve()
        if not part_path.exists():
            raise FileNotFoundError(
                f'Metadata distribution {dist.uuid} references {url!r}, resolved '
                f'to {part_path}, which does not exist'
            )
        paths.append(part_path)

    return paths
