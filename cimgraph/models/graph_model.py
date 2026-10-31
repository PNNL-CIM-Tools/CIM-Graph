from __future__ import annotations

import json
import logging
from collections import defaultdict
from dataclasses import dataclass, field, fields, is_dataclass
from types import ModuleType
from typing import Iterator, TypeVar, cast
from uuid import UUID

from cimprofiles.identity import Identity
from cimgraph.databases import ConnectionInterface, add_object_to_graph
from cimgraph.models.incremental_builder import *

_log = logging.getLogger(__name__)

jsonld = dict['@id':str(UUID),'@type':str(type)]
Graph = dict[type, dict[UUID, object]]
T = TypeVar('T')

@dataclass
class GraphModel():
    container: object
    connection: ConnectionInterface
    distributed: bool = field(default=False)
    graph: dict[type, dict[UUID, object]] = field(default_factory=dict)
    cim: ModuleType = field(default=None)
    incrementals: defaultdict[str, dict[str, any]] = field(default_factory=defaultdict)
    __class_iter__: defaultdict[type, iter] = field(default_factory=defaultdict)
    __mrid_index__: dict[str, Identity] = field(default_factory=dict)
    __mrid_count__: int = field(default=-1)  # objects in graph when the index was built
    # __queried_objects__: defaultdict[UUID] = field(default_factory=defaultdict)
    """
    Underlying root class for all knowledge graph models, inlcuding
    FeederModel, BusBranchModel, and NodeBreakerModel
    Required Args:
        container: a CIM container object inheriting from ConnectivityNodeContainer
        connection: a ConnectionInterface object, such as BlazegraphConnection
        distributed: a boolean to indicate if the graph is distributed
    Returns:
        none
    Methods:
        add_to_graph(object): adds a new CIM object to the knowledge graph
        get_all_edges(cim.ClassName): universal database query to expand graph by one edge
        graph[cim.ClassName]: access to graph dictionary sorted by class and mRID
        pprint(cim.ClassName): pretty-print method for showing graph of a class type
        get_edges_query(cim.ClassName): returns query text for debugging
        find_by_mRID(mRID): the object in the graph with that mRID
        list_identities(): identifier, mRID, name and class of every object
    """

    # -------------------------------------------------------------------------
    # Methods to add objects to GraphModel.graph
    # -------------------------------------------------------------------------

    def add_to_graph(self, obj: object, graph: dict[type, dict[UUID, object]] = None) -> None:
        if graph is None or graph is self.graph:
            # Kept current here so building a model never rescans the graph
            index = self.mrid_index()
            _check_mrid_unique(index, obj)
            add_object_to_graph(self.graph, obj)
            _index_mrid(index, obj)
            self.__mrid_count__ = _object_count(self.graph)
        else:
            add_object_to_graph(graph, obj)

    def add_jsonld_to_graph(self, json_ld: jsonld, graph = None) -> object:
        if type(json_ld) == str:
            json_ld = json.loads(json_ld)
        elif type(json_ld) == dict:
            pass
        else:
            raise TypeError('json_ld input must be string or dict')

        if graph is None:
            graph = self.graph

        obj_id = json_ld['@id']
        obj_class = json_ld['@type']

        # If equipment class is in data profile, add it to the graph also
        if obj_class in self.cim.__all__:
            obj_class = getattr(self.cim, obj_class)
            obj = self.connection.create_object(class_type=obj_class, uri=obj_id, graph=graph)
            return obj
        else:
            # If it is not in the profile, log it as a missing class
            _log.warning(
                f'object class missing from data profile: {obj_class}')

    # -------------------------------------------------------------------------
    # Methods to query databases
    # -------------------------------------------------------------------------

    def get_all_edges(self, cim_class: type,
                      graph: dict[type, dict[str, object]] = None) -> None:
        if graph is None:
            graph = self.graph
        if cim_class in graph:
            self.connection.get_all_edges(graph, cim_class)
        else:
            _log.info('no instances of ' + str(cim_class.__name__) +
                      ' found in graph.')

    def get_edges_query(self, cim_class: type) -> str:
        if cim_class in self.graph:
            sparql_message = self.connection.get_edges_query(
                self.graph, cim_class)
        else:
            _log.info('no instances of ' + str(cim_class.__name__) +
                      ' found in catalog.')
            sparql_message = ''
        return sparql_message

    def get_all_attributes(self, cim_class: type,
            graph: dict[type, dict[str, object]] = None) -> None:
        if graph is None:
            graph = self.graph
        if cim_class in graph:
            self.connection.get_all_attributes(graph, cim_class)
        else:
            _log.info('no instances of ' + str(cim_class.__name__) +
                      ' found in graph.')

    def get_object(self, mRID:str|UUID) -> object:
        if type(mRID) != str:
            mRID = str(mRID)
        obj = self.connection.get_object(mRID, self.graph)
        if obj is None:
            obj = self.connection.get_object(mRID.upper(), self.graph)
        if obj is None:
            obj = self.connection.get_object('_' + mRID, self.graph)
        if obj is None:
            obj = self.connection.get_object('_' + mRID.upper(), self.graph)
        if obj is None:
            _log.warning(f'Could not find any objects matching {mRID}')
        return obj

    def get_from_triple(self, subject:object, predicate:str, add_to_graph = True) -> list[object|str]:
        if add_to_graph:
            new_edges = self.connection.get_from_triple(subject, predicate, self.graph)
        else:
            new_edges = self.connection.get_from_triple(subject, predicate)
        return new_edges

    # -------------------------------------------------------------------------
    # Methods to retrieve objects from GraphModel.graph
    # -------------------------------------------------------------------------

    def list_by_class(self, cim_class:type[T]) -> list[T]:
        '''Get all nodes of a specific type with proper typing.'''
        values = list(self.graph.get(cim_class, {}).values())
        values = [cast(T, value) for value in values]
        values = sorted(values, key=lambda x: x.uri())
        return values

    def iter_by_class(self, cim_class) -> iter:
        '''Iterate through all nodes of a specific type with proper typing.'''
        return iter(self.graph.get(cim_class, {}).values())

    def first(self, cim_class:type):
        '''Get first '''
        values = self.list_by_class(cim_class)
        if values:
            self.__class_iter__[cim_class] = iter(values)
            return next(self.__class_iter__[cim_class])
        else:
            return []

    def next(self, cim_class:type[T]) -> object[T]:
        '''Get next'''
        if not self.__class_iter__[cim_class]:
            return self.first(cim_class)
        else:
            return next(self.__class_iter__[cim_class])


    # -------------------------------------------------------------------------
    # Methods to search GraphModel.graph
    # -------------------------------------------------------------------------

    def mrid_index(self) -> dict[str, Identity]:
        '''
        mRID -> object for every object in the graph that has an mRID. CIM 18 makes
        the mRID a freeform string unique within the model, so two different objects
        with the same mRID raise ValueError.

        add_to_graph keeps the index current. Objects that readers and queries put
        in the graph directly are picked up by a rebuild whenever the number of
        objects has changed, so an object's mRID must not be reassigned once it is
        in the graph (the same rule as for its identifier).
        '''
        count = _object_count(self.graph)
        if count != self.__mrid_count__:
            index = {}
            for objects in self.graph.values():
                for obj in objects.values():
                    _check_mrid_unique(index, obj)
                    _index_mrid(index, obj)
            self.__mrid_index__ = index
            self.__mrid_count__ = count
        return self.__mrid_index__

    def find_by_mRID(self, mRID: str) -> Identity | None:
        '''The object in the graph with this mRID, or None. Unlike get_object, this
        never queries the database.'''
        return self.mrid_index().get(mRID)

    def list_identities(self) -> list[dict[str, str | None]]:
        '''identifier, mRID, name and class of every object in the graph, e.g. to
        search a model. The mRID is listed separately because it need not be a UUID.'''
        return [
            {'identifier': str(obj.identifier), 'mRID': getattr(obj, 'mRID', None),
             'name': getattr(obj, 'name', None), 'class': cim_class.__name__}
            for cim_class, objects in self.graph.items()
            for obj in objects.values()
        ]

    def find_by_attribute(self, cim_class:type[T], attribute:str, value:any) -> list[T]:
        '''Searches the graph to find all object instances with matching value'''
        matching = []
        valid, attr_datatype, value = validate_attr_datatype(cim_class, attribute, value)
        if not valid:
            _log.warning(f'{attribute} with {value} should have datatype {attr_datatype}')
        for cim_object in self.graph.get(cim_class, {}).values():
            if str(value) in str(getattr(cim_object, attribute)):
                matching.append(cim_object)
        return matching

    def find_by_condition(self, cim_class:type[T], attribute:str, predicate:callable[[T], bool]) -> list[T]:
        """Find nodes using a custom lambda search criterion."""
        return [
            cim_object for cim_object in self.graph.get(cim_class, {}).values()
            if predicate(getattr(cim_object, attribute))
        ]

    # -------------------------------------------------------------------------
    # Methods to modify GraphModel.graph via difference message
    # -------------------------------------------------------------------------

    def create(self, cim_class: type, incremental_file: str = None, **kwargs: any) -> Identity:
        """
        Create an instance of a dataclass from keyword arguments.

        Args:
            cim_class: The dataclass type to instantiate
            **kwargs: Attribute names and values for the dataclass instance

        Returns:
            An instance of the specified dataclass type

        Raises:
            TypeError: If cim_class is not a dataclass
            TypeError: If kwargs contains attributes not in the dataclass
        """
        # Verify that class_type is a dataclass
        if not is_dataclass(cim_class):
            raise TypeError(f"{cim_class.__name__} is not a dataclass")
        # Verify that class_type is in CIM profile
        if cim_class.__name__ not in self.cim.__all__:
            raise TypeError(f"{cim_class.__name__} not in CIM profile")

        # Get the field names of the dataclass
        field_names = {field.name for field in fields(cim_class)}

        # Check if all kwargs keys are valid field names
        invalid_attrs = set(kwargs.keys()) - field_names
        if invalid_attrs:
            raise TypeError(f"Invalid attribute(s) for {cim_class.__name__}: {', '.join(invalid_attrs)}")

        # Create and return an instance of the dataclass
        new_object:Identity = cim_class(**kwargs)

        # Add to graph
        self.add_to_graph(new_object)

        # Add to list of incremental messages
        new_obj_incremental(new_object, self.incrementals)

        if incremental_file is not None:
            forward = {}
            forward[cim_class] = {}
            forward[cim_class][new_object.uri()] = self.incrementals['forwardDifferences'][cim_class][new_object.uri()]
            write_incremental(reverse=None, forward=forward, filename=incremental_file)

        return new_object

    def from_incremental(self, filename:str) -> list[object]:
        '''
        Create new object from incremental message
        '''
        if '.xml' in filename.lower():
            message = read_incremental_xml(filename)
        valid_message = validate_incremental(message, self.connection, self.graph)
        # TODO: Delete objects from incremental
        # TODO: Add objects from incremental
        modified = modify_from_incremental(valid_message, self.connection, self.graph)
        return modified


    def delete(self, obj:Identity) -> None:
        """
        Delete an object from a typed property graph dictionary and remove all references to it.

        Args:
            obj: The object to delete
        """

        if obj is None:
            return

        cim_class = obj.__class__

        # Step 1: Find and clean up all references to this object
        obj_id = obj.identifier
        if obj_id is None:
            obj_id = id(obj)  # Fallback to using object id if no mRID exists

        # First, iterate over fields of the object to find inverse references
        for field in fields(obj):
            # Check if this field has metadata about inverse relationships
            if field.metadata.get('type') == 'Association' and 'inverse' in field.metadata:
                # Get the value of this field
                value = getattr(obj, field.name)

                if value is not None:
                    try:
                        inverse_ref = field.metadata['inverse']
                        target_attr = inverse_ref.split('.')[1]

                        # Handle different cardinality cases
                        if isinstance(value, (list, set)):
                            # Many-to-many or one-to-many
                            for related_obj in value:
                                clean_inverse_reference(related_obj, target_attr, obj)
                        else:
                            # One-to-one or many-to-one
                            clean_inverse_reference(value, target_attr, obj)
                    except:
                        _log.warning(f'Error cleaning inverse reference for {field.name} in {cim_class.__name__}')


        if obj_id in self.graph[cim_class]:
            del self.graph[cim_class][obj_id]

    def modify(self, cim_object:Identity, attribute:str, value:any, incremental_file:str=None) -> None:
        if not isinstance(cim_object, Identity):
            raise TypeError(f"{cim_object} is not a CIM-Graph dataclass")
        # Verify that class_type is in CIM profile
        cim_class = cim_object.__class__
        if cim_class.__name__ not in self.cim.__all__:
            raise TypeError(f"{cim_class.__name__} not in CIM profile")
        if attribute not in cim_class.__dataclass_fields__:
            raise TypeError(f"{cim_class.__name__}.{attribute} not in CIM profile")
        cim_class = cim_object.__class__
        if not validate_attr_datatype(cim_class, attribute, value):
            raise TypeError(f'{value} does not match datatype of {attribute}')

        # Get old value for reverse difference
        base_value = self.incrementals['reverseDifferences'].get(cim_class, {}).get(cim_object.uri(), {}).get(attribute, {})
        if base_value != {}:
            old_value = base_value
        else:
            old_value = getattr(cim_object, attribute)

        # Set new value
        setattr(cim_object, attribute, value)
        # Create incremental
        modify_incremental(cim_object, attribute, old_value, value, self.incrementals)
        # Write single incremental to file if specificied
        if incremental_file is not None:
            forward = {}
            reverse = {}
            forward[cim_class] = {}
            reverse[cim_class] = {}
            forward[cim_class][cim_object.uri()] = self.incrementals['forwardDifferences'][cim_class][cim_object.uri()]
            reverse[cim_class][cim_object.uri()] = self.incrementals['reverseDifferences'][cim_class][cim_object.uri()]
            write_incremental(reverse=reverse, forward=forward, filename=incremental_file)


    def write_all_incrementals(self, incremental_file:str):
            write_incremental(reverse=self.incrementals['reverseDifferences'],
                            forward=self.incrementals['forwardDifferences'],
                             filename=incremental_file)




    # -------------------------------------------------------------------------
    # Methods to print GraphModel.graph
    # -------------------------------------------------------------------------

    def pprint(self, cim_class: type, show_empty: bool = False,
               json_ld: bool = False, use_names: bool = False) -> None:
        if cim_class in self.graph:
            json_dump = self.__dumps__(cim_class, show_empty, use_names)
        else:
            json_dump = {}
            _log.info(f'no instances of {cim_class.__name__} found in graph.')
        print(json_dump)

    def upload(self) -> None:
        # Lazy imports: utils.write_xml imports GraphModel, and XMLFile lives
        # under databases.fileparsers — keeping these local avoids the cycle.
        from cimgraph.databases.fileparsers import XMLFile
        if isinstance(self.connection, XMLFile):
            from cimgraph.utils.write_xml import write_xml
            write_xml(self, self.connection.filename)
            return
        self.connection.upload(self.graph)

    def __dumps__(self, cim_class: type, show_empty: bool = False,
                  use_names=False) -> json:
        dump = []
        for obj in self.graph.get(cim_class, {}).values():
            if isinstance(obj, Identity):
                dump.append(json.loads(obj.__str__(
                    show_empty=show_empty,
                    use_names=use_names)))
            else:
                _log.warning(f'Unknown object of type {type(obj)}')
        dump = json.dumps(dump, indent=4)
        return dump

    # -------------------------------------------------------------------------
    # Methods for SHACL validation and access control GraphModel.graph
    # -------------------------------------------------------------------------

    def export_with_shacl(self, shacl_file: str) -> 'GraphModel':
        """Export a filtered graph based on SHACL permissions"""
        # Imported here: cimgraph.shacl needs rdflib, the optional `rdflib` extra
        from cimgraph.shacl import SHACLExportFilter
        export_filter = SHACLExportFilter(shacl_file, self.cim)
        return export_filter.create_filtered_graph(self)

    def export_with_shacl_and_serialize(self, shacl_file: str, output_file: str,
                           format: str = 'xml') -> None:
        """Export and serialize filtered graph in one step"""
        filtered_graph = self.export_with_shacl(shacl_file)

        if format.lower() == 'xml':
            from cimgraph.utils import write_xml
            write_xml(filtered_graph, output_file)
        elif format.lower() in ['jsonld', 'json-ld']:
            from cimgraph.utils import write_json_ld
            write_json_ld(filtered_graph, output_file)
        else:
            raise ValueError(f"Unsupported format: {format}")


def _object_count(graph: Graph) -> int:
    return sum(len(objects) for objects in graph.values())


def _check_mrid_unique(index: dict[str, Identity], obj: object) -> None:
    mRID = getattr(obj, 'mRID', None)
    existing = index.get(mRID) if mRID is not None else None
    if existing is not None and existing is not obj:
        raise ValueError(
            f'mRID {mRID!r} of {type(obj).__name__} {getattr(obj, "name", None)!r} is already '
            f'used by {type(existing).__name__} {getattr(existing, "name", None)!r} '
            f'(an mRID must be unique within the model)')


def _index_mrid(index: dict[str, Identity], obj: object) -> None:
    mRID = getattr(obj, 'mRID', None)
    if mRID is not None:
        index[mRID] = obj
