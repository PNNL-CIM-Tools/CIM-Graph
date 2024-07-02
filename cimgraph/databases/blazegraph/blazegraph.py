from __future__ import annotations

import importlib
import json
import logging
import math
import os

from rdflib import Graph, Namespace, URIRef
from SPARQLWrapper import JSON, POST, SPARQLWrapper

import cimgraph.queries.sparql as sparql
from cimgraph.databases import ConnectionInterface, QueryResponse

_log = logging.getLogger(__name__)


class BlazegraphConnection(ConnectionInterface):

    def __init__(self, connection_params: ConnectionInterface) -> None:
        self.cim_profile = connection_params.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' +
                                           self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.url = connection_params.url
        self.connection_params = connection_params
        self.sparql_obj = None

        try:
            # If old data profile using XSD-data, use oxigraph
            # This will be deprecated in a future release
            self.rdfs_profile = Graph(store='Oxigraph')
            path = os.path.dirname(self.cim.__file__)
            self.rdfs_profile.parse(f'{path}/{self.cim_profile}.rdfs', format='xml')
            self.reverse = URIRef('http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#inverseRoleName')
        except:
            # Else new profiles built from CIM-Tool XSLT Builder
            self.rdfs_profile = None

    def connect(self) -> None:
        if not self.sparql_obj:
            self.sparql_obj = SPARQLWrapper(self.url)
            self.sparql_obj.setReturnFormat(JSON)

    def disconnect(self) -> None:
        self.sparql_obj = None

    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        self.sparql_obj.setQuery(query_message)
        self.sparql_obj.setMethod(POST)
        query_output = self.sparql_obj.query().convert()
        return query_output

    def create_new_graph(self,
                         container: object) -> dict[type, dict[str, object]]:
        graph = {}
        self.add_to_graph(graph=graph, obj=container)
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(
            container, self.namespace)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def parse_node_query(self, graph: dict,
                         query_output: dict) -> dict[type, dict[str, object]]:

        for result in query_output['results']['bindings']:
            # Parse query results
            node_mrid = result['ConnectivityNode']['value']
            term_mrid = result['Terminal']['value']
            eq = json.loads(result['Equipment']['value'])
            eq_id = eq['@id']
            eq_class = eq['@type']
            # Add each object to graph
            node = self.create_object(graph, self.cim.ConnectivityNode,
                                      node_mrid)
            terminal = self.create_object(graph, self.cim.Terminal, term_mrid)
            if eq_class in self.cim.__all__:
                eq_class = eval(f'self.cim.{eq_class}')
                equipment = self.create_object(graph, eq_class, eq_id)

            else:
                _log.warning(f'object class missing from data profile: {eq_class}')
                continue
            # Link objects in graph
            if terminal not in equipment.Terminals:
                equipment.Terminals.append(terminal)
            if terminal not in node.Terminals:
                node.Terminals.append(terminal)
            setattr(terminal, 'ConnectivityNode', node)
            setattr(terminal, 'ConductingEquipment', equipment)

        return graph

    def build_graph_from_list(
            self, graph,
            mrid_list: list[str]) -> dict[type, dict[str, object]]:
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_nodes_from_list(
                eq_mrids, self.namespace)
            # print(sparql_message)
            query_output = self.execute(sparql_message)
            graph = self.parse_node_query(graph, query_output)
        return graph

    def get_edges_query(self, graph: dict[type, dict[str, object]],
                        cim_class: type) -> str:

        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids,
                                                     self.connection_params)

        return sparql_message

    def get_all_edges(self, graph: dict[type, dict[str, object]],
                      cim_class: type) -> None:
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_edges_sparql(
                cim_class, eq_mrids, self.connection_params)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    def get_all_attributes(self, graph: dict[type, dict[str, object]],
                           cim_class: type) -> None:
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_attributes_sparql(
                cim_class, eq_mrids, self.connection_params)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: dict[type, dict[str, object]],
                          cim_class: type) -> None:
        for result in query_output['results']['bindings']:
            is_association = False
            is_enumeration = False
            if result['attribute']['value'] != 'type':  #skip 'type' and other single attributes

                mRID = result['mRID']['value']  #get mRID
                attr = result['attribute']['value']  #edge attribute
                attribute = result['attribute']['value'].split('.')  #split edge attribute
                value = result['value']['value']  #get edge value

                if self.namespace in value:  #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    is_enumeration = True

                if 'edge' in result:  #check if association
                    is_association = True
                    edge = json.loads(result['edge']['value'])
                    edge_mRID = edge['@id']
                    edge_class = edge['@type']
                    if edge_class in self.cim.__all__:
                        edge_class = eval(f'self.cim.{edge_class}')
                    else:
                        _log.warning(f'unknown class {edge_class}')
                        continue

                if is_association:  # if association to another CIM object
                    self.create_assocation(graph, attribute, cim_class, mRID,
                                           attr, edge_class, edge_mRID)
   

                elif is_enumeration:
                    if enum_class in self.cim.__all__:  # if enumeration
                        edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                        setattr(graph[cim_class][mRID], attribute[1],
                                edge_enum)
                else:
                    setattr(graph[cim_class][mRID], attribute[1], value)

    def upload(self, graph: dict[type, dict[str, object]]) -> None:
        for cim_class in graph.keys():
            for obj in graph[cim_class].values():
                query = sparql.upload_triples_sparql(obj,
                                                     self.connection_params)
                self.execute(query)

