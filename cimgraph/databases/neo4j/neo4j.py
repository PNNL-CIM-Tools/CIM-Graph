from __future__ import annotations
import math
import importlib
import logging
import re
from typing import Dict, List, Optional

import cimgraph.queries.cypher as cypher
from cimgraph.databases import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cimgraph.models.model_parsers import add_to_graph, add_to_catalog, item_dump

from neo4j import GraphDatabase
from neo4j.exceptions import DriverError, Neo4jError



_log = logging.getLogger(__name__)

class Neo4jConnection(ConnectionInterface):
    def __init__(self, connection_parameters):
        self.cim_profile = connection_parameters.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.connection_parameters = connection_parameters
        self.namespace = connection_parameters.namespace
        self.url = connection_parameters.url
        self.username = connection_parameters.username
        self.password = connection_parameters.password
        self.database = connection_parameters.database
        self.driver = None

    def connect(self):
        if not self.driver:
            self.driver = GraphDatabase.driver(self.url, auth=(self.username, self.password))
            self.driver.verify_connectivity()

    def disconnect(self):
        self.driver.close()
        self.driver = None
        
    def execute(self, query_message: str) -> QueryResponse:
        self.connect()

        # try:
        #     records, summary, keys = self.driver.execute_query(query_message, database_=self.database )
        #     return records, summary, keys
        # # Capture any errors along with the query and data for traceability
        # except (DriverError, Neo4jError) as exception:
        #     _log.error("%s raised an error: \n%s", query_message, exception)

        with self.driver.session() as session:
            result = session.read_transaction(
                lambda tx: tx.run(query_message).data()
            )
        return result
            
    def create_new_graph(self, container:object) -> dict[type, dict[str, object]] :
        graph = {}
        # Generate cypher message from correct loaders>cypher python script based on class name
        cypher_message = cypher.get_all_nodes_cypher(container, self.namespace)
        # Execute cypher query
        query_output = self.execute(cypher_message)
        parsed = {}
        for result in query_output:

            # Parse query results
            # node = result['ConnectivityNode']['IdentifiedObject.mRID']
            # terminal = result['Terminal']['IdentifiedObject.mRID']
            # eq_id = result['Equipment']['IdentifiedObject.mRID']
            node = result['ConnectivityNode']
            terminal = result['Terminal']
            eq_id = result['eq_id']
            eq_class = result['eq_class'][1]
            # Add each object to graph
            try:
                graph[self.cim.ConnectivityNode][node]
            except:
                self.create_object(graph, self.cim.ConnectivityNode, node)
            self.create_object(graph, self.cim.Terminal, terminal)
            if eq_class in self.cim.__all__:
                eq_class = eval(f"self.cim.{eq_class}")
                self.create_object(graph, eq_class, eq_id)
            else:
                _log.warning('object class missing from data profile:' + str(eq_class))
                continue
            # Link objects in graph
            graph[eq_class][eq_id].Terminals.append(graph[self.cim.Terminal][terminal])
            graph[self.cim.ConnectivityNode][node].Terminals.append(graph[self.cim.Terminal][terminal])
            setattr(graph[self.cim.Terminal][terminal], "ConnectivityNode", graph[self.cim.ConnectivityNode][node])
            setattr(graph[self.cim.Terminal][terminal], "ConductingEquipment", graph[eq_class][eq_id])
            
        return graph
    
    
    def get_edges_query(self, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):

        eq_mrids=list(graph[cim_class].keys())[0:100]
        cypher_message = cypher.get_all_edges_cypher(cim_class, eq_mrids, self.namespace)

        return cypher_message
    
    
    def get_all_edges(self, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list)/100)):
            eq_mrids = mrid_list[index*100: (index+1)*100]
            #generate cypher message from correct loaders>cypher python script based on class name
            cypher_message = cypher.get_all_edges_cypher(cim_class, eq_mrids, self.namespace)
            #execute cypher query
            query_output = self.execute(cypher_message)
            self.edge_query_parser(query_output, container, graph, cim_class)

    def edge_query_parser(self, query_output, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):
        parsed = []
        for result in query_output:
            is_association = False
            is_enumeration = False

            mRID = result['mRID'] #get mRID
            if "urn:uuid:" in mRID:
                mRID = mRID.split('urn:uuid:')[1]
            elif "#" in mRID:
                mRID = mRID.split('#')[1]

            if mRID not in parsed:
                parsed.append(mRID)
                attr_list = list(result['eq'].keys())
                for attr in attr_list:
                    if attr != 'uri':
                        try:
                            attribute = attr.split('.')[1]
                            value = result['eq'][attr]
                            setattr(graph[cim_class][mRID], attribute, value)
                        except:
                            _log.warning(f'attribute {attribute} not recognized')


                 

            edge = result['attribute'].split('.') #split edge attribute
            edge_node = result['edge_mrid'] #get edge value
            # edge_node = result['edge_node'] #get edge value
            edge_class = result['edge_class']

            if len(edge_class) == 1: #check if enumeration
                enum = edge_node.split('#')[1]
                enum_class = enum.split('.')[0]
                enum_value = enum.split('.')[1]
                is_enumeration = True

            else:
                edge_class = edge_class[1]

                if edge_class in self.cim.__all__:
                    is_association = True
                    edge_class = eval(f"self.cim.{edge_class}")
                else:
                    _log.warning('unknown class', edge_class)
                    continue



            if is_association: # if association to another CIM object

                # if 'IdentifiedObject.mRID' in edge_node:
                #     edge_mRID = edge_node['IdentifiedObject.mRID']
                # if "urn:uuid" in edge_node['uri']:
                #     edge_mRID = edge_node['uri'].split('urn:uuid:')[1]
                # elif "#" in edge_node['uri']:
                #     edge_mRID = edge_node['uri'].split('#')[1]
                if "urn:uuid" in edge_node:
                    edge_mRID = edge_node.split('urn:uuid:')[1]
                elif "#" in edge_node:
                    edge_mRID = edge_node.split('#')[1]
                else:
                    edge_mRID = edge_node


                if edge[0] in cim_class.__dataclass_fields__: #check if first name is the attribute
                    self.create_edge(graph, cim_class, mRID, edge[0], edge_class, edge_mRID)
                    
                elif edge[1] in cim_class.__dataclass_fields__: #check if second name is the attribute
                    self.create_edge(graph, cim_class, mRID, edge[1], edge_class, edge_mRID)

                elif edge[0]+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                    self.create_edge(graph, cim_class, mRID, edge[0]+'s', edge_class, edge_mRID)
                
                elif edge[1]+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                    self.create_edge(graph, cim_class, mRID, edge[1]+'s', edge_class, edge_mRID)
                    
                else: #fallback: match class type until a suitable parent edge class is found
                    for node_attr in list(cim_class.__dataclass_fields__.keys()):
                        attr_str = cim_class.__dataclass_fields__[node_attr].type
                        edge_parent = attr_str.split('[')[1].split(']')[0]
                        if edge_parent in self.cim.__all__:
                            parent_class = eval(f"self.cim.{edge_parent}")
                            if issubclass(edge_class, parent_class):
                                self.create_edge(graph, cim_class, mRID, node_attr, edge_class, edge_mRID)
                                break

            elif is_enumeration:
                if enum_class in self.cim.__all__: # if enumeration
                    edge_enum = eval(f"self.cim.{enum_class}(enum_value)")
                    setattr(graph[cim_class][mRID], edge[1], edge_enum)




    def create_object(self, graph, class_type, mRID):
        
        if class_type not in graph.keys():
            graph[class_type] = {}

        if mRID in graph[class_type].keys():
            obj = graph[class_type][mRID]
        else:
                obj = class_type()
                setattr(obj, "mRID", mRID)
                add_to_graph(obj, graph)

        return obj
    
    
    def create_edge(self, graph, cim_class, mRID, attribute, edge_class, edge_mRID):
        edge_object = self.create_object(graph, edge_class, edge_mRID)
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if "List" in attribute_type:
            obj_list = getattr(graph[cim_class][mRID], attribute)
            obj_list.append(edge_object)
            setattr(graph[cim_class][mRID], attribute, obj_list)
        else:
            setattr(graph[cim_class][mRID], attribute, edge_object)
            
