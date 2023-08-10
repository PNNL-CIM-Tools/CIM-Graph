from __future__ import annotations
import math
import importlib
import logging
import re
from typing import Dict, List, Optional

import cimgraph.loaders.cypher as cypher
from cimgraph.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cimgraph.models.model_parsers import add_to_graph, add_to_catalog, item_dump

from neo4j import GraphDatabase


_log = logging.getLogger(__name__)

class Neo4jConnection(ConnectionInterface):
    def __init__(self, connection_params, cim_profile:str):

        self.cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)
        self.connection_params = connection_params

    def connect(self):
        if not self.sparql_obj:
            url = self.connection_params.url
            
            