from __future__ import annotations

import importlib
import json
import logging
import math
import os
from uuid import UUID

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF

import cimgraph.queries.sparql as sparql
from cimgraph.databases import (ConnectionInterface, ConnectionParameters,
                                QueryResponse)

_log = logging.getLogger(__name__)


class RDFlibConnection(ConnectionInterface):

    def __init__(self,
                 connection_params: ConnectionParameters,
                 use_oxigraph: bool = True):
        self.cim_profile = connection_params.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.filename = connection_params.filename
        self.connection_params = connection_params
        self.libgraph = None
        self.use_oxigraph = use_oxigraph

    def connect(self):
        if not self.libgraph:
            if self.use_oxigraph:
                self.libgraph = Graph(store='Oxigraph')
            else:
                self.libgraph = Graph()

            if self.filename is not None:
                try:
                    self.libgraph.parse(self.filename)
                    self.libgraph.bind('cim', Namespace(self.namespace))
                    self.libgraph.bind('rdf', RDF)
                except:
                    _log.warning(f'File {self.filename} not found. Defaulting to empty network graph')
                    self.filename = None

    def disconnect(self):
        self.libgraph = None

    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        query_output = self.libgraph.query(query_message)
        return query_output

    def get_object(self, mrid:str, graph = {}) -> object:
        sparql_message = sparql.get_object_sparql(mrid, self.connection_params)
        query_output = self.execute(sparql_message)
        obj = None
        for result in query_output:
            uri = result['identifier']['value']
            obj_class = result['obj_class']['value']
            class_type = eval(f'self.cim.{obj_class}')
            obj = self.create_object(graph, class_type, uri)
        return obj

    def create_new_graph(self, container: object) -> dict[type, dict[UUID, object]]:
        graph = {}
        self.add_to_graph(graph=graph, obj=container)
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(container, self.connection_params)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def parse_node_query(self, graph: dict, query_output: dict) -> dict[type, dict[UUID, object]]:

        for result in query_output:
            # Parse query results
            node_mrid = str(result.ConnectivityNode)
            term_mrid = str(result.Terminal)
            eq = json.loads(result.Equipment)
            eq_id = eq['@id']
            eq_class = eq['@type']

            if eq_class in self.cim.__all__:
                eq_class = eval(f'self.cim.{eq_class}')
                equipment = self.create_object(graph, eq_class, eq_id)

            else:
                _log.warning(f'object class missing from data profile: {eq_class}')
                continue

            if node_mrid != 'None':
                # Add each object to graph
                node = self.create_object(graph, self.cim.ConnectivityNode, node_mrid)
                terminal = self.create_object(graph, self.cim.Terminal, term_mrid)
                # Associate the node and equipment with the terminal
                if terminal not in equipment.Terminals:
                    equipment.Terminals.append(terminal)
                if terminal not in node.Terminals:
                    node.Terminals.append(terminal)
                # Associate the terminal with the equipment and node
                setattr(terminal, 'ConnectivityNode', node)
                setattr(terminal, 'ConductingEquipment', equipment)

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

    def get_all_attributes(self, graph: dict[type, dict[UUID, object]],
                           cim_class: type) -> None:
        mrid_list = list(graph[cim_class].keys())

        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_attributes_sparql(graph,
                cim_class, eq_mrids, self.connection_params)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class, expand_graph = False)

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: dict[type, dict[UUID, object]],
                          cim_class: type, expand_graph = True) -> None:
        for result in query_output:
            if 'type' not in result.attribute and result.attribute is not None:  #skip 'type' and other single attributes

                is_association = False
                is_enumeration = False
                if result.mRID is not None:  #get mRID
                    mRID = str(result.mRID)
                else:
                    iri = str(result.eq)
                    if self.iec61970_301 > 7:
                        mRID = iri.split('uuid:')[1]
                    else:
                        mRID = iri.split('rdf:id:')[1]
                identifier = UUID(mRID.strip('_').lower())
                attr_uri = result.attr
                attr = str(result.attr).split(self.namespace)[1]
                attribute = attr.split('.')  #split edge attribute
                value = str(result.val)  #get edge value

                if self.namespace in value:  #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    is_enumeration = True

                if result.edge_class is not None:  #check if association
                    is_association = True
                    # edge = json.loads(result.edge)
                    # edge_mRID = edge['@id']
                    # edge_class = edge['@type']
                    edge_class = str(result.edge_class)
                    if result.edge_mRID is not None:
                        edge_mRID = str(result.edge_mRID)
                    else:
                        if self.iec61970_301 > 7:
                            edge_mRID = value.split('uuid:')[1]
                        else:
                            edge_mRID = value.split('#')[1]
                    if edge_class in self.cim.__all__:
                        edge_class = eval(f'self.cim.{edge_class}')
                    else:
                        _log.warning(f'unknown class {edge_class}')
                        continue

                    if expand_graph:
                        self.create_edge(graph, cim_class, identifier, attribute, edge_class, edge_mRID)
                    else:
                        self.create_value(graph, cim_class, identifier, attribute, value)


                elif is_enumeration:
                    edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                    association = self.check_attribute(cim_class, attribute)
                    if association is not None:
                        setattr(graph[cim_class][identifier], association, edge_enum)
                else:
                    association = self.check_attribute(cim_class, attribute)
                    if association is not None:
                        self.create_value(graph, cim_class, identifier, attribute, value)


    #     return obj

    def upload(self, graph):
        pass


    def get_from_triple(self, subject, predicate, graph = ...):
        pass

    def create_distributed_graph(self, area, graph = ...):
        pass
