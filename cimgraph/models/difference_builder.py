from __future__ import annotations
from dataclasses import fields
from cimgraph.data_profile.identity import Identity

def new_obj_difference(new_object:Identity, differences:dict[str, dict]):
    if not isinstance(new_object, Identity):
        raise TypeError('Input must be a CIM class')
    
    cim_class = new_object.__class__
    uuid = new_object.identifier

    if cim_class not in differences:
        differences['forwardDifferences'][cim_class] = {}
    if uuid not in differences['forwardDifferences'][cim_class]:
        differences['forwardDifferences'][cim_class][uuid] = {}

    for field in fields(cim_class):
        if field.name == 'identifier': # Skip CIM 18 Identity.identifier
            continue
        if 'list' not in field.type:
            value = getattr(new_object, field.name)
            if value is not None:
                if isinstance(value, Identity):
                    differences['forwardDifferences'][cim_class][uuid][field.name] = value.uri()
                else:
                    differences['forwardDifferences'][cim_class][uuid][field.name] = str(value)

def del_obj_difference(new_object:Identity, differences:dict[str, dict]):
    if not isinstance(new_object, Identity):
        raise TypeError('Input must be a CIM class')
    
    cim_class = new_object.__class__
    uuid = new_object.identifier

    if cim_class not in differences:
        differences['reverseDifferences'][cim_class] = {}
    if uuid not in differences['reverseDifferences'][cim_class]:
        differences['reverseDifferences'][cim_class][uuid] = {}

    for field in fields(cim_class):
        if field.name == 'identifier': # Skip CIM 18 Identity.identifier
            continue
        if 'list' not in field.type:
            value = getattr(new_object, field.name)
            if value is not None:
                if isinstance(value, Identity):
                    differences['reverseDifferences'][cim_class][uuid][field.name] = value.uri()
                else:
                    differences['reverseDifferences'][cim_class][uuid][field.name] = str(value)

