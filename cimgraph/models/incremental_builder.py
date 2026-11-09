from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import fields
from uuid import UUID

from defusedxml.ElementTree import parse

from cimgraph.core.attribute_utils import field_properties, validate_attr_datatype
from cimgraph.core.serialization import property_to_xml, rdf_id_text, rdf_xml_identifiers
from cimprofiles.identity import Identity, as_uuid, normalize_identifier
from cimgraph.databases import ConnectionInterface, get_iec61970_552, get_namespace

_log = logging.getLogger(__name__)

NAMESPACES = {'cim': get_namespace(),
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', # resource description framework
        'prov': 'http://www.w3.org/ns/prov#', # W3C provenance
        'dcat': 'http://www.w3.org/ns/dcat#', # W3C data catalog vocabulary
        'time': 'http://www.w3.org/2006/time#', # W3C time standard
        'prof': 'http://www.w3.org/ns/dx/prof/#', # W3C profile standard
        'profcim': 'http://iec.ch/TC57/ns/CIM/prof-cim#', # CIM profile namespace
        'md': 'http://iec.ch/TC57/61970-552/ModelDescription#', # CIM model description
        # 'dm': 'http://iec.ch/TC57/61970-552/DifferenceModel#', # CIM difference model
        'dm': 'http://iec.ch/2002/schema/CIM_difference_model#',
        'nc': 'http://entsoe.eu/ns/nc#', # ENTSO-E CIM network codes
        'eumd':'http://entsoe.eu/ns/Metadata-European#' # ENTSO-E CIM metdata
        }

REVERSE_NS = {v: k for k, v in NAMESPACES.items()}
INDENT = '  '





def read_incremental_xml(filename) -> dict:
    # Create a dictionary to store the incremental changes
    incremental = {
        'forwardDifferences': defaultdict(dict),
        'reverseDifferences': defaultdict(dict)
    }

    # Parse the XML string
    root = parse(filename)

    # Find the DifferenceModel element, falling back to the alternate namespace.
    # Use a local copy so the fallback doesn't change NAMESPACES for later reads and writes.
    namespaces = dict(NAMESPACES)
    diff_model = root.find('.//dm:DifferenceModel', namespaces)
    if diff_model is None:
        namespaces['dm'] = 'http://iec.ch/TC57/61970-552/DifferenceModel#'
        diff_model = root.find('.//dm:DifferenceModel', namespaces)

    if diff_model is None:
        raise ValueError('Could not find DifferenceModel element')

    # Process forward and reverse differences
    for diff_type in ['forwardDifferences', 'reverseDifferences']:
        diff_element = diff_model.find(f'dm:{diff_type}', namespaces)

        if diff_element is not None:
            # Find all Description elements under this difference type
            descriptions = diff_element.findall('rdf:Description', namespaces)

            for desc in descriptions:
                # Get the identifier without its '#', '_' or 'urn:uuid:' serialization prefix
                uri = normalize_identifier(desc.get(f'{{{namespaces["rdf"]}}}about'))

                # Process each attribute in the Description
                for child in desc:
                    # Extract tag without namespace prefix
                    tag = child.tag
                    if '}' in tag:
                        tag = tag.split('}', 1)[1]  # Remove namespace part

                    # Store the value in the dictionary
                    incremental[diff_type][uri][tag] = child.text

    return incremental




def _graph_object(uri: str, graph: dict[type, dict[UUID, object]]) -> object | None:
    """Return the graph object whose identifier is the difference URI, if any."""
    identifier = as_uuid(uri)
    for objects in graph.values():
        if identifier in objects:
            return objects[identifier]
    return None


def _difference_object(uri: str, connection: ConnectionInterface,
                       graph: dict[type, dict[UUID, object]]) -> object | None:
    """Return the object a difference refers to: from the graph, else from the connection."""
    if as_uuid(uri) is None:
        return None
    obj = _graph_object(uri, graph)
    if obj is None:
        obj = connection.get_object(mRID=uri, graph=graph)
    return obj


def _converted_value(obj: object, attribute: str, value: object) -> object:
    """
    Return a difference value converted to the datatype of the object's attribute.
    Raises ValueError if the 'Class.attribute' name or the value does not fit the object.
    """
    class_name, _, attr = attribute.rpartition('.')
    cim_class = obj.__class__
    if attr not in cim_class.__dataclass_fields__:
        raise ValueError(f'{cim_class.__name__} has no attribute {attribute}')
    if class_name and class_name not in [parent.__name__ for parent in cim_class.__mro__]:
        raise ValueError(f'{cim_class.__name__} does not inherit from {class_name}')
    valid, attr_datatype, value = validate_attr_datatype(cim_class, attr, value)
    if not valid:
        raise ValueError(f'{attribute} value {value!r} should have datatype {attr_datatype}')
    return value


