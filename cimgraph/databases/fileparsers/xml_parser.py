from __future__ import annotations

import logging
import re
from collections import defaultdict
from pathlib import Path

from cimprofiles.identity import Identity, read_identifier
from defusedxml.ElementTree import parse

from cimgraph.core import (get_cim_profile, get_iec61970_552, get_namespace, get_use_units,
                           get_validation_log_level)
from cimgraph.databases import ConnectionInterface, Graph, QueryResponse, reference_key
from cimgraph.databases.fileparsers.metadata import (ModelHeader, is_header_element,
                                                     parse_metadata, parse_model_header,
                                                     resolve_part_paths, use_model_scope)

_log = logging.getLogger(__name__)


class XMLFile(ConnectionInterface):

    def __init__(self, filename:str|list[str]=None, namespaces:dict=None,
                 metadata:str=None):
        super().__init__()

        # A metadata graph (IEC 61970-552/-557) names the model's part files.
        # Resolve it into a list of part paths to load into one graph.
        self.metadata_graph = None
        if metadata is not None:
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
            self.model_headers = []
            # A missing or malformed file raises (FileNotFoundError, ParseError, or a
            # defusedxml error for entities): a partial model would look complete.
            for fname in filenames:
                tree = parse(fname)
                self.trees.append(tree)
                self.roots.append(tree.getroot())
                # Extract namespaces from this file's XML header and merge.
                # Note: 'rdf' is stored with curly braces for backward compat.
                for prefix, uri in self.extract_namespaces_from_header(fname).items():
                    if prefix == 'rdf':
                        self.rdf = '{' + uri + '}'
                    self.namespaces[prefix] = uri

            # Back-compat: single-file consumers still read self.tree / self.root.
            self.tree = self.trees[0] if self.trees else None
            self.root = self.roots[0] if self.roots else None
            # rdf:ID/rdf:about text -> object read with it, so edges in a later pass
            # get the identifier each object got under its own part's model scope
            self.object_index = {}
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
        return namespaces

    def disconnect(self):
        del self.tree
        del self.root
        del self.graph

    def execute(self, query_message: str) -> QueryResponse:
        pass

    def element_uri(self, element) -> str | None:
        """The rdf:about of an element, else its rdf:ID, else None."""
        uri = element.get(f'{self.rdf}about')
        if uri is None:
            uri = element.get(f'{self.rdf}ID')
        return uri

    @staticmethod
    def use_part_scope(root) -> ModelHeader:
        """Read a part file's header and set the model scope from it (use_model_scope)."""
        header = parse_model_header(root)
        use_model_scope(header)
        return header

    def get_object(self, mRID:str, graph = None) -> object:
        """
        The object whose rdf:about or rdf:ID is mRID, from any loaded file, or None.
        Both are compared in any of their forms ('urn:uuid:x', '#_x', '_x', 'x'), and
        UUIDs in any case. The object is read into self.graph (the graph argument is
        unused: it is the model's graph once create_new_graph has run).
        """
        key = reference_key(mRID)
        for root in self.roots:
            for element in root:
                uri = self.element_uri(element)
                if uri is not None and not is_header_element(element) and reference_key(uri) == key:
                    self.use_part_scope(root)   # the identifier create_new_graph gives it
                    return self.parse_nodes(element)
        return None

    def get_from_triple(self, subject:Identity, predicate:str, graph: Graph = None) -> list[object]:
        """Values of the subject's predicate in any loaded file: [] if none is written.
        References resolve only to objects create_new_graph has read."""
        results = []
        class_type = subject.__class__
        for root in self.roots:
            for element in root.findall(f'.//cim:{class_type.__name__}', self.namespaces):
                if read_identifier(class_type.__name__, self.element_uri(element)) != subject.identifier:
                    continue
                for value in element.findall(f'cim:{predicate}', self.namespaces):
                    results.append(self.parse_value(value, class_type, subject.identifier))
        return results

    def create_distributed_graph(self, area: object, graph: dict = None) -> Graph:
        # A file has no query to select one area's equipment, terminals and nodes, and
        # XMLFile.get_all_edges is a no-op, so the area hierarchy cannot be walked.
        raise NotImplementedError(
            f'XMLFile does not support distributed models (area {area.uri()}): load the file '
            'with RDFlibConnection(filename=...), which does, or build the model with '
            'distributed=False.')

    def create_new_graph(self, container: object, graph:dict = None) -> Graph:
        if graph is not None:
            self.graph = graph

        if not self.roots:
            _log.warning('No root element found in XML file')
            self.graph = defaultdict(lambda: defaultdict(dict))
            return self.graph

        # Add the model's container first, so pass 1 fills in that instance (as the
        # other connections do) instead of reading a second copy of it.
        if container is not None:
            self.add_to_graph(obj=container, graph=self.graph)

        # Pass 1: create all node objects across every part file, so edges in
        # later passes can resolve targets defined in any file. Each part's header
        # sets the model scope first (use_part_scope).
        self.model_headers = []
        for root in self.roots:
            self.model_headers.append(self.use_part_scope(root))
            for element in root:
                self.parse_nodes(element)

        # Pass 2: wire up all edges and attribute values across every part file.
        for root in self.roots:
            for element in root:
                self.parse_edges(element)

        return self.graph

    def parse_nodes(self, element:object) -> Identity:
        if is_header_element(element):
            return None  # file header, read by parse_model_header
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
            uri = self.element_uri(element)
            if uri is None:
                raise ValueError(f'{class_name} element has neither rdf:ID nor rdf:about')
            obj = self.create_object(self.graph, cim_class, uri)
            self.object_index[reference_key(uri)] = obj

        else:
            _log.log(self.log_level, f'{class_name} not in data profile')
        return obj

    # @time_func
    def parse_edges(self, element):

        # class_name = element.tag.split('{'+self.namespace+'}')[1]
        if is_header_element(element):
            return  # file header, read by parse_model_header
        class_name = element.tag.split('}')[1]

        if class_name in self.cim.__all__:
            cim_class = getattr(self.cim, class_name)
            uri = self.element_uri(element)
            identifier = self.object_index[reference_key(uri)].identifier
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

        edge_uri = sub_element.attrib.get(f'{self.rdf}resource')

        if edge_uri is not None:
            # A resource in a declared namespace is an enumeration value, else an object
            if (edge_uri.split('#')[0] + '#') not in self.namespaces.values():
                edge_object = self.object_index.get(reference_key(edge_uri))
                if edge_object is None:
                    _log.log(self.log_level, f'Object with ID {edge_uri} not found for {sub_tag}')
                    return None
                edge_class = type(edge_object)
                edge_uuid = edge_object.identifier
                value = self.create_edge(self.graph, cim_class, identifier, sub_tag, edge_class, edge_uuid)
                if association is None:    # undefined in the profile: no inverse to set
                    return value
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
                    edge_enum = self.profile_enum(enum_class, enum_value)
                    if association is None:
                        self.set_undefined_attribute(self.graph, cim_class, identifier, sub_tag,
                                                     enum_text)
                    elif edge_enum is None:
                        _log.log(self.log_level, f'{enum_class} is not an enumeration in the profile')
                    else:
                        value = setattr(self.graph[cim_class][identifier], association, edge_enum)
                except (IndexError, ValueError) as error:
                    _log.log(self.log_level, f'Could not parse enumeration {edge_uri}: {error}')
        else:
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
        # Lazy import avoids a circular dependency: cimgraph.utils imports
        # GraphModel, which imports ConnectionInterface from this package.
        from cimgraph.utils.write_xml import write_graph_xml

        write_graph_xml(graph, self.filename)
