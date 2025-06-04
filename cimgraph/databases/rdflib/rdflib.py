from __future__ import annotations

import json
import logging
import math
from collections import defaultdict
from uuid import UUID

from rdflib import Graph, Namespace
from rdflib.namespace import RDF

import cimgraph.queries.rdflib as rdflib_sparql
import cimgraph.queries.sparql as sparql
from cimgraph.databases import (ConnectionInterface, QueryResponse, get_cim_profile,
                                get_iec61970_301, get_namespace)

_log = logging.getLogger(__name__)


class RDFlibConnection(ConnectionInterface):

    def __init__(self, filename:str=None, use_oxigraph:bool=True):
        self.cim_profile, self.cim = get_cim_profile()
        self.namespace = get_namespace()
        self.iec61970_301 = get_iec61970_301()
        self.filename = filename
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

    def get_object(self, mRID:str, graph = None) -> object:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        sparql_message = sparql.get_object_sparql(mRID)
        query_output = self.execute(sparql_message)
        obj = None
        for result in query_output:
            uri = result.identifier.value
            obj_class = result.obj_class.value
            class_type = getattr(self.cim, obj_class)
            obj = self.create_object(graph, class_type, uri)
        return obj

    def create_new_graph(self, container: object) -> dict[type, dict[UUID, object]]:
        graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=container)
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(container)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def parse_node_query(self, graph: dict, query_output: dict) -> dict[type, dict[UUID, object]]:

        for result in query_output:
            # Parse query results

            eq = json.loads(result.Equipment.value)
            eq_id = eq['@id']
            eq_class = eq['@type']

            # If equipment class is in data profile, add it to the graph also
            if eq_class in self.cim.__all__:
                eq_class = getattr(self.cim, eq_class)
                equipment = self.create_object(graph, eq_class, eq_id)
            else:
                # If it is not in the profile, log it as a missing class
                _log.warning(
                    f'object class missing from data profile: {eq_class}')
                continue
            try:
                # Get uri strings of nodes and terminals
                node_mrid = str(result.ConnectivityNode.value)
                term_mrid = str(result.Terminal.value)
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
            except:
                pass
        return graph


    def get_edges_query(self, graph: dict[type, dict[UUID, object]],
                        cim_class: type) -> str:

        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = rdflib_sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)

        return sparql_message

    def get_all_edges(self, graph: dict[type, dict[UUID, object]], cim_class: type) -> None:
        uuid_list = list(graph[cim_class].keys())
        for index in range(math.ceil(len(uuid_list) / 100)):
            eq_mrids = uuid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct queries>sparql python script based on class name
            sparql_message = rdflib_sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    def get_all_attributes(self, graph: dict[type, dict[UUID, object]], cim_class: type) -> None:
        mrid_list = list(graph[cim_class].keys())

        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = rdflib_sparql.get_all_attributes_sparql(graph, cim_class, eq_mrids)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class, expand_graph = False)

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: dict[type, dict[UUID, object]],
                          cim_class: type, expand_graph = True) -> None:

        for result in query_output:
            if result.attr is not None:  #skip 'type' and other single attributes
                if 'type' not in str(result.attr):

                    is_enumeration = False

                    identifier = UUID(result.identifier.value.strip('_').lower())
                    attribute = str(result.attr).split(self.namespace)[1]
                    # attribute = attr.split('.')[1]  #split edge attribute
                    value = str(result.val)  #get edge value

                    if self.namespace in value:  #check if enumeration
                        enum_text = value.split(self.namespace)[1]
                        enum_text = enum_text.split('>')[0]
                        enum_class = enum_text.split('.')[0]
                        enum_value = enum_text.split('.')[1]
                        is_enumeration = True

                    if result.edge_class is not None:  #check if association


                        edge_class = str(result.edge_class)


                        if self.iec61970_301 > 7:
                            edge_mRID = value.split('uuid:')[1]
                        else:
                            edge_mRID = value.split('#')[1]
                        if edge_class in self.cim.__all__:
                            edge_class = getattr(self.cim, edge_class)
                        else:
                            _log.warning(f'unknown class {edge_class}')
                            continue

                        if expand_graph:
                            self.create_edge(graph, cim_class, identifier, attribute, edge_class, edge_mRID)
                        else:
                            self.create_value(graph, cim_class, identifier, attribute, value)


                    elif is_enumeration:
                        edge_enum = getattr(self.cim, enum_class)(enum_value)
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
