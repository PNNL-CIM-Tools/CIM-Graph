from __future__ import annotations

import logging

from SPARQLWrapper import JSON, POST, SPARQLWrapper

from cimgraph.core import get_url
from cimgraph.databases.sparql_endpoint import SPARQLEndpointConnection

_log = logging.getLogger(__name__)


class BlazegraphConnection(SPARQLEndpointConnection):
    """
    A class to handle connections and operations with a Blazegraph database.

    Blazegraph-specific features:
    - SPARQLWrapper-based connection
    """

    def __init__(self):
        super().__init__()
        self.url = get_url()
        self.connect()

    # -------------------------------------------------------------------------
    # Database-specific method implementations
    # -------------------------------------------------------------------------

    def _setup_connection(self) -> None:
        """Initialize SPARQLWrapper connection for Blazegraph."""
        self.connection_obj = SPARQLWrapper(self.url)
        self.connection_obj.setReturnFormat(JSON)

    def _execute_raw_query(self, query_message: str):
        """Execute query using SPARQLWrapper and return JSON results. Each call gets its
        own SPARQLWrapper (it holds the query), so batches can run in parallel threads."""
        query = SPARQLWrapper(self.url)
        query.setReturnFormat(JSON)
        query.setQuery(query_message)
        query.setMethod(POST)
        return query.query().convert()

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
