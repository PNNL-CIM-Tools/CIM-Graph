from __future__ import annotations

import importlib
import json
import logging
import math
import os
import re

from rdflib import Graph, Namespace, URIRef
from SPARQLWrapper import JSON, POST, SPARQLWrapper

import cimgraph.queries.ontotext as ontotext
import cimgraph.queries.sparql as sparql
from cimgraph.databases import (ConnectionInterface, ConnectionParameters,
                                QueryResponse)

_log = logging.getLogger(__name__)


class GraphDBConnection(ConnectionInterface):

    def __init__(self, connection_params: ConnectionParameters) -> None:
        self.cim_profile = connection_params.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.sparql_obj = None
        self.connection_parameters = connection_params

        try:
            self.data_profile = Graph(store='Oxigraph')
            path = os.path.dirname(self.cim.__file__)
            self.data_profile.parse(f'{path}/{self.cim_profile}.rdfs', format='xml')
            self.reverse = URIRef(
                'http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#inverseRoleName')
        except:
            _log.warning('No RDFS schema found, reverting to default logic')
            self.data_profile = None

    def connect(self) -> None:
        if not self.sparql_obj:
            self.sparql_obj = SPARQLWrapper(self.connection_parameters.url)
            self.sparql_obj.setReturnFormat(JSON)

    def disconnect(self) -> None:
        self.sparql_obj = None

    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        self.sparql_obj.setQuery(query_message)
        self.sparql_obj.setMethod(POST)
        query_output = self.sparql_obj.query().convert()
        return query_output

    def create_new_graph(self, container: object) -> dict[type, dict[str, object]]:
        graph = {}
        # Get all nodes, terminal, and equipment by
        sparql_message = ontotext.get_all_nodes_ontotext(container, self.namespace)

        query_output = self.execute(sparql_message)

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
                _log.warning(f'object class missing from data profile:{eq_class}')
                continue
            # Link objects in graph
            if terminal not in equipment.Terminals:
                equipment.Terminals.append(terminal)
            if terminal not in node.Terminals:
                node.Terminals.append(terminal)
            setattr(terminal, 'ConnectivityNode', node)
            setattr(terminal, 'ConductingEquipment', equipment)

        return graph

    def get_edges_query(self, graph: dict[type, dict[str, object]], cim_class: type):

        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = ontotext.get_all_edges_ontotext(cim_class, eq_mrids, self.namespace,
                                                         self.iec61970_301)

        return sparql_message

    def get_all_edges(self, graph: dict[type, dict[str, object]], cim_class: type) -> None:
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = ontotext.get_all_edges_ontotext(cim_class, eq_mrids, self.namespace,
                                                             self.iec61970_301)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    def edge_query_parser(self, query_output: QueryResponse, graph: dict[type, dict[str, object]],
                          cim_class: type) -> None:
        for result in query_output['results']['bindings']:
            if result['attribute']['value'] != 'type':    #skip 'type' and other single attributes

                is_association = False
                is_enumeration = False
                mRID = result['mRID']['value']    #get mRID
                attr = result['attribute']['value']    #edge attribute
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
                        _log.warning(f'unknown class {edge_class}')
                        continue

                if is_association:    # if association to another CIM object

                    if attribute[
                            1] in cim_class.__dataclass_fields__:    #check if forward attribute
                        self.create_edge(graph, cim_class, mRID, attribute[1], edge_class,
                                         edge_mRID)

                    elif self.data_profile is not None:    # use data profile to look up reverse attribute
                        attr_uri = URIRef(f'{self.namespace}{attr}')
                        reverse_uri = self.data_profile.value(object=attr_uri,
                                                              predicate=self.reverse)
                        try:
                            reverse_attribute = reverse_uri.split('#')[1].split('.')[
                                1]    # split string
                            self.create_edge(graph, cim_class, mRID, reverse_attribute, edge_class,
                                             edge_mRID)
                        except:
                            _log.warning(f'{cim_class.__name__} does not have attribute {attr}')

                    else:    # fallback to use basic logic to identify
                        if attribute[
                                0] in cim_class.__dataclass_fields__:    #check if first name is the attribute
                            self.create_edge(graph, cim_class, mRID, attribute[0], edge_class,
                                             edge_mRID)

                        elif attribute[
                                0] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                            self.create_edge(graph, cim_class, mRID, attribute[0] + 's',
                                             edge_class, edge_mRID)

                        elif attribute[
                                1] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                            self.create_edge(graph, cim_class, mRID, attribute[1] + 's',
                                             edge_class, edge_mRID)

                        elif edge_class.__name__ in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                            self.create_edge(graph, cim_class, mRID, edge_class.__name__,
                                             edge_class, edge_mRID)

                        elif edge_class.__name__ + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                            self.create_edge(graph, cim_class, mRID, edge_class.__name__ + 's',
                                             edge_class, edge_mRID)

                        else:    #fallback: match class type until a suitable parent edge class is found
                            parsed = False
                            for node_attr in list(cim_class.__dataclass_fields__.keys()):
                                attr_str = cim_class.__dataclass_fields__[node_attr].type
                                edge_parent = attr_str.split('[')[1].split(']')[0]
                                if edge_parent in self.cim.__all__:
                                    parent_class = eval(f'self.cim.{edge_parent}')
                                    if issubclass(edge_class, parent_class):
                                        self.create_edge(graph, cim_class, mRID, node_attr,
                                                         edge_class, edge_mRID)
                                        parsed = True
                                        break
                            if not parsed:
                                _log.warning(f'unable to find match for {attr} for {mRID}')

                elif is_enumeration:
                    if enum_class in self.cim.__all__:    # if enumeration
                        edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                        setattr(graph[cim_class][mRID], attribute[1], edge_enum)
                else:
                    setattr(graph[cim_class][mRID], attribute[1], value)

    def create_edge(self, graph: dict[type, dict[str, object]], cim_class: type, mRID: str,
                    attribute: str, edge_class: type, edge_mRID: str) -> None:
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if 'List' in attribute_type:
            obj_list = getattr(graph[cim_class][mRID], attribute)
            found = False
            for obj in obj_list:
                if obj.mRID == edge_mRID:
                    found = True
            if not found:
                edge_object = self.create_object(graph, edge_class, edge_mRID)
                obj_list.append(edge_object)
                setattr(graph[cim_class][mRID], attribute, obj_list)
        else:
            edge_object = self.create_object(graph, edge_class, edge_mRID)
            setattr(graph[cim_class][mRID], attribute, edge_object)

    def create_object(self, graph: dict[type, dict[str, object]], class_type: type,
                      mRID: str) -> object:

        if class_type not in graph.keys():
            graph[class_type] = {}

        if mRID in graph[class_type].keys():
            obj = graph[class_type][mRID]
        else:
            obj = class_type()
            setattr(obj, 'mRID', mRID)
            graph[class_type][mRID] = obj

        return obj

    def upload(self, graph: dict[type, dict[str, object]]) -> None:
        for cim_class in graph.keys():
            for obj in graph[cim_class].values():
                query = sparql.upload_triples_sparql(obj, self.connection_params)
                self.execute(query)
