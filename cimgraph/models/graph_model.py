from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields, is_dataclass
from typing import TypeVar, Iterator, cast
from uuid import UUID

from cimgraph.data_profile.identity import Identity
from cimgraph.databases import ConnectionInterface
from cimgraph.models.difference_builder import new_obj_difference

_log = logging.getLogger(__name__)

jsonld = dict['@id':str(UUID),'@type':str(type)]
Graph = dict[type, dict[UUID, object]]
T = TypeVar('T')

@dataclass
class GraphModel(ABC):
    container: object
    connection: ConnectionInterface
    distributed: bool = field(default=False)
    graph: dict[type, dict[UUID, object]] = field(default_factory=dict)
    differences: dict[str, dict[UUID, any]] = field(default_factory=dict)
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
    """

    # -------------------------------------------------------------------------
    # Methods to add objects to GraphModel.graph
    # -------------------------------------------------------------------------

    def add_to_graph(self, obj: object, graph: dict[type, dict[UUID, object]] = None) -> None:
        if graph is None:
            graph = self.graph
        if type(obj) not in graph:
            graph[type(obj)] = {}
        if obj.identifier not in graph[type(obj)]:
            graph[type(obj)][obj.identifier] = obj

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

    def list_by_type(self, cim_class:type[T]) -> list[T]:
        '''Get all nodes of a specific type with proper typing.'''
        values = list(self.graph.get(cim_class, {}).values())
        return values

    def iter_by_type(self, cim_class):
        '''Iterate through all nodes of a specific type with proper typing.'''
        return iter(self.graph.get(cim_class, {}).values())

    def first(self, cim_class:type):
        '''Get first '''
        values = self.list_by_type(cim_class)
        if values:
            self.__
            return values[0]
        else:
            return []

    def next(self, cim_class:type[T]) -> object[T]:
        '''Get next'''


    # -------------------------------------------------------------------------
    # Methods to search GraphModel.graph
    # -------------------------------------------------------------------------

    def find_by_attribute(self, cim_class:type[T], attribute:str, value:any) -> list[T]:
        '''Searches the graph to find all object instances with matching value'''


    # -------------------------------------------------------------------------
    # Methods to modify GraphModel.graph via difference message
    # -------------------------------------------------------------------------

    def create(self, cim_class: type[T], **kwargs: any) -> object[T]:
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
        
        self.add_to_graph(new_object)

        new_obj_difference(new_object, self.differences)

        return new_object

    def delete(self, cim_class:type[T], uuid:UUID) -> None:
        '''
        Delete object from graph all references by other objects
        '''


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
