from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set
from uuid import UUID

import rdflib
from rdflib import Graph as RDFGraph
from rdflib import Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import RDF, SH

from cimgraph.data_profile.attribute_utils import (get_attr_datatype, get_attr_field_type,
                                                   get_attr_inverse, get_attr_uml_type)

_log = logging.getLogger(__name__)
EX = Namespace('http://gridappsd.org/export#')

@dataclass
class ConditionalExport:
    """Represents a conditional export constraint"""
    condition_path: str
    allowed_types: Set[type]
    condition_name: str = 'default'
    condition_type: str = 'direct'  # "direct" or "hasAnyRelatedOfType"
    related_path: Optional[str] = None  # For complex conditions

@dataclass
class TraversalRule:
    """Represents traversal permissions for a specific association"""
    allowed: bool = False
    max_depth: Optional[int] = None
@dataclass
class ExportPermissions:
    """Represents parsed SHACL export permissions for a single class"""
    class_type: type
    allowed_attributes: Set[str] = field(default_factory=set)
    allowed_associations: Set[str] = field(default_factory=set)
    traversal_rules: Dict[str, TraversalRule] = field(default_factory=dict)
    conditional_exports: List[ConditionalExport] = field(default_factory=list)

    def can_export_attribute(self, attr_name: str) -> bool:
        return attr_name in self.allowed_attributes

    def can_export_association(self, attr_name: str) -> bool:
        return attr_name in self.allowed_associations

    def can_traverse_relationship(self, attr_name: str, current_depth: int = 0) -> bool:
        rule = self.traversal_rules.get(attr_name)
        if not rule or not rule.allowed:
            return False
        if rule.max_depth is not None and current_depth >= rule.max_depth:
            return False
        return True

    def passes_conditional_constraints(self, obj: Any) -> bool:
        """Check if object passes all conditional export constraints"""
        if not self.conditional_exports:
            return True  # No constraints means always allowed

        for condition in self.conditional_exports:
            if not self._check_single_condition(obj, condition):
                _log.debug(f"Object {obj.__class__.__name__}({obj.identifier}) failed condition {condition.condition_name}")
                return False
        return True

    def _check_single_condition(self, obj: Any, condition: ConditionalExport) -> bool:
        """Check a single conditional constraint"""
        try:
            if condition.condition_type == 'direct':
                return self._check_direct_condition(obj, condition)
            elif condition.condition_type == 'hasAnyRelatedOfType':
                return self._check_has_any_related_condition(obj, condition)
            else:
                _log.warning(f"Unknown condition type: {condition.condition_type}")
                return True

        except Exception as e:
            _log.warning(f"Error checking condition {condition.condition_name}: {e}")
            return True  # Default to allowing if we can't check

    def _check_direct_condition(self, obj: Any, condition: ConditionalExport) -> bool:
        """Check direct condition (e.g., Terminal.ConductingEquipment must be a switch)"""
        # Parse the condition path (e.g., "Terminal.ConductingEquipment")
        path_parts = condition.condition_path.split('.')
        if len(path_parts) != 2:
            _log.warning(f"Invalid condition path: {condition.condition_path}")
            return True

        attr_name = path_parts[1]

        # Get the related object
        if not hasattr(obj, attr_name):
            return True  # If attribute doesn't exist, condition passes

        related_obj = getattr(obj, attr_name)
        if related_obj is None:
            return True  # If no related object, condition passes

        # Check if the related object's type is in the allowed types
        related_type = related_obj.__class__
        return related_type in condition.allowed_types

    def _check_has_any_related_condition(self, obj: Any, condition: ConditionalExport) -> bool:
        """Check if any related object through a path matches the condition"""
        # Parse the first condition path (e.g., "ConnectivityNode.Terminals")
        path_parts = condition.condition_path.split('.')
        if len(path_parts) != 2:
            return True

        first_attr = path_parts[1]  # e.g., "Terminals"

        # Get the collection of related objects
        if not hasattr(obj, first_attr):
            return False

        related_objects = getattr(obj, first_attr)
        if not related_objects:
            return False

        # Handle single object vs list
        if not isinstance(related_objects, list):
            related_objects = [related_objects]

        # Parse the second path (e.g., "Terminal.ConductingEquipment")
        if not condition.related_path:
            return False

        related_path_parts = condition.related_path.split('.')
        if len(related_path_parts) != 2:
            return False

        second_attr = related_path_parts[1]  # e.g., "ConductingEquipment"

        # Check if any of the related objects has a connection to allowed types
        for related_obj in related_objects:
            if not hasattr(related_obj, second_attr):
                continue

            final_obj = getattr(related_obj, second_attr)
            if final_obj is None:
                continue

            final_type = final_obj.__class__
            if final_type in condition.allowed_types:
                return True  # Found at least one matching connection

        return False  # No matching connections found

