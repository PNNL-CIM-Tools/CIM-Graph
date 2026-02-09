from __future__ import annotations

import logging

from SPARQLWrapper import JSON, POST, SPARQLWrapper

from cimgraph.core import (get_cim_profile, get_iec61970_301, get_namespace,
                           get_url)
from cimgraph.databases.sparql_endpoint import SPARQLEndpointConnection

_log = logging.getLogger(__name__)


class GraphDBConnection(SPARQLEndpointConnection):
    """
    A class to handle connections and operations with a GraphDB database.

    GraphDB-specific features:
    - Cache clearing on initialization
    - SPARQLWrapper-based connection
    """

    def __init__(self) -> None:
        # Clear cached env variables before parent init
        get_url.cache_clear()
        get_namespace.cache_clear()
        get_cim_profile.cache_clear()
        get_iec61970_301.cache_clear()

        # Initialize parent class (which sets up standard variables)
        super().__init__()

        # Set GraphDB-specific URL
        self.url = get_url()

    # -------------------------------------------------------------------------
    # Database-specific method implementations
    # -------------------------------------------------------------------------

    def _setup_connection(self) -> None:
        """Initialize SPARQLWrapper connection for GraphDB."""
        self.connection_obj = SPARQLWrapper(self.url)
        self.connection_obj.setReturnFormat(JSON)

    def _execute_raw_query(self, query_message: str):
        """Execute query using SPARQLWrapper and return JSON results."""
        self.connection_obj.setQuery(query_message)
        self.connection_obj.setMethod(POST)
        return self.connection_obj.query().convert()

    def _parse_result_field(self, result: dict, field_name: str) -> str:
        """Extract field value from SPARQLWrapper dict-based result format."""
        if field_name in result:
            return result[field_name]['value']
        return None

    def _update_raw(self, update_message: str) -> str:
        """Execute SPARQL update using SPARQLWrapper."""
        self.connection_obj.setQuery(update_message)
        self.connection_obj.setMethod(POST)
        return self.connection_obj.query()
