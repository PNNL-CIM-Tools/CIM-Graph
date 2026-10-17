from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from xml.sax.saxutils import escape

from cimgraph.core.serialization import (DEFAULT_NAMESPACES, RDF_XML_CLOSE, object_to_xml,
                                         rdf_xml_identifiers, rdf_xml_open)
from cimgraph.utils.model_header import model_header

if TYPE_CHECKING:
    from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def _model_header_xml() -> str:
    """Render the md:FullModel and cim:ModelAuthority header elements."""
    rdf_about, _ = rdf_xml_identifiers()
    header = model_header()
    authority = escape(header['authority'])
    xml = f'<md:FullModel {rdf_about}{header["full_model_uuid"]}">\n'
    xml += f'  <md:Model.created>{header["created"]}</md:Model.created>\n'
    if header['model_name']:
        xml += f'  <md:Model.description>{escape(header["model_name"])}</md:Model.description>\n'
    xml += f'  <md:Model.modelingAuthoritySet>{authority}</md:Model.modelingAuthoritySet>\n'
    xml += '</md:FullModel>\n'
    xml += f'<cim:ModelAuthority {rdf_about}{header["authority_uuid"]}">\n'
    xml += f'  <cim:IdentifiedObject.name>{authority}</cim:IdentifiedObject.name>\n'
    xml += '</cim:ModelAuthority>\n'
    return xml


def write_graph_xml(graph: dict, filename: str, namespaces: dict = None,
                    write_identifier: bool = True, write_model_header: bool = True) -> None:
    """
    Write a graph dict ({cim_class: {identifier: obj}}) to an RDF/XML file.
    Classes are written in alphabetical order and objects sorted by URI, so
    output is stable between runs.

    Args:
        graph: The graph of CIM objects to write.
        filename: Output file path.
        namespaces: Extra or overriding prefix -> namespace URI entries, merged
            over DEFAULT_NAMESPACES.
        write_identifier: Write the cim:Identity.identifier property.
        write_model_header: Write md:FullModel and cim:ModelAuthority elements at the top of the file.
    """
    all_namespaces = DEFAULT_NAMESPACES | (namespaces or {})
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(rdf_xml_open(all_namespaces))
        if write_model_header:
            f.write(_model_header_xml())
        for cim_class in sorted(graph, key=lambda cls: cls.__name__):
            for obj in sorted(graph[cim_class].values(), key=lambda obj: obj.uri()):
                f.write(object_to_xml(obj, all_namespaces, write_identifier))
            _log.info(f'wrote {len(graph[cim_class])} {cim_class.__name__} objects')
        f.write(RDF_XML_CLOSE)


def write_xml(network: GraphModel, filename: str, namespaces: dict = None,
              write_identifier: bool = True, write_model_header: bool = True) -> None:
    """Write the network graph to an RDF/XML file. See write_graph_xml for arguments."""
    write_graph_xml(network.graph, filename, namespaces, write_identifier, write_model_header)
