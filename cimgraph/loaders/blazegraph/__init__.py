import re

from cimgraph.loaders import (ConnectionInterface, ConnectionParameters,
                              Parameter, QueryResponse)
from cimgraph.loaders.blazegraph.blazegraph import BlazegraphConnection
from SPARQLWrapper import JSON, POST, SPARQLWrapper

# from cimgraph.loaders.blazegraph.query_parsers import query_parser, query_list_parser