def validate_incremental(message:dict, connection:ConnectionInterface,
                        graph:dict[type, dict[UUID, object]]) -> dict:
    """
    Drop the differences that don't fit the model, so modify_from_incremental can apply the
    rest. A URI's differences are dropped as a whole, with an error logged, when its object
    can't be found or any of its attributes or values don't fit the object's class. A reverse
    value that differs from the current value is only a warning.
    """
    for direction in ('reverseDifferences', 'forwardDifferences'):
        for uri, differences in message[direction].items():
            obj = _difference_object(uri, connection, graph)
            if obj is None:
                _log.error(f'Dropping {direction} for {uri}: no object with that mRID')
                message[direction][uri] = {}
                continue
            for attribute, value in differences.items():
                try:
                    value = _converted_value(obj, attribute, value)
                except ValueError as error:
                    _log.error(f'Dropping {direction} for {uri}: {error}')
                    message[direction][uri] = {}
                    break
                current_value = getattr(obj, attribute.rpartition('.')[2])
                if direction == 'reverseDifferences' and current_value != value:
                    _log.warning(f'Current value {current_value} does not match reverse {value}')
    return message


def modify_from_incremental(message:dict, connection:ConnectionInterface,
                        graph:dict[type, dict[UUID, object]]) -> list[object]:
    """
    Apply the forward differences to objects in the graph and return the modified objects.
    Raises ValueError for a difference that doesn't fit the model; run validate_incremental
    first to drop those. Creating new objects from a difference is not supported yet.
    """
    modified = []
    for uri, differences in message['forwardDifferences'].items():
        if not differences:
            continue
        obj = _graph_object(uri, graph)
        if obj is None:
            raise ValueError(f'No object with mRID {uri} in the graph for its forward differences')
        for attribute, value in differences.items():
            setattr(obj, attribute.rpartition('.')[2], _converted_value(obj, attribute, value))
        modified.append(obj)
    return modified


def add_to_incremental(cim_class, uuid, differences):
    if cim_class not in differences['forwardDifferences']:
        differences['forwardDifferences'][cim_class] = {}
    if uuid not in differences['forwardDifferences'][cim_class]:
        differences['forwardDifferences'][cim_class][uuid] = {}

    if cim_class not in differences['reverseDifferences']:
        differences['reverseDifferences'][cim_class] = {}
    if uuid not in differences['reverseDifferences'][cim_class]:
        differences['reverseDifferences'][cim_class][uuid] = {}



def new_obj_incremental(new_object:Identity, differences:dict[str, dict]):
    if not isinstance(new_object, Identity):
        raise TypeError('Input must be a CIM class')

    cim_class = new_object.__class__
    uuid = new_object.uri()

    add_to_incremental(cim_class, uuid, differences)

    for field in fields(cim_class):
        if field.name == 'identifier': # Skip CIM 18 Identity.identifier
            continue
        if 'list' not in field.type:
            value = getattr(new_object, field.name)
            if value is not None:
                if isinstance(value, Identity):
                    differences['forwardDifferences'][cim_class][uuid][field.name] = value.uri()
                    differences['reverseDifferences'][cim_class][uuid][field.name] = None
                else:
                    differences['forwardDifferences'][cim_class][uuid][field.name] = value
                    differences['reverseDifferences'][cim_class][uuid][field.name] = None


def del_obj_difference(new_object:Identity, differences:dict[str, dict]) -> None:
    if not isinstance(new_object, Identity):
        raise TypeError('Input must be a CIM class')

    cim_class = new_object.__class__
    uuid = new_object.uri()

    add_to_incremental(cim_class, uuid, differences)

    for field in fields(cim_class):
        if field.name == 'identifier': # Skip CIM 18 Identity.identifier
            continue
        if 'list' not in field.type:
            value = getattr(new_object, field.name)
            if value is not None:
                if isinstance(value, Identity):
                    differences['reverseDifferences'][cim_class][uuid][field.name] = value.uri()
                else:
                    differences['reverseDifferences'][cim_class][uuid][field.name] = value

def modify_incremental(cim_object:Identity, attribute:str, old_value:any, new_value:any, differences:dict):
    cim_class = cim_object.__class__
    uuid = cim_object.uri()

    add_to_incremental(cim_class, uuid, differences)

    differences['forwardDifferences'][cim_class][uuid][attribute] = _difference_value(new_value)
    differences['reverseDifferences'][cim_class][uuid][attribute] = _difference_value(old_value)


