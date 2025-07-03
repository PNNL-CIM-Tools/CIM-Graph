import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from rdflib import Graph as RDFGraph
from rdflib import Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import RDF, SH

_log = logging.getLogger(__name__)

# Catalog-specific namespace
CAT = Namespace('http://gridappsd.org/catalog/')
TMPL = Namespace('http://gridappsd.org/template/')
EX = Namespace('http://gridappsd.org/export#')  # Reuse your existing namespace

@dataclass
class CatalogTemplateConfig:
    """Configuration for catalog template output"""
    output_key: str = None
    serialize_as: str = 'auto'
    unit_handling: str = 'value'
    include_if_null: bool = True
    required: bool = False
    use_template: Optional[str] = None
    order_by: Optional[str] = None
    reference_fields: List[str] = field(default_factory=lambda: ['mRID', 'name'])

@dataclass
class CatalogConfig:
    """Overall catalog configuration"""
    catalog_name: str
    catalog_description: str = ''
    output_format: str = 'json'
    root_element: str = 'catalog'
    target_class: str = None
    include_metadata: bool = True

@dataclass
class CatalogShape:
    """Parsed catalog shape definition"""
    target_class: type
    config: CatalogConfig
    property_templates: Dict[str, CatalogTemplateConfig] = field(default_factory=dict)

