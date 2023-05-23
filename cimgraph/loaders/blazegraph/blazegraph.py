from __future__ import annotations

import importlib
import logging
import re
from typing import Dict, List, Optional

from cimgraph.loaders import (ConnectionInterface, ConnectionParameters,
                              Parameter, QueryResponse)
from cimgraph.models.model_parsers import add_to_catalog, add_to_typed_catalog
from SPARQLWrapper import JSON, POST, SPARQLWrapper

_log = logging.getLogger(__name__)

class BlazegraphConnection(ConnectionInterface):
    def __init__(self, connection_params, cim_profile:str):
        self.sparql = importlib.import_module('cimgraph.loaders.sparql.' + cim_profile)
        self.cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)
        self.sparql_obj: Optional[SPARQLWrapper] = None
        self.connection_params = connection_params

    def connect(self):
        if not self.sparql_obj:
            url = self.connection_params.parameters[0].value
            self.sparql_obj = SPARQLWrapper(url)
            self.sparql_obj.setReturnFormat(JSON)

    def disconnect(self):
        self.sparql_obj = None
        
    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        self.sparql_obj.setQuery(query_message)
        self.sparql_obj.setMethod(POST)
        query_output = self.sparql_obj.query().convert()
        return query_output

        
    def create_default_instances(self, feeder_mrid: str | cim.Feeder, mrid_list: List[str]) -> List[object]:
        """ 
        Creates empty CIM objects with the correct class type with mRID and name fields populated based on 
        a list of mRID strings.
        Args:
            feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
            mrid_list (list[str]): A list of object mRID strings to be converted into CIM objects
        Returns:
            object_list: A list of CIM object instances
        """
        #generate correct sparql message using create_default.py
        sparql_message = self.sparql.get_class_type_sparql(feeder_mrid, mrid_list)
        #execute sparql query
        query_output = self.execute(sparql_message)
        # parse query results and add new CIM objects to list
        object_list = [] 
        for result in query_output['results']['bindings']:
           # print(result)
            cls = result['class']['value']
            mRID = result['mRID']['value']
            name = result['name']['value']
            try:
                object_list.append(eval(f"self.cim.{cls}(mRID='{mRID}', name = '{name}')"))
            except:
                _log.warning('object class missing from data profile:' + str(cls))
        return object_list
    
    
          
    def get_all_attributes(self, feeder_mrid: str | cim.Feeder, typed_catalog: dict[type, dict[str, object]], cim_class: type):
        """ Populates all available attribute fields of CIM objects in the typed catalog of a specified CIM class. 
        Objects are stored in memory, so no values are returned.
        Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
        cim_class (type): The CIM class type (e.g. cim:ACLineSegment)
        Returns:
        none
        """
        #generate SPARQL message from correct loaders>sparql python script based on class name
        sparql_message = self.get_attributes_query(feeder_mrid, typed_catalog, cim_class)
        #execute sparql query
        query_output = self.execute(sparql_message)

        for result in query_output['results']['bindings']: #iterate through rows of response
            attribute_list = result.keys()
            mRID = result['mRID']['value']
            for attribute in attribute_list: 
                try: #check if attribute is in data profile
                    attribute_type = cim_class.__dataclass_fields__[attribute].type
                except:
                    #replace with warning message                       
                    _log.warning('attribute '+str(attribute) +' missing from '+str(cim_class.__name__))
                    
                if 'List' in attribute_type: #check if attribute is association to a list of class objects
                    if '\'' in attribute_type: #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'List\[\'(.*)\']',attribute_type)
                        attribute_class = at_cls.group(1)
                    else:        
                        at_cls = re.match(r'List\[(.*)]',attribute_type)
                        attribute_class = at_cls.group(1)
                    # pass query response of associated objects to list parser
                    self.query_list_parser(feeder_mrid, typed_catalog, cim_class, mRID, result, attribute, attribute_class, ';')
                elif 'Optional' in attribute_type: #check if attribute is association to a class object
                    if '\'' in attribute_type: #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'Optional\[\'(.*)\']',attribute_type)
                        attribute_class = at_cls.group(1)
                    else:        
                        at_cls = re.match(r'Optional\[(.*)]',attribute_type)
                        attribute_class = at_cls.group(1)

                    # pass query response of associated objects to list parser
                    self.query_parser(feeder_mrid, typed_catalog, cim_class, mRID, result, attribute, attribute_class, ';')
                else: #otherwise assign query response

                    self.query_parser(feeder_mrid, typed_catalog, cim_class, mRID, result, attribute, attribute_class, ';')
                    
    def get_attributes_query(self, feeder_mrid: str | cim.Feeder, typed_catalog: dict[type, dict[str, object]], cim_class: type):
        """ Generates SPARQL query for a given catalog of objects and feeder id
        Args:
            feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
            typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
                class type and object mRID
            cim_class (type): The CIM class type (e.g. cim:ACLineSegment)
        Returns:
            sparql_message: query string that can be used in blazegraph connection or STOMP client
        none
        """
        sparql_func = getattr(self.sparql, f"{cim_class.__name__}SPARQL")
        sparql_message = sparql_func.get_all_attributes(feeder_mrid, typed_catalog)
        
        return sparql_message
    
    
    def query_parser(self, feeder_mrid, typed_catalog:Dict, class_name:str, mRID:str, query:List, attribute:str, attribute_class:str, separator:str) -> object | str:
        value = query[attribute]['value']
        #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
        if attribute_class in self.cim.__all__:
            value = value.split(',')
            obj_mrid = value[0]
            try:
                obj_class = value[1]
            except:
                obj_class = attribute_class
            class_type = eval(f"self.cim.{obj_class}")
            if type(class_type) is type and len(obj_mrid) > 0:
                result = self.create_object(typed_catalog, class_type, obj_mrid)

            else:
                result = value

        else:
            result = value
        setattr(typed_catalog[class_name][mRID], attribute, result)

    def query_list_parser(self, feeder_mrid, typed_catalog:Dict, class_name:type, mRID:str, query:List, attribute:str, attribute_class:str, separator:str):
        value = query[attribute]['value']
        values = value.split(separator)
        obj_list = []
        #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
        if attribute_class in self.cim.__all__:
            for value in values:
                value = value.split(',')
                obj_mrid = value[0]
                try:
                    obj_class = value[1]
                except:
                    obj_class = attribute_class
                class_type = eval(f"self.cim.{obj_class}")
                if type(class_type) is type and len(obj_mrid) > 0:
                    result = self.create_object(typed_catalog, class_type, obj_mrid)
                    obj_list.append(result)
                else:
                    obj_list = values
        else:
            obj_list = values
        #set attribute of queried object to list parsed from query results
        setattr(typed_catalog[class_name][mRID], attribute, obj_list)


    def create_object(self, typed_catalog, class_type, mRID):
        
        if class_type not in typed_catalog.keys():
            typed_catalog[class_type] = {}

        if mRID in typed_catalog[class_type].keys():
            obj = typed_catalog[class_type][mRID]
        else:
                obj = class_type(mRID = mRID)
                add_to_typed_catalog(obj, typed_catalog)

        return obj
