from __future__ import annotations

import atexit
import os
from typing import Dict, List

import cimlab.data_profile as cim
from cimlab.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cimlab.models import add_to_catalog, add_to_typed_catalog
from gridappsd import GridAPPSD
from SPARQLWrapper import SPARQLWrapper, JSON, POST
import cimlab.loaders.sparql as sparql


# os.environ["GRIDAPPSD_ADDRESS"] = "gridappsd"
# os.environ["GRIDAPPSD_PORT"] = "61613"
os.environ['GRIDAPPSD_APPLICATION_ID'] = 'gridappsd-cim-profile'
os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
os.environ['GRIDAPPSD_USER'] = 'app_user'
os.environ['GRIDAPPSD_PASSWORD'] = '1234App'

def query_string_parser(obj_dict: Dict, mRID: str, query: List, key: str, separator):
    try:
        value = query[key]['value']
        if separator in value:
            value = value.split(separator)
        setattr(obj_dict[mRID], key, value)
    except:
        []

def query_class_parser(typed_catalog, mRID, query, class_name, separator):
    try: 
        cls = class_name
        value = query[class_name]['value']
        if separator in value:
            values = value.split(separator)
            obj = []
            for mrid in values:
                obj.append(eval(f"cim.{cls}(mRID='{mrid}')"))
        else:
            obj = eval(f"cim.{cls}(mRID='{value}')")
        setattr(typed_catalog[mRID], class_name, obj)
    except:
        []
    return typed_catalog

def query_list_parser(obj_dict: Dict, mRID: str, query: List, key, separator):

    try:
        value = query[key]['value'].split(separator)
        if getattr(obj_dict[mRID], key) == None:
            setattr(obj_dict[mRID], key, value)
        else:
            setattr(obj_dict[mRID], key, getattr(obj_dict[mRID], key) + value)
    except:
        []


class GridappsdConnection(ConnectionInterface):
    __gapps__ = None

    def connect(self):
        if self.__gapps__ is None:
            self.__gapps__ = GridAPPSD()

    def disconnect(self):
        if self.__gapps__ is not None:
            self.__gapps__.disconnect()

    def load_attributes(self, obj: object):
        if isinstance(obj, cim.Terminal):
            # load terminal stuff here
            pass
        
    def get_logger(self):
        self.connect()
        return self.__gapps__.get_logger()
    
    def query_data(self, query, database_type="powergridmodel", timeout=30):
        return self.__gapps__.query_data(query, database_type, timeout)

    def create_default_instances(self, feeder_mrid: str | cim.Feeder, mrid_list: List[str]) -> List[object]:
        """ Creates an empty CIM object with the correct class type with mRID and name fields populated
        Args:
            feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
            mrid_list (list[str]): A list of object mRID strings to be converted into CIM objects
        Returns:
            objects: A list of CIM object instances
        """
        sparql_message = sparql.create_default_sparql(feeder_mrid, mrid_list, False)
        objects = self.query_object_builder(sparql_message)
        return objects
    
    def get_all_attributes(self, feeder_mrid, typed_catalog, cim_class):
        if cim_class in typed_catalog:
            mrid_list = list(typed_catalog[cim_class].keys())
            sparql_message = eval(f"sparql.{cim_class.__name__}SPARQL.get_all_attributes('{feeder_mrid}', {mrid_list})")
            self.query_attribute_builder(sparql_message, typed_catalog, cim_class)
    
    def query_object_builder(self, query_message):
        self.connect()
        request = {"requestType": "QUERY",
                   "resultFormat": "JSON",
                   "queryString": query_message}
        query_output = self.execute(topic='goss.gridappsd.process.request.data.powergridmodel',message=request, timeout=5)
        
        objects = []
        for result in query_output['data']['results']['bindings']:
            cls = result['class']['value']
            mRID = result['mRID']['value']
            name = result['name']['value']
            try:
                objects.append(eval(f"cim.{cls}(mRID='{mRID}', name = '{name}')"))
            except:
                print('warning: object class missing:', cls)
        return objects

    def execute(self, **kwargs) -> QueryResponse:
        for x in ('topic', 'message', 'timeout'):
            if x not in kwargs:
                raise ValueError(f"Parameter {x} required")

        response = self.__gapps__.get_response(**kwargs)
        return response
    
    def query_attribute_builder(self, query_message, typed_catalog, cim_class):
        self.connect()
        request = {"requestType": "QUERY",
                   "resultFormat": "JSON",
                   "queryString": query_message}
        query_output = self.execute(topic='goss.gridappsd.process.request.data.powergridmodel',message=request, timeout=5)
        attribute_list = query_output['data']['head']['vars']
        for result in query_output['data']['results']['bindings']:
            mRID = result['mRID']['value']
            name = result['name']['value']
            for attribute in attribute_list:
                if attribute == 'Measurements' or attribute == 'Terminals':
                    query_list_parser(typed_catalog[cim_class], mRID, result, attribute, ';')
                elif attribute in cim.__all__:
                    query_class_parser(typed_catalog[cim_class], mRID, result, attribute, ';')
                    try:
                        add_to_typed_catalog(getattr(typed_catalog[cim_class][mRID], attribute), typed_catalog)
                    except:
                        []
                else:
                    query_string_parser(typed_catalog[cim_class], mRID, result, attribute, ';')
#             query_list_parser(typed_catalog[cim_class], mRID, result, 'Measurements', ';')
#             query_list_parser(typed_catalog[cim_class], mRID, result, 'Terminals', ';')


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
