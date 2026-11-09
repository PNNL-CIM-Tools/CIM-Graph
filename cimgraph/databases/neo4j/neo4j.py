from __future__ import annotations

import logging
from collections import defaultdict
from uuid import UUID

from neo4j import GraphDatabase, RoutingControl

import cimgraph.queries.cypher as cypher
from cimgraph.core import get_database, get_password, get_url, get_username
from cimgraph.core.serialization import RDF_XML_CLOSE, object_to_xml, profile_namespaces, rdf_xml_open
from cimgraph.databases import (BATCH_SIZE, ConnectionInterface, Graph, QueryResponse,
                                run_queries_in_parallel)

_log = logging.getLogger(__name__)


class Neo4jConnection(ConnectionInterface):
    """
    A class to handle connections and operations with a Neo4J database.

    """

    def __init__(self):
        super().__init__()
        self.url = get_url()
        self.username = get_username()
        self.password = get_password()
        self.database = get_database()
        self.driver = None


    def connect(self):
        """
        Establish a connection to the Neo4J endpoint. The driver is thread-safe and
        shared by the queries that get_all_edges runs in parallel.
        """
        if self.driver is None:
            self.driver = GraphDatabase.driver(self.url, auth=(self.username, self.password))
            self.driver.verify_connectivity()

    def disconnect(self):
        """
        Disconnect from the Neo4J endpoint. Safe to call when not connected.
        """
        if self.driver is not None:
            self.driver.close()
            self.driver = None

    def execute(self, query_message: str) -> QueryResponse:
        """
        Execute a read-only cypher query on the Neo4J endpoint.

        Args:
            query_message (str): The cypher query to be executed.

        Returns:
            query_output (QueryResponse): one dict per record.
        """
        self.connect()
        records, _, _ = self.driver.execute_query(
            query_message, database_=self.database, routing_=RoutingControl.READ)
        return [record.data() for record in records]

    def execute_with_params(self, query_message: str, **params) -> QueryResponse:
        """
        Execute a cypher query that writes, with bound parameters.

        Required for payloads that contain quotes or newlines (e.g. RDF sent to
        n10s.rdf.import.inline), where string interpolation would corrupt the
        query or allow injection.

        Args:
            query_message (str): cypher query using $param placeholders.
            **params: values bound to those placeholders.

        Returns:
            query_output (QueryResponse): one dict per record.
        """
        self.connect()
        records, _, _ = self.driver.execute_query(
            query_message, parameters_=params, database_=self.database,
            routing_=RoutingControl.WRITE)
        return [record.data() for record in records]

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
        self.add_to_graph(graph=graph, obj=container)
        cypher_message = cypher.get_all_nodes_from_container(container)
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
                equipment = self.create_object(graph, eq_class, eq_id)
            else:
                # If it is not in the profile, log it as a missing class
                _log.warning(
                    f'object class missing from data profile: {eq_class}')
                continue
            if node_id:
                # Add each object to graph
                node = self.create_object(graph, self.cim.ConnectivityNode, node_id)
                terminal = self.create_object(graph, self.cim.Terminal, terminal_id)

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
            _log.error('Area object is not a SubSchedulingArea')
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

        eq_mrids = list(graph[cim_class].keys())[0:BATCH_SIZE]
        cypher_message = cypher.get_all_edges_cypher(graph, cim_class, eq_mrids)

        return cypher_message

    def get_all_edges(self, graph: dict[type, dict[str, object]], cim_class: type) -> None:
        """Expand the graph by one edge for every object of cim_class: associated objects
        are added to the graph, and attributes are set."""
        self._expand_by_batches(graph, cim_class, expand_graph=True)

    def get_all_attributes(self, graph: dict[type, dict[str, object]], cim_class: type) -> None:
        """Set the attributes of every object of cim_class. Associations are set to the
        referenced objects' identifier text (create_reference), not to new objects."""
        self._expand_by_batches(graph, cim_class, expand_graph=False)

    def _expand_by_batches(self, graph: Graph, cim_class: type, expand_graph: bool) -> None:
        """
        Query the relationships and the properties of every object of cim_class,
        BATCH_SIZE objects per query. The queries are built before any result is parsed
        and run in parallel; parsing, which changes the graph, stays on this thread.
        """
        self.connect()
        uuid_list = list(graph[cim_class].keys())
        batches = [uuid_list[start:start + BATCH_SIZE]
                   for start in range(0, len(uuid_list), BATCH_SIZE)]
        edge_queries = [cypher.get_all_edges_cypher(graph, cim_class, batch) for batch in batches]
        property_queries = [cypher.get_all_properties_cypher(graph, cim_class, batch)
                            for batch in batches]
        outputs = run_queries_in_parallel(self.execute, edge_queries + property_queries)
        for query_output in outputs[:len(batches)]:
            self.edge_query_parser(query_output, graph, cim_class, expand_graph)
        for query_output in outputs[len(batches):]:
            self.property_query_parser(query_output, graph, cim_class)

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

                if expand_graph:
                    edge_object = self.create_edge(graph, cim_class, identifier,
                                        attribute, edge_class, edge_value)
                    new_edges.append(edge_object)
                else:
                    new_edges.append(self.create_reference(graph, cim_class, identifier,
                                                           attribute, edge_class, edge_value))

            else:
                # An enumeration value, in the cim or an extension namespace
                edge_enum = self.enum_from_iri(edge_value)
                if edge_enum is not None:
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


    def upload(self, graph: Graph, batch_size: int = 100) -> None:
        """
        Upload a graph of CIM objects to Neo4j via the n10s RDF plugin.

        Objects are serialized to RDF/XML with the same per-object serializer
        used for file exports, then ingested with n10s.rdf.import.inline() so no file has to
        be reachable from the Neo4j server. Requires n10s to be initialized
        (see the n10s.graphconfig.init() docs); uploading without it raises.

        Args:
            graph (Graph): dict of {cim_class: {identifier: object}}, e.g.
                GraphModel.graph. Works for any GraphModel subclass.
            batch_size (int): objects per inline() call. Defaults to 100,
                matching the query batching used elsewhere in this class.
        """
        for cim_class, objects in graph.items():
            instances = list(objects.values())
            for index in range(0, len(instances), batch_size):
                batch = instances[index:index + batch_size]
                rdf_xml = self._serialize_to_rdf_xml(batch)
                self.execute_with_params(
                    "CALL n10s.rdf.import.inline($payload, 'RDF/XML')",
                    payload=rdf_xml,
                )

    def _serialize_to_rdf_xml(self, objects: list) -> str:
        """Serialize CIM objects to an RDF/XML document string, without a model header."""
        namespaces = profile_namespaces({type(obj) for obj in objects})
        body = ''.join(object_to_xml(obj, namespaces) for obj in objects)
        return rdf_xml_open(namespaces) + body + RDF_XML_CLOSE
