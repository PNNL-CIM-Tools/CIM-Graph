from __future__ import annotations

import importlib
import json
import logging
import math
import os
from uuid import UUID

from gridappsd import GridAPPSD
from rdflib import Graph, URIRef

import cimgraph.queries.sparql as sparql
from cimgraph.databases import ConnectionInterface, QueryResponse

_log = logging.getLogger(__name__)


class GridappsdConnection(ConnectionInterface):

    def __init__(self, connection_params):
        self.cim_profile = connection_params.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.connection_params = connection_params

        if connection_params.host:
            os.environ['GRIDAPPSD_ADDRESS'] = connection_params.host
        else:
            os.environ['GRIDAPPSD_ADDRESS'] = 'localhost'

        if connection_params.port:
            os.environ['GRIDAPPSD_PORT'] = connection_params.port
        else:
            os.environ['GRIDAPPSD_PORT'] = '61613'

        if connection_params.database:
            self.database = connection_params.database
        else:
            self.database = 'powergridmodel'

        if not connection_params.url:
            self.connection_params.url = 'http://localhost:8889/bigdata/namespace/kb/sparql'

        os.environ['GRIDAPPSD_APPLICATION_ID'] = 'cimantic-graphs'
        os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
        os.environ['GRIDAPPSD_USER'] = 'app_user'
        os.environ['GRIDAPPSD_PASSWORD'] = '1234App'

        self.gapps = None

        try:
            self.rdfs_profile = Graph(store='Oxigraph')
            path = os.path.dirname(self.cim.__file__)
            self.rdfs_profile.parse(f'{path}/{self.cim_profile}.rdfs', format='xml')
            self.reverse = URIRef('http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#inverseRoleName')
        except:
            self.rdfs_profile = None

    def connect(self):
        if not self.gapps:
            self.gapps = GridAPPSD()

    def disconnect(self):
        self.gapps.disconnect()

    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        response = self.gapps.query_data(query_message, database_type=self.database, timeout=30)
        return response['data']

    def create_new_graph(self, container: object) -> dict[type, dict[UUID, object]]:
        graph = {}
        self.add_to_graph(graph=graph, obj=container)
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(container, self.connection_params)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def parse_node_query(self, graph: dict, query_output: dict) -> dict[type, dict[UUID, object]]:

        for result in query_output['results']['bindings']:
            # Parse query results
            node_mrid = result['ConnectivityNode']['value']
            term_mrid = result['Terminal']['value']
            eq = json.loads(result['Equipment']['value'])
            eq_id = eq['@id']
            eq_class = eq['@type']
            # Add each object to graph
            node = self.create_object(graph, self.cim.ConnectivityNode, node_mrid)
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

    def get_edges_query(self, graph: dict[type, dict[UUID, object]],
                        cim_class: type) -> str:

        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(graph, cim_class, eq_mrids,
                                                     self.connection_params)

        return sparql_message

    def get_all_edges(self, graph: dict[type, dict[UUID, object]], cim_class: type) -> None:
        uuid_list = list(graph[cim_class].keys())
        for index in range(math.ceil(len(uuid_list) / 100)):
            eq_mrids = uuid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct queries>sparql python script based on class name
            sparql_message = sparql.get_all_edges_sparql(graph,
                cim_class, eq_mrids, self.connection_params)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    def get_all_attributes(self, graph: dict[type, dict[str, object]],
                           cim_class: type):
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

    def edge_query_parser(self, query_output, graph: dict[type, dict[str,
                                                                     object]],
                          cim_class: type) -> None:
        for result in query_output['results']['bindings']:
            if result['attribute']['value'] != 'type':  #skip 'type' and other single attributes

                uri = result['identifier']['value']  #get mRID
                identifier = UUID(uri.strip('_').lower())
                attr = result['attribute']['value']  #edge attribute
                attribute = result['attribute']['value'].split('.')  #split edge attribute
                value = result['value']['value']  #get edge value



                if 'edge' in result:  #check if association
                    edge = json.loads(result['edge']['value'])
                    edge_mRID = edge['@id']
                    edge_class = edge['@type']
                    if edge_class in self.cim.__all__:
                        edge_class = eval(f'self.cim.{edge_class}')
                    else:
                        _log.warning(f'Class {edge_class} not in data profile')
                        continue

                     # Old method, this will be deprecated in a future release
                    if self.rdfs_profile is not None:
                        self.create_assocation(graph, attribute, cim_class, identifier,
                                           attr, edge_class, edge_mRID)

                    else:
                        self.create_edge(graph, cim_class, identifier, attr, edge_class, edge_mRID)

                elif self.namespace in value:  #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]

                    if enum_class in self.cim.__all__:  # if enumeration
                        edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                        setattr(graph[cim_class][identifier], attribute[1], edge_enum)
                else:
                    setattr(graph[cim_class][identifier], attribute[1], value)



    def upload(self, graph: dict[type, dict[str, object]]) -> None:
        for cim_class in graph.keys():
            for obj in graph[cim_class].values():
                query = sparql.upload_triples_sparql(obj, self.connection_params)
                self.execute(query)
