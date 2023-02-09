from __future__ import annotations
import sys
import atexit
import importlib
import os

from typing import Dict, List
from SPARQLWrapper import SPARQLWrapper, JSON, POST
import re
from cimlab.data_profile import CIM_PROFILE
from cimlab.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cimlab.models import add_to_catalog, add_to_typed_catalog
from gridappsd import GridAPPSD
from SPARQLWrapper import SPARQLWrapper, JSON, POST
from cimlab.loaders.blazegraph.blazegraph import BlazegraphConnection


cim = None
sparql = None


def set_cim_profile(cim_profile: CIM_PROFILE):
    global cim
    global sparql
    cim = importlib.import_module('cimlab.data_profile.' + cim_profile)
    sparql = importlib.import_module('cimlab.loaders.sparql.' + cim_profile)

os.environ["GRIDAPPSD_ADDRESS"] = "localhost"
os.environ["GRIDAPPSD_PORT"] = "61613"
os.environ['GRIDAPPSD_APPLICATION_ID'] = 'gridappsd-cim-profile'
os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
os.environ['GRIDAPPSD_USER'] = 'app_user'
os.environ['GRIDAPPSD_PASSWORD'] = '1234App'




class GridappsdConnection(ConnectionInterface):
    __gapps__ = GridAPPSD()

    
    def connect(self):
        if self.__gapps__ is None:
            self.__gapps__ = GridAPPSD()

    def disconnect(self):
        if self.__gapps__ is not None:
            self.__gapps__.disconnect()
            
#     def load_attributes(self, obj: object):
#         if isinstance(obj, cim.Terminal):
#             # load terminal stuff here
#             pass
        
    def get_logger(self):
        self.connect()
        return self.__gapps__.get_logger()
    
    def query_data(self, query, database_type="powergridmodel", timeout=30):
        response = self.__gapps__.query_data(query, database_type, timeout)
        return response['data']
    
    def execute(self, sparql_message):
        params = ConnectionParameters([Parameter(key="url", value="http://localhost:8889/bigdata/namespace/kb/sparql")])
        bg = BlazegraphConnection(params, 'rc4_2021')
        return bg.execute(sparql_message)

    def create_default_instances(self, feeder_mrid: str | cim.Feeder, mrid_list: List[str]) -> List[object]:
        """ Creates an empty CIM object with the correct class type with mRID and name fields populated
        Args:
            feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
            mrid_list (list[str]): A list of object mRID strings to be converted into CIM objects
        Returns:
            objects: A list of CIM object instances
        """
        sparql_message = sparql.get_class_type_sparql(feeder_mrid, mrid_list)
#         query_output = self.query_data(sparql_message)
        query_output = self.execute(sparql_message)
        
        # parse query results and add new CIM objects to list
        object_list = [] 
        for result in query_output['results']['bindings']:
           # print(result)
            cls = result['class']['value']
            mRID = result['mRID']['value']
            name = result['name']['value']
            try:
                object_list.append(eval(f"cim.{cls}(mRID='{mRID}', name = '{name}')"))
            except:
                print('warning: object class missing from data profile:', cls)
        return object_list

    
    def get_all_attributes(self, feeder_mrid, typed_catalog, cim_class):
         #generate SPARQL message from correct loaders>sparql python script based on class name
        sparql_message = self.get_attributes_query(feeder_mrid, typed_catalog, cim_class)
        #execute sparql query

        query_output = self.execute(sparql_message)
#         query_output = self.query_data(sparql_message)


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
                elif 'Optional' in attribute_type: #check if attribute is association to a class object
                    if '\'' in attribute_type: #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'Optional\[\'(.*)\']',attribute_type)
                        attribute_class = at_cls.group(1)
                    else:        
                        at_cls = re.match(r'Optional\[(.*)]',attribute_type)
                        attribute_class = at_cls.group(1)
#                     print(attribute_class)
                    # pass query response of associated objects to list parser
                    self.query_parser(feeder_mrid, typed_catalog, cim_class, mRID, result, attribute, attribute_class, ';')
                else: #otherwise assign query response
#                     print(attribute)
#                     print(result)
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
        sparql_func = getattr(sparql, f"{cim_class.__name__}SPARQL")
        sparql_message = sparql_func.get_all_attributes(feeder_mrid, typed_catalog) 
        return sparql_message
    
    
    def query_parser(self, feeder_mrid, typed_catalog:Dict, class_name:str, mRID:str, query:List, attribute:str, attribute_class:str, separator:str) -> object | str:
    #     try:
        value = query[attribute]['value']

        #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
    #         print(attribute)
        if attribute in cim.__all__:
            value = value.split(separator)
            class_type = eval(f"cim.{attribute_class}")
            if type(class_type) is type:
                result = self.build_cim_object(feeder_mrid, typed_catalog, value, attribute_class)  
            else:
                result = [value]
            if len(result) == 1:
                result = result[0]
        else:
            result = value
        setattr(typed_catalog[class_name][mRID], attribute, result)

    def query_list_parser(self, feeder_mrid, typed_catalog:Dict, class_name:type, mRID:str, query:List, attribute:str, attribute_class:str, separator:str):
        value = query[attribute]['value']
        values = value.split(separator)
        #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
        if attribute_class in cim.__all__:
            class_type = eval(f"cim.{attribute_class}")
            if type(class_type) is type:
                obj_list = self.build_cim_object(feeder_mrid, typed_catalog, values, attribute_class)
            else:
                obj_list = values    
        else:
            obj_list = values
        #set attribute of queried object to list parsed from query results
        setattr(typed_catalog[class_name][mRID], attribute, obj_list)


    def build_cim_object(self, feeder_mrid, typed_catalog:Dict, mRID_list:List[str], default_class = 'IdentifiedObject') -> List(object):
        sparql_message = sparql.get_class_type_sparql(feeder_mrid, mRID_list)
        #execute sparql query
#         query_output = self.query_data(sparql_message)
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
        class_type = eval(f"cim.{cls}")
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




def get_topology_response(feeder_mrid: str) -> QueryResponse:
    assert feeder_mrid is not None

    gapps = GridAPPSD()
    topic = "goss.gridappsd.request.data.topology"
    message = {
        "requestType": "GET_SWITCH_AREAS",
        "modelID": feeder_mrid,
        "resultFormat": "JSON"
    }

    topo_response = gapps.get_response(topic=topic, message=message, timeout=30)
    return topo_response

# Close gridappsd connection when exiting program.
#atexit.register(lambda: __gapps__.disconnect())
