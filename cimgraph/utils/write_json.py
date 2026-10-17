from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING

from cimgraph.core.serialization import DEFAULT_NAMESPACES, object_to_json_ld
from cimgraph.utils.model_header import model_header

if TYPE_CHECKING:
    from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def _model_header_json_ld() -> list[dict]:
    """Build the md:FullModel and cim:ModelAuthority header nodes."""
    header = model_header()
    full_model = {
        '@id': 'urn:uuid:' + header['full_model_uuid'],
        '@type': 'md:FullModel',
        'md:Model.created': header['created'],
    }
    if header['model_name']:
        full_model['md:Model.description'] = header['model_name']
    full_model['md:Model.modelingAuthoritySet'] = header['authority']
    model_authority = {
        '@id': 'urn:uuid:' + header['authority_uuid'],
        '@type': 'cim:ModelAuthority',
        'cim:IdentifiedObject.name': header['authority'],
    }
    return [full_model, model_authority]


def write_json_ld(network: GraphModel, filename: str, namespaces: dict = None, indent: int = 4) -> None:
    """
    Write the network graph to a JSON-LD file.

    Args:
        network (GraphModel): The network graph to be written.
        filename: Output file path.
        namespaces: Extra or overriding prefix -> namespace URI entries, merged
            over DEFAULT_NAMESPACES. Also written as the @context.
        indent: JSON indentation.
    """
    all_namespaces = DEFAULT_NAMESPACES | (namespaces or {})
    nodes = _model_header_json_ld()
    for cim_class in sorted(network.graph, key=lambda cls: cls.__name__):
        for obj in sorted(network.graph[cim_class].values(), key=lambda obj: obj.uri()):
            nodes.append(object_to_json_ld(obj, all_namespaces))
        _log.info(f'wrote {len(network.graph[cim_class])} {cim_class.__name__} objects')

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({'@context': all_namespaces, '@graph': nodes}, f, indent=indent)
