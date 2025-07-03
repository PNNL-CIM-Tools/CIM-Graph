from __future__ import annotations

import concurrent.futures
import enum
import importlib
import logging
import os
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from uuid import UUID

from defusedxml.ElementTree import parse

from cimgraph.data_profile.identity import Identity
from cimgraph.data_profile.known_problem_classes import ClassesWithManytoMany
from cimgraph.databases import (ConnectionInterface, Graph, QueryResponse, get_cim_profile,
                                get_iec61970_301, get_namespace, get_validation_log_level)

# from cimgraph.utils.timing import timing as time_func

_log = logging.getLogger(__name__)

class XMLFile(ConnectionInterface):

    def __init__(self, filename:str|list[str], namespaces:dict=None):
        # clear cached env variables
        get_namespace.cache_clear()
        get_cim_profile.cache_clear()
        get_iec61970_301.cache_clear()
        get_validation_log_level.cache_clear()

        # retrieve env variables
        self.cim_profile, self.cim = get_cim_profile()
        self.namespace = get_namespace()
        self.iec61970_301 = get_iec61970_301()
        self.log_level = get_validation_log_level()
        self.filename = filename
        self.rdf = '''{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'''

        self.namespaces = {'cim': self.namespace, 'rdf': self.rdf}
        if namespaces is not None:
            self.namespaces.update(namespaces)
        # self.graph = None
        self.connect()

    def connect(self):
        # if not graph:
        if self.filename is not None:
            try:
                self.tree = parse(self.filename)
                self.root = self.tree.getroot()

            except:
                _log.warning(f'File {self.filename} not found. Defaulting to empty network graph')
                self.tree = None
                self.root = None
            self.class_index = {}
            self.graph = defaultdict(lambda: defaultdict(dict))
        else:
            raise ValueError('filename must be specified')


    def disconnect(self):
        del self.tree
        del self.root
        del self.graph

    def execute(self, query_message: str) -> QueryResponse:
        pass

    def get_object(self, mRID:str, graph = None) -> object:
        obj = None
        for element in self.root:
            if 'about' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}about')
            elif 'ID' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}ID')
            if mRID in uri:
                obj = self.parse_nodes(element)
        return obj

    def get_from_triple(self, subject:Identity, predicate:str, graph: Graph = None) -> list[object]:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        results = []
        class_type = subject.__class__
        elements = self.tree.findall(f'.//cim:{class_type.__name__}', self.namespaces)
        for element in elements:
            if 'about' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}about')
            elif 'ID' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}ID')
            if subject.uri() in uri:
                value = element.find(f'.//cim:{predicate}', self.namespaces)
                results.append(self.parse_value(value, class_type, subject.identifier))
        return results




    def create_distributed_graph(self, area: object, graph: dict = None) -> Graph:
        _log.error('distributed models not supported for XML file read')
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))


    def create_new_graph(self, container: object, graph:dict = None) -> Graph:
        if graph is not None:
            self.graph = graph
        if self.root is not None:
            for element in self.root:
                self.parse_nodes(element)

            for element in self.root:
                self.parse_edges(element)

            # with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:

            #     futures = [executor.submit(self.parse_edges, element) for element in self.root]
            #     results = [future.result() for future in concurrent.futures.as_completed(futures)]
        else:
            _log.warning('No root element found in XML file')
            self.graph = defaultdict(lambda: defaultdict(dict))
        return self.graph

    def parse_nodes(self, element:object) -> Identity:
        obj = None
        class_name = None
        try:
            # Iterate over the elements and create dataclass instances
            class_name = element.tag.split('{'+self.namespace+'}')[1]
        except:
            for namespace in self.namespaces.values():
                try:
                    class_name = element.tag.split('{'+namespace+'}')[1]
                except:
                    pass
        if class_name is None:
            _log.error(f'Unable to parse {element}. This may be caused by an invalid namespace')
            return None

        if class_name in self.cim.__all__:
            # print(class_name)
            cim_class = getattr(self.cim, class_name)
            if 'about' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}about')
            elif 'ID' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}ID')
            else:
                _log.error(f'Unable to parse {element}. Elements must be rdf:ID or rdf:about')

            uri = uri.split(':')[-1]  # Extract UUID from the full URI
            # try:
            #     identifier = UUID(uri.strip('_').lower())
            # except:
            #     _log.warning(f'Unable to parse URI. Check the IEC61970-301 serialization')


            obj = self.create_object(self.graph, cim_class, uri)
            self.class_index[obj.uri()] = cim_class
            if uri != obj.uri():
                self.class_index[uri]=obj.uri()

        else:
            _log.log(self.log_level, f'{class_name} not in data profile')
        return obj

    # @time_func
    def parse_edges(self, element):

        # class_name = element.tag.split('{'+self.namespace+'}')[1]
        class_name = element.tag.split('}')[1]


        if class_name in self.cim.__all__:
            cim_class = getattr(self.cim, class_name)
            if 'about' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}about')
            elif 'ID' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}ID')
            try:
                uri = uri.split(':')[-1]  # Extract UUID from the full URI
                identifier = UUID(uri.strip('#').strip('_').lower())
            except:
                # identifier = UUID(self.class_index[uri].strip('_').lower())
                identifier = uri
            obj = self.graph[cim_class][identifier]
            for sub_element in element:
                if 'Identity.identifier' not in sub_element.tag:
                    self.parse_value(sub_element, cim_class, identifier)

        else:
            _log.log(self.log_level, f'{class_name} not in data profile')

    def parse_value(self, sub_element, cim_class, identifier):
        value = None
        sub_tag = sub_element.tag.split('}')[-1]
        association = self.check_attribute(cim_class, sub_tag)
        try:
            edge_uri = sub_element.attrib[f'{self.rdf}resource'].split('uuid:')[-1].strip('#')
        except:
            edge_uri = None

        if edge_uri is not None:
            if (edge_uri.split('#')[0] + '#') not in self.namespaces.values():
                try:
                    edge_uuid = UUID(edge_uri.strip('#').strip('_').lower())
                except:
                    edge_uuid = edge_uri

                try:
                    edge_class = self.class_index[edge_uri]
                except:
                    _log.log(self.log_level, f'Object with ID {edge_uri} not found')
                    return None

                value = self.create_edge(self.graph, cim_class, identifier, sub_tag, edge_class, edge_uri)
                try:
                    reverse = cim_class.__dataclass_fields__[association].metadata['inverse']
                    self.create_edge(self.graph, edge_class, edge_uuid, reverse,
                                        cim_class, self.graph[cim_class][identifier].uri())
                except Exception as e:
                    _log.log(self.log_level, f'Could not identify inverse for {cim_class.__name__} association {association}')
                # except:
                #     value = self.get_object(edge_uri)

                # except:
                #     _log.warning(f'unable to create object with uuid {edge_uri}')
            else:
                try:
                    enum_text = edge_uri.split('#')[1]
                    enum_text = enum_text.split('>')[0]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    edge_enum = getattr(self.cim, enum_class)(enum_value)
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
        namespace = self.namespace
        iec61970_301 = self.iec61970_301
        classes_with_many_to_many = ClassesWithManytoMany()
        many_to_many = classes_with_many_to_many.attributes
        # Handling of formatting change between different 301 standard versions
        if int(iec61970_301) > 7:
            rdf_header = 'rdf:about="urn:uuid:'
            rdf_resource = 'urn:uuid:'
        else:
            rdf_header = 'rdf:ID="'
            rdf_resource = '#'
        f = open(self.filename, 'w', encoding='utf-8')
        header = '<?xml version="1.0" encoding="utf-8"?>\n'
        header += '<!-- un-comment this line to enable validation\n'
        header += '-->\n'
        header += f'<rdf:RDF xmlns:cim="{namespace}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
        header += '<!--\n'
        header += '-->\n'
        f.write(header)
        for root_class in list(graph.keys()):
            counter = 0
            for obj in graph[root_class].values():
                cim_class = obj.__class__
                header = f'<cim:{cim_class.__name__} {rdf_header}{obj.uri()}">\n'
                f.write(header)
                parent_classes = list(cim_class.__mro__)
                parent_classes.pop(len(parent_classes) - 1)
                for parent in parent_classes:
                    for attribute in parent.__annotations__.keys():
                        # Check if attribute is in data profile
                        attribute_type = cim_class.__dataclass_fields__[attribute].type
                        rdf = f'{parent.__name__}.{attribute}'
                        if attribute == 'identifier':
                            continue
                        # Upload attributes that are many-to-one or are known problem classes
                        if 'list' not in attribute_type or rdf in many_to_many:
                            edge_class = attribute_type.split('[')[1].split(']')[0]
                            edge = getattr(obj, attribute)
                            # Check if attribute is association to a class object
                            if edge_class in self.cim.__all__:
                                if edge is not None and edge != []:
                                    if type(edge.__class__) is enum.EnumMeta:
                                        resource = f'rdf:resource="{namespace}{str(edge)}"'
                                        row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                        f.write(row)
                                    elif type(edge) is str or type(edge) is bool or type(edge) is float:
                                        row = f'  <cim:{parent.__name__}.{attribute}>{str(edge)}</cim:{parent.__name__}'
                                        row += f'.{attribute}>\n'
                                        f.write(row)
                                    elif type(edge) is list:
                                        for value in edge:
                                            #TODO: lookup how to handle multiple rows of same value
                                            if type(value.__class__) is enum.EnumMeta:
                                                resource = f'rdf:resource="{namespace}{str(edge)}"'
                                                row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                                f.write(row)
                                            elif type(value) is str or type(value) is bool or type(value) is float:
                                                row = f'  <cim:{parent.__name__}.{attribute}>{str(value)}</cim:'
                                                row += f'{parent.__name__}.{attribute}>\n'
                                                f.write(row)
                                            else:
                                                resource = f'rdf:resource="{rdf_resource}{value.uri()}"'
                                                row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                                f.write(row)
                                    else:
                                        # try:
                                            resource = f'rdf:resource="{rdf_resource}{edge.uri()}"'
                                            row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                            f.write(row)
                                        # except:
                                        #     _log.warning(obj.__dict__)
                            else:
                                if edge is not None and edge != [] and rdf != 'Identity.identifier':
                                    row = f'  <cim:{parent.__name__}.{attribute}>{str(edge)}</cim:{parent.__name__}.'
                                    row += f'{attribute}>\n'
                                    f.write(row)
                tail = f'</cim:{cim_class.__name__}>\n'
                f.write(tail)
                counter = counter + 1
            _log.info(f'wrote {counter} {cim_class.__name__} objects')
        f.write('</rdf:RDF>')
        f.close()
