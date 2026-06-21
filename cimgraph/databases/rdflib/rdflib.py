from __future__ import annotations

import json
import logging
import math
from uuid import UUID

from rdflib import Graph, Namespace
from rdflib.namespace import RDF

import cimgraph.queries.rdflib as rdflib_sparql
from cimgraph.databases import Graph as GraphType
from cimgraph.databases.sparql_endpoint import SPARQLEndpointConnection

_log = logging.getLogger(__name__)


class RDFlibConnection(SPARQLEndpointConnection):
    """
    A class to handle connections and operations with an RDFlib database.

    RDFlib-specific features:
    - File-based graph loading
    - Optional Oxigraph backend support
    - Attribute-based result access pattern
    """

    def __init__(self, filename: str = None, use_oxigraph: bool = True):
        super().__init__()
        self.filename = filename
        self.use_oxigraph = use_oxigraph
        self.connect()

    # -------------------------------------------------------------------------
    # Database-specific method implementations
    # -------------------------------------------------------------------------

    def _setup_connection(self) -> None:
        """Initialize rdflib.Graph connection with optional file loading."""
        if self.use_oxigraph:
            self.connection_obj = Graph(store='Oxigraph')
        else:
            self.connection_obj = Graph()

        # Load file if specified
        if self.filename is not None:
            try:
                self.connection_obj.parse(self.filename)
                self.connection_obj.bind('cim', Namespace(self.namespace))
                self.connection_obj.bind('rdf', RDF)
            except Exception as e:
                _log.warning(
                    f'File {self.filename} not found. Defaulting to empty network graph. Error: {e}')
                self.filename = None

    def _execute_raw_query(self, query_message: str):
        """
        Execute query using rdflib.Graph and normalize results.

        RDFlib returns a Result object, but we need to normalize it to match
        the SPARQLWrapper format: {'results': {'bindings': [...]}}
        """
        raw_result = self.connection_obj.query(query_message)

        # Normalize to match SPARQLWrapper format
        # Convert rdflib Result iterable to list of result bindings
        return {
            'results': {
                'bindings': list(raw_result)
            }
        }

    def _parse_result_field(self, result, field_name: str) -> str:
        """
        Extract field value from rdflib attribute-based result format.

        RDFlib results use attribute access: result.field_name.value
        """
        if hasattr(result, field_name):
            field_obj = getattr(result, field_name)
            if field_obj is not None:
                if hasattr(field_obj, 'value'):
                    return str(field_obj.value)
                return str(field_obj)
        return None

    def _update_raw(self, update_message: str) -> str:
        """
        Execute SPARQL update using rdflib.

        Note: RDFlib update support may be limited compared to server-based endpoints.
        """
        try:
            self.connection_obj.update(update_message)
            return 'Update completed'
        except AttributeError:
            _log.warning('RDFlib update not fully supported in this version')
            raise NotImplementedError('Update operations not supported for RDFlib backend')

    # -------------------------------------------------------------------------
    # Override query generation to use RDFlib-specific queries
    # -------------------------------------------------------------------------

    def get_edges_query(self, graph: GraphType, cim_class: type) -> str:
        """Generate RDFlib-specific SPARQL query for edges."""
        eq_mrids = list(graph[cim_class].keys())[0:100]
        sparql_message = rdflib_sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)
        return sparql_message

    def get_all_edges(self, graph: GraphType, cim_class: type) -> None:
        """
        Override to use RDFlib-specific queries and parser.

        RDFlib queries return different field names than standard SPARQL.
        """
        uuid_list = list(graph[cim_class].keys())
        for index in range(math.ceil(len(uuid_list) / 100)):
            eq_mrids = uuid_list[index * 100:(index + 1) * 100]
            sparql_message = rdflib_sparql.get_all_edges_sparql(graph, cim_class, eq_mrids)
            query_output = self.execute(sparql_message)
            self._rdflib_edge_query_parser(query_output, graph, cim_class)

    def get_all_attributes(self, graph: GraphType, cim_class: type) -> None:
        """
        Override to use RDFlib-specific queries and parser.

        RDFlib queries return different field names than standard SPARQL.
        """
        mrid_list = list(graph[cim_class].keys())
        for index in range(math.ceil(len(mrid_list) / 100)):
            eq_mrids = mrid_list[index * 100:(index + 1) * 100]
            sparql_message = rdflib_sparql.get_all_attributes_sparql(graph, cim_class, eq_mrids)
            query_output = self.execute(sparql_message)
            self._rdflib_edge_query_parser(query_output, graph, cim_class, expand_graph=False)

    def _rdflib_edge_query_parser(self, query_output, graph: GraphType,
                                  cim_class: type, expand_graph=True) -> None:
        """
        RDFlib-specific edge query parser.

        RDFlib queries return ?attr and ?val instead of ?attribute and ?value,
        and ?edge_class instead of ?edge JSON string.
        """
        for result in query_output['results']['bindings']:
            attr = self._parse_result_field(result, 'attr')

            if attr is not None and 'type' not in attr:
                is_enumeration = False

                identifier = UUID(self._parse_result_field(result, 'identifier').strip('_').lower())
                attribute = str(attr).split(self.namespace)[1]
                value = str(self._parse_result_field(result, 'val'))

                # Check if enumeration
                if self.namespace in value:
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    is_enumeration = True

                # Check if association (edge to another object)
                edge_class = self._parse_result_field(result, 'edge_class')
                if edge_class is not None:
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
