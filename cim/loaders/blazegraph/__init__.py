from __future__ import annotations

from typing import Dict, List, Optional

from SPARQLWrapper import SPARQLWrapper, JSON, POST
from cim.models import add_to_catalog, add_to_typed_catalog

from cim.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
# from cim.loaders.blazegraph.blazegraph import BlazegraphConnection
import cim.data_profile as cim
import cim.loaders.sparql as sparql



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


def query_list_parser(obj_dict: Dict, mRID: str, query: List, key, separator):

    try:
        value = query[key]['value'].split(separator)
        if getattr(obj_dict[mRID], key) == None:
            setattr(obj_dict[mRID], key, value)
        else:
            setattr(obj_dict[mRID], key, getattr(obj_dict[mRID], key) + value)
    except:
        []
        



class BlazegraphConnection(ConnectionInterface):
    sparql_obj: Optional[SPARQLWrapper] = None

    def connect(self):
        if not self.sparql_obj:
            url = self.connection_params.parameters[0].value
            self.sparql_obj = SPARQLWrapper(url)
            self.sparql_obj.setReturnFormat(JSON)

    def disconnect(self):
        self.sparql_obj = None

    def load_attributes(self, obj: object):
        if isinstance(obj, cim.Terminal):
            # load terminal stuff here
            pass
        
    def query_object_builder(self, query_message):
        self.connect()
        self.sparql_obj.setQuery(query_message)
        self.sparql_obj.setMethod(POST)
        query_output = self.sparql_obj.query().convert()
        
        objects = []
        for result in query_output['results']['bindings']:
           # print(result)
            cls = result['class']['value']
            mRID = result['mRID']['value']
            name = result['name']['value']
            try:
                objects.append(eval(f"cim.{cls}(mRID='{mRID}', name = '{name}')"))
                print(cls)
            except:
                print('warning: object class missing:', cls)
        return objects
    
    def query_attribute_builder(self, query_message, typed_catalog, cim_class):
        self.connect()
        self.sparql_obj.setQuery(query_message)
        self.sparql_obj.setMethod(POST)
        query_output = self.sparql_obj.query().convert()
#         print(query_output)
#         attribute_list = list(cim_class().__dict__.keys())
        attribute_list = query_output['head']['vars']
        for result in query_output['results']['bindings']:
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
            


    def create_default_instances(self, feeder_mrid: str | cim.Feeder, mrid_list: List[str]) -> List[object]:
        """ Creates an empty CIM object with the correct class type with mRID and name fields populated
        Args:
            feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
            mrid_list (list[str]): A list of object mRID strings to be converted into CIM objects
        Returns:
            objects: A list of CIM object instances
        """
        sparql_message = sparql.create_default_sparql(feeder_mrid, mrid_list)
#         print(sparql_message)
        objects = self.query_object_builder(sparql_message)
        return objects

    def execute(self, query: str) -> QueryResponse:
        raise RuntimeError("Must have implemented query in the inherited class")
        
    def get_all_attributes(self, feeder_mrid, typed_catalog, cim_class):
        mrid_list = list(typed_catalog[cim_class].keys())
        sparql_message = eval(f"sparql.{cim_class.__name__}SPARQL.get_all_attributes('{feeder_mrid}', {mrid_list})")
#       sparql_message = sparql.LinearShuntCompensatorSPARQL.get_all_attributes(feeder_mrid, mrid_list)
#         print(sparql_message)
        self.query_attribute_builder(sparql_message, typed_catalog, cim_class)
        
        
