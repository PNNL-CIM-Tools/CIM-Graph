from __future__ import annotations

import asyncio
import logging
import math
from collections import defaultdict
from uuid import UUID

import nest_asyncio
from neo4j import AsyncGraphDatabase, GraphDatabase
from neo4j.exceptions import DriverError, Neo4jError

import cimgraph.data_profile.cimhub_2023 as cim
import cimgraph.queries.cypher as cypher
from cimgraph.databases import (ConnectionInterface, Graph, QueryResponse, get_cim_profile,
                                get_database, get_iec61970_301, get_namespace, get_password,
                                get_url, get_username)

nest_asyncio.apply()

_log = logging.getLogger(__name__)


class Neo4jConnection(ConnectionInterface):
    """
    A class to handle connections and operations with a Neo4J database.

    """

    def __init__(self):

        # clear cached env variables
        get_url.cache_clear()
        get_namespace.cache_clear()
        get_cim_profile.cache_clear()
        get_iec61970_301.cache_clear()
        get_username.cache_clear()
        get_password.cache_clear()
        get_database.cache_clear()

        # retrieve env variables
        self.cim_profile, cim_module = get_cim_profile()
        self.cim:cim = cim_module
        self.namespace = get_namespace()
        self.url = get_url()
        self.username = get_username()
        self.password = get_password()
        self.database = get_database()
        self.iec61970_301 = get_iec61970_301()
        self.driver = None
        # self.use_async = use_async


    def connect(self):
        """
        Establish a connection to the Neo4J endpoint.
        """
        # Create a neo4j driver object if it does not exist
        if not self.driver:
            # Use Async driver for bettter performance
            # if self.use_async:
                self.driver = AsyncGraphDatabase.driver(self.url, auth=(self.username, self.password))
                asyncio.run(self.driver.verify_connectivity())
                # else:
                #     self.driver = GraphDatabase.driver(self.url, auth=(self.username, self.password))
                #     self.driver.verify_connectivity()
                #     self.session = self.driver.session(database=self.database)

    def disconnect(self):
        """
        Disconnect from the Neo4J endpoint.
        """
        asyncio.run(self.driver.close())
        self.driver = None

    def execute(self, query_message: str) -> QueryResponse:
        """
        Execute a given cypher query on the Neo4J endpoint.
        If performing concurrent calls with the Async driver, use the
        async_execute() method instead.

        Args:
            query_message (str): The cypher query to be executed.

        Returns:
            query_output (QueryResponse): The response from the query execution.
        """
        records = asyncio.run(self.async_execute(query_message))
        return records

    async def async_execute(self, query_message: str) -> QueryResponse:
        """
        Execute a given cypher query on the Neo4J endpoint with the Async driver.
        Call using query_output = asyncio.run(self.async_execute(cypher_message))

        Args:
            query_message (str): The cypher query to be executed.

        Returns:
            query_output (QueryResponse): The response from the query execution.
        """
        self.connect()

        async with self.driver.session(database=self.database) as session:
            result = await session.execute_read(lambda tx: self.query_tx(tx, query_message))

        return result

    async def query_tx(self, tx, query_message):
        """
        Lambda transform for async query execution
        """
        result = await tx.run(query_message)
        records = await result.data()
        return records

    def get_object(self, mRID: str, graph: dict = None) -> object:
        """
        Retrieve an object from the Neo4J database using its mRID.

        Args:
            mrid (str): The mRID of the object to be retrieved.
            graph (dict, optional): The graph database to store the fetched object. Defaults to {}.

        Returns:
            object: The retrieved object.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        # Use cypher module to build get correct query string
        cypher_message = cypher.get_object_cypher(mRID)
        query_output = self.execute(cypher_message)

        obj = None
        # Parse query results to get the correct CIM object
        for result in query_output:
            uri = result['identifier']  # uri / mRID string
            obj_class = result['class']  # class type
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

    def create_new_graph(self, container: object, graph:Graph = None) -> Graph:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        # Generate cypher message from correct loaders>cypher python script based on class name
        cypher_message = cypher.get_all_nodes_from_container(container)
        # async_execute cypher query
        query_output = self.execute(cypher_message)
        self.parse_node_query(graph, query_output)

        return graph


    def parse_node_query(self, graph: dict, query_output: dict) -> Graph:
        """
        Parse the results of a node query to update a graph structure.

        Args:
            graph (dict): Graph to be updated.
            query_output (dict): Query output to be parsed.

        Returns:
            dict: Updated graph structure.
        """

        for result in query_output:
            # Parse query results
            node_id = result['ConnectivityNode']
            terminal_id = result['Terminal']
            eq_id = result['eq_id']
            eq_class = result['eq_class']

            # If equipment class is in data profile, add it to the graph also
            if eq_class in self.cim.__all__:
                eq_class = getattr(self.cim, eq_class)
                equipment:cim.ConductingEquipment = self.create_object(graph, eq_class, eq_id)
            else:
                # If it is not in the profile, log it as a missing class
                _log.warning(
                    f'object class missing from data profile: {eq_class}')
                continue
            if node_id:
                # Add each object to graph
                node:cim.ConnectivityNode = self.create_object(graph, self.cim.ConnectivityNode, node_id)
                terminal:cim.Terminal = self.create_object(graph, self.cim.Terminal, terminal_id)

                # Associate the node and equipment with the terminal
                if terminal not in equipment.Terminals:
                    equipment.Terminals.append(terminal)
                if terminal not in node.Terminals:
                    node.Terminals.append(terminal)
                # Associate the terminal with the equipment and node
                setattr(terminal, 'ConnectivityNode', node)
                setattr(terminal, 'ConductingEquipment', equipment)

        return graph

    def create_distributed_graph(self, area: object, graph: dict = None) -> Graph:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=area)

        if not isinstance(area, self.cim.SubSchedulingArea):
            _log.error(f'Area object is not a SubSchedulingArea')
            raise TypeError('Area object is not a SubSchedulingArea')

        cypher_message = cypher.get_all_nodes_from_area(area)
        # Execute cypher query
        query_output = self.execute(cypher_message)
        # Parse query results and create new graph
        graph = self.parse_node_query(graph, query_output)
        return graph


    def get_from_triple(self, subject:object, predicate:str, graph: Graph = None) -> list[object]:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(subject, graph)
        # Generate cypher query for user-specified triple string
        cypher_message = cypher.get_triple_cypher(subject, predicate)
        # Execute cypher query
        query_output = self.execute(cypher_message)
        # Parse the query output
        new_edges = self.edge_query_parser(query_output, graph, subject.__class__)
        return new_edges

    def get_edges_query(self, graph: dict[type, dict[str, object]], cim_class: type) -> str:

        eq_mrids = list(graph[cim_class].keys())[0:100]
        cypher_message = cypher.get_all_edges_cypher(graph, cim_class, eq_mrids)

        return cypher_message

    def get_all_edges(self, graph: dict[type, dict[str, object]], cim_class: type) -> None:
        uuid_list = list(graph[cim_class].keys())

        asyncio.run(self.get_all_edges_async(uuid_list, graph, cim_class))


    async def get_all_edges_async(self, mrid_list, graph: dict[type, dict[str, object]],
                                  cim_class: type):
        for f in asyncio.as_completed([
                self.edge_query_runner(mrid_list, index, graph, cim_class)
                for index in range(math.ceil(len(mrid_list) / 100))
        ]):
            await f

    async def edge_query_runner(self, mrid_list: list[str], index: int,
                                graph: dict[type, dict[str, object]], cim_class: type):

        # Run a batch of 100 UUIDs at a time
        eq_mrids = mrid_list[index * 100:(index + 1) * 100]
        #generate cypher message from graph and CIM class name
        cypher_message = cypher.get_all_edges_cypher(graph, cim_class, eq_mrids)
        #async_execute cypher query
        query_output = asyncio.run(self.async_execute(cypher_message))
        self.edge_query_parser(query_output, graph, cim_class)

        #generate cypher message from graph and CIM class name
        cypher_message = cypher.get_all_properties_cypher(graph, cim_class, eq_mrids)
        #async_execute cypher query
        query_output = asyncio.run(self.async_execute(cypher_message))
        self.property_query_parser(query_output,graph,cim_class)



    def edge_query_parser(self, query_output: QueryResponse,
                          graph: Graph, cim_class: type, expand_graph=True):

        new_edges = []
        for result in query_output:

            uri = result['identifier']    #get mRID
            attribute = result['attribute']
            edge_value = result['edge_id']   #get edge value
            edge_class = result['edge_class']

            if 'urn:uuid:' in uri:
                uri = uri.split('urn:uuid:')[1]
            elif '#' in uri:
                uri = uri.split('#')[1]

            identifier = UUID(uri.strip('_').lower())

            if edge_class: # Check if association to another class
                if edge_class in self.cim.__all__:
                    edge_class = getattr(self.cim, edge_class)
                else:
                    _log.warning(f'Class {edge_class} not in data profile')
                    continue

                edge_object = self.create_edge(graph, cim_class, identifier,
                                            attribute, edge_class, edge_value)
                new_edges.append(edge_object)
            else:
                if self.namespace in edge_value: # Check if enumeration
                    enum_text = edge_value.split(self.namespace)[1]
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
                        new_edges.append(edge_value)
                        self.create_value(graph, cim_class, identifier, attribute, edge_value)
        return new_edges

    def property_query_parser(self, query_output: QueryResponse,
                          graph: Graph, cim_class: type, expand_graph=True):

        for result in query_output:

            uri = result['identifier']    #get mRID
            if 'urn:uuid:' in uri:
                uri = uri.split('urn:uuid:')[1]
            elif '#' in uri:
                uri = uri.split('#')[1]

            identifier = UUID(uri.strip('_').lower())

            properties = result['attributes']
            for attribute in properties.keys():
                if attribute != 'uri':
                    association = self.check_attribute(cim_class, attribute)
                    if association is not None:
                        self.create_value(graph, cim_class, identifier, attribute, properties[attribute])


    def get_all_attributes(self, graph, cim_class):
        pass

    def upload(self, graph):
        pass
