from __future__ import annotations

from abc import ABC, abstractmethod
import logging

from dataclasses import dataclass, field, is_dataclass

from uuid import UUID

from rdflib import URIRef

_log = logging.getLogger(__name__)

Graph = dict[type, dict[UUID, object]]

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
    use_units: bool = field(default=False)

@dataclass
class QueryResponse:
    response: str


class ConnectionInterface(ABC):
    connection_params: ConnectionParameters
    
    @abstractmethod
    def connect(self):
        raise RuntimeError('Must have implemented connect in inherited class')

    @abstractmethod
    def disconnect(self):
        raise RuntimeError('Must have implemented disconnect in inherited class')

    @abstractmethod
    def execute(self, query: str) -> QueryResponse:
        raise RuntimeError('Must have implemented query in the inherited class')
    
    @abstractmethod
    def upload(self, graph: Graph) -> None:
        raise RuntimeError('Must have implemented query in the inherited class')

    @abstractmethod
    def get_all_edges(self, graph: Graph, cim_class: type) -> None:
        raise RuntimeError('Must have implemented query in the inherited class')
    
    @abstractmethod
    def get_all_attributes(self, graph: Graph, cim_class: type) -> None:
        raise RuntimeError('Must have implemented query in the inherited class')

    @abstractmethod
    def get_object(self, mRID:str, graph: Graph) -> None:
        raise RuntimeError('Must have implemented query in the inherited class')
    
    @abstractmethod
    def create_feeder_area(self, container: object, graph: dict = {}) -> Graph:
        raise RuntimeError('Must have implemented query in the inherited class')
    
    @abstractmethod
    def create_distributed_graph(self, area: object, graph: dict = {}) -> Graph:
        raise RuntimeError('Must have implemented query in the inherited class')



    def check_attribute(self, cim_class:type, attribute:str) -> str:
        attr_class = attribute.split('.')[0]
        attr_link = attribute.split('.')[1]
        association = None

        if attr_link in cim_class.__dataclass_fields__:
            association = attr_link
        else:
            from_class = eval(f'self.cim.{attr_class}')
            if attr_link not in from_class.__dataclass_fields__:
                _log.warning(f'Association {attr_link} missing from class {attr_class} in data profile')
                
            else:
                try:
                    reverse = from_class.__dataclass_fields__[attr_link].metadata['inverse']
                    reverse_assc = reverse.split('.')[1]
                    if reverse_assc in cim_class.__dataclass_fields__:
                        association = reverse_assc
                    else:
                        _log.warning(f'Association {reverse_assc} missing from class {attr_class} in data profile')
                except:
                    _log.warning(f'Unable to find inverse of {attribute} for {cim_class.__name__}')


        return association
    

    def create_value(self, graph: dict[type, dict[str, object]],
                    cim_class: type, identifier: UUID, attribute: str,
                    value: str) -> None:
        
        association = self.check_attribute(cim_class, attribute)
        if association is not None:
            attribute_type = cim_class.__dataclass_fields__[association].type
            if 'List' in attribute_type or 'list' in attribute_type:
                obj_list = getattr(graph[cim_class][identifier], association)
                if value not in str(obj_list):
                    obj_list.append(value)

            elif 'bool' in attribute_type:
                try:
                    setattr(graph[cim_class][identifier], association, bool(value))
                except:
                    _log.warning(f'{value} for {cim_class.__name__}.{association} is not a boolean')
                    setattr(graph[cim_class][identifier], association, value)

            elif 'int' in attribute_type:
                try:
                    setattr(graph[cim_class][identifier], association, int(float(value)))
                except:
                    _log.warning(f'{value} for {cim_class.__name__}.{association} is not an integer')
                    setattr(graph[cim_class][identifier], association, value)

            elif 'float' in attribute_type:
                try:
                    setattr(graph[cim_class][identifier], association, float(value))
                except:
                    _log.warning(f'{value} for {cim_class.__name__}.{association} is not a float')
                    setattr(graph[cim_class][identifier], association, value)

            else:
                if self.connection_params.use_units:
                    pass
                    #TODO: Implement evaluation of units
                else:
                    setattr(graph[cim_class][identifier], association, value)




    
    def create_edge(self, graph: dict[type, dict[str, object]],
                    cim_class: type, identifier: UUID, attribute: str,
                    edge_class: type, edge_mRID: str) -> None:
        
        association = self.check_attribute(cim_class, attribute)
        if association is not None:
            if association in cim_class.__dataclass_fields__:
                attribute_type = cim_class.__dataclass_fields__[association].type
                if 'List' in attribute_type or 'list' in attribute_type:
                    obj_list = getattr(graph[cim_class][identifier], association)
                    if type(obj_list) is not list:
                        obj_list = [obj_list]
                    edge_uuid = (edge_mRID.strip('_').lower())
                    if edge_uuid not in str(obj_list):
                        edge_object = self.create_object(graph, edge_class, edge_mRID)
                        obj_list.append(edge_object)
                        setattr(graph[cim_class][identifier], association, obj_list)
                else:
                    edge_object = self.create_object(graph, edge_class, edge_mRID)
                    setattr(graph[cim_class][identifier], association, edge_object)
            else:
                _log.warning(f'{cim_class.__name__} does not have attribute {association}')

    def create_object(self, graph:Graph,
                      class_type:type, uri:str) -> object:
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
        identifier = UUID(uri.strip('_').lower())

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

    def add_to_graph(self, obj: object, graph: Graph) -> None:
        """
        Method for adding existing objects to the graph
        Required Args:
            obj: a dataclass instance inheriting from the Identity class
        Returns:
            none
        """
        # Add class type to graph if not there
        if type(obj) not in graph:
            graph[type(obj)] = {}

        # Add instance to graph keys if not there
        if obj.identifier not in graph[type(obj)]:
            graph[type(obj)][obj.identifier] = obj

    def create_assocation(self, graph: Graph, attribute: str,
                          cim_class: type, mRID: str, attr_text: str,
                          edge_class: type, edge_mRID: str) -> None:
        
        # Old method to identify attributes using RDFS profile
        # This will be deprecated in a future release
    
    
        if attribute[1] in cim_class.__dataclass_fields__:    #check if forward attribute
            self.create_edge(graph, cim_class, mRID, attribute[1], edge_class, edge_mRID)

        elif self.rdfs_profile is not None:    # use data profile to look up reverse attribute
            attr_uri = URIRef(f'{self.namespace}{attr_text}')
            reverse_uri = self.rdfs_profile.value(object=attr_uri,
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
        
        

            



from cimgraph.databases.blazegraph import BlazegraphConnection
from cimgraph.databases.graphdb import GraphDBConnection
from cimgraph.databases.gridappsd import GridappsdConnection
from cimgraph.databases.neo4j import Neo4jConnection
from cimgraph.databases.rdflib import RDFlibConnection
from cimgraph.databases.fileparsers import XMLFile
