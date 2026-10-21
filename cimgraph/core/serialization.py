"""Per-object serialization of CIM objects to RDF/XML, JSON-LD, and SPARQL triples.

Which attributes are written, and how each value is classified, comes from the
field metadata via :func:`cimgraph.core.attribute_utils.iter_properties`. This
module only renders those properties in each output format.
"""
from __future__ import annotations

from xml.sax.saxutils import escape

from cimprofiles.identity import as_uuid, normalize_identifier

from cimgraph.core.attribute_utils import Property, iter_properties
from cimgraph.core.env_vars import get_iec61970_552, get_namespace, get_url

RDF_NAMESPACE = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
MD_NAMESPACE = 'http://iec.ch/TC57/61970-552/ModelDescription/1#'

DEFAULT_NAMESPACES = {'cim': 'http://iec.ch/TC57/CIM100#',
                      'eu': 'http://iec.ch/TC57/CIM100-European#',
                      'nc': 'http://entsoe.eu/ns/nc#',
                      'gb': 'http://GB/placeholder/ext#',
                      'md': MD_NAMESPACE,
                      'rdf': RDF_NAMESPACE}

RDF_XML_CLOSE = '</rdf:RDF>\n'


def _prefix(namespaces: dict, namespace: str) -> str:
    """Return the prefix for a namespace URI, failing clearly if it is not mapped."""
    for prefix, uri in namespaces.items():
        if uri == namespace:
            return prefix
    raise KeyError(f'Namespace {namespace} has no prefix. Add it to the namespaces argument.')


def _literal_text(value) -> str:
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)


def rdf_id_text(uuid_text: str, style: str | None = None) -> str:
    """
    Returns a UUID as written in rdf:ID, rdf:about, rdf:resource and RDF IRIs for a
    serialization style (default: CIMG_IEC61970_552). 552-NEW 'urn:uuid:' IRIs carry the
    bare UUID; 552-LEGACY and CGMES rdf:IDs start with '_' (an XML ID cannot start with a
    digit).
    """
    style = style or get_iec61970_552()
    return uuid_text if style == '552-NEW' else '_' + uuid_text


def rdf_identifier(obj, style: str | None = None) -> str:
    """Returns a CIM object's identifier as written in RDF for a style (see rdf_id_text)."""
    return rdf_id_text(obj.uri(), style)


def mrid_text(obj, mrid: str, style: str | None = None) -> str:
    """
    Returns IdentifiedObject.mRID as written for a style. An mRID that is the object's own
    UUID is '_<uuid>' in 552-LEGACY and '<uuid>' in CGMES and 552-NEW; any other mRID
    (e.g. 'LINE_650_632') is written as-is.
    """
    if as_uuid(mrid) != obj.identifier:
        return mrid
    style = style or get_iec61970_552()
    return '_' + obj.uri() if style == '552-LEGACY' else obj.uri()


def _reference_text(value, style: str | None = None) -> str:
    """
    A reference is a resolved CIM object or a string: a bare uri() or the raw text of an
    unresolved reference. UUIDs get the style's form once; other strings are kept as-is.
    """
    if not isinstance(value, str):
        return rdf_identifier(value, style)
    return rdf_id_text(normalize_identifier(value), style) if as_uuid(value) else value


def _with_style_mrid(obj, prop: Property, style: str | None = None) -> Property:
    if prop.name == 'IdentifiedObject.mRID' and isinstance(prop.value, str):
        return prop._replace(value=mrid_text(obj, prop.value, style))
    return prop


def rdf_xml_identifiers() -> tuple[str, str]:
    """
    Return (about, resource) prefixes for the active IEC 61970-552 format:
    ``('rdf:about="urn:uuid:', 'urn:uuid:')`` or ``('rdf:ID="', '#')``.
    Identifiers follow them in their style's form (rdf_id_text).
    """
    if get_iec61970_552() == '552-NEW':
        return 'rdf:about="urn:uuid:', 'urn:uuid:'
    return 'rdf:ID="', '#'


