from __future__ import annotations

import asyncio
import logging
import threading
from collections import defaultdict
from collections.abc import Coroutine
from uuid import UUID

from neo4j import AsyncGraphDatabase

import cimgraph.queries.cypher as cypher
from cimgraph.core import get_database, get_password, get_url, get_username
from cimgraph.core.serialization import RDF_XML_CLOSE, object_to_xml, profile_namespaces, rdf_xml_open
from cimgraph.databases import BATCH_SIZE, MAX_PARALLEL_QUERIES, ConnectionInterface, Graph, QueryResponse

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
        self._loop = None

    def _run(self, coroutine: Coroutine):
        """
        Run a coroutine on this connection's event loop and return its result. The loop
        runs in its own thread, so the synchronous methods work in scripts and where a
        loop is already running (Jupyter), and the async driver always stays on one loop.
        """
        if self._loop is None:
            self._loop = asyncio.new_event_loop()
            threading.Thread(target=_run_event_loop, args=(self._loop,), daemon=True,
                             name='cimgraph-neo4j').start()
        return asyncio.run_coroutine_threadsafe(coroutine, self._loop).result()

    def connect(self):
        """
        Establish a connection to the Neo4J endpoint.
        """
        if self.driver is None:
            self._run(self._connect())

    async def _connect(self):
        # The async driver is faster than the sync one: get_all_edges awaits its batches together
        self.driver = AsyncGraphDatabase.driver(self.url, auth=(self.username, self.password))
        await self.driver.verify_connectivity()

    def disconnect(self):
        """
        Disconnect from the Neo4J endpoint and stop the event loop. Safe to call when not
        connected.
        """
        if self.driver is not None:
            self._run(self.driver.close())
            self.driver = None
        if self._loop is not None:
            self._loop.call_soon_threadsafe(self._loop.stop)
            self._loop = None

    def execute(self, query_message: str) -> QueryResponse:
        """
        Execute a read-only cypher query on the Neo4J endpoint.

        Args:
            query_message (str): The cypher query to be executed.

        Returns:
            query_output (QueryResponse): one dict per record.
        """
        self.connect()
        return self._run(self.async_execute(query_message))

    async def async_execute(self, query_message: str) -> QueryResponse:
        """
        Async form of execute(), on this connection's event loop: await it only in a
        coroutine run by self._run.
        """
        async with self.driver.session(database=self.database) as session:
            return await session.execute_read(lambda tx: self.query_tx(tx, query_message))

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
        return self._run(self.async_execute_with_params(query_message, **params))

    async def async_execute_with_params(self, query_message: str, **params) -> QueryResponse:
        """
        Async form of execute_with_params(), on this connection's event loop. Uses
        execute_write, since the parameterized queries we send (n10s imports) change the graph.
        """
        async with self.driver.session(database=self.database) as session:
            return await session.execute_write(
                lambda tx: self.query_tx_with_params(tx, query_message, **params))

    async def query_tx_with_params(self, tx, query_message: str, **params) -> QueryResponse:
        """Transaction function for parameterized queries: one dict per record."""
        result = await tx.run(query_message, **params)
        return await result.data()

    async def query_tx(self, tx, query_message: str) -> QueryResponse:
        """Transaction function: one dict per record."""
        result = await tx.run(query_message)
        return await result.data()

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
        self.connect()
        self._run(self.get_all_edges_async(list(graph[cim_class].keys()), graph, cim_class))

    def get_all_attributes(self, graph: dict[type, dict[str, object]], cim_class: type) -> None:
        """Set the attributes of every object of cim_class. Associations are set to the
        referenced objects' identifier text (create_reference), not to new objects."""
        self.connect()
        self._run(self.get_all_attributes_async(list(graph[cim_class].keys()), graph, cim_class))

    async def get_all_edges_async(self, mrid_list: list[UUID], graph: Graph,
                                  cim_class: type) -> None:
        await self._run_batches(mrid_list, graph, cim_class, expand_graph=True)

    async def get_all_attributes_async(self, mrid_list: list[UUID], graph: Graph,
                                       cim_class: type) -> None:
        await self._run_batches(mrid_list, graph, cim_class, expand_graph=False)

    async def _run_batches(self, mrid_list: list[UUID], graph: Graph, cim_class: type,
                           expand_graph: bool) -> None:
        """Run edge_query_runner for every BATCH_SIZE objects, up to MAX_PARALLEL_QUERIES
        batches at once."""
        limit = asyncio.Semaphore(MAX_PARALLEL_QUERIES)

        async def run_batch(index: int) -> None:
            async with limit:
                await self.edge_query_runner(mrid_list, index, graph, cim_class, expand_graph)

        batches = (len(mrid_list) + BATCH_SIZE - 1) // BATCH_SIZE
        await asyncio.gather(*(run_batch(index) for index in range(batches)))

    async def edge_query_runner(self, mrid_list: list[UUID], index: int, graph: Graph,
                                cim_class: type, expand_graph: bool) -> None:
        """Query and parse the relationships and properties of batch number index. The
        queries of different batches overlap; parsing runs on the event loop's thread between
        awaits, so batches never change the graph at the same time."""
        batch = mrid_list[index * BATCH_SIZE:(index + 1) * BATCH_SIZE]
        query_output = await self.async_execute(cypher.get_all_edges_cypher(graph, cim_class, batch))
        self.edge_query_parser(query_output, graph, cim_class, expand_graph)
        query_output = await self.async_execute(
            cypher.get_all_properties_cypher(graph, cim_class, batch))
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


def _run_event_loop(loop: asyncio.AbstractEventLoop) -> None:
    """Thread target for Neo4jConnection's event loop: run it until disconnect() stops it."""
    loop.run_forever()
    loop.close()
