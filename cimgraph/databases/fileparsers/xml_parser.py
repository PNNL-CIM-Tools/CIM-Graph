from __future__ import annotations

import logging
import re
from collections import defaultdict
from pathlib import Path
from uuid import UUID

from defusedxml.ElementTree import parse

from cimgraph.core import (get_cim_profile, get_iec61970_552, get_namespace,
                           get_use_units, get_validation_log_level)
from cimgraph.data_profile.identity import Identity
from cimgraph.databases import ConnectionInterface, Graph, QueryResponse

_log = logging.getLogger(__name__)


class XMLFile(ConnectionInterface):

    def __init__(self, filename:str|list[str]=None, namespaces:dict=None,
                 metadata:str=None):
        super().__init__()

        # A metadata graph (IEC 61970-552/-557) names the model's part files.
        # Resolve it into a list of part paths to load into one graph.
        self.metadata_graph = None
        if metadata is not None:
            from cimgraph.databases.fileparsers.metadata import (parse_metadata,
                                                                 resolve_part_paths)
            self.metadata_graph = parse_metadata(metadata)
            base_dir = Path(metadata).resolve().parent
            filename = [str(p) for p in resolve_part_paths(self.metadata_graph, base_dir)]

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
            # filename may be a single path or a list of part files (e.g. from a
            # metadata graph). Parse each into its own root; the two-pass graph
            # build then accumulates them all into one graph.
            filenames = [self.filename] if isinstance(self.filename, str) else list(self.filename)
            self.trees = []
            self.roots = []
            for fname in filenames:
                try:
                    tree = parse(fname)
                    self.trees.append(tree)
                    self.roots.append(tree.getroot())
                    # Extract namespaces from this file's XML header and merge.
                    # Note: 'rdf' is stored with curly braces for backward compat.
                    for prefix, uri in self.extract_namespaces_from_header(fname).items():
                        if prefix == 'rdf':
                            self.rdf = '{' + uri + '}'
                        self.namespaces[prefix] = uri
                except:
                    _log.warning(f'File {fname} not found. Skipping.')

            # Back-compat: single-file consumers still read self.tree / self.root.
            self.tree = self.trees[0] if self.trees else None
            self.root = self.roots[0] if self.roots else None
            if not self.roots:
                _log.warning('No files could be parsed. Defaulting to empty network graph')
            self.class_index = {}
            self.graph = defaultdict(lambda: defaultdict(dict))
        else:
            raise ValueError('filename or metadata must be specified')

    def extract_namespaces_from_header(self, filename:str=None) -> dict:
        """
        Extract namespace declarations from the XML root element.

        This method parses the xmlns: attributes from the root RDF element by reading
        the raw XML file and using regex to extract namespace declarations.

        Args:
            filename: file to read. Defaults to self.filename (single-file case).

        Returns:
            dict: Dictionary mapping namespace prefixes to their URIs WITHOUT curly braces.
                  This format is compatible with ElementTree find/findall operations.
                  For direct tag matching, add curly braces when needed.
                  e.g., {'cim': 'http://example.com#'}
        """
        if filename is None:
            filename = self.filename
        if filename is None:
            _log.warning('No filename specified, cannot extract namespaces')
            return {}

        namespaces = {}

        try:
            # Read the file to extract namespace declarations
            with open(filename, 'r', encoding='utf-8') as f:
                # Read only the first few KB to find the root element
                content = f.read(8192)  # Read first 8KB which should contain the root element

            # Pattern to match xmlns:prefix="uri" or xmlns="uri"
            # This regex captures both prefixed and default namespaces
            xmlns_pattern = r'xmlns(?::([a-zA-Z0-9_-]+))?=["\']([^"\']+)["\']'

            matches = re.finditer(xmlns_pattern, content)

            for match in matches:
                prefix = match.group(1)  # The namespace prefix (None for default namespace)
                uri = match.group(2)     # The namespace URI

                if prefix:
                    # Prefixed namespace like xmlns:cim="..."
                    # Store WITHOUT curly braces for ElementTree find/findall compatibility
                    namespaces[prefix] = uri
                    _log.debug(f'Found namespace: {prefix} -> {uri}')
                else:
                    # Default namespace like xmlns="..."
                    namespaces['default'] = uri
                    _log.debug(f'Found default namespace: {uri}')

            _log.info(f'Extracted {len(namespaces)} namespaces from XML header')

        except Exception as e:
            _log.error(f'Error extracting namespaces: {e}')

        return namespaces

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

        if not self.roots:
            _log.warning('No root element found in XML file')
            self.graph = defaultdict(lambda: defaultdict(dict))
            return self.graph

        # Pass 1: create all node objects across every part file, so edges in
        # later passes can resolve targets defined in any file.
        for root in self.roots:
            for element in root:
                self.parse_nodes(element)

        # Pass 2: wire up all edges and attribute values across every part file.
        for root in self.roots:
            for element in root:
                self.parse_edges(element)

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
                uri = uri.split(':')[-1]  # Extract UUID from the full URI

            elif 'ID' in str(element.attrib.keys()):
                uri = element.get(f'{self.rdf}ID')
                uri = uri.split(':')[-1]  # Extract UUID from the full URI

            else:
                _log.error(f'Unable to parse {element}. Elements must be rdf:ID or rdf:about')
                uri = element
            # try:
            #     identifier = UUID(uri.strip('_').lower())
            # except:
            #     _log.warning(f'Unable to parse URI. Check the IEC61970-301 serialization')

            # _log.warning(f'{cim_class.__name__}, {uri}')
            obj = self.create_object(self.graph, cim_class, uri)
            self.class_index[obj.uri()] = cim_class
            if uri != obj.uri():
                self.class_index[uri]=cim_class

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

        # Check for rdf:datatype attribute
        datatype_uri = sub_element.attrib.get(f'{self.rdf}datatype', None)

        try:
            edge_uri = sub_element.attrib[f'{self.rdf}resource'].split('uuid:')[-1].strip('#')
        except:
            edge_uri = None

        if edge_uri is not None:
            # ... existing edge handling code ...
            # (keep all your existing edge handling logic here)
            if (edge_uri.split('#')[0] + '#') not in self.namespaces.values():
                try:
                    edge_uuid = UUID(edge_uri.strip('#').strip('_').lower())
                except:
                    edge_uuid = edge_uri
                try:
                    edge_class = self.class_index[edge_uri]
                except:
                    _log.log(self.log_level, f'Object with ID {edge_uri} not found for {sub_tag}')
                    return None
                value = self.create_edge(self.graph, cim_class, identifier, sub_tag, edge_class, edge_uri)
                try:
                    reverse = cim_class.__dataclass_fields__[association].metadata['inverse']
                    self.create_edge(self.graph, edge_class, edge_uuid, reverse,
                                        cim_class, identifier)
                except Exception as e:
                    _log.log(self.log_level, f'Could not identify inverse for {cim_class.__name__} association {association}')
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
                # Pass datatype to create_value
                value = self.create_value(self.graph, cim_class, identifier, sub_tag,
                                        sub_element.text, datatype_uri)
        return value

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
        # Delegate to the canonical writer in cimgraph.utils.write_xml. Lazy
        # import avoids a circular dependency: write_xml imports GraphModel,
        # which imports ConnectionInterface from this package.
        from types import SimpleNamespace

        from cimgraph.utils.write_xml import write_xml

        # write_xml only needs network.graph, network.connection, and
        # network.list_by_class(cls) — shim those here for direct callers that
        # invoke connection.upload(graph) without going through GraphModel.
        shim = SimpleNamespace(
            graph=graph,
            connection=self,
            list_by_class=lambda cls: list(graph.get(cls, {}).values()),
        )
        write_xml(shim, self.filename)
