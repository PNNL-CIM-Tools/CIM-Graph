from __future__ import annotations

import logging
from dataclasses import dataclass, field

from rdflib import Graph, Namespace, URIRef

_log = logging.getLogger(__name__)


@dataclass
class ConnectionParameters:
    cim_profile: str = field(default_factory=str)
    url: str = field(default_factory=str)
    host: str = field(default_factory=str)
    port: str = field(default_factory=str)
    username: str = field(default_factory=str)
    password: str = field(default_factory=str)
    database: str = field(default_factory=str)
    namespace: str = field(default='http://iec.ch/TC57/CIM100#')
    iec61970_301: int = field(default=7)
    filename: str = field(default_factory=str)

    # parameters: List[Parameter] = field(default_factory=list)


@dataclass
class QueryResponse:
    response: str


@dataclass
class ConnectionInterface:
    connection_params: ConnectionParameters

    def connect(self):
        raise RuntimeError('Must have implemented connect in inherited class')

    def disconnect(self):
        raise RuntimeError('Must have implemented disconnect in inherited class')

    def execute(self, query: str) -> QueryResponse:
        raise RuntimeError('Must have implemented query in the inherited class')

    def create_edge(self, graph: dict[type, dict[str, object]],
                    cim_class: type, mRID: str, attribute: str,
                    edge_class: type, edge_mRID: str) -> None:
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if 'List' in attribute_type:
            obj_list = getattr(graph[cim_class][mRID], attribute)
            found = False
            for obj in obj_list:
                if obj.mRID == edge_mRID:
                    found = True
                    self.add_to_graph(obj, graph)
            if not found:
                edge_object = self.create_object(graph, edge_class, edge_mRID)
                obj_list.append(edge_object)
                setattr(graph[cim_class][mRID], attribute, obj_list)
        else:
            edge_object = self.create_object(graph, edge_class, edge_mRID)
            setattr(graph[cim_class][mRID], attribute, edge_object)

    def create_object(self, graph: dict[type, dict[str, object]],
                      class_type: type, mRID: str) -> object:

        if class_type not in graph.keys():
            graph[class_type] = {}

        if mRID in graph[class_type].keys():
            obj = graph[class_type][mRID]
        else:
            obj = class_type()
            setattr(obj, 'mRID', mRID)
            graph[class_type][mRID] = obj

        return obj

    def add_to_graph(self, obj: object,
                     graph: dict[type, dict[str, object]]) -> None:
        if type(obj) not in graph.keys():
            graph[type(obj)] = {}
        if obj.mRID not in graph[type(obj)].keys():
            graph[type(obj)][obj.mRID] = obj

    def create_assocation(self, graph: dict[type, dict[str, object]], attribute: str,
                          cim_class: type, mRID: str, attr_text: str,
                          edge_class: type, edge_mRID: str) -> None:
        
        # Old method to identify attributes using RDFS profile
        # This will be deprecated in a future release
        if self.data_profile is not None:
        
            if attribute[1] in cim_class.__dataclass_fields__:    #check if forward attribute
                self.create_edge(graph, cim_class, mRID, attribute[1], edge_class, edge_mRID)

            elif self.data_profile is not None:    # use data profile to look up reverse attribute
                attr_uri = URIRef(f'{self.namespace}{attr_text}')
                reverse_uri = self.data_profile.value(object=attr_uri,
                                                    predicate=self.reverse)
                try:
                    reverse_attribute = reverse_uri.split('#')[1].split('.')[1]    # split string
                except:
                    _log.warning(f'{cim_class.__name__} does not have attribute {attr_text}')

                self.create_edge(graph, cim_class, mRID, reverse_attribute, edge_class, edge_mRID)

            else:    # fallback to use basic logic to identify
                if attribute[0] in cim_class.__dataclass_fields__:    #check if first name is the attribute
                    self.create_edge(graph, cim_class, mRID, attribute[0], edge_class, edge_mRID)

                elif attribute[0] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                    self.create_edge(graph, cim_class, mRID, attribute[0] + 's', edge_class, edge_mRID)

                elif attribute[1] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                    self.create_edge(graph, cim_class, mRID, attribute[1] + 's',edge_class, edge_mRID)

                elif edge_class.__name__ in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                    self.create_edge(graph, cim_class, mRID, edge_class.__name__, edge_class, edge_mRID)

                elif edge_class.__name__ + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                    self.create_edge(graph, cim_class, mRID, edge_class.__name__ + 's', edge_class, edge_mRID)

                else:    #fallback: match class type until a suitable parent edge class is found
                    parsed = False
                    for node_attr in list(cim_class.__dataclass_fields__.keys()):
                        attr_str = cim_class.__dataclass_fields__[node_attr].type
                        edge_parent = attr_str.split('[')[1].split(']')[0]
                        if edge_parent in self.cim.__all__:
                            parent_class = eval(f'self.cim.{edge_parent}')
                            if issubclass(edge_class, parent_class):
                                self.create_edge(graph, cim_class, mRID, node_attr, edge_class, edge_mRID)
                                parsed = True
                                break
                    if not parsed:
                        _log.warning(
                            f'unable to find match for {attr_text} for {mRID}')
        
        # New method to build associations based on CIM-Tool profiles
        else:
            from_class = eval(f'self.cim.{attribute[0]}')
            to_class = eval(f'self.cim.{attribute[1]}')
            # inverse = from_class.__dataclass_fields__[]

            



from cimgraph.databases.blazegraph import BlazegraphConnection
from cimgraph.databases.graphdb import GraphDBConnection
from cimgraph.databases.gridappsd import GridappsdConnection
from cimgraph.databases.neo4j import Neo4jConnection
from cimgraph.databases.rdflib import RDFlibConnection