class SHACLCatalogProcessor:
    """Separate catalog processor - works alongside your existing SHACLExportFilter"""

    def __init__(self, shacl_catalog_file: str, cim_module: object):
        self.shacl_catalog_file = shacl_catalog_file
        self.cim_module = cim_module
        self.shacl_graph = RDFGraph()
        self.catalog_shapes: Dict[str, CatalogShape] = {}

        # Parse the catalog SHACL file
        self.shacl_graph.bind('cat', CAT)
        self.shacl_graph.bind('tmpl', TMPL)
        self.shacl_graph.bind('ex', EX)
        self.shacl_graph.parse(shacl_catalog_file, format='turtle')

        self._parse_catalog_shapes()

    def _parse_catalog_shapes(self):
        """Parse catalog shapes from SHACL file"""
        for shape_uri in self.shacl_graph.subjects(RDF.type, CAT.CatalogShape):
            catalog_shape = self._parse_single_catalog_shape(shape_uri)
            if catalog_shape:
                shape_name = str(shape_uri).split('#')[-1].split('/')[-1]
                self.catalog_shapes[shape_name] = catalog_shape

    def _parse_single_catalog_shape(self, shape_uri: URIRef) -> Optional[CatalogShape]:
        """Parse a single catalog shape"""
        # Get target class
        target_classes = list(self.shacl_graph.objects(shape_uri, SH.targetClass))
        if not target_classes:
            return None

        class_name = str(target_classes[0]).split('#')[-1]
        if class_name not in self.cim_module.__all__:
            _log.warning(f"Class {class_name} not found in CIM profile")
            return None

        target_class = getattr(self.cim_module, class_name)

        # Parse catalog configuration
        catalog_config = CatalogConfig(
            catalog_name=class_name + 'Catalog',
            target_class=class_name
        )

        # Look for catalog configuration block
        for prop, value in self.shacl_graph.predicate_objects(shape_uri):
            prop_name = str(prop).split('#')[-1].split('/')[-1]

            if prop_name == 'catalogName':
                catalog_config.catalog_name = str(value)
            elif prop_name == 'catalogDescription':
                catalog_config.catalog_description = str(value)
            elif prop_name == 'outputFormat':
                catalog_config.output_format = str(value)
            elif prop_name == 'rootElement':
                catalog_config.root_element = str(value)
            elif prop_name == 'includeMetadata':
                catalog_config.include_metadata = bool(value.value)

        # Parse property templates
        property_templates = {}
        for prop_shape in self.shacl_graph.objects(shape_uri, SH.property):
            template_config = self._parse_property_template(prop_shape)
            if template_config:
                # Get property name from path
                paths = list(self.shacl_graph.objects(prop_shape, SH.path))
                if paths:
                    attr_name = str(paths[0]).split('#')[-1].split('.')[-1]
                    property_templates[attr_name] = template_config

        return CatalogShape(
            target_class=target_class,
            config=catalog_config,
            property_templates=property_templates
        )

    def _parse_property_template(self, prop_shape: URIRef) -> Optional[CatalogTemplateConfig]:
        """Parse template configuration for a single property"""
        template_config = CatalogTemplateConfig()

        # Look for template configuration
        for prop, value in self.shacl_graph.predicate_objects(prop_shape):
            prop_name = str(prop).split('#')[-1].split('/')[-1]

            if prop_name == 'outputKey':
                template_config.output_key = str(value)
            elif prop_name == 'serializeAs':
                template_config.serialize_as = str(value)
            elif prop_name == 'unitHandling':
                template_config.unit_handling = str(value)
            elif prop_name == 'includeIfNull':
                template_config.include_if_null = bool(value.value)
            elif prop_name == 'required':
                template_config.required = bool(value.value)
            elif prop_name == 'useTemplate':
                template_config.use_template = str(value).split('#')[-1].split('/')[-1]
            elif prop_name == 'orderBy':
                template_config.order_by = str(value)
            elif prop_name == 'referenceFields':
                try:
                    fields_collection = Collection(self.shacl_graph, value)
                    template_config.reference_fields = [str(field) for field in fields_collection]
                except:
                    pass

        return template_config

    def create_catalog(self, graph_model: 'GraphModel',
                      catalog_shape_name: str,
                      format: str = None,
                      **kwargs) -> Union[dict, str]:
        """Create catalog using specified shape"""

        if catalog_shape_name not in self.catalog_shapes:
            available = list(self.catalog_shapes.keys())
            raise ValueError(f"Catalog shape '{catalog_shape_name}' not found. Available: {available}")

        catalog_shape = self.catalog_shapes[catalog_shape_name]
        output_format = format or catalog_shape.config.output_format

        if output_format.lower() == 'json':
            return self._create_json_catalog(graph_model, catalog_shape, **kwargs)
        elif output_format.lower() == 'xml':
            return self._create_xml_catalog(graph_model, catalog_shape, **kwargs)
        else:
            raise ValueError(f"Unsupported format: {output_format}")

    def _create_json_catalog(self, graph_model: 'GraphModel',
                           catalog_shape: CatalogShape,
                           **kwargs) -> dict:
        """Create JSON catalog"""

        # Get all objects of target class
        target_objects = graph_model.list_by_class(catalog_shape.target_class)

        catalog_data = {}

        # Add metadata if requested
        if catalog_shape.config.include_metadata:
            catalog_data['metadata'] = {
                'catalogName': catalog_shape.config.catalog_name,
                'catalogDescription': catalog_shape.config.catalog_description,
                'generatedAt': self._get_timestamp(),
                'objectCount': len(target_objects),
                'targetClass': catalog_shape.target_class.__name__
            }

        # Serialize objects
        equipment_list = []
        for obj in target_objects:
            serialized_obj = self._serialize_object(obj, catalog_shape, graph_model)
            equipment_list.append(serialized_obj)

        catalog_data['equipment'] = equipment_list

        # Wrap in root element
        return {catalog_shape.config.root_element: catalog_data}

    def _serialize_object(self, obj: Any, catalog_shape: CatalogShape,
                         graph_model: 'GraphModel') -> dict:
        """Serialize single object using catalog shape"""
        result = {}

        # Always include @type
        result['@type'] = obj.__class__.__name__

        # Process each field that has a template
        for field_name, template_config in catalog_shape.property_templates.items():
            if not hasattr(obj, field_name):
                continue

            field_value = getattr(obj, field_name)
            output_key = template_config.output_key or field_name

            serialized_value = self._serialize_field_value(
                field_value, template_config, catalog_shape, graph_model
            )

            if serialized_value is not None or template_config.include_if_null:
                result[output_key] = serialized_value

        return result

    def _serialize_field_value(self, value: Any, template_config: CatalogTemplateConfig,
                              catalog_shape: CatalogShape, graph_model: 'GraphModel') -> Any:
        """Serialize field value according to template config"""

        if value is None:
            return None

        # Handle unit quantities (your Pint integration)
        if hasattr(value, 'value') and hasattr(value, 'quantity'):
            if template_config.unit_handling == 'value':
                return str(value.value)
            elif template_config.unit_handling == 'valueWithUnit':
                return {
                    'value': value.value,
                    'unit': str(value.quantity.units)
                }

        # Handle different serialization types
        serialize_as = template_config.serialize_as

        if serialize_as == 'string':
            return str(value)

        elif serialize_as == 'enumString' and hasattr(value, '__class__'):
            if hasattr(value, 'name'):
                return f"{value.__class__.__name__}.{value.name}"
            return str(value)

        elif serialize_as == 'reference':
            if hasattr(value, 'identifier'):
                ref_obj = {}
                for field in template_config.reference_fields:
                    if hasattr(value, field):
                        if field == 'identifier' or field == 'mRID':
                            ref_obj[field] = str(getattr(value, field))
                        else:
                            ref_obj[field] = getattr(value, field)
                return ref_obj
            return str(value)

        elif serialize_as == 'nestedArray' and isinstance(value, list):
            result = []
            for item in value:
                if template_config.use_template:
                    # Use nested template
                    nested_shape = self.catalog_shapes.get(template_config.use_template)
                    if nested_shape:
                        serialized_item = self._serialize_object(item, nested_shape, graph_model)
                    else:
                        serialized_item = self._serialize_simple_object(item)
                else:
                    serialized_item = self._serialize_simple_object(item)
                result.append(serialized_item)

            # Apply ordering if specified
            if template_config.order_by:
                try:
                    result.sort(key=lambda x: x.get(template_config.order_by, 0))
                except:
                    pass

            return result

        elif serialize_as == 'nested':
            if template_config.use_template:
                nested_shape = self.catalog_shapes.get(template_config.use_template)
                if nested_shape:
                    return self._serialize_object(value, nested_shape, graph_model)
            return self._serialize_simple_object(value)

        # Default serialization
        return str(value)

    def _serialize_simple_object(self, obj: Any) -> Any:
        """Simple object serialization for objects without templates"""
        if hasattr(obj, 'identifier'):
            result = {
                '@type': obj.__class__.__name__,
                'mRID': str(obj.identifier)
            }
            if hasattr(obj, 'name') and getattr(obj, 'name'):
                result['name'] = getattr(obj, 'name')
            return result
        return str(obj)

    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()

    def list_available_catalogs(self) -> List[str]:
        """List available catalog shapes"""
        return list(self.catalog_shapes.keys())
