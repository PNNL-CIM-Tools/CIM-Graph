from __future__ import annotations

import json
import logging
import re
from collections import defaultdict
from uuid import UUID

from cimprofiles.identity import model_authority_namespace
from cimprofiles.jsonld import document_prefixes, load_vocabulary_units, profile_jsonld

from cimgraph.core import get_allow_remote_context, set_model_scope
from cimgraph.core.attribute_utils import get_attr_datatype
from cimgraph.databases import ConnectionInterface, Graph, QueryResponse, reference_key
from cimgraph.databases.fileparsers.metadata import HEADER_CLASSES, ModelHeader

_log = logging.getLogger(__name__)

# An enumeration value: 'prefix:Enum.member' or a full IRI '...#Enum.member' (older
# cimgraph releases wrote '...#:Enum.member')
_ENUM_VALUE = re.compile(r'(?:[A-Za-z][\w.-]*:|.*#:?)([A-Za-z_]\w*)\.(\w+)')

DCAT_DATASET = 'http://www.w3.org/ns/dcat#Dataset'
DCT_CONFORMS_TO = 'http://purl.org/dc/terms/conformsTo'
DCT_DESCRIPTION = 'http://purl.org/dc/terms/description'
DCT_ISSUED = 'http://purl.org/dc/terms/issued'
DCAT_IS_VERSION_OF = 'http://www.w3.org/ns/dcat#isVersionOf'
HEADER_NAMESPACES = ('http://www.w3.org/ns/dcat#', 'http://purl.org/dc/terms/')


