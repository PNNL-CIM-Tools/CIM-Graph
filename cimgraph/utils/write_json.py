from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

from cimprofiles.jsonld import document_prefixes, load_vocabulary_units, profile_jsonld
from cimprofiles.jsonld.build import build_context

from cimgraph.core import get_allow_remote_context
from cimgraph.core.serialization import object_to_json_ld, profile_namespaces
from cimgraph.utils.model_header import model_header

if TYPE_CHECKING:
    from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def _dataset_header(vocabularies: list[str], header: dict | None) -> dict:
    """
    The dcat:Dataset header (IEC 61970-552 ed3 / ENTSO-E metadata specification style).

    - dct:issued, dct:identifier and @id: the export time and a new UUID, unless `header`
      sets them (set @id "urn:uuid:<id>" and dct:identifier "<id>" together).
    - md:Model.modelingAuthoritySet: CIMG_MODEL_AUTHORITY, the namespace of the UUIDs seeded
      from names and non-UUID mRIDs, which the reader restores.
    - dct:title: CIMG_MODEL_NAME, if set.
    - dcat:distribution: this file, conforming to the units vocabularies of its numbers.
    - `header`: further properties (e.g. dcat:isVersionOf, the model series IRI; dct:license;
      extension terms and blank nodes), which replace the ones above. The units distribution
      is the writer's: a dcat:distribution in `header` raises.
    """
    header = header or {}
    if 'dcat:distribution' in header:
        raise ValueError('header must not set dcat:distribution: the writer writes the distribution '
                         'naming the units vocabularies of the numbers; list other distributions '
                         'in a separate catalog')
    is_version_of = header.get('dcat:isVersionOf')
    if is_version_of is not None and not urlsplit(is_version_of).scheme:
        raise ValueError(f'dcat:isVersionOf {is_version_of!r} is not an absolute IRI')
    values = model_header()
    dataset = {
        '@id': 'urn:uuid:' + values['full_model_uuid'],
        '@type': 'dcat:Dataset',
        'dct:identifier': values['full_model_uuid'],
        'dct:issued': values['created'],
        'md:Model.modelingAuthoritySet': values['authority'],
    }
    if values['model_name']:
        dataset['dct:title'] = values['model_name']
    if vocabularies:
        dataset['dcat:distribution'] = {'@type': 'dcat:Distribution', 'dct:conformsTo': vocabularies}
    dataset.update(header)
    return dataset


def _compact_prefixes(value) -> set[str]:
    """The prefixes of the compact IRIs used as keys and @type values in a JSON-LD value."""
    prefixes = set()
    if isinstance(value, list):
        for item in value:
            prefixes |= _compact_prefixes(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            names = [key]
            if key == '@type':
                names += item if isinstance(item, list) else [item]
            prefixes |= {name.partition(':')[0] for name in names
                         if ':' in name and not name.startswith('@') and '//' not in name}
            prefixes |= _compact_prefixes(item)
    return prefixes


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


def _check_prefixes(context: list, namespaces: dict[str, str], header: dict) -> None:
    """
    The prefixes the objects use must mean the same namespace in the contexts, and every
    prefix of the header must be defined by one of them (an undefined one would be read as
    an IRI scheme).
    """
    context_namespaces = document_prefixes({'@context': context}, get_allow_remote_context())
    for prefix, namespace in namespaces.items():
        if prefix != 'rdf' and context_namespaces.get(prefix) != namespace:
            raise ValueError(f'Prefix {prefix}: ({namespace}) is not defined that way by the context {context}')
    undefined = _compact_prefixes(header) - set(context_namespaces)
    if undefined:
        raise ValueError(f'Header prefixes {sorted(undefined)} are not defined by the context {context}')


def write_json_ld(network: GraphModel, filename: str, indent: int = 4,
                  convention: str | None = None, header: dict | None = None,
                  contexts: list[str | dict] | None = None) -> None:
    """
    Write the network graph to a JSON-LD file in the ENTSO-E metadata layout: the
    top-level map is the dcat:Dataset header (see _dataset_header) and its @graph, a named
    graph, holds the objects. As in the CGMES draft style, @context is the profile's
    published context URL, references are "urn:uuid:..." strings, and numbers are strings
    in the units of a units convention (see cimprofiles.jsonld), which the header's
    dcat:distribution names in dct:conformsTo.

    Args:
        network (GraphModel): The network graph to be written.
        filename: Output file path.
        indent: JSON indentation.
        convention: Units convention name (e.g. 'si', 'distribution', 'cgmes'); default:
            the profile's default convention.
        header: Properties added to (or replacing) those of the dcat:Dataset header.
        contexts: Further contexts (URLs or inline maps) defining the header's other
            prefixes, written after the profile's context.
    """
    namespaces = profile_namespaces(network.graph)
    profile_context, vocabularies, units = _context_and_units(network.cim, convention)
    context = [profile_context, *(contexts or [])]
    dataset = _dataset_header(vocabularies, header)
    _check_prefixes(context, namespaces, dataset)

    nodes = []
    for cim_class in sorted(network.graph, key=lambda cls: cls.__name__):
        for obj in sorted(network.graph[cim_class].values(), key=lambda obj: obj.uri()):
            nodes.append(object_to_json_ld(obj, namespaces, units))
        _log.info(f'wrote {len(network.graph[cim_class])} {cim_class.__name__} objects')

    document = {'@context': context[0] if len(context) == 1 else context, **dataset, '@graph': nodes}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(document, f, indent=indent)
