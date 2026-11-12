from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

from cimprofiles.jsonld import document_prefixes, load_document, load_vocabulary_units, profile_jsonld
from cimprofiles.jsonld.build import build_context

from cimgraph.core.serialization import object_to_json_ld, profile_namespaces
from cimgraph.utils.model_header import model_header

if TYPE_CHECKING:
    from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def _header_json_ld(vocabularies: list[str]) -> dict:
    """
    The dcat:Dataset header node (CGMES 3 / IEC 61970-552 ed3 style). The context types
    dct:issued as a date and dcat:isVersionOf (the model authority) and dct:conformsTo (the
    units vocabularies of the numbers) as IRIs, so the authority must be an absolute IRI.
    """
    header = model_header()
    if not urlsplit(header['authority']).scheme:
        raise ValueError(f'Model authority {header["authority"]!r} is not an absolute IRI, which '
                         f'dcat:isVersionOf needs; set CIMG_MODEL_AUTHORITY to a URI such as '
                         f'https://example.com')
    dataset = {
        '@id': 'urn:uuid:' + header['full_model_uuid'],
        '@type': 'dcat:Dataset',
        'dct:identifier': header['full_model_uuid'],
        'dct:issued': header['created'],
        'dcat:isVersionOf': header['authority'],
    }
    if header['model_name']:
        dataset['dct:description'] = header['model_name']
    if vocabularies:
        dataset['dct:conformsTo'] = vocabularies
    return dataset


def _context_and_units(profile, convention: str | None) -> tuple[str | dict, list[str], dict[str, str]]:
    """
    (@context, vocabulary IRIs, {'Class.attribute': unit}) for a profile module.
    A profile with published documents uses its context URL and the convention's
    vocabularies (default: the profile's default convention). A runtime-merged profile has
    none: its context is written inline and numbers are in each CIMUnit's base unit.
    """
    try:
        documents = profile_jsonld(profile.__name__)
    except KeyError:
        if convention is not None:
            raise ValueError(f'{profile.__name__} has no published units conventions') from None
        return build_context(profile)['@context'], [], {}
    convention = convention or documents['default']
    if convention not in documents['conventions']:
        raise ValueError(f'Unknown units convention {convention!r}; '
                         f'{profile.__name__} has {", ".join(documents["conventions"])}')
    vocabularies = documents['conventions'][convention]
    units = {}
    for iri in vocabularies:
        units.update(load_vocabulary_units(iri))
    return documents['context'], vocabularies, units


def _check_prefixes(context: str, namespaces: dict[str, str]) -> None:
    """Every prefix the nodes use must mean the same namespace in the published context."""
    context_namespaces = document_prefixes(load_document(context))
    for prefix, namespace in namespaces.items():
        if prefix != 'rdf' and context_namespaces.get(prefix) != namespace:
            raise ValueError(f'Prefix {prefix}: ({namespace}) is not defined that way by {context}')


def write_json_ld(network: GraphModel, filename: str, indent: int = 4,
                  convention: str | None = None) -> None:
    """
    Write the network graph to a JSON-LD file in the CGMES draft style: the profile's
    published @context URL, a flat @graph, references as "urn:uuid:..." strings, and
    numbers as strings in the units of a units convention (see cimprofiles.jsonld), which
    the dcat:Dataset header names in dct:conformsTo.

    Args:
        network (GraphModel): The network graph to be written.
        filename: Output file path.
        indent: JSON indentation.
        convention: Units convention name (e.g. 'si', 'distribution', 'cgmes'); default:
            the profile's default convention.
    """
    namespaces = profile_namespaces(network.graph)
    context, vocabularies, units = _context_and_units(network.cim, convention)
    if isinstance(context, str):
        _check_prefixes(context, namespaces)

    nodes = [_header_json_ld(vocabularies)]
    for cim_class in sorted(network.graph, key=lambda cls: cls.__name__):
        for obj in sorted(network.graph[cim_class].values(), key=lambda obj: obj.uri()):
            nodes.append(object_to_json_ld(obj, namespaces, units))
        _log.info(f'wrote {len(network.graph[cim_class])} {cim_class.__name__} objects')

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({'@context': context, '@graph': nodes}, f, indent=indent)
