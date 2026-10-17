
from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum
from functools import cache
from typing import Any, Iterator, NamedTuple

from cimgraph.data_profile.units import CIMUnit

_log = logging.getLogger(__name__)


class Property(NamedTuple):
    """One serializable value of a CIM object attribute."""
    name: str       # RDF property name, e.g. 'ACLineSegment.length'
    namespace: str  # namespace of the attribute
    kind: str       # 'literal', 'unit', 'enum', or 'reference'
    value: Any      # a single value (list attributes yield one Property per item)

def convert_datatype(value, attribute_type):
    if 'bool' in attribute_type:
        if 'true' in str(value).lower()  or str(value).lower() == '1':
            value = True
        elif 'false' in str(value).lower() or str(value).lower() == '0':
            value = False

    elif 'int' in attribute_type:
        try:
            value = int(float(value))
        except:
            pass
            # _log.warning(f'{value} is not an integer')

    if 'float' in attribute_type:
        try:
            value = float(value)
        except:
            pass
            # _log.warning(f'{value} is not a float')
    return value

def get_attr_field(cim_class:dataclass, attribute:str):
    if attribute not in cim_class.__dataclass_fields__:
        _log.warning(f"{cim_class.__name__}.{attribute} not in CIM profile")
        return None
    else:
        return cim_class.__dataclass_fields__[attribute]


def get_attr_datatype(cim_class:dataclass, attribute:str) -> list[str]:
    datatype = [None]
    if attribute in cim_class.__dataclass_fields__:
        attr_field = cim_class.__dataclass_fields__[attribute]
        datatype = attr_field.type.split('[')[1].split(']')[0]
        if '|' in datatype:
            datatype = datatype.replace(' ','').split('|')
        else:
            datatype = [datatype]
    return datatype

def validate_attr_datatype(cim_class:dataclass, attribute:str, value:any) -> bool:
    attr_datatype = get_attr_datatype(cim_class, attribute)
    valid = True

    value = convert_datatype(value, attr_datatype)
    value_datatype = value.__class__.__name__

    if value_datatype == 'list':
        for item in value:
            item_check, _ = validate_attr_datatype(cim_class, attribute, item)
            if not item_check:
                valid = False
    else:
        valid = value_datatype in attr_datatype

    return valid, attr_datatype, value


def get_attr_uml_type(cim_class:dataclass, attribute:str):
    attr_field = get_attr_field(cim_class, attribute)
    uml_type = attr_field.metadata['type']
    return uml_type

def get_attr_field_type(cim_class:dataclass, attribute:str):
    attr_field = get_attr_field(cim_class, attribute)
    field_type = attr_field.type.split('[')[0]
    return field_type

def get_attr_inverse(cim_class:dataclass, attribute:str):
    try:
        attr_field = get_attr_field(cim_class, attribute)
        inverse = attr_field.metadata['inverse']
    except:
        inverse = None
    return inverse

def get_attr_serialize(cim_class:dataclass, attribute:str) -> bool:
    attr_field = get_attr_field(cim_class, attribute)
    return attr_field.metadata['serialize']

@cache
def get_attr_declaring_class(cim_class:dataclass, attribute:str) -> type:
    """Return the class in the inheritance chain that declares the attribute."""
    for parent in cim_class.__mro__[:-1]:
        if attribute in parent.__annotations__:
            return parent
    raise AttributeError(f'{cim_class.__name__}.{attribute} not declared in class hierarchy')

@cache
def get_serialized_attributes(cim_class:dataclass) -> tuple[str, ...]:
    """
    Return the attributes of a class that are written when serializing, in
    inheritance order (most-derived class first). Follows the serialize
    metadata, so each association is written from one end only.
    """
    attributes = []
    for parent in cim_class.__mro__[:-1]:
        for attribute in parent.__annotations__:
            if attribute == 'identifier' or attribute in attributes:
                continue
            if get_attr_serialize(cim_class, attribute):
                attributes.append(attribute)
    return tuple(attributes)

def field_properties(cim_class:dataclass, attribute:str, value:Any) -> list[Property]:
    """Classify an attribute value into Properties. Lists yield one Property per item."""
    if value is None or value == []:
        return []
    attr_field = get_attr_field(cim_class, attribute)
    name = f'{get_attr_declaring_class(cim_class, attribute).__name__}.{attribute}'
    namespace = attr_field.metadata['namespace']
    is_association = attr_field.metadata['type'] == 'Association'

    values = value if isinstance(value, list) else [value]
    properties = []
    for item in values:
        if is_association:
            kind = 'reference'
        elif isinstance(item, CIMUnit):
            kind = 'unit'
        elif isinstance(item, Enum):
            kind = 'enum'
        else:
            kind = 'literal'
        properties.append(Property(name, namespace, kind, item))
    return properties

def iter_properties(obj:object) -> Iterator[Property]:
    """Yield every serializable Property of a CIM object."""
    cim_class = obj.__class__
    for attribute in get_serialized_attributes(cim_class):
        yield from field_properties(cim_class, attribute, getattr(obj, attribute))
