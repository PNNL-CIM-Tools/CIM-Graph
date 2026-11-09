from __future__ import annotations

import logging
from collections import defaultdict
from enum import Enum
from types import ModuleType
from uuid import UUID, uuid4

from cimprofiles.identity import Identity, as_uuid, normalize_identifier, read_identifier
from cimprofiles.merge import merge_namespaces
from cimprofiles.units import CIMUnit
from defusedxml.ElementTree import parse

from cimgraph.core.attribute_utils import (_same_value, field_properties, get_attr_datatype,
                                           get_attr_serialize, get_serialized_attributes,
                                           validate_attr_datatype)
from cimgraph.core.env_vars import get_namespace, get_use_units
from cimgraph.core.serialization import (RDF_NAMESPACE, RDF_XML_CLOSE, _prefix, profile_namespaces,
                                         property_to_xml, rdf_id_text, rdf_xml_identifiers,
                                         rdf_xml_open)
from cimgraph.databases import enum_from_iri

_log = logging.getLogger(__name__)

DM_NAMESPACE = 'http://iec.ch/2002/schema/CIM_difference_model#'
# The newer IEC 61970-552 difference model namespace, also accepted when reading
DM_NAMESPACE_552 = 'http://iec.ch/TC57/61970-552/DifferenceModel#'
NAMESPACES = {'rdf': RDF_NAMESPACE, 'dm': DM_NAMESPACE}
# The key of an object's class in a difference: a created object's forward difference
# and a deleted object's reverse difference have it, as rdf:type statements
RDF_TYPE = 'rdf:type'
INDENT = '  '


def _local_name(tag: str) -> str:
    return tag.split('}', 1)[-1]


def read_incremental_xml(filename) -> dict:
    """
    Read a difference file into {'forwardDifferences': {uri: {'Class.attribute': text}},
    'reverseDifferences': ...}. A reference or enumeration is its rdf:resource text, a
    repeated property is a list, and an object written as a typed element (created or
    deleted) has its class name under RDF_TYPE.
    """
    incremental = {
        'forwardDifferences': defaultdict(dict),
        'reverseDifferences': defaultdict(dict)
    }
    root = parse(filename)

    # Find the DifferenceModel element, falling back to the 552 namespace.
    # Use a local copy so the fallback doesn't change NAMESPACES.
    namespaces = dict(NAMESPACES)
    diff_model = root.find('.//dm:DifferenceModel', namespaces)
    if diff_model is None:
        namespaces['dm'] = DM_NAMESPACE_552
        diff_model = root.find('.//dm:DifferenceModel', namespaces)
    if diff_model is None:
        raise ValueError('Could not find DifferenceModel element')

    about = f'{{{RDF_NAMESPACE}}}about'
    resource = f'{{{RDF_NAMESPACE}}}resource'
    for diff_type in ['forwardDifferences', 'reverseDifferences']:
        diff_element = diff_model.find(f'dm:{diff_type}', namespaces)
        if diff_element is None:
            continue
        for description in diff_element:
            # The identifier without its '#', '_' or 'urn:uuid:' serialization prefix
            difference = incremental[diff_type][normalize_identifier(description.get(about))]
            class_name = _local_name(description.tag)
            if class_name != 'Description':
                difference[RDF_TYPE] = class_name
            for child in description:
                tag = _local_name(child.tag)
                value = child.get(resource, child.text)
                if tag not in difference:
                    difference[tag] = value
                elif isinstance(difference[tag], list):
                    difference[tag].append(value)
                else:
                    difference[tag] = [difference[tag], value]
    return incremental


# -------------------------------------------------------------------------
# Applying differences
# -------------------------------------------------------------------------

