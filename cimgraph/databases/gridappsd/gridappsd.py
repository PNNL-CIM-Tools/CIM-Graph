from __future__ import annotations

import json
import logging
import math
import os
from collections import defaultdict
from uuid import UUID

from gridappsd import GridAPPSD

import cimgraph.queries.sparql as sparql
from cimgraph.databases import (ConnectionInterface, Graph, QueryResponse, get_cim_profile,
                                get_database, get_host, get_iec61970_301, get_namespace,
                                get_password, get_port, get_url, get_username)

_log = logging.getLogger(__name__)


class GridappsdConnection(ConnectionInterface):

    def __init__(self):

        # clear cached env variables
        get_url.cache_clear()
        get_namespace.cache_clear()
        get_cim_profile.cache_clear()
        get_iec61970_301.cache_clear()
        get_host.cache_clear()
        get_port.cache_clear()
        get_username.cache_clear()
        get_password.cache_clear()

        # retrieve env variables
        self.cim_profile, self.cim = get_cim_profile()
        self.namespace = get_namespace()
        self.iec61970_301 = get_iec61970_301()
        self.host = get_host()
        self.port = get_port()
        self.username = get_username()
        self.password = get_password()
        self.use_units = False
        self.url = get_url()
        self.database = get_database()


        self.gapps = None

    # -------------------------------------------------------------------------
    # Methods for connecting to the platform and executing SPARQL queries
    # -------------------------------------------------------------------------

    def connect(self):
        if not self.gapps:
            os.environ['GRIDAPPSD_ADDRESS'] = self.host
            os.environ['GRIDAPPSD_PORT'] = str(self.port)
            os.environ['GRIDAPPSD_USER'] = self.username
            os.environ['GRIDAPPSD_PASSWORD'] = self.password
            os.environ['GRIDAPPSD_DATABASE'] = self.database
            os.environ['GRIDAPPSD_URL'] = self.url
            self.gapps = GridAPPSD()

    def disconnect(self):
        self.gapps.disconnect()

    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        response = self.gapps.query_data(query_message, database_type=self.database, timeout=30)
        return response['data']

    def upload(self, graph: dict[type, dict[str, object]]) -> None:
        for cim_class in graph.keys():
            for obj in graph[cim_class].values():
                query = sparql.upload_triples_sparql(obj)
                self.execute(query)

    # -------------------------------------------------------------------------
    # Methods for creating new graph structures
    # -------------------------------------------------------------------------

    def create_new_graph(self, container: object, graph:Graph = None) -> dict[type, dict[UUID, object]]:
        """
        Create a new graph structure for a CIM EquipmentContainer object.
        The method uses a SPARQL query to obtain all terminals in the graph,
        along with all nodes and conducting equipment associated with each
        terminal. This forms the baseline knowledge graph for the GraphModel.
        If a graph is specified, the new objects will be added to the existing
        graph. Otherwise, a new graph will be created from scratch.

        Args:
            container (object): The container object for which the graph is created.
            graph (dict, optional): Graph of CIM objects, grouped by class and UUID.

        Returns:
            dict: Graph consisting of types and UUID mapped to object instances.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=container)
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(container)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def create_distributed_graph(self, area: object, graph: dict = None) -> Graph:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=area)

        if not isinstance(area, self.cim.SubSchedulingArea):
            _log.error(f'Area object is not a SubSchedulingArea')
            raise TypeError('Area object is not a SubSchedulingArea')

        sparql_message = sparql.get_all_nodes_from_area(area)
        # Execute SPARQL query
        query_output = self.execute(sparql_message)
        # Parse query results and create new graph
        graph = self.parse_node_query(graph, query_output)
        return graph

    def build_graph_from_list( self, graph, mrid_list: list[str]) -> Graph:
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_nodes_from_list(
                eq_mrids, self.namespace)
            # print(sparql_message)
            query_output = self.execute(sparql_message)
            graph = self.parse_node_query(graph, query_output)
        return graph

    # -------------------------------------------------------------------------
    # Methods for retrieving objects from the database
    # -------------------------------------------------------------------------

    def get_object(self, mRID: str, graph: dict = None) -> object:
        """
        Retrieve an object from the Blazegraph database using its mRID.

        Args:
            mrid (str): The mRID of the object to be retrieved.
            graph (dict, optional): The graph database to store the fetched object. Defaults to {}.

        Returns:
            object: The retrieved object.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        # Use sparql module to build get correct query string
        sparql_message = sparql.get_object_sparql(mRID)
        # Execute query
        query_output = self.execute(sparql_message)
        obj = None
        # Parse query results to get the correct CIM object
        for result in query_output['results']['bindings']:
            uri = result['identifier']['value']  # uri / mRID string
            obj_class = result['obj_class']['value']  # class type
            # If equipment class is in data profile, create a new object
            if obj_class in self.cim.__all__:
                class_type = getattr(self.cim, obj_class)  # get type
                obj = self.create_object(graph, class_type, uri)  # get object
            else:
                # If it is not in the profile, log it as a missing class
                _log.warning(
                    f'object class missing from data profile: {obj_class}')
                continue

        return obj

    def get_from_triple(self, subject:object, predicate:str, graph: Graph = None) -> list[object]:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(subject, graph)
        # Generate SPARQL query for user-specified triple string
        sparql_message = sparql.get_triple_sparql(subject, predicate)
        # Execute SPARQL query
        query_output = self.execute(sparql_message)
        # Parse the query output
        new_edges = self.edge_query_parser(query_output, graph, subject.__class__)
        return new_edges


    def get_edges_query(self, graph: dict[type, dict[UUID, object]],
                        cim_class: type) -> str:

        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)

        return sparql_message

    def get_all_edges(self, graph: dict[type, dict[UUID, object]], cim_class: type) -> None:
        uuid_list = list(graph[cim_class].keys())
        for index in range(math.ceil(len(uuid_list) / 100)):
            eq_mrids = uuid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct queries>sparql python script based on class name
            sparql_message = sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    def get_all_attributes(self, graph: dict[type, dict[str, object]],
                           cim_class: type):
        mrid_list = list(graph[cim_class].keys())
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_attributes_sparql(cim_class, eq_mrids)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

    # -------------------------------------------------------------------------
    # Methods for parsing query results
    # -------------------------------------------------------------------------



    def parse_node_query(self, graph: dict, query_output: dict) -> Graph:
        """
        Parse the results of a node query to update a graph structure.

        Args:
            graph (dict): Graph to be updated.
            query_output (dict): Query output to be parsed.

        Returns:
            dict: Updated graph structure.
        """
        # Iterate through all rows of query output
        for result in query_output['results']['bindings']:

            # Associated conducting equipment are JSON-LD strings
            eq = json.loads(result['Equipment']['value'])
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
            if 'ConnectivityNode' in result:
                # Get uri strings of nodes and terminals
                node_mrid = result['ConnectivityNode']['value']
                term_mrid = result['Terminal']['value']
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
            if 'Measurement' in result:
                # Associated conducting equipment are JSON-LD strings
                meas = json.loads(result['Measurement']['value'])
                meas_id = meas['@id']
                meas_class = meas['@type']
                # Get uri strings of nodes and terminals
                if meas_class in self.cim.__all__:
                    meas_class = getattr(self.cim, meas_class)
                    measurement = self.create_object(graph, meas_class, meas_id)

        return graph

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: Graph, cim_class: type, expand_graph=True) -> list[object]:
        """
        Parse the results of an edge query to update a graph structure.

        Args:
            query_output (QueryResponse): Query output to be parsed.
            graph (dict): Graph structure.
            cim_class (type): The CIM class for which to parse edges.
            expand_graph (bool, optional): Whether to expand the graph with new edges. Defaults to True.
        """
        new_edges = []
        for result in query_output['results']['bindings']:

            if result['attribute']['value'] != 'type':  #skip 'type' and other single attributes

                uri = result['identifier']['value']  #get mRID
                identifier = UUID(uri.strip('_').lower())
                attribute = result['attribute']['value']  #edge attribute
                value = result['value']['value']  #get edge value
                if 'edge' in result:  #check if association
                    edge = json.loads(result['edge']['value'])
                    edge_mRID = edge['@id']
                    edge_class = edge['@type']
                    if edge_class in self.cim.__all__:
                        edge_class = getattr(self.cim, edge_class)
                    else:
                        _log.warning(f'Class {edge_class} not in data profile')
                        continue

                    if expand_graph:
                        edge_object = self.create_edge(graph, cim_class, identifier,
                                         attribute, edge_class, edge_mRID)
                        new_edges.append(edge_object)
                    else:
                        self.create_value(graph, cim_class, identifier, attribute, value)

                elif self.namespace in value:  #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]

                    if enum_class in self.cim.__all__:  # if enumeration
                        edge_enum = getattr(self.cim, enum_class)(enum_value)
                        new_edges.append(edge_enum)
                        association = self.check_attribute(
                            cim_class, attribute)
                        if association is not None:
                            setattr(graph[cim_class][identifier], association, edge_enum)
                else:
                    association = self.check_attribute(cim_class, attribute)
                    if association is not None:
                        new_edges.append(value)
                        self.create_value(graph, cim_class, identifier, attribute, value)
        return new_edges
