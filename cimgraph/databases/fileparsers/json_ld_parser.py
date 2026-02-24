from __future__ import annotations

import enum
import json
import logging
from collections import defaultdict
from uuid import UUID

from cimgraph.core import (get_cim_profile, get_iec61970_301, get_namespace,
                           get_validation_log_level)
from cimgraph.databases import ConnectionInterface, Graph, QueryResponse

_log = logging.getLogger(__name__)


class JSONLDFile(ConnectionInterface):

    def __init__(self, filename: str | list[str], namespaces: dict = None):
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

        self.namespaces = {}
        if namespaces is not None:
            self.namespaces.update(namespaces)

        self.connect()

    def connect(self):
        if self.filename is not None:
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)

                # Extract namespaces from @context
                self.extract_namespaces()

            except FileNotFoundError:
                _log.warning(f'File {self.filename} not found. Defaulting to empty network graph')
                self.data = None
            except json.JSONDecodeError as e:
                _log.error(f'Invalid JSON in {self.filename}: {e}')
                self.data = None

            self.class_index = {}
            self.graph = defaultdict(lambda: defaultdict(dict))
        else:
            raise ValueError('filename must be specified')

    def extract_namespaces(self) -> None:
        """
        Extract namespace declarations from the JSON-LD @context.

        Updates self.namespaces with prefix -> URI mappings from the @context.
        """
        if self.data is None:
            _log.warning('No data loaded, cannot extract namespaces')
            return

        context = self.data.get('@context', {})
        if isinstance(context, dict):
            for prefix, uri in context.items():
                if isinstance(uri, str) and not prefix.startswith('@'):
                    self.namespaces[prefix] = uri
                    _log.debug(f'Found namespace: {prefix} -> {uri}')

            _log.info(f'Extracted {len(self.namespaces)} namespaces from @context')
        else:
            _log.warning(f'@context is not a dictionary: {type(context)}')

    def disconnect(self):
        del self.data
        del self.graph

    def execute(self, query_message: str) -> QueryResponse:
        pass

    def get_object(self, mRID: str, graph=None) -> object:
        obj = None
        if self.data is None:
            return None

        graph_data = self.data.get('@graph', [])
        for item in graph_data:
            obj_id = item.get('@id', '')
            if mRID in obj_id:
                obj = self.parse_node(item)
        return obj

    def get_from_triple(self, subject: object, predicate: str, graph: Graph = None) -> list[object]:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        results = []
        # This would require searching through the JSON-LD data
        # Implementation depends on specific requirements
        return results

    def create_distributed_graph(self, area: object, graph: dict = None) -> Graph:
        _log.error('distributed models not supported for JSON-LD file read')
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        return graph

    def create_new_graph(self, container: object, graph: dict = None) -> Graph:
        if graph is not None:
            self.graph = graph

        if self.data is not None:
            graph_data = self.data.get('@graph', [])

            # First pass: create all nodes/objects
            for item in graph_data:
                self.parse_node(item)

            # Second pass: create all edges/relationships
            for item in graph_data:
                self.parse_edges(item)
        else:
            _log.warning('No data found in JSON-LD file')
            self.graph = defaultdict(lambda: defaultdict(dict))

        return self.graph

    def parse_node(self, item: dict) -> object:
        """
        Parse a JSON-LD object and create a CIM object instance.

        Args:
            item: A dictionary representing a JSON-LD object with @id and @type

        Returns:
            The created CIM object or None if parsing fails
        """
        obj = None
        obj_id = item.get('@id', '')
        obj_type = item.get('@type', '')

        if not obj_id or not obj_type:
            _log.error(f'Missing @id or @type in item: {item}')
            return None

        # Extract class name from @type (e.g., "cim:ACLineSegment" -> "ACLineSegment")
        class_name = self._extract_class_name(obj_type)
        if class_name is None:
            _log.log(self.log_level, f'Unable to extract class name from @type: {obj_type}')
            return None

        # Extract URI from @id (e.g., "urn:uuid:12345" -> "12345")
        uri = self._extract_uri(obj_id)

        if class_name in self.cim.__all__:
            cim_class = getattr(self.cim, class_name)
            obj = self.create_object(self.graph, cim_class, uri)

            # Store multiple variations of the URI for lookup
            normalized_uri = uri.strip('#').strip('_').lower()
            self.class_index[normalized_uri] = cim_class
            self.class_index[obj.uri()] = cim_class
            if uri != obj.uri():
                self.class_index[uri] = cim_class
        else:
            _log.log(self.log_level, f'{class_name} not in data profile')

        return obj

    def parse_edges(self, item: dict) -> None:
        """
        Parse relationships and attributes from a JSON-LD object.

        Args:
            item: A dictionary representing a JSON-LD object
        """
        obj_id = item.get('@id', '')
        obj_type = item.get('@type', '')

        if not obj_id or not obj_type:
            return

        class_name = self._extract_class_name(obj_type)
        if class_name not in self.cim.__all__:
            return

        cim_class = getattr(self.cim, class_name)
        uri = self._extract_uri(obj_id)

        try:
            identifier = UUID(uri.strip('#').strip('_').lower())
        except:
            identifier = uri

        if identifier not in self.graph[cim_class]:
            _log.warning(f'Object {identifier} not found in graph during edge parsing')
            return

        # Process all attributes except @id and @type
        for key, value in item.items():
            if key in ['@id', '@type']:
                continue

            # Extract attribute name (e.g., "cim:IdentifiedObject.name" -> "IdentifiedObject.name")
            attribute = self._extract_attribute_name(key)
            if attribute:
                self.parse_value(attribute, value, cim_class, identifier)

    def parse_value(self, attribute: str, value: any, cim_class: type, identifier: UUID) -> any:
        """
        Parse and set an attribute value on an object.

        Args:
            attribute: The attribute name (e.g., "IdentifiedObject.name")
            value: The value to set (can be a string, dict, or list)
            cim_class: The CIM class type
            identifier: The object identifier

        Returns:
            The parsed value
        """
        association = self.check_attribute(cim_class, attribute)
        if association is None:
            return None

        # Handle different value types
        if isinstance(value, dict):
            # This is a reference to another object
            edge_id = value.get('@id', '')
            if edge_id:
                edge_uri = self._extract_uri(edge_id)

                # Try multiple variations to find the class
                edge_class = self._lookup_class(edge_uri)

                if edge_class is None:
                    _log.log(self.log_level, f'Object with ID {edge_uri} not found for {attribute}')
                    return None

                try:
                    self.create_edge(self.graph, cim_class, identifier, attribute, edge_class, edge_uri)

                    # Create reverse edge if inverse relationship exists
                    try:
                        reverse = cim_class.__dataclass_fields__[association].metadata['inverse']
                        self.create_edge(self.graph, edge_class, edge_uri, reverse,
                                       cim_class, self.graph[cim_class][identifier].uri())
                    except (KeyError, AttributeError):
                        # No inverse relationship defined, which is normal for some attributes
                        pass
                    except Exception as e:
                        _log.log(self.log_level, f'Could not create inverse for {cim_class.__name__} association {association}: {e}')

                except Exception as e:
                    _log.error(f'Error creating edge for {attribute}: {e}')
        elif isinstance(value, str):
            # Check if it's an enum or a literal value
            if ':' in value and '.' in value:
                # Likely an enum (e.g., "cim:WindingConnection.D")
                try:
                    enum_text = value.split(':')[-1]
                    enum_class = enum_text.split('.')[0]
                    enum_value = enum_text.split('.')[1]
                    edge_enum = getattr(self.cim, enum_class)(enum_value)
                    setattr(self.graph[cim_class][identifier], association, edge_enum)
                except Exception as e:
                    _log.log(self.log_level, f'Failed to parse enum {value}: {e}')
            else:
                # It's a literal value
                self.create_value(self.graph, cim_class, identifier, attribute, value)
        elif isinstance(value, list):
            # Handle list of values
            for item in value:
                self.parse_value(attribute, item, cim_class, identifier)
        else:
            # Handle other primitive types (bool, int, float)
            self.create_value(self.graph, cim_class, identifier, attribute, str(value))

        return value

    def _extract_class_name(self, obj_type: str) -> str | None:
        """
        Extract class name from @type value.

        Args:
            obj_type: The @type value (e.g., "cim:ACLineSegment")

        Returns:
            Class name (e.g., "ACLineSegment") or None if extraction fails
        """
        if ':' in obj_type:
            return obj_type.split(':')[-1]
        return obj_type if obj_type else None

    def _extract_uri(self, obj_id: str) -> str:
        """
        Extract URI from @id value.

        Args:
            obj_id: The @id value (e.g., "urn:uuid:12345-67890")

        Returns:
            Extracted URI (e.g., "12345-67890")
        """
        # Remove common prefixes
        uri = obj_id
        if 'urn:uuid:' in uri:
            uri = uri.replace('urn:uuid:', '')
        elif 'uuid:' in uri:
            uri = uri.replace('uuid:', '')
        elif '#' in uri:
            uri = uri.split('#')[-1]

        return uri.strip('#').strip('_')

    def _lookup_class(self, uri: str) -> type | None:
        """
        Look up a class in the class_index, trying multiple URI variations.

        Args:
            uri: The URI to look up

        Returns:
            The CIM class type or None if not found
        """
        # Try the URI as provided
        if uri in self.class_index:
            return self.class_index[uri]

        # Try lowercase
        normalized = uri.lower()
        if normalized in self.class_index:
            return self.class_index[normalized]

        # Try uppercase
        upper = uri.upper()
        if upper in self.class_index:
            return self.class_index[upper]

        # Try with underscore prefix
        with_underscore = '_' + uri
        if with_underscore in self.class_index:
            return self.class_index[with_underscore]

        # Try lowercase with underscore
        with_underscore_lower = '_' + normalized
        if with_underscore_lower in self.class_index:
            return self.class_index[with_underscore_lower]

        return None

    def _extract_attribute_name(self, key: str) -> str | None:
        """
        Extract attribute name from JSON-LD key.

        Args:
            key: The key (e.g., "cim:IdentifiedObject.name")

        Returns:
            Attribute name (e.g., "IdentifiedObject.name") or None
        """
        if ':' in key:
            return key.split(':', 1)[-1]
        return key if key else None

    def parse_node_query(self, graph: dict, query_output: dict) -> Graph:
        pass

    def get_edges_query(self, graph: Graph, cim_class: type) -> str:
        pass

    def get_all_edges(self, graph: Graph, cim_class: type) -> None:
        pass

    def get_all_attributes(self, graph: Graph, cim_class: type) -> None:
        pass

    def edge_query_parser(self, query_output: QueryResponse,
                          graph: Graph, cim_class: type, expand_graph=True) -> None:
        pass

    def upload(self, graph):
        _log.warning('Upload to JSON-LD file not implemented. Use write_json_ld from cimgraph.utils instead.')