def apply_incremental(model, message: dict) -> list[Identity]:
    """
    Apply a difference (from read_incremental_xml) to a GraphModel through its create,
    modify and delete, so the graph, its inverse associations and model.incrementals are
    as if the changes had been made on the model. Objects are created first, then
    modified, then deleted. A list attribute loses its reverse items and gains its
    forward items; a single-valued one gets its forward value, or None if it only has a
    reverse value.

    Every difference is checked before any is applied: an unknown class, object,
    attribute or referenced object, or a value that does not fit its attribute, raises
    ValueError and the model is not changed. A reverse value that differs from the current
    value (the difference was made from another version of the model) is a warning.

    Returns the created and modified objects.
    """
    forward, reverse = message['forwardDifferences'], message['reverseDifferences']
    created = {uri: _created_class(model, uri, difference[RDF_TYPE])
               for uri, difference in forward.items() if RDF_TYPE in difference}
    objects = {}  # uri -> existing object, for every object a difference names
    deleted = []
    for uri, difference in reverse.items():
        if RDF_TYPE in difference:
            obj = _find_object(model, objects, uri)
            if type(obj).__name__ != difference[RDF_TYPE]:
                raise ValueError(f'The difference deletes {uri} as a {difference[RDF_TYPE]}, '
                                 f'but it is a {type(obj).__name__}')
            deleted.append(obj)

    changes = []  # (uri, attribute, forward values, reverse values)
    for uri in dict.fromkeys([*forward, *reverse]):
        if any(obj.uri() == uri for obj in deleted):
            continue  # its reverse difference is the deleted object's values
        cim_class = created[uri] if uri in created else type(_find_object(model, objects, uri))
        forward_values = forward.get(uri, {})
        reverse_values = {} if uri in created else reverse.get(uri, {})
        for name in dict.fromkeys([*forward_values, *reverse_values]):
            if name == RDF_TYPE:
                continue
            attribute = _field_name(cim_class, name)
            if attribute == 'identifier':
                continue  # rdf:about identifies the object
            changes.append((uri, attribute,
                            _values(model, objects, created, cim_class, attribute, forward_values.get(name)),
                            _values(model, objects, created, cim_class, attribute, reverse_values.get(name))))

    for uri, attribute, _, reverse_items in changes:
        if uri not in created:
            _warn_if_not_current(objects[uri], attribute, reverse_items)

    changed = []
    for uri, cim_class in created.items():
        literals = {attribute: _single(cim_class, attribute, forward_items)
                    for change_uri, attribute, forward_items, _ in changes
                    if change_uri == uri and not _is_association(cim_class, attribute)}
        objects[uri] = model.create(cim_class, identifier=uri, **literals)
        changed.append(objects[uri])
    for uri, attribute, forward_items, reverse_items in changes:
        obj = objects[uri]
        if uri in created and not _is_association(type(obj), attribute):
            continue  # set by create
        forward_items = [_resolved(objects, item) for item in forward_items]
        if 'list' in obj.__dataclass_fields__[attribute].type:
            reverse_items = [_resolved(objects, item) for item in reverse_items]
            value = [item for item in getattr(obj, attribute) if item not in reverse_items]
            value += [item for item in forward_items if item not in value]
        else:
            value = _single(type(obj), attribute, forward_items)
        model.modify(obj, attribute, value)
        if not any(obj is item for item in changed):
            changed.append(obj)
    for obj in deleted:
        model.delete(obj)
    return changed


class _Reference(str):
    """The URI of an object a difference refers to, resolved once objects are created."""


def _created_class(model, uri: str, class_name: str) -> type:
    cim_class = getattr(model.cim, class_name, None) if class_name in model.cim.__all__ else None
    if not (isinstance(cim_class, type) and issubclass(cim_class, Identity)):
        raise ValueError(f'The difference creates {uri} as a {class_name}, which is not a '
                         f'class in the profile')
    if _graph_object(model.graph, uri) is not None:
        raise ValueError(f'The difference creates {uri}, which is already in the model')
    return cim_class


def _graph_object(graph: dict[type, dict[UUID, object]], uri: str) -> Identity | None:
    identifier = as_uuid(uri)
    for cim_class, objects in graph.items():
        key = identifier if identifier is not None else read_identifier(cim_class.__name__, uri)
        if key in objects:
            return objects[key]
    return None


def _find_object(model, objects: dict, uri: str) -> Identity:
    """The object with this URI: from objects, the graph, else the database (added to the
    graph). Raises ValueError if there is none."""
    if uri not in objects:
        obj = _graph_object(model.graph, uri)
        if obj is None and model.connection is not None:
            obj = model.connection.get_object(mRID=uri, graph=model.graph)
        if obj is None:
            raise ValueError(f'The difference refers to {uri}, which is not in the model')
        objects[uri] = obj
    return objects[uri]


