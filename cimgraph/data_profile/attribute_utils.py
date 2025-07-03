
from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

from cimgraph.data_profile.identity import Identity

_log = logging.getLogger(__name__)

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
