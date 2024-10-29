from __future__ import annotations

import enum
import json
import logging
from dataclasses import dataclass, field
from uuid import UUID, uuid4

from cimgraph.databases import ConnectionInterface

_log = logging.getLogger(__name__)

jsonld = dict['@id':str(UUID),'@type':str(type)]
Graph = dict[type, dict[UUID, object]]



def new_mrid():
    mRID = str(uuid4())
    return mRID


def json_dump(value: object,
              cim: __package__,
              json_ld: bool = False,
              use_names=False) -> str:
    class_type = value.__class__
    if type(class_type) is enum.EnumMeta:
        result = str(value)
    elif class_type is list:
        result = []
        for item in value:
            result.append(json_dump(item, cim, json_ld, use_names))
    elif value is None:
        result = ''
    elif class_type.__name__ in cim.__all__:
        if json_ld:
            result = {'@type': {value.__class__.__name__}, '@id': {value.mRID}}
        elif use_names:
            result = value.name
        else:
            result = value.mRID
    else:
        result = str(value)
    return result


def create_object(class_type:type, uri:str, graph:Graph = None) -> object:
    """
    Method for creating new objects and adding them to the graph
    Required Args:
        graph: an LPG graph from a GraphModel object
        class_type: a dataclass type, such as cim.ACLineSegment
        uri: the RDF ID or mRID of the object
    Returns:
        obj: a dataclass instance with the correct identifier
    """
    # Convert uri string to a uuid
    try:
        identifier = UUID(uri.strip('_').lower())
    except:
        _log.warning(f'URI {uri} for object {class_type.__name__} is not a valid UUID')
        identifier = uri

    if graph is None:
        graph = {}

    # Add class type to graph keys if not there
    if class_type not in graph:
        graph[class_type] = {}

    # Check if object exists in graph
    if identifier in graph[class_type]:
        obj = graph[class_type][identifier]

    # If not there, create a new object and add to graph
    else:
        obj = class_type()
        obj.uuid(uri = uri)
        graph[class_type][identifier] = obj

    return obj

@dataclass
class GraphModel:
    container: object
    connection: ConnectionInterface
    distributed: bool = field(default=False)
    graph: dict[type, dict[str, object]] = field(default_factory=dict)
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
            obj_class = eval(f'self.cim.{obj_class}')
            obj = create_object(obj_class, obj_id, graph)
            return obj
        else:
            # If it is not in the profile, log it as a missing class
            _log.warning(
                f'object class missing from data profile: {obj_class}')



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




    def pprint(self, cim_class: type, show_empty: bool = False,
               json_ld: bool = False, use_names: bool = False) -> None:
        if cim_class in self.graph:
            json_dump = self.__dumps__(cim_class, show_empty, json_ld, use_names)
        else:
            json_dump = {}
            _log.info(f'no instances of {cim_class.__name__} found in graph.')
        print(json.dumps(json_dump, indent=4))

    def upload(self) -> None:
        self.connection.upload(self.graph)

    def __dumps__(self,
                  cim_class: type,
                  show_empty: bool = False,
                  json_ld: bool = True,
                  use_names=False) -> str:
        if cim_class in self.graph:
            mrid_list = list(self.graph[cim_class].keys())
            attribute_list = list(cim_class.__dataclass_fields__.keys())
            dump = {}

            for uuid in mrid_list:
                mrid = str(uuid)
                dump[mrid] = {}
                for attribute in attribute_list:
                    value = getattr(self.graph[cim_class][uuid], attribute)
                    if value is None or value == []:
                        if show_empty:
                            dump[mrid][attribute] = ''
                    else:
                        result = json_dump(value=value,
                                           cim=self.connection.cim,
                                           json_ld=json_ld,
                                           use_names=use_names)
                        dump[mrid][attribute] = str(result)

        else:
            dump = {}
            _log.info(f'no instances of {cim_class.__name__} found in graph.')

        return dump
