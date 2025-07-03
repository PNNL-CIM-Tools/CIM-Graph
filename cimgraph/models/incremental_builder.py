from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import fields, is_dataclass
from uuid import UUID

from defusedxml.ElementTree import parse

from cimgraph.data_profile.attribute_utils import validate_attr_datatype
from cimgraph.data_profile.identity import Identity
from cimgraph.databases import (ConnectionInterface, get_cim_profile, get_iec61970_301,
                                get_namespace)

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


    # Find the DifferenceModel element
    diff_model = root.find('.//dm:DifferenceModel', NAMESPACES)
    if diff_model is None:
        # Fall back to the alternate namespace in the XML
        NAMESPACES['dm'] = 'http://iec.ch/TC57/61970-552/DifferenceModel#'
        diff_model = root.find('.//dm:DifferenceModel', NAMESPACES)

    if diff_model is None:
        raise ValueError('Could not find DifferenceModel element')

    # Process forward and reverse differences
    for diff_type in ['forwardDifferences', 'reverseDifferences']:
        diff_element = diff_model.find(f'dm:{diff_type}', NAMESPACES)

        if diff_element is not None:
            # Find all Description elements under this difference type
            descriptions = diff_element.findall('rdf:Description', NAMESPACES)

            for desc in descriptions:
                # Get the URI (remove the leading '#' if present)
                uri = desc.get(f'{{{NAMESPACES["rdf"]}}}about')
                uri = uri.strip('#').strip('urn:uuid:')

                # Process each attribute in the Description
                for child in desc:
                    # Extract tag without namespace prefix
                    tag = child.tag
                    if '}' in tag:
                        tag = tag.split('}', 1)[1]  # Remove namespace part

                    # Store the value in the dictionary
                    incremental[diff_type][uri][tag] = child.text

    return incremental




def validate_incremental(message:dict, connection:ConnectionInterface,
                        graph:dict[type, dict[UUID, object]]) -> dict:
    '''
    Validate CIM incremental against classes and attributes in profile
    '''
    get_cim_profile.cache_clear()
    cim_profile, cim = get_cim_profile()

    for uri in message['reverseDifferences']:
        try:
            identifier = UUID(uri.strip('_').lower())
        except:
            _log.warning(f'Invalid UUID string {uri}')
            message['reverseDifferences'][uri] = {}
            # del message['reverseDifferences'][uri]
            continue
        found = False
        for cim_class in graph:
            if identifier in graph[cim_class]:
                found = True
                obj = graph[cim_class][identifier]
                break
        if not found:
            obj = connection.get_object(mRID=uri)
            if obj is None:
                _log.warning(f'Could not find any objects with reverse difference mRID {uri}')
                message['reverseDifferences'][uri] = {}
                # del message['reverseDifferences'][uri]
                continue
        for attribute in message['reverseDifferences'][uri]:
            parent = attribute.split('.')[0]
            try:
                parent = getattr(cim, parent)
            except:
                _log.warning(f'{parent} not found in CIM profile {cim_profile}' )
            if parent not in obj.__class__.__mro__:
                _log.warning(f'{obj.__class__.__name__} does not inherit from {parent}' )

            attr = attribute.split('.')[1]
            old_value = message['reverseDifferences'][uri][attribute]
            current_value = getattr(obj, attr)
            if attr not in obj.__class__.__dataclass_fields__:
                _log.warning(f'{obj.__class__.__name__} does not have attribute {attribute}' )
                message['reverseDifferences'][uri] = {}

            valid, attr_datatype, old_value = validate_attr_datatype(obj.__class__, attr, old_value)
            if not valid:
                _log.warning(f'{attribute} with reverse value {old_value} should have datatype {attr_datatype}')
            if current_value != old_value:
                _log.warning(f'Current value {current_value} does not match reverse {old_value}')



    for uri in message['forwardDifferences']:
        try:
            identifier = UUID(uri.strip('_').lower())
        except:
            _log.warning(f'Invalid UUID string {uri}')
            message['forwardDifferences'][uri] = {}

        for cim_class in graph:
            if identifier in graph[cim_class]:
                found = True
                obj = graph[cim_class][identifier]
                break
        if not found:
            obj = connection.get_object(mRID=uri)


        for attribute in message['forwardDifferences'][uri]:
            parent = attribute.split('.')[0]
            validated = True
            try:
                parent = getattr(cim, parent)
            except:
                validated = False
                _log.warning(f'{parent} not found in CIM profile {cim_profile}' )

            if parent not in obj.__class__.__mro__ and obj is not None:
                validated = False
                _log.warning(f'{obj.__class__.__name__} does not inherit from {parent}' )

            attr = attribute.split('.')[1]
            new_value = message['forwardDifferences'][uri][attribute]
            if obj is not None:
                if attr not in obj.__class__.__dataclass_fields__:
                    validated = False
                    _log.warning(f'{obj.__class__.__name__} does not have attribute {attribute}' )
                    # del message['forwardDifferences'][uri]
                valid, attr_datatype, new_value = validate_attr_datatype(obj.__class__, attr, new_value)
                if not valid:
                    validated = False
                    _log.warning(f'{attribute} with forward value {new_value} should have datatype {attr_datatype}')

            elif is_dataclass(parent):
                if attr not in parent.__dataclass_fields__:
                    validated = False
                    _log.warning(f'{parent.__name__} does not have attribute {attribute}' )
                    # del message['forwardDifferences'][uri]
                valid, attr_datatype, new_value = validate_attr_datatype(parent, attr, new_value)

                if not valid:
                    _log.warning(f'{attribute} with forward value {new_value} should have datatype {attr_datatype}')
            if not validated:
                message['forwardDifferences'][uri] = {}
                # del message['forwardDifferences'][uri]

    return message