def rdf_xml_open(namespaces: dict = DEFAULT_NAMESPACES) -> str:
    """Return the XML declaration and opening rdf:RDF element."""
    header = '<?xml version="1.0" encoding="utf-8"?>\n<rdf:RDF'
    for prefix, uri in namespaces.items():
        header += f' xmlns:{prefix}="{uri}"'
    return header + '>\n'


def property_to_xml(prop: Property, namespaces: dict, rdf_resource: str) -> str:
    """Render one Property as an RDF/XML property element."""
    tag = f'{_prefix(namespaces, prop.namespace)}:{prop.name}'
    if prop.kind == 'reference':
        return f'  <{tag} rdf:resource="{rdf_resource}{_reference_text(prop.value)}"/>\n'
    if prop.kind == 'enum':
        return f'  <{tag} rdf:resource="{prop.namespace}{prop.value}"/>\n'
    if prop.kind == 'unit':
        datatype = f'{prop.namespace}UnitSymbol.{str(prop.value.quantity.units)}'
        return f'  <{tag} rdf:datatype="{datatype}">{prop.value.value}</{tag}>\n'
    return f'  <{tag}>{escape(_literal_text(prop.value))}</{tag}>\n'


def object_to_xml(obj, namespaces: dict = DEFAULT_NAMESPACES, write_identifier: bool = True) -> str:
    """Render a CIM object as an RDF/XML element."""
    rdf_about, rdf_resource = rdf_xml_identifiers()
    class_name = obj.__class__.__name__
    xml = f'<cim:{class_name} {rdf_about}{rdf_identifier(obj)}">\n'
    if write_identifier:
        xml += f'  <cim:Identity.identifier>{obj.uri()}</cim:Identity.identifier>\n'
    for prop in iter_properties(obj):
        xml += property_to_xml(_with_style_mrid(obj, prop), namespaces, rdf_resource)
    return xml + f'</cim:{class_name}>\n'


def object_to_json_ld(obj, namespaces: dict = DEFAULT_NAMESPACES) -> dict:
    """Render a CIM object as a JSON-LD node. Repeated properties become lists."""
    # JSON-LD always identifies objects with urn:uuid: IRIs, as 552-NEW does
    node = {'@id': f'urn:uuid:{obj.uri()}', '@type': f'cim:{obj.__class__.__name__}'}
    for prop in iter_properties(obj):
        prop = _with_style_mrid(obj, prop, '552-NEW')
        prefix = _prefix(namespaces, prop.namespace)
        key = f'{prefix}:{prop.name}'
        if prop.kind == 'reference':
            value = {'@id': f'urn:uuid:{_reference_text(prop.value, "552-NEW")}'}
        elif prop.kind == 'enum':
            value = f'{prefix}:{prop.value}'
        elif prop.kind == 'unit':
            value = str(prop.value.value)
        else:
            value = _literal_text(prop.value)

        if key not in node:
            node[key] = value
        elif isinstance(node[key], list):
            node[key].append(value)
        else:
            node[key] = [node[key], value]
    return node


def _sparql_literal(text: str) -> str:
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


def object_to_sparql_triples(obj) -> list[str]:
    """Render a CIM object as SPARQL triple patterns using full IRIs."""
    if get_iec61970_552() == '552-NEW':
        rdf_resource = 'urn:uuid:'
    else:
        rdf_resource = f'{get_url()}#'
    subject = f'<{rdf_resource}{rdf_identifier(obj)}>'
    triples = [f'{subject} a <{get_namespace()}{obj.__class__.__name__}> .']
    for prop in iter_properties(obj):
        prop = _with_style_mrid(obj, prop)
        predicate = f'<{prop.namespace}{prop.name}>'
        if prop.kind == 'reference':
            value = f'<{rdf_resource}{_reference_text(prop.value)}>'
        elif prop.kind == 'enum':
            value = f'<{prop.namespace}{prop.value}>'
        elif prop.kind == 'unit':
            value = _sparql_literal(str(prop.value.value))
        else:
            value = _sparql_literal(_literal_text(prop.value))
        triples.append(f'{subject} {predicate} {value} .')
    return triples