def _field_name(cim_class: type, name: str) -> str:
    """The field of a 'Class.attribute' property name. Raises ValueError if the name does
    not fit the class."""
    class_name, _, attribute = name.rpartition('.')
    if attribute not in cim_class.__dataclass_fields__:
        raise ValueError(f'{cim_class.__name__} has no attribute {name}')
    if class_name and class_name not in [parent.__name__ for parent in cim_class.__mro__]:
        raise ValueError(f'{cim_class.__name__} does not inherit from {class_name}')
    return attribute


def _is_association(cim_class: type, attribute: str) -> bool:
    return cim_class.__dataclass_fields__[attribute].metadata.get('type') == 'Association'


def _values(model, objects: dict, created: dict, cim_class: type, attribute: str,
            text: str | list[str] | None) -> list:
    """The values of a property's text (None for no property): references as _Reference,
    which must name a created or existing object, others converted to the datatype."""
    texts = [] if text is None else text if isinstance(text, list) else [text]
    if not _is_association(cim_class, attribute):
        return [_converted_value(model.cim, cim_class, attribute, item) for item in texts]
    references = []
    for item in texts:
        uri = normalize_identifier(item)
        if uri not in created:
            _find_object(model, objects, uri)
        references.append(_Reference(uri))
    return references


def _converted_value(cim: ModuleType, cim_class: type, attribute: str, text: str) -> object:
    """
    A literal or enumeration (its rdf:resource IRI) as the attribute's datatype. A number
    of a unit attribute is the unit's base SI value, as the writers write it, and is a
    CIMUnit if CIMG_USE_UNITS is set. Raises ValueError if the text does not fit.
    """
    datatypes = get_attr_datatype(cim_class, attribute)
    datatypes = [getattr(cim, name, None) for name in
                 (datatypes if isinstance(datatypes, list) else [datatypes])]
    for datatype in datatypes:
        if isinstance(datatype, type) and issubclass(datatype, Enum):
            member = enum_from_iri(cim, text, get_namespace())
            if not isinstance(member, datatype):
                raise ValueError(f'{cim_class.__name__}.{attribute} value {text!r} is not a '
                                 f'{datatype.__name__}')
            return member
    valid, attr_datatype, value = validate_attr_datatype(cim_class, attribute, text)
    if not valid:
        raise ValueError(f'{cim_class.__name__}.{attribute} value {text!r} should have '
                         f'datatype {attr_datatype}')
    if isinstance(value, float) and get_use_units():
        for datatype in datatypes:
            if isinstance(datatype, type) and issubclass(datatype, CIMUnit):
                return datatype(value)
    return value


def _single(cim_class: type, attribute: str, items: list) -> object:
    if len(items) > 1:
        raise ValueError(f'{cim_class.__name__}.{attribute} has one value, not {len(items)}')
    return items[0] if items else None


def _resolved(objects: dict, item: object) -> object:
    return objects[item] if isinstance(item, _Reference) else item


def _warn_if_not_current(obj: Identity, attribute: str, reverse_items: list) -> None:
    current = getattr(obj, attribute)
    current_items = current if isinstance(current, list) else [] if current is None else [current]
    current_uris = [_difference_value(item) for item in current_items]
    for item in reverse_items:
        expected = str(item) if isinstance(item, _Reference) else item
        if not any(_same_value(expected, value) for value in current_uris):
            _log.warning(f'{type(obj).__name__} {obj.uri()} {attribute} is {current!r}, '
                         f'not {expected!r} as the difference expects')


# -------------------------------------------------------------------------
# Recording differences. A difference model is two sets of statements: the forward
# differences are added and the reverse differences removed. differences[direction]
# [cim_class][uri][attribute] holds the attribute's value after the changes (forward) and
# before the first of them (reverse); an attribute changed back to its original value has
# no difference. Creating an object changes its RDF_TYPE from None to its class name and
# deleting it changes it back, so an object created and deleted has no differences.
# -------------------------------------------------------------------------

def new_differences() -> dict[str, dict[type, dict]]:
    return {'forwardDifferences': defaultdict(dict), 'reverseDifferences': defaultdict(dict)}


