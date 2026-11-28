from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

from cimgraph.core.serialization import object_to_json_ld, profile_namespaces
from cimgraph.utils.dataset_header import (check_header_prefixes, dataset_header,
                                           profile_context_and_units)

if TYPE_CHECKING:
    from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def write_json_ld(network: GraphModel, filename: str, indent: int = 4,
                  convention: str | None = None, header: dict | None = None,
                  contexts: list[str | dict] | None = None) -> None:
    """
    Write the network graph to a JSON-LD file in the ENTSO-E metadata layout: the
    top-level map is the dcat:Dataset header (see dataset_header) and its @graph, a
    named graph, holds the objects. As in the CGMES draft style, @context is the profile's
    published context URL, references are "urn:uuid:..." strings, and numbers are strings
    in the units of a units convention (see cimprofiles.jsonld), which the header's
    dcat:distribution names in dct:conformsTo.

    Args:
        network (GraphModel): The network graph to be written.
        filename: Output file path.
        indent: JSON indentation.
        convention: Units convention name (e.g. 'si', 'distribution', 'cgmes'); default:
            the profile's default convention.
        header: Properties added to (or replacing) those of the dcat:Dataset header. With
            dct:identifier, @id and dct:issued set, the output depends only on the graph, the
            header and the model scope (dct:title, md:Model.modelingAuthoritySet, unless set).
        contexts: Further contexts (URLs or inline maps) defining the header's other
            prefixes, written after the profile's context.
    """
    namespaces = profile_namespaces(network.graph)
    profile_context, vocabularies, units = profile_context_and_units(network.cim, convention)
    context = [profile_context, *(contexts or [])]
    dataset = dataset_header(vocabularies, header)
    check_header_prefixes(context, namespaces, dataset)

    nodes = []
    for cim_class in sorted(network.graph, key=lambda cls: cls.__name__):
        for obj in sorted(network.graph[cim_class].values(), key=lambda obj: obj.uri()):
            nodes.append(object_to_json_ld(obj, namespaces, units))
        _log.info(f'wrote {len(network.graph[cim_class])} {cim_class.__name__} objects')

    document = {'@context': context[0] if len(context) == 1 else context, **dataset, '@graph': nodes}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(document, f, indent=indent)
