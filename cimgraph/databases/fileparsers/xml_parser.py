from __future__ import annotations

import importlib
import logging
import math
from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

import cimgraph.queries.sparql as sparql
from cimgraph.databases import ConnectionInterface, QueryResponse

__xml_context__ = XmlContext()
__parser_config__ = ParserConfig(fail_on_unknown_attributes=True, fail_on_unknown_properties=True)

__xml_parser__ = XmlParser(config=__parser_config__, context=__xml_context__)
__config__ = SerializerConfig(xml_declaration=False, pretty_print=True)
__serializer__ = XmlSerializer(config=__config__)

_log = logging.getLogger(__name__)


class XMLParser(ConnectionInterface):

    def __init__(self, connection_params, cim_profile: str):
        self.cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)
        self.namespace = connection_params.namespace
        self.filename = connection_params.filename
        self.connection_parameters = connection_params
        self.read = False

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute(self, query_message: str) -> QueryResponse:
        pass

    def create_new_graph(self, container: object) -> dict[type, dict[str, object]]:
        graph = {}
        # Get all nodes, terminal, and equipment by
        sparql_message = sparql.get_all_nodes_from_container(container, self.namespace)
        query_output = self.execute(sparql_message)
        graph = self.new_graph_parser

        return graph


# def serialize_dataclass(obj: dataclass) -> str:
#     """
#     Serializes a dataclass that was created via xsdata to an xml string for
#     returning to a client.
#     """

#     return __serializer__.render(obj, ns_map=__ns_map__)

# def xml_to_dataclass(xml: str, type: Optional[Type] = None) -> dataclass:
#     """

#     Parse the xml passed and return result from loaded classes.

#     """

#     parsed = __xml_parser__.from_string(xml, type)

#     if isinstance(parsed, EndDevice):

#         parsed.lFDI = base64.b16encode(parsed.lFDI)

#     elif isinstance(parsed, EndDeviceList):

#         for ed in parsed.EndDevice:

#             ed.lFDI = base64.b16encode(ed.lFDI)

#     return parsed
