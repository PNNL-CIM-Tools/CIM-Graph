from __future__ import annotations

import importlib
import logging
from uuid import UUID
from defusedxml.ElementTree import parse

from cimgraph.databases import ConnectionInterface, ConnectionParameters, QueryResponse


_log = logging.getLogger(__name__)


class XMLFile(ConnectionInterface):

    def __init__(self, connection_params: ConnectionParameters):
        self.cim_profile = connection_params.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.filename = connection_params.filename
        self.connection_params = connection_params
        self.graph = None



    def connect(self):
        if not self.graph:
            if self.filename is not None:
                try:
                    self.rdf = '''{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'''
                    tree = parse(self.filename)
                    self.root = tree.getroot()
                    self.class_index = {}
                    self.graph = {}
                except:
                    _log.warning(f'File {self.filename} not found. Defaulting to empty network graph')
                    self.filename = None

    def disconnect(self):
        pass

    def execute(self, query_message: str) -> QueryResponse:
        pass
    
    def get_object(self, mrid:str, graph = {}) -> object:
        pass

    def create_new_graph(self, container: object) -> dict[type, dict[UUID, object]]:
        
        self.connect()
        # Iterate over the elements and create dataclass instances
        for element in self.root:

            class_name = element.tag.split('{'+self.namespace+'}')[1]
            cim_class = eval(f'self.cim.{class_name}')

            if class_name in self.cim.__all__:
                uri = element.get(f'{self.rdf}about')
                identifier = UUID(uri.strip('_').lower())
                uri = uri.split(':')[-1]  # Extract UUID from the full URI
                self.class_index[identifier] = cim_class
                obj = self.create_object(self.graph, cim_class, uri)

        for element in self.root:      
            class_name = element.tag.split('{'+self.namespace+'}')[1]
            cim_class = eval(f'self.cim.{class_name}')

            if class_name in self.cim.__all__:
                uri = element.get(f'{self.rdf}about')
                
                identifier = UUID(uri.strip('_').lower())
                uri = uri.split(':')[-1]  # Extract UUID from the full URI
                
                obj = self.graph[cim_class][UUID(uri)]
                for sub_element in element:
                    sub_tag = sub_element.tag.split('}')[-1]
                    association = self.check_attribute(cim_class, sub_tag)
                    try:
                        edge_uri = sub_element.attrib[f'{self.rdf}resource'].split('uuid:')[-1]
                    except:
                        edge_uri = None

                    if edge_uri is not None:
                        if self.namespace not in edge_uri:
                            edge_uuid = UUID(edge_uri.strip('_').lower())                  
                            edge_class = self.class_index[edge_uuid]
                            self.create_edge(self.graph, cim_class, identifier, sub_tag, edge_class, edge_uri)
                            reverse = cim_class.__dataclass_fields__[association].metadata['inverse']
                            self.create_edge(self.graph, edge_class, edge_uuid, reverse,
                                              cim_class, self.graph[cim_class][identifier].uri())
                        else:
                            enum_text = edge_uri.split(self.namespace)[1]
                            enum_text = enum_text.split('>')[0]
                            enum_class = enum_text.split('.')[0]
                            enum_value = enum_text.split('.')[1]
                            edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                            if association is not None:
                                setattr(self.graph[cim_class][identifier], association, edge_enum)
                    else:
                        if association is not None:
                            # setattr(obj, association, sub_element.text)
                            self.create_value(self.graph, cim_class, identifier, sub_tag, sub_element.text)

        return self.graph

    def parse_node_query(self, graph: dict, query_output: dict) -> dict[type, dict[UUID, object]]:

        pass

    def get_edges_query(self, graph: dict[type, dict[UUID, object]],
                        cim_class: type) -> str:
        pass

    def get_all_edges(self, graph: dict[type, dict[UUID, object]], cim_class: type) -> None:
        pass

    def get_all_attributes(self, graph: dict[type, dict[UUID, object]],
                           cim_class: type) -> None:
        pass

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: dict[type, dict[UUID, object]],
                          cim_class: type, expand_graph = True) -> None:
        pass
                   
             
   
    def upload(self, graph):
        pass