def record_difference(differences: dict, cim_class: type, uri: str, attribute: str,
                      old_value: any, new_value: any) -> None:
    """Record that attribute (a field name or RDF_TYPE) of the object changed from
    old_value to new_value, both as written in a difference (see _difference_value)."""
    forward = differences['forwardDifferences'].setdefault(cim_class, {}).setdefault(uri, {})
    reverse = differences['reverseDifferences'].setdefault(cim_class, {}).setdefault(uri, {})
    original = reverse.setdefault(attribute, old_value)
    if _same_value(original, new_value):
        forward.pop(attribute, None)
        del reverse[attribute]
    else:
        forward[attribute] = new_value
    if not forward and not reverse:
        for direction in differences.values():
            del direction[cim_class][uri]
            if not direction[cim_class]:
                del direction[cim_class]


def record_change(differences: dict, obj: Identity, attribute: str,
                  old_value: any, new_value: any) -> None:
    """
    Record that obj.attribute changed from old_value to new_value. Only serialized
    attributes are recorded: an association is written from one end, and a change to the
    other end is recorded on that one by sync_inverse_references.
    """
    if get_attr_serialize(obj.__class__, attribute):
        record_difference(differences, obj.__class__, obj.uri(), attribute,
                          _difference_value(old_value), _difference_value(new_value))


def record_created(differences: dict, obj: Identity) -> None:
    """Record a new object: its class and every serialized attribute that has a value."""
    record_difference(differences, obj.__class__, obj.uri(), RDF_TYPE, None, obj.__class__.__name__)
    for attribute in get_serialized_attributes(obj.__class__):
        record_change(differences, obj, attribute, None, getattr(obj, attribute))


def record_deleted(differences: dict, obj: Identity) -> None:
    """Record a deleted object: its class and every serialized attribute that has a value."""
    for attribute in get_serialized_attributes(obj.__class__):
        record_change(differences, obj, attribute, getattr(obj, attribute), None)
    record_difference(differences, obj.__class__, obj.uri(), RDF_TYPE, obj.__class__.__name__, None)


def _difference_value(value: any) -> any:
    """A referenced object is recorded by its URI, a list by a new list (so changes to the
    object's list don't change the difference), and other values as they are. An empty
    list is None: neither writes a statement."""
    if isinstance(value, Identity):
        return value.uri()
    if isinstance(value, list):
        return [_difference_value(item) for item in value] or None
    return value


# -------------------------------------------------------------------------
# Writing differences
# -------------------------------------------------------------------------

def _difference_row(cim_class: type, uri: str, difference: dict, other: dict,
                    namespaces: dict, rdf_resource: str) -> str:
    """
    The statements of one object's forward or reverse difference: a typed element if it
    creates or deletes the object, else an rdf:Description. A list writes only the items
    that are not also in the other direction's list. None writes no statement.
    """
    properties = []
    for attribute, value in difference.items():
        if attribute == RDF_TYPE:
            continue
        if isinstance(value, list):
            other_items = other.get(attribute) or []
            value = [item for item in value if item not in other_items]
        properties.extend(field_properties(cim_class, attribute, value))
    if difference.get(RDF_TYPE) is not None:
        # __namespace__ is a property that returns its class's namespace: read it without an object
        tag = f'{_prefix(namespaces, cim_class.__namespace__.fget(None))}:{cim_class.__name__}'
    elif properties:
        tag = 'rdf:Description'
    else:
        return ''
    # Difference models refer to the objects they change, so always use rdf:about
    row = INDENT*2 + f'<{tag} rdf:about="{rdf_resource}{rdf_id_text(uri)}">\n'
    for prop in properties:
        row += INDENT*2 + property_to_xml(prop, namespaces, rdf_resource)
    return row + INDENT*2 + f'</{tag}>\n'


def _difference_rows(differences: dict, others: dict, namespaces: dict, rdf_resource: str) -> str:
    rows = ''
    for cim_class, objects in differences.items():
        for uri, difference in objects.items():
            other = others.get(cim_class, {}).get(uri, {})
            rows += _difference_row(cim_class, uri, difference, other, namespaces, rdf_resource)
    return rows