class JSONLDFile(ConnectionInterface):
    """
    Read CIM JSON-LD files (CGMES draft style, e.g. Nordic44) into a graph.

    - ``@context`` may be inline, a URL or a list. URLs resolve from the cimprofiles
      offline cache; others are fetched only with CIMG_ALLOW_REMOTE_CONTEXT=true.
    - Numbers are in the units of the vocabularies the file's ``dcat:Dataset`` header
      names in ``dct:conformsTo`` (e.g. CGMES Equipment: kV, MW). A file without one is
      read with the profile's default units vocabulary.
    - References are ``"urn:uuid:..."`` strings or ``{"@id": ...}`` objects.
    - Each file's ``dcat:Dataset`` header is read into ``model_headers``; its authority
      (``dcat:isVersionOf``) and description set the model scope, as ``md:FullModel``
      does for XMLFile.
    """

    def __init__(self, filename: str | list[str], namespaces: dict = None):
        super().__init__()
        self.filename = filename
        self.allow_fetch = get_allow_remote_context()

        self.namespaces = {}
        if namespaces is not None:
            self.namespaces.update(namespaces)

        self.connect()

    def connect(self):
        if self.filename is None:
            raise ValueError('filename must be specified')
        # filename may be one file or a list of files loaded into one graph. A missing
        # or malformed file raises: a partial model would look complete.
        filenames = [self.filename] if isinstance(self.filename, str) else list(self.filename)
        self.items = []
        self.model_headers = []
        self._file_items = []   # each file's items, read under its own header's model scope
        vocabularies = []
        for filename in filenames:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.extract_namespaces(data)
            items = data.get('@graph', [])
            self.items.extend(items)
            self._file_items.append(items)
            datasets = [item for item in items if DCAT_DATASET in self._types(item)]
            self.model_headers.append(self._model_header(datasets))
            vocabularies.extend(self._conforms_to(datasets) or self._default_vocabularies())
        # 'Class.attribute' -> pint unit its numbers are written in
        self.units = self._vocabulary_units(dict.fromkeys(vocabularies))
        # @id text -> object read with it, so references find their objects
        self.object_index = {}
        self.graph = defaultdict(lambda: defaultdict(dict))

    def extract_namespaces(self, data: dict) -> None:
        """Add the prefix -> namespace entries of the file's @context (inline or remote)."""
        context = {'@context': data.get('@context', {})}
        self.namespaces.update(document_prefixes(context, self.allow_fetch))
        _log.info(f'Extracted {len(self.namespaces)} namespaces from @context')

    def _types(self, item: dict) -> list[str]:
        """The full IRIs of an item's @type (one type or a list)."""
        types = item.get('@type', [])
        return [self._expand_curie(t) for t in (types if isinstance(types, list) else [types])]

    def _is_header(self, obj_type: str | list[str]) -> bool:
        """
        True for the DCAT/Dublin Core metadata nodes of a dataset header, and for the
        md:FullModel and cim:ModelAuthority header nodes older cimgraph releases wrote
        (not CIM objects).
        """
        types = obj_type if isinstance(obj_type, list) else [obj_type]
        return (any(self._expand_curie(t).startswith(HEADER_NAMESPACES) for t in types)
                or self._extract_class_name(obj_type) in HEADER_CLASSES)

    def _header_values(self, node: dict, iri: str) -> list[str]:
        """The values of one header property: strings, or the text of {"@id"} / {"@value"} objects."""
        values = []
        for key, value in node.items():
            if self._expand_curie(key) != iri:
                continue
            for target in value if isinstance(value, list) else [value]:
                if isinstance(target, dict):
                    target = target['@id'] if '@id' in target else target['@value']
                values.append(target)
        return values

    def _conforms_to(self, datasets: list[dict]) -> list[str]:
        """The dct:conformsTo IRIs of the dcat:Dataset header nodes."""
        return [self._expand_curie(iri) for dataset in datasets
                for iri in self._header_values(dataset, DCT_CONFORMS_TO)]

    def _model_header(self, datasets: list[dict]) -> ModelHeader:
        """
        A file's dcat:Dataset header as the ModelHeader the XML reader reads from
        md:FullModel: dct:issued (Model.created), dct:description (Model.description) and
        dcat:isVersionOf, the model authority (Model.modelingAuthoritySet).
        """
        header = ModelHeader()
        if not datasets:
            return header
        dataset = datasets[0]
        header.full_model_uuid = dataset['@id'].removeprefix('urn:uuid:')
        for attribute, iri in (('created', DCT_ISSUED), ('description', DCT_DESCRIPTION),
                               ('authority', DCAT_IS_VERSION_OF)):
            values = self._header_values(dataset, iri)
            if values:
                setattr(header, attribute, values[0])
        if header.authority is not None:
            header.authority_uuid = str(model_authority_namespace(header.authority))
        return header

    def _default_vocabularies(self) -> list[str]:
        """
        The profile's default units vocabularies, for a file whose header names none.
        A profile without published JSON-LD documents (a runtime merge) has none: its
        numbers are read in each CIMUnit's base unit.
        """
        try:
            documents = profile_jsonld(self.cim.__name__)
        except KeyError:
            return []
        return documents['conventions'][documents['default']]

    def _vocabulary_units(self, iris) -> dict[str, str]:
        """{'Class.attribute': pint unit} of the vocabularies; files must agree on each unit."""
        units = {}
        for iri in iris:
            for name, unit in load_vocabulary_units(iri, self.allow_fetch).items():
                if units.setdefault(name, unit) != unit:
                    raise ValueError(f'{name} is in {units[name]} in one file and {unit} in {iri}: '
                                     f'files loaded together must use the same units')
        return units

    def disconnect(self):
        del self.items
        del self.graph

    def execute(self, query_message: str) -> QueryResponse:
        pass

    def get_object(self, mRID: str, graph=None) -> object:
        obj = None
        for item in self.items:
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

        # First pass: create all nodes/objects, so references can find any of them. Each
        # file's header sets the model scope first (as in XMLFile), so UUIDs seeded from
        # its non-UUID identifiers use the authority that issued them.
        for header, items in zip(self.model_headers, self._file_items):
            if header.authority is not None:
                set_model_scope(header.authority, header.description or '')
            for item in items:
                self.parse_node(item)

        # Second pass: create all edges/relationships
        for item in self.items:
            self.parse_edges(item)

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
        if self._is_header(obj_type):
            return None

        # Extract class name from @type (e.g., "cim:ACLineSegment" -> "ACLineSegment")
        class_name = self._extract_class_name(obj_type)
        if class_name in self.cim.__all__:
            cim_class = getattr(self.cim, class_name)
            obj = self.create_object(self.graph, cim_class, obj_id)
            self.object_index[reference_key(obj_id)] = obj
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

        if not obj_id or not obj_type or self._is_header(obj_type):
            return

        class_name = self._extract_class_name(obj_type)
        if class_name not in self.cim.__all__:
            return

        cim_class = getattr(self.cim, class_name)
        identifier = self.object_index[reference_key(obj_id)].identifier

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
            value: a reference ("urn:uuid:..." or {"@id"}), a typed literal
                ({"@value", "@type"}), an enumeration value ("cim:PhaseCode.ABC"), a
                literal, or a list of these
            cim_class: The CIM class type
            identifier: The object identifier

        Returns:
            The parsed value
        """
        association = self.check_attribute(cim_class, attribute)
        if association is None:
            return None

        input_unit = self.units.get(attribute)
        if isinstance(value, list):
            for item in value:
                self.parse_value(attribute, item, cim_class, identifier)
        elif isinstance(value, dict) and '@id' in value:
            self._parse_reference(value['@id'], attribute, association, cim_class, identifier)
        elif isinstance(value, str) and self._is_association(cim_class, association):
            self._parse_reference(value, attribute, association, cim_class, identifier)
        elif isinstance(value, dict) and '@value' in value:
            datatype_uri = self._expand_curie(value.get('@type'))
            self.create_value(self.graph, cim_class, identifier, attribute,
                              str(value['@value']), datatype_uri, input_unit)
        elif isinstance(value, str) and self._parse_enum(value, association, cim_class, identifier):
            pass
        else:
            # A literal: a string, or a bool/int/float JSON value
            self.create_value(self.graph, cim_class, identifier, attribute, str(value),
                              input_unit=input_unit)

        return value

    @staticmethod
    def _is_association(cim_class: type, association: str) -> bool:
        return cim_class.__dataclass_fields__[association].metadata['type'] == 'Association'

    def _parse_reference(self, edge_id: str, attribute: str, association: str,
                         cim_class: type, identifier: UUID) -> None:
        """Set the association to the object with @id edge_id, and its inverse."""
        edge_object = self.object_index.get(reference_key(edge_id))
        if edge_object is None:
            _log.log(self.log_level, f'Object with ID {edge_id} not found for {attribute}')
            return
        edge_class = type(edge_object)
        self.create_edge(self.graph, cim_class, identifier, attribute,
                         edge_class, edge_object.identifier)
        reverse = cim_class.__dataclass_fields__[association].metadata.get('inverse')
        if reverse is not None:
            self.create_edge(self.graph, edge_class, edge_object.identifier, reverse,
                             cim_class, identifier)

    def _parse_enum(self, value: str, association: str, cim_class: type,
                    identifier: UUID) -> bool:
        """
        Set the attribute to the enumeration member value names, and return True, if value
        is 'prefix:Enum.member' (or a full IRI) and the attribute's datatype is that
        profile enumeration. Any other string (a name such as 'Line 1: 12.47kV', a
        timestamp) returns False, to be read as a literal.
        """
        match = _ENUM_VALUE.fullmatch(value)
        if match is None:
            return False
        enum_class, member = match.groups()
        if enum_class not in get_attr_datatype(cim_class, association):
            return False
        try:
            edge_enum = self.profile_enum(enum_class, member)
        except ValueError as error:
            _log.log(self.log_level, f'Could not parse enumeration {value}: {error}')
            return True
        if edge_enum is None:
            return False
        setattr(self.graph[cim_class][identifier], association, edge_enum)
        return True

    def _expand_curie(self, curie: str | None) -> str | None:
        """'cim:Voltage.kV' -> the full IRI, for a prefix declared in @context."""
        if curie is None:
            return None
        prefix, _, local = curie.partition(':')
        if local and prefix in self.namespaces:
            return self.namespaces[prefix] + local
        return curie

    def _extract_class_name(self, obj_type: str | list[str]) -> str | None:
        """
        Extract class name from @type value.

        Args:
            obj_type: The @type value (e.g., "cim:ACLineSegment"), or a list of types
                (header nodes: ["dcat:Dataset", ...]), of which the first is used

        Returns:
            Class name (e.g., "ACLineSegment") or None if extraction fails
        """
        if isinstance(obj_type, list):
            obj_type = obj_type[0] if obj_type else ''
        if ':' in obj_type:
            return obj_type.split(':')[-1]
        return obj_type if obj_type else None

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
