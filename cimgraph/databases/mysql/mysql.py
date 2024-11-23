from __future__ import annotations

import importlib
import json
import logging
import math
import re
import time

import mysql.connector
from SPARQLWrapper import JSON, POST, SPARQLWrapper

import cimgraph.queries.sparql as sparql
from cimgraph.databases import (ConnectionInterface, ConnectionParameters,
                                QueryResponse)
from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


class MySQLJSONConnection(ConnectionInterface):

    def __init__(self, connection_parameters):
        self.connection_parameters = connection_parameters
        self.cim_profile = connection_parameters.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_parameters.namespace
        self.host = connection_parameters.host
        self.port = connection_parameters.port
        self.username = connection_parameters.username
        self.password = connection_parameters.password
        self.database = connection_parameters.database
        self.connection = None
        self.cursor = None

    def connect(self):
        if not self.cursor:
            if not self.database:    # Set database name to CIM Profile name if not specified
                self.database = self.cim_profile
            try:
                self.connection = mysql.connector.connect(host=self.host,
                                                          user=self.username,
                                                          password=self.password,
                                                          database=self.database)
                self.cursor = self.connection.cursor(buffered=True)
            except:
                _log.error('Could not connect to database')

    def disconnect(self):
        self.cursor = None

    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        self.cursor.execute(query_message)
        response = self.cursor.fetchall()
        return response

    def create_new_graph(self, container: object) -> dict[type, dict[str, object]]:
        graph = {}
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(container, self.namespace)
        query_output = self.execute(sparql_message)

        for result in query_output['results']['bindings']:
            # Parse query results
            node = result['ConnectivityNode']['value']
            terminal = result['Terminal']['value']
            eq = json.loads(result['Equipment']['value'])
            eq_id = eq['@id']
            eq_class = eq['@type']
            # Add each object to graph
            self.create_object(graph, self.cim.ConnectivityNode, node)
            self.create_object(graph, self.cim.Terminal, terminal)
            if eq_class in self.cim.__all__:
                eq_class = eval(f'self.cim.{eq_class}')
                obj = self.create_object(graph, eq_class, eq_id)

            else:
                _log.warning('object class missing from data profile:' + str(eq_class))
                continue
            # Link objects in graph
            graph[eq_class][eq_id].Terminals.append(graph[self.cim.Terminal][terminal])
            graph[self.cim.ConnectivityNode][node].Terminals.append(
                graph[self.cim.Terminal][terminal])
            setattr(graph[self.cim.Terminal][terminal], 'ConnectivityNode',
                    graph[self.cim.ConnectivityNode][node])
            setattr(graph[self.cim.Terminal][terminal], 'ConductingEquipment',
                    graph[eq_class][eq_id])

        return graph

    def get_edges_query(self, container: str | cim.ConnectivityNodeContainer,
                        graph: dict[type, dict[str, object]], cim_class: type):

        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids, self.namespace,
                                                     self.iec61970_301)

        return sparql_message

    def get_all_edges(self, container: str | cim.ConnectivityNodeContainer,
                      graph: dict[type, dict[str, object]], cim_class: type):
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids, self.namespace,
                                                         self.iec61970_301)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, container, graph, cim_class)

    def edge_query_parser(self, query_output, container: str | cim.ConnectivityNodeContainer,
                          graph: dict[type, dict[str, object]], cim_class: type):
        for result in query_output['results']['bindings']:
            if result['attribute']['value'] != 'type':    #skip 'type' and other single attributes

                is_association = False
                is_enumeration = False
                mRID = result['mRID']['value']    #get mRID
                attribute = result['attribute']['value'].split('.')    #split edge attribute
                value = result['value']['value']    #get edge value

                if self.namespace in value:    #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    is_enumeration = True

                if 'edge' in result:    #check if association
                    is_association = True
                    edge = json.loads(result['edge']['value'])
                    edge_mRID = edge['@id']
                    edge_class = edge['@type']
                    if edge_class in self.cim.__all__:
                        edge_class = eval(f'self.cim.{edge_class}')
                    else:
                        print('unknown class', edge_class)
                        continue

                if is_association:    # if association to another CIM object

                    if attribute[
                            0] in cim_class.__dataclass_fields__:    #check if first name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[0], edge_class,
                                         edge_mRID)

                    elif attribute[
                            1] in cim_class.__dataclass_fields__:    #check if second name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[1], edge_class,
                                         edge_mRID)

                    elif attribute[
                            0] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[0] + 's', edge_class,
                                         edge_mRID)

                    elif attribute[
                            1] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[1] + 's', edge_class,
                                         edge_mRID)

                    else:    #fallback: match class type until a suitable parent edge class is found
                        for node_attr in list(cim_class.__dataclass_fields__.keys()):
                            attr_str = cim_class.__dataclass_fields__[node_attr].type
                            edge_parent = attr_str.split('[')[1].split(']')[0]
                            if edge_parent in self.cim.__all__:
                                parent_class = eval(f'self.cim.{edge_parent}')
                                if issubclass(edge_class, parent_class):
                                    self.create_edge(graph, cim_class, mRID, node_attr, edge_class,
                                                     edge_mRID)
                                    break

                elif is_enumeration:
                    if enum_class in self.cim.__all__:    # if enumeration
                        edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                        setattr(graph[cim_class][mRID], attribute[1], edge_enum)
                else:
                    setattr(graph[cim_class][mRID], attribute[1], value)

    def create_edge(self, graph, cim_class, mRID, attribute, edge_class, edge_mRID):
        edge_object = self.create_object(graph, edge_class, edge_mRID)
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if 'List' in attribute_type:
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
            setattr(obj, 'mRID', mRID)
            graph[class_type][mRID] = obj

        return obj