def write_incremental(reverse: dict | None, forward: dict | None, filename: str) -> None:
    """Write forward and reverse differences ({cim_class: {uri: {attribute: value}}}, see
    record_difference) as an RDF/XML difference model."""
    forward = forward or {}
    reverse = reverse or {}
    namespaces = merge_namespaces(profile_namespaces(set(forward) | set(reverse)), {'dm': DM_NAMESPACE})
    _, rdf_resource = rdf_xml_identifiers()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(rdf_xml_open(namespaces))
        f.write(f'<dm:DifferenceModel rdf:about="{rdf_resource}{rdf_id_text(str(uuid4()))}">\n')
        f.write(INDENT + '<dm:forwardDifferences rdf:parseType="Statements">\n')
        f.write(_difference_rows(forward, reverse, namespaces, rdf_resource))
        f.write(INDENT + '</dm:forwardDifferences>\n')
        f.write(INDENT + '<dm:reverseDifferences rdf:parseType="Statements">\n')
        f.write(_difference_rows(reverse, forward, namespaces, rdf_resource))
        f.write(INDENT + '</dm:reverseDifferences>\n')
        f.write('</dm:DifferenceModel>\n')
        f.write(RDF_XML_CLOSE)


# -------------------------------------------------------------------------
# Inverse associations
# -------------------------------------------------------------------------

def _set_attribute(obj: Identity, attribute: str, value: any, differences: dict) -> None:
    record_change(differences, obj, attribute, getattr(obj, attribute), value)
    setattr(obj, attribute, value)


def clean_inverse_reference(related_obj: any, attr_name: str, obj_to_remove: any,
                            differences: dict) -> None:
    """
    Remove obj_to_remove from related_obj.attr_name: from the list, or clear the reference,
    and record the change in differences. A related value that is not a CIM object, or whose
    class has no attr_name in this profile (CIMTool profiles may keep only one end of an
    association), is left alone. A list is replaced by a new list, not changed in place, so
    a loop over the old list (for point in location.PositionPoints: network.delete(point))
    sees every item.
    """
    if not isinstance(related_obj, Identity) or attr_name not in related_obj.__dataclass_fields__:
        return
    related_value = getattr(related_obj, attr_name)
    if isinstance(related_value, list):
        if obj_to_remove in related_value:
            _set_attribute(related_obj, attr_name,
                           [item for item in related_value if item is not obj_to_remove], differences)
    elif related_value is obj_to_remove:
        _set_attribute(related_obj, attr_name, None, differences)


def add_inverse_reference(related_obj: any, attr_name: str, obj_to_add: Identity,
                          attribute: str, differences: dict) -> None:
    """
    Make related_obj.attr_name refer to obj_to_add, the inverse of obj_to_add.attribute
    referring to related_obj, and record the changes in differences. A single-valued end
    that referred to another object is moved, and that object's attribute no longer lists
    related_obj. Same skip and list rules as clean_inverse_reference.
    """
    if not isinstance(related_obj, Identity) or attr_name not in related_obj.__dataclass_fields__:
        return
    if 'list' in related_obj.__dataclass_fields__[attr_name].type:
        related_list = getattr(related_obj, attr_name)
        if obj_to_add not in related_list:
            _set_attribute(related_obj, attr_name, related_list + [obj_to_add], differences)
        return
    previous = getattr(related_obj, attr_name)
    if previous is not None and previous is not obj_to_add:
        clean_inverse_reference(previous, attribute, related_obj, differences)
    _set_attribute(related_obj, attr_name, obj_to_add, differences)


def sync_inverse_references(obj: Identity, attribute: str, old_value: any, new_value: any,
                            differences: dict) -> None:
    """
    Update the inverse end of association obj.attribute after it changed from old_value
    to new_value (each None, an object or a list of objects), and record the changes to
    the other objects in differences. No-op for attributes that are not associations
    with an inverse.
    """
    attr_field = obj.__dataclass_fields__[attribute]
    inverse = attr_field.metadata.get('inverse')
    if inverse is None:
        return
    inverse_attr = inverse.split('.')[1]
    old_objects = _as_list(old_value)
    new_objects = _as_list(new_value)
    for related in old_objects:
        if not any(related is new for new in new_objects):
            clean_inverse_reference(related, inverse_attr, obj, differences)
    for related in new_objects:
        add_inverse_reference(related, inverse_attr, obj, attribute, differences)


def _as_list(value: any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return list(value)
    return [value]
