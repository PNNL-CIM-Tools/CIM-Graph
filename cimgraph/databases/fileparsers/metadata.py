"""Read the metadata of a CIM model package (RDF/XML) and the header of a CIMXML part file.

A model may be split across several part files (EQ, SSH, TP, boundary, ...). The package's
*metadata graph* lists them in the plain DCAT layout of the ENTSO-E Metadata for Dataset and
Distribution Specification (v2.4.0): a ``dcat:Catalog`` of ``dcat:Dataset`` nodes, each with
its ``dcat:Distribution`` files (``dcat:accessURL``, ``dcat:mediaType``, ``spdx:checksum``,
``dcterms:conformsTo``). The grid kind of a dataset is an ``rdf:type`` (or the element name):
``cim:FrameModel``, ``cim:BoundaryModel``, ``cim:GridAssembly``, ... of the cim18v17 metadata
profile, with their ``cim:Frame`` and ``cim:Boundary`` resources.

One fallback, for the earlier 557 metadata sketch (``ieee13_metadata.cimx``, 9500node.cimx):
DCAT, Dublin Core and SPDX properties written with a class prefix
(``dcat:Distribution.accessURL``, ``dcterms:MetaThing.title``) are read as the plain terms
(``dcat:accessURL``, ``dcterms:title``), and its ``dcat:Distribution.DataSet`` as the
distribution's dataset.

This module reads that bare graph (NOT the OPC ZIP ``.cimx`` container, which cimloader
handles). ``XMLFile`` uses :func:`resolve_part_paths` to turn its RDF/XML distributions into
local files and load them all into one in-memory graph.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from urllib.parse import unquote, urlsplit

from cimprofiles.identity import model_authority_namespace
from defusedxml.ElementTree import fromstring, parse

from cimgraph.core import get_authority_from_is_version_of, get_model_name, set_model_scope

_log = logging.getLogger(__name__)

RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
DCAT = 'http://www.w3.org/ns/dcat#'
DCTERMS = 'http://purl.org/dc/terms/'
SPDX = 'http://spdx.org/rdf/terms#'
# The cim18v17 metadata namespace, and the one of the earlier 557 sketch
CIM_METADATA_NAMESPACES = ('http://cim.ucaiug.io/cim101/draft#', 'http://cim.ucaiug.io/ns#')
# The cim18v17 metadata classes that are datasets (dcat:Dataset and its specializations)
DATASET_CLASSES = ('Dataset', 'FrameworkEdition', 'GridAssembly', 'GridDataset', 'GridModel',
                   'BoundaryModel', 'EdgeModel', 'EquivalentModel', 'FrameModel', 'NonAlignedModel')
GRID_RESOURCE_CLASSES = ('Frame', 'Boundary')
_RDF_ABOUT = f'{{{RDF}}}about'
_RDF_ID = f'{{{RDF}}}ID'
_RDF_RESOURCE = f'{{{RDF}}}resource'
_RDF_DESCRIPTION = f'{{{RDF}}}Description'


@dataclass
class Distribution:
    """One ``dcat:Distribution``: a file of the package.

    ``conforms_to`` holds the ``dcterms:conformsTo`` IRIs verbatim (serialisation standards,
    profile contexts, units vocabularies); they are compared, never dereferenced.
    """

    uuid: str
    access_url: str | None = None
    media_type: str | None = None
    checksum: str | None = None
    checksum_algorithm: str | None = None
    byte_size: int | None = None
    conforms_to: list[str] = field(default_factory=list)
    dataset_uuid: str | None = None


@dataclass
class Dataset:
    """One ``dcat:Dataset`` (or cim18v17 dataset class) of the metadata graph.

    ``types`` are the local class names (``['Dataset', 'FrameModel']``). ``cim_properties``
    holds the cim properties by name, e.g. ``{'FrameModel.perimeter': [iri, ...],
    'GridModel.usedIn': [iri]}``.
    """

    uuid: str
    types: list[str] = field(default_factory=list)
    identifier: str | None = None
    title: str | None = None
    issued: str | None = None
    version: str | None = None
    spatial: str | None = None
    requires: list[str] = field(default_factory=list)
    distributions: list[str] = field(default_factory=list)
    cim_properties: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class GridResource:
    """A ``cim:Frame`` or ``cim:Boundary`` the datasets refer to, with its cim properties
    (``Frame.connectsTo``, ``Frame.includedIn``, ``Boundary.separates``)."""

    uuid: str
    cim_class: str
    cim_properties: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class MetadataGraph:
    """Parsed metadata graph: the catalog (or md:FullModel) identity, files, datasets, frames and boundaries."""

    full_model_uuid: str | None = None
    catalog_uuid: str | None = None
    distributions: list[Distribution] = field(default_factory=list)
    datasets: list[Dataset] = field(default_factory=list)
    grid_resources: list[GridResource] = field(default_factory=list)


@dataclass
class _Node:
    """One RDF resource of the graph: full type IRIs and {property key: [IRI, text or node IRI]}."""

    iri: str
    types: list[str] = field(default_factory=list)
    properties: dict[str, list[str]] = field(default_factory=dict)


def _split(tag: str) -> tuple[str, str]:
    """'{namespace}local' -> (namespace, local)."""
    namespace, _, local = tag[1:].partition('}')
    return namespace, local


def _property_key(tag: str) -> str:
    """
    The full IRI of a property element. Outside the cim namespaces a class prefix is dropped
    (the 557 sketch's ``dcat:Distribution.accessURL`` is ``dcat:accessURL``); cim properties
    keep theirs (``cim:FrameModel.perimeter``).
    """
    namespace, local = _split(tag)
    if namespace not in CIM_METADATA_NAMESPACES:
        local = local.rpartition('.')[2]
    return namespace + local


def _read_node(element, nodes: dict[str, _Node]) -> str:
    """Read an RDF/XML node element, and the nodes nested in its properties, into `nodes`; return its IRI."""
    iri = element.get(_RDF_ABOUT) or element.get(_RDF_ID) or f'_:b{len(nodes)}'
    node = nodes.setdefault(iri, _Node(iri))
    if element.tag != _RDF_DESCRIPTION:
        namespace, local = _split(element.tag)
        node.types.append(namespace + local)
    for child in element:
        key = _property_key(child.tag)
        if child.get(_RDF_RESOURCE) is not None:
            value = child.get(_RDF_RESOURCE)
        elif len(child):
            value = _read_node(child[0], nodes)
        else:
            value = (child.text or '').strip()
        if key == RDF + 'type':
            node.types.append(value)
        else:
            node.properties.setdefault(key, []).append(value)
    return iri


def _first(node: _Node, key: str) -> str | None:
    values = node.properties.get(key)
    return values[0] if values else None


def _cim_properties(node: _Node) -> dict[str, list[str]]:
    """{'FrameModel.perimeter': [...]} of a node's cim properties."""
    properties = {}
    for key, values in node.properties.items():
        for namespace in CIM_METADATA_NAMESPACES:
            if key.startswith(namespace):
                properties[key[len(namespace):]] = values
    return properties


def _cim_classes(node: _Node) -> list[str]:
    """The local names of a node's types in a cim metadata namespace."""
    return [iri[len(namespace):] for iri in node.types for namespace in CIM_METADATA_NAMESPACES
            if iri.startswith(namespace)]


def _distribution(node: _Node, nodes: dict[str, _Node]) -> Distribution:
    distribution = Distribution(uuid=node.iri, access_url=_first(node, DCAT + 'accessURL'),
                                media_type=_first(node, DCAT + 'mediaType'),
                                conforms_to=node.properties.get(DCTERMS + 'conformsTo', []),
                                # cim18v17 Distribution.realizes, else the 557 sketch's Distribution.DataSet
                                dataset_uuid=_first(node, DCAT + 'realizes') or _first(node, DCAT + 'DataSet'))
    byte_size = _first(node, DCAT + 'byteSize')
    if byte_size is not None:
        distribution.byte_size = int(byte_size)
    checksum = _first(node, SPDX + 'checksum')
    if checksum in nodes:  # an spdx:Checksum node
        distribution.checksum = _first(nodes[checksum], SPDX + 'checksumValue')
        distribution.checksum_algorithm = _first(nodes[checksum], SPDX + 'algorithm')
    else:  # the 557 sketch writes the value as text
        distribution.checksum = checksum
    return distribution


def _dataset(node: _Node) -> Dataset:
    types = [iri.rpartition('#')[2] for iri in node.types]
    return Dataset(uuid=node.iri, types=types, identifier=_first(node, DCTERMS + 'identifier'),
                   title=_first(node, DCTERMS + 'title'), issued=_first(node, DCTERMS + 'issued'),
                   version=_first(node, DCAT + 'version'), spatial=_first(node, DCTERMS + 'spatial'),
                   requires=node.properties.get(DCTERMS + 'requires', []),
                   # dcat:distribution, or cim18v17's Dataset.isRealizedAs
                   distributions=(node.properties.get(DCAT + 'distribution', [])
                                  + node.properties.get(DCAT + 'isRealizedAs', [])),
                   cim_properties=_cim_properties(node))


def parse_metadata(source: str | Path | bytes) -> MetadataGraph:
    """Parse a package's metadata graph (RDF/XML).

    Args:
        source: path to the metadata file, or its raw XML bytes.

    Returns:
        A :class:`MetadataGraph` with the catalog (or md:FullModel) identity, the
        distributions (files) with their datasets, the datasets, and the frames and boundaries.
    """
    root = fromstring(source) if isinstance(source, bytes) else parse(str(source)).getroot()
    nodes: dict[str, _Node] = {}
    for element in root:
        _read_node(element, nodes)

    meta = MetadataGraph()
    for node in nodes.values():
        cim_classes = _cim_classes(node)
        if any(iri.rpartition('#')[2] == 'FullModel' for iri in node.types):
            meta.full_model_uuid = node.iri
        elif DCAT + 'Catalog' in node.types:
            meta.catalog_uuid = node.iri
        elif DCAT + 'Distribution' in node.types:
            meta.distributions.append(_distribution(node, nodes))
        elif DCAT + 'Dataset' in node.types or any(name in DATASET_CLASSES for name in cim_classes):
            meta.datasets.append(_dataset(node))
        elif any(name in GRID_RESOURCE_CLASSES for name in cim_classes):
            (cim_class,) = (name for name in cim_classes if name in GRID_RESOURCE_CLASSES)
            meta.grid_resources.append(GridResource(node.iri, cim_class, _cim_properties(node)))

    # A dataset's dcat:distribution links its files to it, as Distribution.realizes does
    distributions = {distribution.uuid: distribution for distribution in meta.distributions}
    for dataset in meta.datasets:
        for uuid in dataset.distributions:
            if uuid in distributions and distributions[uuid].dataset_uuid is None:
                distributions[uuid].dataset_uuid = dataset.uuid
    return meta


def _is_rdf_xml(distribution: Distribution) -> bool:
    """True for an RDF/XML file: media type application/rdf+xml, as a text, an IANA IRI or
    the 557 sketch's 'rdf+xml'."""
    return distribution.media_type is not None and distribution.media_type.rsplit('/', 1)[-1] == 'rdf+xml'


def _local_path(url: str) -> str:
    """
    The package path of an accessURL. ``file://`` URLs are package paths, as the ENTSO-E
    specification writes them (``file://BoundaryData/EQBDxml.zip``): the first segment, which
    URL parsing reads as the host, is the first directory.
    """
    if url.lower().startswith('file:'):
        parts = urlsplit(url)
        url = unquote(parts.netloc + parts.path)
    # Windows separators (\\contents\\Foo_EQ.xml) and leading slashes: relative to the package
    return url.replace('\\', '/').lstrip('/')


def resolve_part_paths(meta: MetadataGraph, base_dir: str | Path) -> list[Path]:
    """Resolve the RDF/XML distributions of a metadata graph to local part files.

    Part files sit beside the metadata file (the package convention), so each ``accessURL``
    (a relative IRI or ``file://`` package path) is resolved relative to *base_dir*, the
    directory of the metadata file. Distributions in other formats (.cimtbl, JSON-LD) are
    skipped. External ``http(s)://`` URLs are skipped with a warning: network fetch is out of
    scope here (that belongs to cimloader's downloader). A file listed twice is loaded once.

    Args:
        meta: a parsed :class:`MetadataGraph`.
        base_dir: directory the metadata file lives in.

    Returns:
        Existing local part paths, in distribution order.

    Raises:
        ValueError: if an RDF/XML distribution has no accessURL, an ``accessURL`` resolves
            outside *base_dir*, or the metadata lists no local RDF/XML file at all.
        FileNotFoundError: if a resolved local part file does not exist.
    """
    base = Path(base_dir)
    paths: list[Path] = []

    for dist in meta.distributions:
        if not _is_rdf_xml(dist):
            _log.debug('Distribution %s (%s) is not RDF/XML; skipping', dist.uuid, dist.media_type)
            continue
        url = dist.access_url
        if not url:
            raise ValueError(f'Metadata distribution {dist.uuid} has no accessURL')
        if url.lower().startswith(('http://', 'https://')):
            _log.warning(
                'Distribution %s accessURL %r is external; network fetch is not '
                'supported here. Skipping.', dist.uuid, url,
            )
            continue

        part_path = (base / _local_path(url)).resolve()
        # Checked before exists() so a crafted accessURL can neither load nor probe
        # files outside the metadata file's directory.
        if not part_path.is_relative_to(base.resolve()):
            raise ValueError(
                f'Metadata distribution {dist.uuid} accessURL {url!r} points outside '
                f'the metadata directory {base}'
            )
        if not part_path.exists():
            raise FileNotFoundError(
                f'Metadata distribution {dist.uuid} references {url!r}, resolved '
                f'to {part_path}, which does not exist'
            )
        if part_path not in paths:
            paths.append(part_path)

    if not paths:
        media_types = sorted({str(dist.media_type) for dist in meta.distributions})
        raise ValueError(f'The metadata lists no local RDF/XML file to load: {len(meta.distributions)} '
                         f'distributions, media types {media_types}')
    return paths


# Local names of the 552 header elements at the top of a CIMXML part file.
# Matched by local name so ModelDescription/1# (CGMES 2.4, cimgraph) and /3# both work.
HEADER_CLASSES = ('FullModel', 'ModelAuthority')


def is_profile_class(cim: ModuleType, namespace: str, local: str) -> bool:
    """Whether the profile declares the class local in namespace, such as dct:PeriodOfTime."""
    if local not in cim.__all__:
        return False
    # __namespace__ is a property that returns its class's namespace: read it without an object
    class_namespace = getattr(getattr(cim, local), '__namespace__', None)
    return isinstance(class_namespace, property) and class_namespace.fget(None) == namespace


def is_header_element(element, cim: ModuleType) -> bool:
    """
    True for the header elements of a CIMXML part file, which are not CIM objects: md:FullModel,
    cim:ModelAuthority, and the dcat:Dataset header (with any other DCAT / Dublin Core element)
    of the ENTSO-E metadata layout. A class the profile declares in the element's namespace
    (gad:ModelAuthority, dct:PeriodOfTime) is an object.
    """
    namespace, local = _split(element.tag)
    if local not in HEADER_CLASSES and namespace not in (DCAT, DCTERMS):
        return False
    return not is_profile_class(cim, namespace, local)


@dataclass
class ModelHeader:
    """The header of one CIMXML part file: ``md:FullModel`` and ``cim:ModelAuthority``, or ``dcat:Dataset``.

    ``description`` is ``md:Model.description``, or a dcat:Dataset's ``dct:title`` (under the
    ENTSO-E rules, its file name). ``model_name`` is the model name UUIDs are seeded with:
    ``md:Model.description``, and None for a dcat:Dataset, which keeps the current one.
    """

    full_model_uuid: str | None = None
    created: str | None = None
    description: str | None = None
    model_name: str | None = None
    authority: str | None = None
    authority_uuid: str | None = None


def use_model_scope(header: ModelHeader) -> None:
    """Set the model scope from a file's header if it names an authority, so UUIDs seeded
    from the file's non-UUID IDs use the authority that issued them. A header without a
    model name (a dcat:Dataset) keeps the current model name."""
    if header.authority is not None:
        model_name = get_model_name() if header.model_name is None else header.model_name
        set_model_scope(header.authority, model_name)


def dataset_authority(dataset: str | None, authority_set: str | None, is_version_of: str | None) -> str | None:
    """
    The model authority of a dcat:Dataset header: its md:Model.modelingAuthoritySet.
    dcat:isVersionOf names the model series, not an authority, so it is read as one only
    with CIMG_AUTHORITY_FROM_IS_VERSION_OF=true (CGMES files such as Nordic44 put the
    modeling authority set there). Without an authority the model scope stays as it is,
    with a warning.
    """
    if authority_set is not None:
        return authority_set
    if is_version_of is not None and get_authority_from_is_version_of():
        return is_version_of
    _log.warning('dcat:Dataset header %s has no md:Model.modelingAuthoritySet; the model scope stays '
                 'as it is (set CIMG_AUTHORITY_FROM_IS_VERSION_OF=true to take it from dcat:isVersionOf %r)',
                 dataset, is_version_of)
    return None


def _local_name(tag: str) -> str:
    return tag.split('}')[-1]


def _header_uuid(el) -> str | None:
    """UUID of a header element written as rdf:about="urn:uuid:..." (552-NEW) or rdf:ID (552-OLD)."""
    uri = el.attrib.get(_RDF_ABOUT) or el.attrib.get(_RDF_ID, '')
    return uri.split(':')[-1].lstrip('#_') or None


def _child_values(el) -> dict[str, str]:
    """Map each child's local tag name to its rdf:resource, else its stripped text."""
    return {_local_name(child.tag): child.get(_RDF_RESOURCE) or (child.text or '').strip() for child in el}


def parse_model_header(root, cim: ModuleType | None = None) -> ModelHeader:
    """Read the header elements of a parsed part file. With the profile cim, a ModelAuthority
    the profile declares (gad:ModelAuthority, see is_header_element) is an object, not the header.

    - ``md:FullModel``: the authority is ``md:Model.modelingAuthoritySet``, falling back to the
      ``cim:ModelAuthority`` name; the model name written by cimgraph is ``md:Model.description``.
    - ``dcat:Dataset`` (ENTSO-E layout, as write_xml(header=...) writes it): ``dcterms:issued``,
      ``dcterms:title`` (the file name, as description; never the model name) and the
      authority (see dataset_authority), as JSONLDFile reads them. Its other ``rdf:type`` (``gad:GridAssembly``) does not matter.
    """
    header = ModelHeader()
    authority_name = None
    for el in root:
        name = _local_name(el.tag)
        if name == 'FullModel':
            values = _child_values(el)
            header.full_model_uuid = _header_uuid(el)
            header.created = values.get('Model.created')
            header.description = values.get('Model.description')
            header.model_name = header.description or ''
            header.authority = values.get('Model.modelingAuthoritySet')
        elif el.tag == f'{{{DCAT}}}Dataset':
            values = _child_values(el)
            header.full_model_uuid = _header_uuid(el)
            header.created = values.get('issued')
            header.description = values.get('title')
            header.authority = dataset_authority(header.full_model_uuid, values.get('Model.modelingAuthoritySet'),
                                                 values.get('isVersionOf'))
        elif name == 'ModelAuthority' and (cim is None or is_header_element(el, cim)):
            header.authority_uuid = _header_uuid(el)
            authority_name = _child_values(el).get('IdentifiedObject.name')

    if header.authority is None:
        header.authority = authority_name
    elif authority_name is not None and authority_name != header.authority:
        _log.warning(
            'FullModel modelingAuthoritySet %r differs from ModelAuthority name %r; using %r',
            header.authority, authority_name, header.authority,
        )
    if header.authority is not None and header.authority_uuid is None:
        header.authority_uuid = str(model_authority_namespace(header.authority))
    return header
