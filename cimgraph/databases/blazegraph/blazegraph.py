from __future__ import annotations
import math
import importlib
import logging
import re
import json
import enum

from typing import Dict, List, Optional

import cimgraph.queries.sparql as sparql
from cimgraph.databases import ConnectionInterface, QueryResponse

from SPARQLWrapper import JSON, POST, SPARQLWrapper

_log = logging.getLogger(__name__)

class BlazegraphConnection(ConnectionInterface):
    def __init__(self, connection_params):
        self.cim_profile = connection_params.cim_profile
        # self.legacy_sparql = importlib.import_module('cimgraph.queries.sparql.' + self.cim_profile)
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.url = connection_params.url
        self.connection_params = connection_params
        self.sparql_obj: Optional[SPARQLWrapper] = None


    def connect(self):
        if not self.sparql_obj:
            self.sparql_obj = SPARQLWrapper(self.url)
            self.sparql_obj.setReturnFormat(JSON)
            

    def disconnect(self):
        self.sparql_obj = None

        
    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        self.sparql_obj.setQuery(query_message)
        self.sparql_obj.setMethod(POST)
        query_output = self.sparql_obj.query().convert()
        return query_output

            
    def create_new_graph(self, container:object) -> dict[type, dict[str, object]] :
        graph = {}
        # Get all nodes, terminal, and equipment by 
        sparql_message = sparql.get_all_nodes_sparql(container, self.namespace)
        query_output = self.execute(sparql_message)

        for result in query_output['results']['bindings']:
            # Parse query results
            node_mrid = result['ConnectivityNode']['value']
            term_mrid = result['Terminal']['value']
            eq = json.loads(result['Equipment']['value'])
            eq_id = eq["@id"]
            eq_class = eq["@type"]
            # Add each object to graph
            node = self.create_object(graph, self.cim.ConnectivityNode, node_mrid)
            terminal = self.create_object(graph, self.cim.Terminal, term_mrid)
            if eq_class in self.cim.__all__:
                eq_class = eval(f"self.cim.{eq_class}")
                equipment = self.create_object(graph, eq_class, eq_id)
                
            else:
                _log.warning('object class missing from data profile:' + str(eq_class))
                continue
            # Link objects in graph
            if terminal not in equipment.Terminals:
                equipment.Terminals.append(terminal)
            if terminal not in node.Terminals:
                node.Terminals.append(terminal)
            setattr(terminal, "ConnectivityNode", node)
            setattr(terminal, "ConductingEquipment", equipment)
            
        return graph
    
    
    def get_edges_query(self, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):

        eq_mrids=list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids, self.connection_params)

        return sparql_message
    
    
    def get_all_edges(self, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list)/100)):
            eq_mrids = mrid_list[index*100: (index+1)*100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids, self.connection_params)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, container, graph, cim_class)


    def edge_query_parser(self, query_output, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):
        for result in query_output['results']['bindings']:
            is_association = False
            is_enumeration = False
            if result['attribute']['value'] != "type": #skip 'type' and other single attributes
                    
               
                mRID = result['mRID']['value'] #get mRID
                attribute = result['attribute']['value'].split('.') #split edge attribute
                value = result['value']['value'] #get edge value
                

                if self.namespace in value: #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split(">")[0]
                    enum_class = enum_text.split(".")[0]
                    enum_value = enum_text.split(".")[1]
                    is_enumeration = True

                if 'edge' in result: #check if association
                    is_association = True
                    edge = json.loads(result['edge']['value'])
                    edge_mRID = edge['@id']
                    edge_class = edge['@type']
                    if edge_class in self.cim.__all__:
                        edge_class = eval(f"self.cim.{edge_class}")
                    else:
                        _log.warning('unknown class', edge_class)
                        continue

                if is_association: # if association to another CIM object

                    if attribute[0] in cim_class.__dataclass_fields__: #check if first name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[0], edge_class, edge_mRID)
                        
                    elif attribute[1] in cim_class.__dataclass_fields__: #check if second name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[1], edge_class, edge_mRID)

                    elif attribute[0]+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[0]+'s', edge_class, edge_mRID)
                    
                    elif attribute[1]+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[1]+'s', edge_class, edge_mRID)
                    
                    elif edge_class.__name__ in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, edge_class.__name__, edge_class, edge_mRID)

                    elif edge_class.__name__+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, edge_class.__name__+'s', edge_class, edge_mRID)
                        
                    else: #fallback: match class type until a suitable parent edge class is found
                        for node_attr in list(cim_class.__dataclass_fields__.keys()):
                            attr_str = cim_class.__dataclass_fields__[node_attr].type
                            # print(attr_str, attribute)

                            edge_parent = attr_str.split('[')[1].split(']')[0]
                            # print(edge_parent)
                            if edge_parent in self.cim.__all__:
                                parent_class = eval(f"self.cim.{edge_parent}")
                                # print(edge_class.__name__, parent_class.__name__)
                                if issubclass(edge_class, parent_class):
                                    # print('sucess')
                                    self.create_edge(graph, cim_class, mRID, node_attr, edge_class, edge_mRID)
                                    break
                            # if 

                elif is_enumeration:
                    if enum_class in self.cim.__all__: # if enumeration
                        edge_enum = eval(f"self.cim.{enum_class}(enum_value)")
                        setattr(graph[cim_class][mRID], attribute[1], edge_enum)
                else:
                    setattr(graph[cim_class][mRID], attribute[1], value)


    def create_edge(self, graph, cim_class, mRID, attribute, edge_class, edge_mRID):
        edge_object = self.create_object(graph, edge_class, edge_mRID)
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if "List" in attribute_type:
            obj_list = getattr(graph[cim_class][mRID], attribute)
            if edge_object not in obj_list:
                obj_list.append(edge_object)
                setattr(graph[cim_class][mRID], attribute, obj_list)
        else:
            setattr(graph[cim_class][mRID], attribute, edge_object)


    def create_object(self, graph, class_type, mRID):
        
        if class_type not in graph.keys():
            graph[class_type] = {}

        if mRID in graph[class_type].keys():
            obj = graph[class_type][mRID]
        else:
            obj = class_type()
            setattr(obj, "mRID", mRID)
            graph[class_type][mRID] = obj

        return obj


    def upload(self, graph):
        for cim_class in graph.keys():
            for obj in graph[cim_class].values():
                query = sparql.upload_triples_sparql(obj, self.connection_params)
                self.execute(query)