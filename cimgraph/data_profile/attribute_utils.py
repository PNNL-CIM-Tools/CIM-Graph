
from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass


from cimgraph.data_profile.identity import Identity



_log = logging.getLogger(__name__)

def get_attr_field(cim_class:dataclass, attribute:str):
    if attribute not in cim_class.__dataclass_fields__:
        raise TypeError(f"{cim_class.__name__}.{attribute} not in CIM profile")
    
    return cim_class.__dataclass_fields__[attribute]


def get_attr_datatype(cim_class:dataclass, attribute:str) -> list[str]:
    attr_field = get_attr_field(cim_class, attribute)
    datatype = attr_field.type.split('[')[1].split(']')[0]
    if '|' in datatype:
        datatype = datatype.replace(' ','').split('|')
    else:
        datatype = [datatype]
    return datatype

def validate_attr_datatype(cim_class:dataclass, attribute:str, value:any) -> bool:
    attr_datatype = get_attr_datatype(cim_class, attribute)
    value_datatype = value.__class__.__name__
    valid = True

    if 'float' in attr_datatype:
        try: 
            if float(value) == value:
                value_datatype = 'float'
        except:
            pass

    if value_datatype == 'list':
        for item in value:
            item_check, _ = validate_attr_datatype(cim_class, attribute, item)
            if not item_check:
                valid = False
    else:
        valid = value_datatype in attr_datatype
    
    return valid, attr_datatype


def get_attr_uml_type(cim_class:dataclass, attribute:str):
    attr_field = get_attr_field(cim_class, attribute)
    uml_type = attr_field.metadata['type']
    return uml_type




    