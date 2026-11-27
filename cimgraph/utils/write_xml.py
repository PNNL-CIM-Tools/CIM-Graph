from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from xml.sax.saxutils import escape, quoteattr

from cimprofiles.jsonld import load_document
from cimprofiles.jsonld.build import build_context

from cimgraph.core import get_allow_remote_context, get_cim_profile
from cimgraph.core.serialization import (RDF_XML_CLOSE, object_to_xml, profile_namespaces,
                                         rdf_id_text, rdf_xml_identifiers, rdf_xml_open)
from cimgraph.utils.dataset_header import (RDFG_GRAPH, check_header_prefixes, dataset_header,
                                           profile_documents)
from cimgraph.utils.model_header import model_header

if TYPE_CHECKING:
    from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def _model_header_xml() -> str:
    """Render the md:FullModel and cim:ModelAuthority header elements."""
    rdf_about, _ = rdf_xml_identifiers()
    header = model_header()
    authority = escape(header['authority'])
    xml = f'<md:FullModel {rdf_about}{rdf_id_text(header["full_model_uuid"])}">\n'
    xml += f'  <md:Model.created>{header["created"]}</md:Model.created>\n'
    if header['model_name']:
        xml += f'  <md:Model.description>{escape(header["model_name"])}</md:Model.description>\n'
    xml += f'  <md:Model.modelingAuthoritySet>{authority}</md:Model.modelingAuthoritySet>\n'
    xml += '</md:FullModel>\n'
    xml += f'<cim:ModelAuthority {rdf_about}{rdf_id_text(header["authority_uuid"])}">\n'
    xml += f'  <cim:IdentifiedObject.name>{authority}</cim:IdentifiedObject.name>\n'
    xml += '</cim:ModelAuthority>\n'
    return xml


# The XSD datatypes of JSON-LD's native values (bool before int: True is an int)
_NATIVE_DATATYPES = ((bool, 'http://www.w3.org/2001/XMLSchema#boolean'),
                     (int, 'http://www.w3.org/2001/XMLSchema#integer'),
                     (float, 'http://www.w3.org/2001/XMLSchema#double'))


def _term_definitions(context) -> dict[str, dict]:
    """The expanded term definitions ({'dct:issued': {'@type': 'xsd:dateTime'}}) of a JSON-LD
    context: a URL, an inline map, or a list of them (later ones win)."""
    if isinstance(context, str):
        return _term_definitions(load_document(context, get_allow_remote_context())['@context'])
    if isinstance(context, list):
        definitions = {}
        for item in context:
            definitions.update(_term_definitions(item))
        return definitions
    return {term: definition for term, definition in context.items() if isinstance(definition, dict)}


class _HeaderXML:
    """Renders a JSON-LD header node as RDF/XML, with the same triples as in JSON-LD:
    the context's term types decide IRI or typed literal."""

    def __init__(self, context: list, prefixes: dict[str, str]):
        self.definitions = _term_definitions(context)
        self.prefixes = prefixes
        self.used = {}  # {prefix: namespace} of the element names written, to declare

    def expand(self, value: str) -> str:
        """A compact IRI ('xsd:dateTime') as a full IRI; other IRIs unchanged."""
        prefix, _, local = value.partition(':')
        if prefix in self.prefixes and not local.startswith('//'):
            return self.prefixes[prefix] + local
        return value

    def qname(self, term: str) -> str:
        """An element name: a compact IRI with a declared prefix."""
        prefix = term.partition(':')[0]
        if prefix not in self.prefixes:
            raise ValueError(f'Header term {term!r} must be a compact IRI with a prefix the contexts define')
        self.used[prefix] = self.prefixes[prefix]
        return term

    def node(self, node: dict, pad: str = '') -> str:
        """A node element: its first compact type as the element name, others as rdf:type."""
        types = node.get('@type', [])
        types = [types] if isinstance(types, str) else [t for t in types if t != RDFG_GRAPH]
        compact = [t for t in types if t.partition(':')[0] in self.prefixes]
        element = self.qname(compact[0]) if compact else 'rdf:Description'
        about = f' rdf:about={quoteattr(self.expand(node["@id"]))}' if '@id' in node else ''
        xml = f'{pad}<{element}{about}>\n'
        for other in types:
            if other != element:
                xml += f'{pad}  <rdf:type rdf:resource={quoteattr(self.expand(other))}/>\n'
        for term, value in node.items():
            if not term.startswith('@'):
                xml += self.property(term, value, pad + '  ')
        return xml + f'{pad}</{element}>\n'

    def property(self, term: str, value, pad: str) -> str:
        """One property element per value; a list repeats it."""
        if isinstance(value, list):
            return ''.join(self.property(term, item, pad) for item in value)
        tag = self.qname(term)
        coercion = self.definitions.get(term, {}).get('@type')
        if isinstance(value, dict) and set(value) == {'@id'} or isinstance(value, str) and coercion == '@id':
            iri = value['@id'] if isinstance(value, dict) else value
            return f'{pad}<{tag} rdf:resource={quoteattr(self.expand(iri))}/>\n'
        if isinstance(value, dict) and '@value' not in value:
            return f'{pad}<{tag}>\n{self.node(value, pad + "  ")}{pad}</{tag}>\n'
        language = None
        if isinstance(value, dict):
            value, coercion, language = value['@value'], value.get('@type'), value.get('@language')
        if language is not None:   # a language-tagged string has no datatype
            return f'{pad}<{tag} xml:lang={quoteattr(language)}>{escape(value)}</{tag}>\n'
        datatype = coercion and self.expand(coercion)
        if not isinstance(value, str):
            datatype = datatype or next(iri for kind, iri in _NATIVE_DATATYPES if isinstance(value, kind))
            value = str(value).lower() if isinstance(value, bool) else str(value)
        attribute = f' rdf:datatype={quoteattr(datatype)}' if datatype else ''
        return f'{pad}<{tag}{attribute}>{escape(value)}</{tag}>\n'


