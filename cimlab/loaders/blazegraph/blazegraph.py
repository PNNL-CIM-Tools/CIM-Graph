from __future__ import annotations
from typing import Dict, List, Optional
from SPARQLWrapper import SPARQLWrapper, JSON, POST
import re
import importlib
from cimlab.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cimlab.models.model_parsers import add_to_catalog, add_to_typed_catalog

class BlazegraphConnection(ConnectionInterface):
    def __init__(self, connection_params, cim_profile:str):
        self.sparql = importlib.import_module('cimlab.loaders.sparql.' + cim_profile)
        self.cim = importlib.import_module('cimlab.data_profile.' + cim_profile)
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
                print('warning: object class missing from data profile:', cls)
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
#         print(sparql_message)
        query_output = self.execute(sparql_message)
#         print(query_output)

#         attribute_list = query_output['head']['vars'] #list of attributes received in query response
        for result in query_output['results']['bindings']: #iterate through rows of response
            attribute_list = result.keys()
            mRID = result['mRID']['value']
            for attribute in attribute_list: 
                try: #check if attribute is in data profile
                    attribute_type = cim_class.__dataclass_fields__[attribute].type
                except:
                    #replace with warning message
                    print('warning: attribute ', attribute, ' missing from ', cim_class.__name__)
                    
                if 'List' in attribute_type: #check if attribute is association to a list of class objects
                    if '\'' in attribute_type: #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'List\[\'(.*)\']',attribute_type)
                        attribute_class = at_cls.group(1)
                    else:        
                        at_cls = re.match(r'List\[(.*)]',attribute_type)
                        attribute_class = at_cls.group(1)
#                     print(attribute_class)
                    # pass query response of associated objects to list parser
                    self.query_list_parser(feeder_mrid, typed_catalog, cim_class, mRID, result, attribute, attribute_class, ';')

                else: #otherwise assign query response
#                     print(attribute)
#                     print(result)
                    self.query_parser(feeder_mrid, typed_catalog, cim_class, mRID, result, attribute, ';')
                    
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
        mrid_list = list(typed_catalog[cim_class].keys()) #get all object mRIDs in switch area
        #generate SPARQL message from correct loaders>sparql python script based on class name
        sparql_message = eval(f"self.sparql.{cim_class.__name__}SPARQL.get_all_attributes('{feeder_mrid}', {mrid_list})") 
        return sparql_message
    
    
    def query_parser(self, feeder_mrid, typed_catalog:Dict, class_name:str, mRID:str, query:List, attribute:str, separator:str) -> object | str:
    #     try:
        value = query[attribute]['value']

        #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
    #         print(attribute)
        if attribute in self.cim.__all__:
            value = value.split(separator)
            result = self.build_cim_object(feeder_mrid, typed_catalog, value)
            if len(result) == 1:
                result = result[0]
        else:
            result = value
        setattr(typed_catalog[class_name][mRID], attribute, result)

    def query_list_parser(self, feeder_mrid, typed_catalog:Dict, class_name:type, mRID:str, query:List, attribute:str, attribute_class:str, separator:str):
        value = query[attribute]['value']
        values = value.split(separator)
        #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
        if attribute_class in self.cim.__all__:
            obj_list = self.build_cim_object(feeder_mrid, typed_catalog, values, attribute_class)    
        else:
            obj_list = values
        #set attribute of queried object to list parsed from query results
        setattr(typed_catalog[class_name][mRID], attribute, obj_list)


    def build_cim_object(self, feeder_mrid, typed_catalog:Dict, mRID_list:List[str], default_class = 'IdentifiedObject') -> List(object):
        sparql_message = self.sparql.get_class_type_sparql(feeder_mrid, mRID_list)
        #execute sparql query
        query_output = self.execute(sparql_message)
        # parse query results and add new CIM objects to list
        obj_list = [] 
        for result in query_output['results']['bindings']:
            class_name = result['class']['value']
            mRID = result['mRID']['value']
            name = result['name']['value']
            obj = self.create_object(typed_catalog, class_name, mRID, name)
            obj_list.append(obj)
        
        if '' not in mRID_list and not obj_list:
            for mrid in mRID_list:
                print('warning: could not locate mrid: ', mrid,'. creating default object of ', default_class)
                obj = self.create_object(typed_catalog, default_class, mrid, None)
                obj_list.append(obj)
        return obj_list

    def create_object(self, typed_catalog, class_name, mRID, name):
        cls = class_name
#         try: 
        class_type = eval(f"self.cim.{cls}")
        #add class to typed_catalog if not already defined
        if class_type not in typed_catalog.keys():
            typed_catalog[class_type] = {}

        if mRID in typed_catalog[class_type].keys():
            obj = typed_catalog[class_type][mRID]
        else:
#                 print(class_type)
                obj = class_type(mRID = mRID, name = name)
                add_to_typed_catalog(obj, typed_catalog)
#         except:
#         obj = mRID
#         print('warning: object class missing from data profile:', cls)
        return obj
