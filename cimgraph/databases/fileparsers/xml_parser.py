from __future__ import annotations

import concurrent.futures
import importlib
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from uuid import UUID

from defusedxml.ElementTree import parse

from cimgraph.databases import (ConnectionInterface, ConnectionParameters,
                                Graph, QueryResponse)
from cimgraph.utils.timing import timing as time_func

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
        self.connect()

    def connect(self):
        # if not graph:
        if self.filename is not None:
            try:
                self.rdf = '''{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'''
                self.namespaces = {'cim': self.namespace, 'rdf': self.rdf}
                self.tree = parse(self.filename)
                self.root = self.tree.getroot()
                self.class_index = {}
                self.graph = {}
            except:
                _log.warning(f'File {self.filename} not found. Defaulting to empty network graph')
                self.filename = None

    def disconnect(self):
        del self.tree
        del self.root
        del self.graph

    def async_execute(self, query_message: str) -> QueryResponse:
        pass

    def get_object(self, mrid:str, graph = {}) -> object:
        for element in self.root:
            if mrid in element.get(f'{self.rdf}about'):
                obj = self.parse_nodes(element)
        return obj

    def get_from_triple(self, subject:object, predicate:str, graph: Graph = {}) -> list[object]:
        results = []
        class_type = subject.__class__
        elements = self.tree.findall(f'.//cim:{class_type.__name__}', self.namespaces)
        for element in elements:
            if subject.uri() in element.get(f'{self.rdf}about'):
                value = element.find(f'.//cim:{predicate}', self.namespaces)
                results.append(self.parse_value(value, class_type, subject.identifier))
        return results




    def create_distributed_graph(self, area: object, graph: dict = {}) -> Graph:
        _log.error('distributed models not supported for XML file read')


    @time_func
    def create_new_graph(self, container: object) -> Graph:

        for element in self.root:
            self.parse_nodes(element)

        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:

            futures = [executor.submit(self.parse_edges, element) for element in self.root]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]

        return self.graph

    # async def create_new_graph_async(self):
    #     for f in asyncio.as_completed([
    #             asyncio.to_thread(self.parse_nodes(element))
    #             for element in self.root]):
    #         await f

    #     for f in asyncio.as_completed([
    #             asyncio.to_thread(self.parse_edges(element))
    #             for element in self.root]):
    #         await f

    @time_func
    def parse_nodes(self, element:object, graph:Graph=None):
        if not graph:
            graph = self.graph

        # Iterate over the elements and create dataclass instances
        class_name = element.tag.split('{'+self.namespace+'}')[1]

        if class_name in self.cim.__all__:
            # print(class_name)
            cim_class = eval(f'self.cim.{class_name}')
            uri = element.get(f'{self.rdf}about')
            identifier = UUID(uri.strip('_').lower())
            uri = uri.split(':')[-1]  # Extract UUID from the full URI
            self.class_index[identifier] = cim_class
            obj = self.create_object(graph, cim_class, uri)
        else:
            _log.warning(f'{class_name} not in data profile')
        return obj

    @time_func
    def parse_edges(self, element):

        class_name = element.tag.split('{'+self.namespace+'}')[1]


        if class_name in self.cim.__all__:
            cim_class = eval(f'self.cim.{class_name}')
            uri = element.get(f'{self.rdf}about')

            identifier = UUID(uri.strip('_').lower())
            uri = uri.split(':')[-1]  # Extract UUID from the full URI
            obj = self.graph[cim_class][UUID(uri)]
            for sub_element in element:
                self.parse_value(sub_element, cim_class, identifier)

        else:
            _log.warning(f'{class_name} not in data profile')

    def parse_value(self, sub_element, cim_class, identifier):

        sub_tag = sub_element.tag.split('}')[-1]
        association = self.check_attribute(cim_class, sub_tag)
        try:
            edge_uri = sub_element.attrib[f'{self.rdf}resource'].split('uuid:')[-1]
        except:
            edge_uri = None

        if edge_uri is not None:
            if self.namespace not in edge_uri:
                # try:
                    edge_uuid = UUID(edge_uri.strip('_').lower())

                    try:
                        edge_class = self.class_index[edge_uuid]
                        value = self.create_edge(self.graph, cim_class, identifier, sub_tag, edge_class, edge_uri)
                        reverse = cim_class.__dataclass_fields__[association].metadata['inverse']
                        self.create_edge(self.graph, edge_class, edge_uuid, reverse,
                                            cim_class, self.graph[cim_class][identifier].uri())
                    except:
                        value = self.get_object(edge_uri)

                # except:
                #     _log.warning(f'unable to create object with uuid {edge_uri}')
            else:
                try:
                    enum_text = edge_uri.split(self.namespace)[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                    if association is not None:
                        value = setattr(self.graph[cim_class][identifier], association, edge_enum)
                except:
                    pass
        else:
            if association is not None:
                value = self.create_value(self.graph, cim_class, identifier, sub_tag, sub_element.text)
        return value
        # return graph

    def parse_node_query(self, graph: dict, query_output: dict) -> Graph:
        pass

    def get_edges_query(self, graph: Graph, cim_class: type) -> str:
        pass

    def get_all_edges(self, graph: Graph, cim_class: type) -> None:
        pass

    def get_all_attributes(self, graph: Graph, cim_class: type) -> None:
        pass

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: Graph, cim_class: type, expand_graph = True) -> None:
        pass



    def upload(self, graph):
        pass
