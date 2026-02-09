from __future__ import annotations

import concurrent.futures
import json
import logging
import math
import os
from abc import abstractmethod
from collections import defaultdict
from uuid import UUID

import cimgraph.queries.sparql as sparql
from cimgraph.databases import ConnectionInterface, Graph, QueryResponse

_log = logging.getLogger(__name__)


class SPARQLEndpointConnection(ConnectionInterface):
    """
    Unified base class for SPARQL endpoint connections.

    This class provides a common implementation for all SPARQL endpoint databases
    (Blazegraph, GraphDB, RDFlib, etc.) and defines abstract methods for
    database-specific behavior.

    Subclasses must implement:
    - _setup_connection(): Initialize the database-specific connection object
    - _execute_raw_query(): Execute a query and return raw results
    - _parse_result_field(): Extract field values from query results
    - _update_raw(): Execute an update statement

    Subclasses may optionally override:
    - _get_namespaces(): Return list of namespaces for enumeration parsing
    """

    def __init__(self):
        super().__init__()
        self.connection_obj = None

    # -------------------------------------------------------------------------
    # Abstract methods - Database-specific implementations required
    # -------------------------------------------------------------------------

    @abstractmethod
    def _setup_connection(self) -> None:
        """
        Initialize the database-specific connection object.

        This method should create and configure the connection object
        (e.g., SPARQLWrapper for Blazegraph/GraphDB, rdflib.Graph for RDFlib).
        """
        raise NotImplementedError("Subclass must implement _setup_connection()")

    @abstractmethod
    def _execute_raw_query(self, query_message: str) -> QueryResponse:
        """
        Execute a SPARQL query and return raw results.

        Args:
            query_message (str): The SPARQL query to execute

        Returns:
            QueryResponse: The raw query results in database-specific format
        """
        raise NotImplementedError("Subclass must implement _execute_raw_query()")

    @abstractmethod
    def _parse_result_field(self, result: dict, field_name: str) -> str:
        """
        Extract a field value from a query result.

        Different databases return results in different formats:
        - Blazegraph/GraphDB: result['field_name']['value']
        - RDFlib: result.field_name.value

        Args:
            result: A single result binding from query results
            field_name (str): The name of the field to extract

        Returns:
            str: The field value, or None if field doesn't exist
        """
        raise NotImplementedError("Subclass must implement _parse_result_field()")

    @abstractmethod
    def _update_raw(self, update_message: str) -> str:
        """
        Execute a SPARQL update statement.

        Args:
            update_message (str): The SPARQL update to execute

        Returns:
            str: The response from the update statement
        """
        raise NotImplementedError("Subclass must implement _update_raw()")

    # -------------------------------------------------------------------------
    # Hook methods - Optional overrides for customization
    # -------------------------------------------------------------------------

    def _get_namespaces(self) -> list[str]:
        """
        Return list of namespaces to check for enumeration parsing.

        Default implementation returns single namespace.
        Override in subclass to support multiple namespaces (e.g., Blazegraph).

        Returns:
            list[str]: List of namespace URIs
        """
        return [self.namespace]

    # -------------------------------------------------------------------------
    # Connection management methods
    # -------------------------------------------------------------------------

    def connect(self) -> None:
        """Establish a connection to the SPARQL endpoint."""
        if not self.connection_obj:
            self._setup_connection()

    def disconnect(self) -> None:
        """Disconnect from the SPARQL endpoint."""
        self.connection_obj = None

    # -------------------------------------------------------------------------
    # Query execution methods
    # -------------------------------------------------------------------------

    def execute(self, query_message: str) -> QueryResponse:
        """
        Execute a given SPARQL query on the endpoint.

        Args:
            query_message (str): The SPARQL query to be executed.

        Returns:
            query_output (QueryResponse): The response from the query execution.
        """
        self.connect()
        query_output = self._execute_raw_query(query_message)
        return query_output

    def update(self, update_message: str) -> str:
        """
        Execute SPARQL update on the endpoint.

        Args:
            update_message (str): The SPARQL update to be executed.

        Returns:
            output (str): The response from the update statement.
        """
        self.connect()
        output = self._update_raw(update_message)
        return output

    # -------------------------------------------------------------------------
    # Object retrieval methods
    # -------------------------------------------------------------------------

    def get_object(self, mRID: str, graph: dict = None) -> object:
        """
        Retrieve an object from the database using its mRID.

        Args:
            mRID (str): The mRID of the object to be retrieved.
            graph (dict, optional): The graph catalog to store the fetched object.

        Returns:
            object: The retrieved object.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))

        sparql_message = sparql.get_object_sparql(mRID)
        query_output = self.execute(sparql_message)
        obj = None

        # Parse query results to get the correct CIM object
        for result in query_output['results']['bindings']:
            uri = self._parse_result_field(result, 'identifier')
            obj_class = self._parse_result_field(result, 'obj_class')

            if obj_class in self.cim.__all__:
                class_type = getattr(self.cim, obj_class)
                obj = self.create_object(graph, class_type, uri)
            else:
                _log.warning(
                    f'object class missing from data profile: {obj_class}')
                continue

        return obj

    def get_from_triple(self, subject: object, predicate: str, graph: Graph = None) -> list[str] | list[object]:
        """
        Retrieve the object of an RDF triple from the database from the subject and predicate.

        Args:
            subject (object): A CIM object instance created using CIM-Graph
            predicate (str): A CIM RDF property string, such as `IdentifiedObject.name`

        Returns:
            new_edges: A list of the retrieved objects or property strings.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))

        self.add_to_graph(obj=subject, graph=graph)
        sparql_message = sparql.get_triple_sparql(subject, predicate)
        query_output = self.execute(sparql_message)
        new_edges = self.edge_query_parser(query_output, graph, subject.__class__)
        return new_edges

    # -------------------------------------------------------------------------
    # Graph creation methods
    # -------------------------------------------------------------------------

    def create_new_graph(self, container: object, graph: dict = None) -> Graph:
        """
        Create a new graph structure for a CIM EquipmentContainer object.

        The method uses a SPARQL query to obtain all terminals in the graph,
        along with all nodes and conducting equipment associated with each
        terminal. This forms the baseline knowledge graph for the GraphModel.

        Args:
            container (object): The container object for which the graph is created.
            graph (dict, optional): Graph of CIM objects, grouped by class and UUID.

        Returns:
            dict: Graph consisting of types and UUID mapped to object instances.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=container)

        sparql_message = sparql.get_all_nodes_from_container(container)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def create_distributed_graph(self, area: object, graph: dict = None) -> Graph:
        """
        Create a distributed graph structure for a SubSchedulingArea.

        Args:
            area (object): The SubSchedulingArea object for which the graph is created.
            graph (dict, optional): Graph of CIM objects, grouped by class and UUID.

        Returns:
            dict: Graph consisting of types and UUID mapped to object instances.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=area)

        if not isinstance(area, self.cim.SubSchedulingArea):
            _log.error(f'Area object is not a SubSchedulingArea')
            raise TypeError('Area object is not a SubSchedulingArea')

        sparql_message = sparql.get_all_nodes_from_area(area)
        query_output = self.execute(sparql_message)
        graph = self.parse_node_query(graph, query_output)
        return graph

    def build_graph_from_list(self, graph: Graph, mrid_list: list[str]) -> Graph:
        """
        Build a graph structure based on a list of mRIDs.

        This method is used with original GridAPPS-D Topology Processor, which
        provided a list of addressable and unaddressable equipment in each
        distributed area.

        Args:
            graph (dict): Initial graph structure.
            mrid_list (list[str]): List of mRIDs to be included in the graph.

        Returns:
            dict: Updated graph structure.
        """
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            sparql_message = sparql.get_all_nodes_from_list(eq_mrids, self.namespace)
            query_output = self.execute(sparql_message)
            graph = self.parse_node_query(graph, query_output)
        return graph

    # -------------------------------------------------------------------------
    # Query parsing methods
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
        for result in query_output['results']['bindings']:
            # Associated conducting equipment are JSON-LD strings
            eq_json = self._parse_result_field(result, 'Equipment')
            eq = json.loads(eq_json)
            eq_id = eq['@id']
            eq_class = eq['@type']

            # If equipment class is in data profile, add it to the graph
            if eq_class in self.cim.__all__:
                eq_class = getattr(self.cim, eq_class)
                equipment = self.create_object(graph, eq_class, eq_id)
            else:
                _log.warning(
                    f'object class missing from data profile: {eq_class}')
                continue

            # Handle ConnectivityNode and Terminal associations
            node_mrid = self._parse_result_field(result, 'ConnectivityNode')
            if node_mrid is not None:
                term_mrid = self._parse_result_field(result, 'Terminal')

                node = self.create_object(graph, self.cim.ConnectivityNode, node_mrid)
                terminal = self.create_object(graph, self.cim.Terminal, term_mrid)

                if terminal not in equipment.Terminals:
                    equipment.Terminals.append(terminal)
                if terminal not in node.Terminals:
                    node.Terminals.append(terminal)

                setattr(terminal, 'ConnectivityNode', node)
                setattr(terminal, 'ConductingEquipment', equipment)

            # Handle Measurement associations (if present)
            meas_json = self._parse_result_field(result, 'Measurement')
            if meas_json is not None:
                meas = json.loads(meas_json)
                meas_id = meas['@id']
                meas_class = meas['@type']

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
            expand_graph (bool, optional): Whether to expand the graph with new edges.

        Returns:
            list[object]: List of new edges added.
        """
        new_edges = []

        for result in query_output['results']['bindings']:
            attribute_value = self._parse_result_field(result, 'attribute')

            if attribute_value is not None and attribute_value != 'type':
                parsed = False
                uri = self._parse_result_field(result, 'identifier')
                identifier = UUID(uri.strip('_').lower())
                attribute = attribute_value
                value = self._parse_result_field(result, 'value')

                # Check if this is an association (edge to another object)
                edge_json = self._parse_result_field(result, 'edge')
                if edge_json is not None:
                    parsed = True
                    edge = json.loads(edge_json)
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

                # Check if this is an enumeration
                if value is not None:
                    for namespace in self._get_namespaces():
                        if namespace in value:
                            parsed = True
                            enum_text = value.split(namespace)[1]
                            enum_text = enum_text.split('>')[0]
                            enum_class = enum_text.split('.')[0]
                            enum_value = enum_text.split('.')[1]

                            if enum_class in self.cim.__all__:
                                edge_enum = getattr(self.cim, enum_class)(enum_value)
                                new_edges.append(edge_enum)
                                association = self.check_attribute(cim_class, attribute)
                                if association is not None:
                                    setattr(graph[cim_class][identifier], association, edge_enum)

                # If not parsed as edge or enumeration, treat as simple value
                if not parsed:
                    association = self.check_attribute(cim_class, attribute)
                    if association is not None:
                        new_edges.append(value)
                        self.create_value(graph, cim_class, identifier, attribute, value)

        return new_edges

    # -------------------------------------------------------------------------
    # Edge retrieval methods
    # -------------------------------------------------------------------------

    def get_edges_query(self, graph: Graph, cim_class: type) -> str:
        """
        Generate a SPARQL query to get edges from the graph for a specific CIM class.

        This method is used to provide the graph traversal query for debugging.

        Args:
            graph (dict): Graph structure.
            cim_class (type): The CIM class for which edges query is to be generated.

        Returns:
            str: SPARQL query string.
        """
        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)
        return sparql_message

    def get_all_edges(self, graph: Graph, cim_class: type) -> None:
        """
        Expands the knowledge graph by one edge for all instances of the
        requested CIM class. Associated objects are added to the graph
        as new CIM objects.

        Args:
            graph (dict): Graph structure.
            cim_class (type): The CIM class for which to retrieve edges.
        """
        def process_batch(eq_mrids):
            sparql_message = sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class)

        # Create list of all nodes within graph to be expanded
        uuid_list = list(graph[cim_class].keys())
        # Parallel process in batches of 100 uuids per query
        num_batches = math.ceil(len(uuid_list) / 100)
        eq_mrids_batches = [uuid_list[i * 100:(i + 1) * 100] for i in range(num_batches)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            futures = [executor.submit(process_batch, batch)
                      for batch in eq_mrids_batches]
            for future in concurrent.futures.as_completed(futures):
                future.result()

    def get_all_attributes(self, graph: Graph, cim_class: type) -> None:
        """
        Retrieve all attributes for a given CIM class in the graph.

        Associated objects are added to the graph as strings instead of new CIM objects.

        Args:
            graph (dict): Graph structure.
            cim_class (type): The CIM class for which to retrieve attributes.
        """
        mrid_list = list(graph[cim_class].keys())

        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            sparql_message = sparql.get_all_attributes_sparql(graph, cim_class, eq_mrids)
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, graph, cim_class, expand_graph=False)

    # -------------------------------------------------------------------------
    # Upload methods
    # -------------------------------------------------------------------------

    def upload(self, graph: Graph) -> None:
        """
        Upload a graph structure to the database.

        Args:
            graph (dict): The graph structure to be uploaded.
        """
        for cim_class in graph.keys():
            for obj in graph[cim_class].values():
                query = sparql.upload_triples_sparql(obj)
                self.update(query)
