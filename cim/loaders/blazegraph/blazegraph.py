from __future__ import annotations
from typing import Dict, List, Optional
from SPARQLWrapper import SPARQLWrapper, JSON, POST
import re
from cim.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cim.loaders.blazegraph.query_parsers import query_parser, query_list_parser, build_cim_object
import cim.loaders.sparql as sparql
import cim.data_profile as cim



class BlazegraphConnection(ConnectionInterface):
    sparql_obj: Optional[SPARQLWrapper] = None

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
        sparql_message = sparql.create_default_sparql(feeder_mrid, mrid_list)
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
                object_list.append(eval(f"cim.{cls}(mRID='{mRID}', name = '{name}')"))
                print(cls)
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
        mrid_list = list(typed_catalog[cim_class].keys()) #get all object mRIDs in switch area
        #generate SPARQL message from correct loaders>sparql python script based on class name
        sparql_message = eval(f"sparql.{cim_class.__name__}SPARQL.get_all_attributes('{feeder_mrid}', {mrid_list})") 
        #execute sparql query
        query_output = self.execute(sparql_message)
#         print(query_output)

#         attribute_list = query_output['head']['vars'] #list of attributes received in query response
        for result in query_output['results']['bindings']: #iterate through rows of response
            attribute_list = result.keys()
            mRID = result['mRID']['value']
            name = result['name']['value']
            for attribute in attribute_list: 
                try: #check if attribute is in data profile
                    attribute_type = cim_class.__dataclass_fields__[attribute].type
                except:
                    #replace with warning message
                    print('warning: attribute ', attribute, ' missing from ', cim_class)
                    
                if 'List' in attribute_type: #check if attribute is association to a list of class objects
                    if '\'' in attribute_type: #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'List\[\'(.*)\']',attribute_type)
                        attribute_class = at_cls.group(1)
                    else:        
                        at_cls = re.match(r'List\[(.*)]',attribute_type)
                        attribute_class = at_cls.group(1)
#                     print(attribute_class)
                    # pass query response of associated objects to list parser
                    query_list_parser(typed_catalog, cim_class, mRID, result, attribute, attribute_class, ';')

                else: #otherwise assign query response
#                     print(attribute)
#                     print(result)
                    query_parser(typed_catalog, cim_class, mRID, result, attribute, ';')
                    

  