from __future__ import annotations
from typing import Dict, List, Optional
import traceback
from cim.models.model_parsers import add_to_catalog, add_to_typed_catalog
import cim.data_profile as cim

def query_parser(typed_catalog:Dict, class_name:str, mRID:str, query:List, attribute:str, separator:str) -> object | str:
#     try:
    value = query[attribute]['value']

    #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
#         print(attribute)
    if attribute in cim.__all__:
        value = value.split(separator)
        result = build_cim_object(typed_catalog, attribute, value)
    else:
        result = value
    setattr(typed_catalog[class_name][mRID], attribute, result)
#     except Exception:
#         traceback.print_exc()


def query_list_parser(typed_catalog:Dict, class_name:type, mRID:str, query:List, attribute:str, attribute_class:str, separator:str):
    value = query[attribute]['value']
    values = value.split(separator)
    #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
    if attribute_class in cim.__all__:
        obj_list = build_cim_object(typed_catalog, attribute_class, values)
    else:
        obj_list = values
    #set attribute of queried object to list parsed from query results
    setattr(typed_catalog[class_name][mRID], attribute, obj_list)
    

def build_cim_object(typed_catalog:Dict, class_name:str, mRID_list:List[str]) -> List(object):
    cls = class_name
    #add class to typed_catalog if not already defined
    if class_name not in typed_catalog.keys():
        typed_catalog[class_name] = {}
    obj_list = []
    for mRID in mRID_list:
        #add object to typed_catalog if not already included
        if mRID in typed_catalog[class_name].keys():
            obj = typed_catalog[class_name][mRID]
        else:
            obj = eval(f"cim.{cls}(mRID='{mRID}')")
            add_to_typed_catalog(obj, typed_catalog)
        obj_list.append(obj)
    return obj_list
