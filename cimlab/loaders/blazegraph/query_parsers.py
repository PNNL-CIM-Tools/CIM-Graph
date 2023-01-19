from __future__ import annotations
from typing import Dict, List, Optional
import traceback
from cimlab.models.model_parsers import add_to_catalog, add_to_typed_catalog


def query_parser(conn, cim, feeder_mrid, typed_catalog:Dict, class_name:str, mRID:str, query:List, attribute:str, separator:str) -> object | str:
#     try:
    value = query[attribute]['value']

    #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
#         print(attribute)
    if attribute in cim.__all__:
        value = value.split(separator)
        result = build_cim_object(conn, cim, feeder_mrid, typed_catalog, value)
        if len(result) == 1:
            result = result[0]
    else:
        result = value
    setattr(typed_catalog[class_name][mRID], attribute, result)
#     except Exception:
#         traceback.print_exc()


def query_list_parser(conn, cim, feeder_mrid, typed_catalog:Dict, class_name:type, mRID:str, query:List, attribute:str, attribute_class:str, separator:str):
    value = query[attribute]['value']
    values = value.split(separator)
    #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
    if attribute_class in cim.__all__:
        obj_list = build_cim_object(conn, cim, feeder_mrid, typed_catalog, values)
    else:
        obj_list = values
    #set attribute of queried object to list parsed from query results
    setattr(typed_catalog[class_name][mRID], attribute, obj_list)
    

def build_cim_object(conn, cim, feeder_mrid, typed_catalog:Dict, mRID_list:List[str]) -> List(object):
    sparql_message = sparql.get_class_type_sparql(feeder_mrid, mRID_list)
    #execute sparql query
    query_output = conn.execute(sparql_message)
    # parse query results and add new CIM objects to list
    obj_list = [] 
#     print(query_output)
    for result in query_output['results']['bindings']:
       # print(result)
        class_name = result['class']['value']
        cls = class_name
        mRID = result['mRID']['value']
        name = result['name']['value']
        try: 
            class_type = eval(f"cim.{cls}")
            #add class to typed_catalog if not already defined
            if class_type not in typed_catalog.keys():
                typed_catalog[class_type] = {}

    #         for mRID in mRID_list:
                #add object to typed_catalog if not already included
            if mRID in typed_catalog[class_type].keys():
                obj = typed_catalog[class_type][mRID]
            else:
                    obj = class_type(mRID = mRID, name = name)
                    add_to_typed_catalog(obj, typed_catalog)
        except:
            obj = mRID
            print('warning: object class missing from data profile:', cls)

        obj_list.append(obj)
    return obj_list