def _difference_value(value: any) -> any:
    """A referenced object is recorded by its URI; None and other values as they are."""
    if isinstance(value, Identity):
        return value.uri()
    return value






def incremantal_row(cim_class:type, uri:str, difference:dict) -> str:

    if all(value is None for value in difference.values()):
        return ''

    # Difference models refer to existing objects, so always use rdf:about
    _, rdf_resource = rdf_xml_identifiers()
    row = INDENT*2 + f'<rdf:Description rdf:about="{rdf_resource}{rdf_id_text(uri)}">\n'
    for attribute, value in difference.items():
        if attribute not in cim_class.__dataclass_fields__:
            continue
        for prop in field_properties(cim_class, attribute, value):
            row += INDENT*2 + property_to_xml(prop, NAMESPACES, rdf_resource)
    row += INDENT*2 + '</rdf:Description>\n'
    return row

def write_incremental(reverse:dict, forward:dict, filename:str):
    '''

    '''
    indent = '  '

    header = '<?xml version="1.0" encoding="utf-8"?>\n'
    header += '<rdf:RDF'
    for prefix in NAMESPACES:
        header += f' xmlns:{prefix}="{NAMESPACES[prefix]}"'
    header += '>\n'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write('<dm:DifferenceModel xmlns:dm="http://iec.ch/2002/schema/CIM_difference_model#">\n')
        f.write(indent + '<dm:forwardDifferences rdf:parseType="Statements">\n')
        if forward is not None:
            for cim_class in forward:
                for uri in forward[cim_class]:
                    f.write(incremantal_row(cim_class, uri, forward[cim_class][uri]))
        f.write(indent + '</dm:forwardDifferences>\n')
        f.write(indent + '<dm:reverseDifferences rdf:parseType="Statements">\n')
        if reverse is not None:
            for cim_class in reverse:
                for uri in reverse[cim_class]:
                    f.write(incremantal_row(cim_class, uri, reverse[cim_class][uri]))
        f.write(indent + '</dm:reverseDifferences>\n')
        f.write('</dm:DifferenceModel>\n')
        f.write('</rdf:RDF>')



def clean_inverse_reference(related_obj: any, attr_name: str, obj_to_remove: any) -> None:
    """
    Remove obj_to_remove from related_obj.attr_name: from the list, or clear the reference.
    A related value that is not a CIM object, or whose class has no attr_name in this
    profile (CIMTool profiles may keep only one end of an association), is left alone.
    """
    if not isinstance(related_obj, Identity) or attr_name not in related_obj.__dataclass_fields__:
        return
    related_value = getattr(related_obj, attr_name)
    if isinstance(related_value, list):
        if obj_to_remove in related_value:
            related_value.remove(obj_to_remove)
    elif related_value is obj_to_remove:
        setattr(related_obj, attr_name, None)


def add_inverse_reference(related_obj: any, attr_name: str, obj_to_add: Identity,
                          attribute: str) -> None:
    """
    Make related_obj.attr_name refer to obj_to_add, the inverse of obj_to_add.attribute
    referring to related_obj. A single-valued end that referred to another object is moved,
    and that object's attribute no longer lists related_obj. Same skip rules as
    clean_inverse_reference.
    """
    if not isinstance(related_obj, Identity) or attr_name not in related_obj.__dataclass_fields__:
        return
    if 'list' in related_obj.__dataclass_fields__[attr_name].type:
        related_list = getattr(related_obj, attr_name)
        if obj_to_add not in related_list:
            related_list.append(obj_to_add)
        return
    previous = getattr(related_obj, attr_name)
    if previous is not None and previous is not obj_to_add:
        clean_inverse_reference(previous, attribute, related_obj)
    setattr(related_obj, attr_name, obj_to_add)


def sync_inverse_references(obj: Identity, attribute: str, old_value: any, new_value: any) -> None:
    """
    Update the inverse end of association obj.attribute after it changed from old_value
    to new_value (each None, an object or a list of objects). No-op for attributes that
    are not associations with an inverse.
    """
    attr_field = obj.__dataclass_fields__[attribute]
    inverse = attr_field.metadata.get('inverse')
    if inverse is None:
        return
    inverse_attr = inverse.split('.')[1]
    old_objects = _as_list(old_value)
    new_objects = _as_list(new_value)
    for related in old_objects:
        if not any(related is new for new in new_objects):
            clean_inverse_reference(related, inverse_attr, obj)
    for related in new_objects:
        add_inverse_reference(related, inverse_attr, obj, attribute)


def _as_list(value: any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return list(value)
    return [value]
