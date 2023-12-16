from __future__ import annotations

import enum
import importlib
import json
import logging
import re
import uuid
from dataclasses import dataclass, field

from cimgraph.databases import ConnectionInterface

_log = logging.getLogger(__name__)


def new_mrid():
    mRID = str(uuid.uuid4())
    return mRID


def json_dump(value: object, cim: __package__, json_ld: bool = False) -> str:
    class_type = value.__class__
    if type(class_type) is enum.EnumMeta:
        result = str(value)
    elif class_type is list:
        result = []
        for item in value:
            result.append(json_dump(item, cim, json_ld))
    elif value is None:
        result = ''
    elif class_type.__name__ in cim.__all__:
        if json_ld:
            result = {'@type': {value.__class__.__name__}, '@id': {value.mRID}}
        else:
            result = value.mRID
    else:
        result = str(value)
    return result


@dataclass
class GraphModel:
    container: object
    connection: ConnectionInterface
    distributed: bool = field(default_factory=False)
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

    def add_to_graph(self, obj: object, graph: GraphModel = None) -> None:
        if graph is None:
            graph = self.graph
        if type(obj) not in graph.keys():
            graph[type(obj)] = {}
        if obj.mRID not in graph[type(obj)].keys():
            graph[type(obj)][obj.mRID] = obj

    def get_all_edges(self, cim_class: type, graph: dict[type, dict[str, object]] = None) -> None:
        if graph is None:
            graph = self.graph
        if cim_class in graph:
            self.connection.get_all_edges(graph, cim_class)
        else:
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in graph.')

    def get_edges_query(self, cim_class: type) -> str:
        if cim_class in self.graph:
            sparql_message = self.connection.get_edges_query(self.graph, cim_class)
        else:
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in catalog.')
            sparql_message = ''
        return sparql_message

    def pprint(self, cim_class: type, show_empty: bool = False, json_ld: bool = False) -> None:
        if cim_class in self.graph:
            json_dump = self.__dumps__(cim_class, show_empty, json_ld)
        else:
            json_dump = {}
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in graph.')
        print(json.dumps(json_dump, indent=4))

    def upload(self) -> None:
        self.connection.upload(self.graph)

    def __dumps__(self, cim_class: type, show_empty: bool = False, json_ld: bool = True) -> str:
        if cim_class in self.graph:
            mrid_list = list(self.graph[cim_class].keys())
            attribute_list = list(cim_class.__dataclass_fields__.keys())
            dump = {}

            for mrid in mrid_list:
                dump[mrid] = {}
                for attribute in attribute_list:
                    value = getattr(self.graph[cim_class][mrid], attribute)
                    if value is None or value == []:
                        if show_empty:
                            dump[mrid][attribute] = ''
                    else:
                        result = json_dump(value=value, cim=self.connection.cim, json_ld=json_ld)
                        dump[mrid][attribute] = str(result)

        else:
            dump = {}
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in catalog.')

        return dump
