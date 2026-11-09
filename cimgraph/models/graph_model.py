from __future__ import annotations

import json
import logging
import math
from dataclasses import dataclass, field, fields, is_dataclass
from types import ModuleType
from typing import Iterator, TypeVar, cast
from uuid import UUID

from cimprofiles.identity import Identity
from cimprofiles.units import CIMUnit

from cimgraph.core.env_vars import DEFAULT_FREQUENCY_HZ, get_system_mva_base
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
    # Every create, modify and delete since the model was loaded (see incremental_builder)
    incrementals: dict[str, dict[type, dict]] = field(default_factory=new_differences)
    # Internal state, not constructor arguments
    _class_iter: dict[type, Iterator] = field(default_factory=dict, init=False, repr=False)
    _mrid_index: dict[str, Identity] = field(default_factory=dict, init=False, repr=False)
    _mrid_count: int = field(default=-1, init=False, repr=False)  # objects in graph when the index was built
    # System bases for per-unit conversion, filled by set_default_bases once self.cim and the graph are known
    base_power: CIMUnit = field(default=None)       # cim.ApparentPower
    base_frequency: CIMUnit = field(default=None)   # cim.Frequency
    # __queried_objects__: defaultdict[UUID] = field(default_factory=defaultdict)
    """
    Underlying root class for all knowledge graph models, inlcuding
    FeederModel, BusBranchModel, and NodeBreakerModel
    Required Args:
        container: a CIM container object inheriting from ConnectivityNodeContainer
        connection: a ConnectionInterface object, such as BlazegraphConnection
        distributed: a boolean to indicate if the graph is distributed
    Optional Args:
        base_power: system power base (cim.ApparentPower), default the graph's BasePower, else CIMG_SYSTEM_MVA_BASE or 100 MVA
        base_frequency: system frequency (cim.Frequency), default 60 Hz
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

    def set_default_bases(self) -> None:
        """Fill unset base_power/base_frequency once self.cim and self.graph
        are known (call it after the graph is loaded). base_power is the
        graph's BasePower.basePower (PSS/E SBASE, MATPOWER baseMVA), else
        CIMG_SYSTEM_MVA_BASE or 100 MVA. A model has one system base: several
        BasePower objects that disagree, or one that disagrees with an
        explicit base_power, raise rather than leave pu values on the wrong
        base. The CIMUnit classes are per profile, and a profile part may
        lack one (cim18gmdm has no Frequency); that base then stays None."""
        base_power_cls = getattr(self.cim, 'BasePower', None)
        graph_bases = []
        if base_power_cls is not None:
            graph_bases = [bp for bp in self.graph.get(base_power_cls, {}).values() if bp.basePower is not None]
        if self.base_power is None and graph_bases:
            self.base_power = graph_bases[0].basePower
        for base in graph_bases:
            if not math.isclose(base.basePower.to('VA'), self.base_power.to('VA')):
                raise ValueError(
                    f"BasePower {base.mRID!r} ({base.basePower.to('MVA')} MVA) disagrees with the "
                    f"model's system base ({self.base_power.to('MVA')} MVA): a model has one system base"
                )
        if self.base_power is None and hasattr(self.cim, 'ApparentPower'):
            self.base_power = self.cim.ApparentPower(get_system_mva_base(), 'MVA')
        if self.base_frequency is None and hasattr(self.cim, 'Frequency'):
            self.base_frequency = self.cim.Frequency(DEFAULT_FREQUENCY_HZ, 'Hz')

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
            self._mrid_count = _object_count(self.graph)
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

    def iter_by_class(self, cim_class:type[T]) -> Iterator[T]:
        '''Iterate through all nodes of a specific type with proper typing.'''
        return iter(self.graph.get(cim_class, {}).values())

    def first(self, cim_class:type[T]) -> T | None:
        '''The first object of the class (in list_by_class order, so the same object every
        time the same file is read: a quick sanity check), or None if there are none.
        Restarts the iteration that next() continues.'''
        self._class_iter[cim_class] = iter(self.list_by_class(cim_class))
        return self.next(cim_class)

    def next(self, cim_class:type[T]) -> T | None:
        '''
        The object after the one last returned by first() or next(), or None after the
        last one; the call after that starts over. Starts with first() if the class is
        not being iterated. Objects deleted during the iteration are skipped, objects
        added to the graph after first() are not returned. There is one iteration per
        class for the whole model, so use list_by_class for nested or concurrent loops.
        '''
        if cim_class not in self._class_iter:
            return self.first(cim_class)
        objects = self.graph.get(cim_class, {})
        for obj in self._class_iter[cim_class]:
            if objects.get(obj.identifier) is obj:
                return obj
        del self._class_iter[cim_class]
        return None


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
        if count != self._mrid_count:
            index = {}
            for objects in self.graph.values():
                for obj in objects.values():
                    _check_mrid_unique(index, obj)
                    _index_mrid(index, obj)
            self._mrid_index = index
            self._mrid_count = count
        return self._mrid_index

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
        '''Objects of the class whose attribute equals value (converted to the attribute's
        datatype, so '12.5' finds 12.5), or, for a list attribute, contains it. A number
        matches a unit attribute in its base SI unit. Use find_by_condition for partial
        matches.'''
        matching = []
        valid, attr_datatype, value = validate_attr_datatype(cim_class, attribute, value)
        if not valid:
            _log.warning(f'{attribute} with {value} should have datatype {attr_datatype}')
        for cim_object in self.graph.get(cim_class, {}).values():
            if _attribute_matches(getattr(cim_object, attribute), value):
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
        Create an instance of a dataclass from keyword arguments, add it to the graph,
        and record it in self.incrementals.

        Args:
            cim_class: The dataclass type to instantiate
            incremental_file: Write every difference recorded so far to this file
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

        # Add to graph, then point the other end of each given association at it
        self.add_to_graph(new_object)
        record_created(self.incrementals, new_object)
        for attribute, value in kwargs.items():
            sync_inverse_references(new_object, attribute, None, value, self.incrementals)
        self._write_incrementals(incremental_file)
        return new_object

    def from_incremental(self, filename:str, incremental_file:str=None) -> list[object]:
        '''
        Apply an RDF/XML difference file to the model: create, modify and delete its
        objects with create, modify and delete, so the model and self.incrementals are as
        if the changes had been made here. Nothing is changed if any difference does not
        fit the model (ValueError); see incremental_builder.apply_incremental.
        Returns the created and modified objects.
        '''
        if not filename.lower().endswith('.xml'):
            raise ValueError(f'{filename}: only RDF/XML difference files (.xml) can be read')
        changed = apply_incremental(self, read_incremental_xml(filename))
        self._write_incrementals(incremental_file)
        return changed


    def delete(self, obj:Identity, incremental_file:str=None) -> None:
        """
        Delete an object from a typed property graph dictionary and remove all references to it.

        Args:
            obj: The object to delete, or None to do nothing
            incremental_file: Write every difference recorded so far to this file

        Raises:
            TypeError: If obj is not a CIM object (e.g. a class such as cim.Terminal)
            ValueError: If obj is not in the graph
        """
        if obj is None:
            return
        if not isinstance(obj, Identity):
            raise TypeError(f'{obj!r} is not a CIM object')
        objects = self.graph.get(obj.__class__, {})
        if objects.get(obj.identifier) is not obj:
            raise ValueError(f'{obj.__class__.__name__} {obj.identifier} '
                             f'(name={getattr(obj, "name", None)!r}) is not in the graph')

        # Remove every reference to the object from the other end of its associations
        record_deleted(self.incrementals, obj)
        for attr_field in fields(obj):
            sync_inverse_references(obj, attr_field.name, getattr(obj, attr_field.name), None,
                                    self.incrementals)

        del objects[obj.identifier]
        self._write_incrementals(incremental_file)

    def modify(self, cim_object:Identity, attribute:str, value:any, incremental_file:str=None) -> None:
        """
        Set an attribute (validated and converted to its datatype), update the other end
        of an association, and record the change in self.incrementals. incremental_file:
        write every difference recorded so far to this file.
        """
        if not isinstance(cim_object, Identity):
            raise TypeError(f"{cim_object} is not a CIM-Graph dataclass")
        # Verify that class_type is in CIM profile
        cim_class = cim_object.__class__
        if cim_class.__name__ not in self.cim.__all__:
            raise TypeError(f"{cim_class.__name__} not in CIM profile")
        if attribute not in cim_class.__dataclass_fields__:
            raise TypeError(f"{cim_class.__name__}.{attribute} not in CIM profile")
        if value is None:
            if not cim_class.__dataclass_fields__[attribute].type.startswith('Optional'):
                raise TypeError(f'{cim_class.__name__}.{attribute} cannot be None')
        else:
            valid, attr_datatype, value = validate_attr_datatype(cim_class, attribute, value)
            if not valid:
                raise TypeError(f'{value!r} does not match datatype {attr_datatype} of {attribute}')

        # Set new value, and move the other end of an association
        current_value = getattr(cim_object, attribute)
        setattr(cim_object, attribute, value)
        record_change(self.incrementals, cim_object, attribute, current_value, value)
        sync_inverse_references(cim_object, attribute, current_value, value, self.incrementals)
        self._write_incrementals(incremental_file)

    def _write_incrementals(self, incremental_file: str | None) -> None:
        if incremental_file is not None:
            self.write_all_incrementals(incremental_file)

    def write_all_incrementals(self, incremental_file:str):
        """Write the differences of every create, modify and delete since the model was
        loaded: each attribute's value then (reverse) and now (forward)."""
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


def _attribute_matches(attribute_value: any, value: any) -> bool:
    if isinstance(attribute_value, list):
        return value in attribute_value
    if isinstance(attribute_value, CIMUnit) and isinstance(value, (int, float)):
        return float(attribute_value) == value
    return attribute_value == value


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
