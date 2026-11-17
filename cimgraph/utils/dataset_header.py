"""The dcat:Dataset header of written files, shared by write_json_ld and write_xml(header=...)."""
from __future__ import annotations

import re
from urllib.parse import urlsplit

from cimprofiles.jsonld import document_prefixes, load_vocabulary_units, profile_jsonld
from cimprofiles.jsonld.build import build_context

from cimgraph.core import get_allow_remote_context
from cimgraph.utils.model_header import model_header

# The type of a dataset whose @graph is a named graph, as Nordic44 and KGraphPy write it
RDFG_GRAPH = 'http://www.w3.org/2004/03/trix/rdfg-1/Graph'
# dct:issued as KGraphPy requires it: one xsd:dateTime in UTC, ending with Z
_UTC_DATETIME = re.compile(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d+)?Z')


def dataset_header(vocabularies: list[str], header: dict | None) -> dict:
    """
    The dcat:Dataset header (IEC 61970-552 ed3 / ENTSO-E metadata specification style), as a
    JSON-LD node in compact form.

    - dct:issued, dct:identifier and @id: the export time and a new UUID, unless `header`
      sets them (set @id "urn:uuid:<id>" and dct:identifier "<id>" together).
    - md:Model.modelingAuthoritySet: CIMG_MODEL_AUTHORITY, the namespace of the UUIDs seeded
      from names and non-UUID mRIDs, which the readers restore.
    - dct:title: CIMG_MODEL_NAME, if set.
    - dct:conformsTo, and the dct:conformsTo of dcat:distribution (this file): the units
      vocabularies of its numbers. The Dataset's own is what survives tools that drop the
      distribution (KGraphPy) and what CGMES files use.
    - @type: dcat:Dataset and rdfg:Graph, as in JSON-LD the dataset is the named graph of the objects.
    - `header`: further properties (e.g. dcat:isVersionOf, the model series IRI; dct:license;
      extension terms and blank nodes), which replace the ones above. The units distribution
      is the writer's: a dcat:distribution in `header` raises.
    """
    header = header or {}
    if 'dcat:distribution' in header:
        raise ValueError('header must not set dcat:distribution: the writer writes the distribution '
                         'naming the units vocabularies of the numbers; list other distributions '
                         'in a separate catalog')
    issued = header.get('dct:issued')
    if issued is not None and not _UTC_DATETIME.fullmatch(issued):
        raise ValueError(f'dct:issued {issued!r} is not a UTC date-time such as 2026-11-01T00:00:00Z')
    is_version_of = header.get('dcat:isVersionOf')
    if isinstance(is_version_of, dict):
        is_version_of = is_version_of.get('@id')
    if is_version_of is not None and not urlsplit(is_version_of).scheme:
        raise ValueError(f'dcat:isVersionOf {is_version_of!r} is not an absolute IRI')
    values = model_header()
    dataset = {
        '@id': 'urn:uuid:' + values['full_model_uuid'],
        '@type': ['dcat:Dataset', RDFG_GRAPH],
        'dct:identifier': values['full_model_uuid'],
        'dct:issued': values['created'],
        'md:Model.modelingAuthoritySet': values['authority'],
    }
    if values['model_name']:
        dataset['dct:title'] = values['model_name']
    if vocabularies:
        dataset['dct:conformsTo'] = vocabularies
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


def check_header_prefixes(context: list, namespaces: dict[str, str], header: dict) -> dict[str, str]:
    """
    The prefixes the objects use must mean the same namespace in the contexts, and every
    prefix of the header must be defined by one of them (an undefined one would be read as
    an IRI scheme). Returns the contexts' {prefix: namespace}.
    """
    context_namespaces = document_prefixes({'@context': context}, get_allow_remote_context())
    for prefix, namespace in namespaces.items():
        if prefix != 'rdf' and context_namespaces.get(prefix) != namespace:
            raise ValueError(f'Prefix {prefix}: ({namespace}) is not defined that way by the context {context}')
    undefined = _compact_prefixes(header) - set(context_namespaces)
    if undefined:
        raise ValueError(f'Header prefixes {sorted(undefined)} are not defined by the context {context}')
    return context_namespaces


def profile_documents(profile) -> dict | None:
    """The published JSON-LD documents of a profile module (profile_jsonld), or None for a
    runtime-merged profile, which has none."""
    try:
        return profile_jsonld(profile.__name__)
    except KeyError:
        return None


def profile_context_and_units(profile, convention: str | None) -> tuple[str | dict, list[str], dict[str, str]]:
    """
    (@context, vocabulary IRIs, {'Class.attribute': unit}) for a profile module.
    A profile with published documents uses its context URL and the convention's
    vocabularies (default: the profile's default convention). A runtime-merged profile has
    none: its context is written inline and numbers are in each CIMUnit's base unit.
    """
    documents = profile_documents(profile)
    if documents is None:
        if convention is not None:
            raise ValueError(f'{profile.__name__} has no published units conventions')
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