def modify_from_incremental(message:dict, connection:ConnectionInterface,
                        graph:dict[type, dict[UUID, object]]):
    modified = []
    obj = None
    for uri in message['forwardDifferences']:
        identifier = UUID(uri.strip('_').lower())
        for cim_class in graph:
            if identifier in graph[cim_class]:
                obj = graph[cim_class][identifier]
                break
        if obj is not None:
            for attribute in message['forwardDifferences'][uri]:
                attr = attribute.split('.')[1]
                new_value = message['forwardDifferences'][uri][attribute]
                setattr(obj,attr,new_value)
                modified.append(obj)
        else:
            # TODO: Create new object
            pass
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

    if isinstance(new_value, Identity):
        differences['forwardDifferences'][cim_class][uuid][attribute] = new_value.uri()
        differences['reverseDifferences'][cim_class][uuid][attribute] = old_value.uri()
    else:
        differences['forwardDifferences'][cim_class][uuid][attribute] = new_value
        differences['reverseDifferences'][cim_class][uuid][attribute] = old_value






def incremantal_row(cim_class:type, uri:str, difference:dict) -> str:

    iec61970_301=get_iec61970_301()
    attr_fields = cim_class.__dataclass_fields__
    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)

    if set(difference.values()) == {None}:
        return ''

    if iec61970_301>7:
        row = INDENT*2 + f'<rdf:Description rdf:about="urn:uuid:{uri}">\n'
    else:
        row = INDENT*2 + f'<rdf:Description rdf:about="#{uri}"/>\n'
    for attribute in difference:
        value = difference[attribute]

        if attribute in attr_fields and value is not None:


            for parent in parent_classes:
                if attribute in parent.__annotations__:

                    attr_type = attr_fields[attribute].metadata['type']
                    ns_prefix = REVERSE_NS[attr_fields[attribute].metadata['namespace']]
                    row += INDENT*3 + f'<{ns_prefix}:{parent.__name__}.{attribute}'
                    if 'attribute' in attr_type.lower() and 'enumeration' in attr_type.lower():
                        row += f'>{str(value)}</{ns_prefix}:{parent.__name__}.{attribute}>\n'
                    elif 'enumeration' in attr_type.lower():
                        row += f' rdf:resouce={ns_prefix}{str(value)}>\n'
                    else:
                        if isinstance(value, Identity):
                            row += f' rdf:resouce={ns_prefix}{value}>\n'
                            # row += f' rdf:resouce={ns_prefix}{value.uri()}>\n'
                        else:
                            # _log.warning(f'unknown format of {str(value)}')
                            row += f' rdf:resouce={ns_prefix}{str(value)}>\n'
    row += '</rdf:Description>\n'
    return row

def write_incremental(reverse:dict, forward:dict, filename:str):
    '''

    '''
    indent = '  '

    f = open(filename, 'w', encoding='utf-8')
    header = '<?xml version="1.0" encoding="utf-8"?>\n'
    header += '<rdf:RDF'
    for prefix in NAMESPACES:
        header += f' xmlns:{prefix}="{NAMESPACES[prefix]}"'
    header += '>\n'
    f.write(header)
    f.write('<dm:DifferenceModel xmlns:dm="http://iec.ch/2002/schema/CIM_difference_model#">\n')
    # f.write('<dm:DifferenceModel about="">\n')
    f.write(indent + '<dm:forwardDifferences rdf:parseType="Statements">\n')
    if forward is not None:
        for cim_class in forward:
            for uri in forward[cim_class]:
                row = incremantal_row(cim_class, uri, forward[cim_class][uri])
                f.write(row)
    f.write(indent + '</dm:forwardDifferences>\n')
    f.write(indent + '<dm:reverseDifferences rdf:parseType="Statements">\n')
    if reverse is not None:
        for cim_class in reverse:
            for uri in reverse[cim_class]:
                row = incremantal_row(cim_class, uri, reverse[cim_class][uri])
                f.write(row)
    f.write(indent + '</dm:reverseDifferences>\n')
    f.write('</dm:DifferenceModel>\n')
    f.write('</rdf:RDF>')
    f.close()



def clean_inverse_reference(related_obj: any, attr_name: str, obj_to_remove: any) -> None:
    """
    Clean up an inverse reference from a related object to the object being deleted.

    Args:
        related_obj: The object that might have references to the object being deleted
        attr_name: The attribute name on the related object that contains the reference
        obj_to_remove: The object being deleted
    """
    if related_obj is None:
        return
    try:
        related_value = getattr(related_obj, attr_name)

        # Handle collection (list/set) references
        if isinstance(related_value, list) and obj_to_remove in related_value:
            related_value.remove(obj_to_remove)
        elif isinstance(related_value, set) and obj_to_remove in related_value:
            related_value.remove(obj_to_remove)
        # Handle direct references
        elif related_value is obj_to_remove:
            setattr(related_obj, attr_name, None)
    except Exception as e:
        _log.warning(f'Unable to remove {attr_name} from {related_obj} and {obj_to_remove} due to error \n {e}')