@dataclass
class SHACLExportFilter:
    """Parses SHACL shapes to determine export permissions and creates filtered graphs"""

    shacl_file: str
    cim_profile: Any
    shacl_graph: RDFGraph = field(init=False)
    permissions: Dict[type, ExportPermissions] = field(default_factory=dict, init=False)

    def __post_init__(self):
        self.shacl_graph = RDFGraph()
        self.shacl_graph.bind('ex', EX)
        self.shacl_graph.bind('sh', SH)
        self.shacl_graph.parse(self.shacl_file, format='turtle')
        self._parse_permissions()

    def _parse_permissions(self) -> None:
        """Parse SHACL shapes into export permissions"""
        for shape in self.shacl_graph.subjects(RDF.type, SH.NodeShape):
            self._parse_node_shape(shape)

    def _parse_node_shape(self, shape_uri: URIRef) -> None:
        """Parse a single NodeShape for export permissions"""
        target_classes = list(self.shacl_graph.objects(shape_uri, SH.targetClass))
        if not target_classes:
            return

        target_class_uri = target_classes[0]
        class_name = str(target_class_uri).split('#')[-1]

        if class_name not in self.cim_profile.__all__:
            _log.warning(f"Class {class_name} not found in CIM profile")
            return

        cim_class = getattr(self.cim_profile, class_name)
        permissions = ExportPermissions(class_type=cim_class)

        # Parse conditional export constraints
        for conditional in self.shacl_graph.objects(shape_uri, EX.conditionalExport):
            self._parse_conditional_export(conditional, permissions)

        # Parse property shapes
        for prop_shape in self.shacl_graph.objects(shape_uri, SH.property):
            self._parse_property_shape(prop_shape, permissions, cim_class)

        self.permissions[cim_class] = permissions
        _log.info(f"Parsed permissions for {class_name}: "
                 f"{len(permissions.allowed_attributes)} attributes, "
                 f"{len(permissions.allowed_associations)} associations, "
                 f"{len(permissions.conditional_exports)} conditions")

    def _parse_conditional_export(self, conditional_node: URIRef, permissions: ExportPermissions) -> None:
        """Parse conditional export constraints"""
        try:
            # Get condition path
            condition_paths = list(self.shacl_graph.objects(conditional_node, EX.conditionPath))
            if not condition_paths:
                return

            condition_path = str(condition_paths[0]).split('#')[-1]

            # Get condition type (default to "direct")
            condition_types = list(self.shacl_graph.objects(conditional_node, EX.conditionType))
            condition_type = 'direct'
            if condition_types:
                condition_type = str(condition_types[0]).split('#')[-1]

            # Get related path (for complex conditions)
            related_path = None
            related_paths = list(self.shacl_graph.objects(conditional_node, EX.relatedPath))
            if related_paths:
                related_path = str(related_paths[0]).split('#')[-1]

            # Get allowed types
            allowed_types_nodes = list(self.shacl_graph.objects(conditional_node, EX.allowedTypes))
            if not allowed_types_nodes:
                return

            # Parse the RDF list of allowed types
            allowed_types = set()
            try:
                type_collection = Collection(self.shacl_graph, allowed_types_nodes[0])
                for type_uri in type_collection:
                    type_name = str(type_uri).split('#')[-1]
                    if type_name in self.cim_profile.__all__:
                        cim_type = getattr(self.cim_profile, type_name)
                        allowed_types.add(cim_type)
            except Exception as e:
                _log.warning(f"Could not parse allowed types list: {e}")
                return

            # Get condition name (optional)
            condition_names = list(self.shacl_graph.objects(conditional_node, EX.condition))
            condition_name = str(condition_names[0]).split('#')[-1] if condition_names else 'unnamed'

            conditional_export = ConditionalExport(
                condition_path=condition_path,
                allowed_types=allowed_types,
                condition_name=condition_name,
                condition_type=condition_type,
                related_path=related_path
            )

            permissions.conditional_exports.append(conditional_export)
            _log.debug(f"Added conditional export: {condition_name} ({condition_type}) for {condition_path}")

        except Exception as e:
            _log.warning(f"Failed to parse conditional export: {e}")

    def _parse_property_shape(self, prop_shape: URIRef, permissions: ExportPermissions,
                             cim_class: type) -> None:
        """Parse a property shape for export permissions"""
        paths = list(self.shacl_graph.objects(prop_shape, SH.path))
        if not paths:
            return

        path_uri = paths[0]
        attr_name = str(path_uri).split('#')[-1].split('.')[-1]

        # Check if export is allowed
        export_allowed = list(self.shacl_graph.objects(prop_shape, EX.exportAllowed))
        if not (export_allowed and export_allowed[0].value):
            return

        try:
            uml_type = get_attr_uml_type(cim_class=cim_class, attribute=attr_name)

            if uml_type in ['Association', 'OfAggregate', 'AggregateOf']:
                permissions.allowed_associations.add(attr_name)

                # Parse traversal rules
                traverse_allowed = list(self.shacl_graph.objects(prop_shape, EX.traverseAllowed))
                if traverse_allowed and traverse_allowed[0].value:
                    max_depth = self._get_max_depth(prop_shape)
                    permissions.traversal_rules[attr_name] = TraversalRule(
                        allowed=True,
                        max_depth=max_depth
                    )
                else:
                    permissions.traversal_rules[attr_name] = TraversalRule(allowed=False)
            else:
                permissions.allowed_attributes.add(attr_name)

        except Exception as e:
            _log.warning(f"Could not determine type for {cim_class.__name__}.{attr_name}: {e}")
            permissions.allowed_attributes.add(attr_name)

    def _get_max_depth(self, prop_shape: URIRef) -> Optional[int]:
        """Extract maximum traversal depth if specified"""
        depths = list(self.shacl_graph.objects(prop_shape, EX.maxTraversalDepth))
        return int(depths[0].value) if depths else None

    def create_filtered_graph(self, source_graph: 'GraphModel') -> 'GraphModel':
        """Create a new GraphModel with only permitted objects and attributes"""
        from cimgraph.models import GraphModel

        filtered_graph = GraphModel(
            container=source_graph.container,
            connection=source_graph.connection,
            distributed=source_graph.distributed
        )
        filtered_graph.cim = source_graph.cim

        # Track objects and traversal paths
        created_objects: Dict[UUID, Any] = {}
        traversal_paths: Set[tuple] = set()

        # Find root classes (those with permissions and no conditional constraints)
        root_classes = []
        conditional_classes = []

        for cls, permissions in self.permissions.items():
            if cls in source_graph.graph and source_graph.graph[cls]:
                if permissions.conditional_exports:
                    conditional_classes.append(cls)
                else:
                    root_classes.append(cls)

        _log.info(f"Root classes: {[cls.__name__ for cls in root_classes]}")
        _log.info(f"Conditional classes: {[cls.__name__ for cls in conditional_classes]}")

        # Process root objects first
        for root_class in root_classes:
            _log.info(f"Processing {len(source_graph.graph[root_class])} objects of type {root_class.__name__}")
            for obj_id, source_obj in source_graph.graph[root_class].items():
                self._process_object_tree(
                    source_obj, source_graph, filtered_graph,
                    created_objects, traversal_paths, depth=0
                )

        # Then process conditional objects that meet their conditions
        for conditional_class in conditional_classes:
            permissions = self.permissions[conditional_class]
            valid_objects = []

            for obj_id, source_obj in source_graph.graph[conditional_class].items():
                if permissions.passes_conditional_constraints(source_obj):
                    valid_objects.append(source_obj)

            _log.info(f"Processing {len(valid_objects)} valid objects of type {conditional_class.__name__} "
                     f"(out of {len(source_graph.graph[conditional_class])} total)")

            for source_obj in valid_objects:
                self._process_object_tree(
                    source_obj, source_graph, filtered_graph,
                    created_objects, traversal_paths, depth=0
                )

        _log.info(f"Export complete. Created {len(created_objects)} objects total:")
        for cls, objs in filtered_graph.graph.items():
            _log.info(f"  {cls.__name__}: {len(objs)} objects")

        return filtered_graph

    def _process_object_tree(self, source_obj: Any, source_graph: 'GraphModel',
                            filtered_graph: 'GraphModel', created_objects: Dict[UUID, Any],
                            traversal_paths: Set[tuple], depth: int = 0) -> Optional[Any]:
        """Recursively process an object and its allowed associations"""

        obj_class = source_obj.__class__
        obj_id = source_obj.identifier

        # Check if we have permissions for this class
        if obj_class not in self.permissions:
            return None

        permissions = self.permissions[obj_class]

        # Check conditional constraints
        if not permissions.passes_conditional_constraints(source_obj):
            _log.debug(f"Object {obj_class.__name__}({obj_id}) failed conditional constraints")
            return None

        # If already created, return existing object
        if obj_id in created_objects:
            return created_objects[obj_id]

        # Create the filtered object
        filtered_obj = self._create_filtered_object(source_obj, permissions, created_objects)
        if not filtered_obj:
            return None

        filtered_graph.add_to_graph(filtered_obj)
        _log.debug(f"Created {obj_class.__name__} at depth {depth}")

        # Process allowed associations
        for assoc_name in permissions.allowed_associations:
            if not hasattr(source_obj, assoc_name):
                continue

            source_edge = getattr(source_obj, assoc_name)
            if source_edge is None:
                continue

            # Check if we can traverse this relationship at current depth
            if not permissions.can_traverse_relationship(assoc_name, depth):
                continue

            # Handle list vs single associations
            if isinstance(source_edge, list):
                for related_obj in source_edge:
                    if related_obj and hasattr(related_obj, 'identifier'):
                        self._build_association_recursive(
                            source_obj, filtered_obj, assoc_name, related_obj,
                            source_graph, filtered_graph, created_objects,
                            traversal_paths, depth
                        )
            else:
                if hasattr(source_edge, 'identifier'):
                    self._build_association_recursive(
                        source_obj, filtered_obj, assoc_name, source_edge,
                        source_graph, filtered_graph, created_objects,
                        traversal_paths, depth
                    )

        return filtered_obj

    def _build_association_recursive(self, source_obj: Any, filtered_obj: Any,
                                   attribute: str, target_source_obj: Any,
                                   source_graph: 'GraphModel', filtered_graph: 'GraphModel',
                                   created_objects: Dict[UUID, Any], traversal_paths: Set[tuple],
                                   depth: int) -> None:
        """Build association and recursively process target if needed"""

        source_id = source_obj.identifier
        target_id = target_source_obj.identifier
        path_key = (source_id, target_id, attribute)

        # Prevent infinite loops
        if path_key in traversal_paths:
            return

        traversal_paths.add(path_key)

        try:
            # Recursively process the target object
            target_filtered_obj = self._process_object_tree(
                target_source_obj, source_graph, filtered_graph,
                created_objects, traversal_paths, depth + 1
            )

            if target_filtered_obj is None:
                # Target doesn't meet conditions or no permissions - create stub
                target_class = target_source_obj.__class__
                target_filtered_obj = target_class(identifier=target_id)
                filtered_graph.add_to_graph(target_filtered_obj)

            # Set up associations
            self._set_association(filtered_obj, attribute, target_filtered_obj)
            self._set_inverse_association(filtered_obj, attribute, target_filtered_obj)

        finally:
            traversal_paths.discard(path_key)

    def _create_filtered_object(self, source_obj: Any, permissions: ExportPermissions,
                               created_objects: Dict[UUID, Any]) -> Optional[Any]:
        """Create a new object with only allowed attributes"""
        obj_class = source_obj.__class__
        obj_id = source_obj.identifier

        if obj_id in created_objects:
            return created_objects[obj_id]

        filtered_data = {'identifier': obj_id}

        # Copy allowed simple attributes
        for attr_name in permissions.allowed_attributes:
            if hasattr(source_obj, attr_name):
                attr_value = getattr(source_obj, attr_name)
                try:
                    uml_type = get_attr_uml_type(cim_class=obj_class, attribute=attr_name)
                    if uml_type not in ['Association', 'OfAggregate', 'AggregateOf']:
                        filtered_data[attr_name] = attr_value
                except:
                    if not hasattr(attr_value, 'identifier'):
                        filtered_data[attr_name] = attr_value

        try:
            filtered_obj = obj_class(**filtered_data)
            created_objects[obj_id] = filtered_obj
            return filtered_obj
        except Exception as e:
            _log.error(f"Failed to create filtered {obj_class.__name__}: {e}")
            return None

    def _set_association(self, source_obj: Any, attribute: str, target_obj: Any) -> None:
        """Set forward association"""
        try:
            field_type = get_attr_field_type(cim_class=source_obj.__class__, attribute=attribute)
            if field_type == 'list':
                current_list = getattr(source_obj, attribute, [])
                if target_obj not in current_list:
                    current_list.append(target_obj)
                    setattr(source_obj, attribute, current_list)
            else:
                setattr(source_obj, attribute, target_obj)
        except Exception as e:
            _log.debug(f"Could not set {source_obj.__class__.__name__}.{attribute}: {e}")

    def _set_inverse_association(self, source_obj: Any, attribute: str, target_obj: Any) -> None:
        """Set inverse association"""
        try:
            inverse = get_attr_inverse(cim_class=source_obj.__class__, attribute=attribute)
            if inverse and '.' in inverse:
                inverse_attr = inverse.split('.')[1]
                inverse_field_type = get_attr_field_type(
                    cim_class=target_obj.__class__, attribute=inverse_attr
                )

                if inverse_field_type == 'list':
                    inverse_list = getattr(target_obj, inverse_attr, [])
                    if source_obj not in inverse_list:
                        inverse_list.append(source_obj)
                        setattr(target_obj, inverse_attr, inverse_list)
                else:
                    setattr(target_obj, inverse_attr, source_obj)
        except Exception as e:
            _log.debug(f"Could not set inverse for {attribute}: {e}")