def _dataset_header_xml(profile, header: dict, contexts: list | None,
                        namespaces: dict[str, str]) -> tuple[str, dict[str, str]]:
    """
    The dcat:Dataset header block (ENTSO-E metadata layout) and the {prefix: namespace} its
    element names use.
    The same node as write_json_ld writes (dataset_header), but CIM XML numbers are in base
    SI units: the units vocabularies are the profile's 'si' convention, when it publishes one.
    In RDF/XML the dataset is not a named graph, so it is not typed rdfg:Graph.
    """
    documents = profile_documents(profile)
    if documents is None:
        context, vocabularies = build_context(profile)['@context'], []
    else:
        context, vocabularies = documents['context'], documents['conventions'].get('si', [])
    context = [context, *(contexts or [])]
    dataset = dataset_header(vocabularies, header)
    writer = _HeaderXML(context, check_header_prefixes(context, namespaces, dataset))
    return writer.node(dataset), writer.used


def write_graph_xml(graph: dict, filename: str, write_identifier: bool = True,
                    write_model_header: bool = True, header: dict | None = None,
                    contexts: list[str | dict] | None = None, profile=None) -> None:
    """
    Write a graph dict ({cim_class: {identifier: obj}}) to an RDF/XML file.
    Classes are written in alphabetical order and objects sorted by URI, so
    output is stable between runs. The header declares the profile's namespaces
    (profile_namespaces).

    Args:
        graph: The graph of CIM objects to write.
        filename: Output file path.
        write_identifier: Write the cim:Identity.identifier property.
        write_model_header: Write a header at the top of the file: md:FullModel and
            cim:ModelAuthority, or with `header` the dcat:Dataset block.
        header: Write the dcat:Dataset header of the ENTSO-E metadata layout in place of
            md:FullModel: the node write_json_ld writes (see dataset_header), with these
            properties in JSON-LD compact form, e.g. {'dcat:isVersionOf': {'@id': iri}}.
            Values the contexts type as @id, and {"@id"} objects, are written as rdf:resource;
            {"@value", "@language"} objects with xml:lang, other typed values with rdf:datatype.
            With dct:identifier, @id and dct:issued set, the output depends only on the graph,
            the header and the model scope (dct:title, md:Model.modelingAuthoritySet, unless set).
        contexts: Further JSON-LD contexts defining the header's other prefixes.
        profile: The CIM profile module of the graph's classes (default: the active
            profile), whose context types the header.
    """
    all_namespaces = profile_namespaces(graph)
    if header is not None:
        if not write_model_header:
            raise ValueError('header is the dcat:Dataset model header; it needs write_model_header=True')
        header_xml, prefixes = _dataset_header_xml(profile or get_cim_profile()[1], header, contexts,
                                                   all_namespaces)
        all_namespaces = {**all_namespaces, **prefixes}
    elif write_model_header:
        header_xml = _model_header_xml()
    else:
        header_xml = ''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(rdf_xml_open(all_namespaces))
        f.write(header_xml)
        for cim_class in sorted(graph, key=lambda cls: cls.__name__):
            for obj in sorted(graph[cim_class].values(), key=lambda obj: obj.uri()):
                f.write(object_to_xml(obj, all_namespaces, write_identifier))
            _log.info(f'wrote {len(graph[cim_class])} {cim_class.__name__} objects')
        f.write(RDF_XML_CLOSE)


def write_xml(network: GraphModel, filename: str, write_identifier: bool = True,
              write_model_header: bool = True, header: dict | None = None,
              contexts: list[str | dict] | None = None) -> None:
    """Write the network graph to an RDF/XML file. See write_graph_xml for arguments."""
    write_graph_xml(network.graph, filename, write_identifier, write_model_header, header, contexts,
                    network.cim)
