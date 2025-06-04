from __future__ import annotations

import importlib
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, is_dataclass
from functools import cache
from uuid import UUID

_log = logging.getLogger(__name__)

Graph = dict[type, dict[UUID, object]]

DEFAULT_NAMESPACE = 'http://iec.ch/TC57/CIM100#'
DEFAULT_CIM_PROFILE = 'cimhub_2023'
DEFAULT_URL = 'http://localhost:8889/bigdata/namespace/kb/sparql'
DEFAULT_DATABASE = 'powergridmodel'
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = '61613'
DEFAULT_USERNAME = 'system'
DEFAULT_PASSWORD = 'manager'
DEFAULT_IEC61970_301 = 8
DEFAULT_USE_UNITS = 'false'
DEFAULT_VALIDATION_LOG_LEVEL = 'WARNING'
DEFAULT_ALLOW_UNDEFINED_ATTRIBUTES = 'false'

@cache
def get_cim_profile() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        cim_profile: library
    """
    cim_profile = os.getenv('CIMG_CIM_PROFILE')
    if cim_profile is None:
        raise ValueError('CIMG_CIM_PROFILE environment variable is not set.')
    else:
        # try:
            if '.' in cim_profile:
                cim = importlib.import_module(cim_profile)
            else:
                cim = importlib.import_module('cimgraph.data_profile.'+cim_profile)
        # except:
        #     raise ValueError('CIMG_CIM_PROFILE environment variable must be name of a valid object module on the PATH')
    return cim_profile, cim

@cache
def get_namespace() -> str:
    """
    Returns the namespace for the cimgraph database
    Returns:
        namespace: the namespace for the cimgraph database
    """
    namespace = os.getenv('CIMG_NAMESPACE')
    if namespace is None:
        namespace = DEFAULT_NAMESPACE
        _log.debug('Default namespace for CIM100 used')
        # raise ValueError('CIMG_NAMESPACE environment variable is not set.')
    return namespace

@cache
def get_iec61970_301() -> int:
    """
    Returns the IEC61970_301 version for the cimgraph database
    Returns:
        iec61970_301: the IEC61970_301 version for the cimgraph database
    """
    iec61970_301 = os.getenv('CIMG_IEC61970_301')
    if iec61970_301 is None:
        iec61970_301 = DEFAULT_IEC61970_301
        _log.info('CIMG_IEC61970_301 environment variable not set. Defaulting to 8 for urn:uuid:mRID. Set to 7 for mRIDs with underscores')
    else:
        try:
            iec61970_301 = int(iec61970_301)
        except:
            raise ValueError('CIMG_IEC61970_301 environment variable should be an integer')
    return iec61970_301


@cache
def get_url() -> str:
    """
    Returns the URL for the cimgraph database
    Returns:
        url: the URL for the cimgraph database
    """
    url = os.getenv('CIMG_URL')
    if url is None:
        _log.warning('CIMG_URL environment variable is not set. Using Blazegraph default')
        url = DEFAULT_URL
        # raise ValueError('CIMG_URL environment variable is not set.')
    return url

@cache
def get_database() -> str:
    """
    Returns the database name for the cimgraph database
    Returns:
        database: the database name for the cimgraph database
    """
    database = os.getenv('CIMG_DATABASE')
    if database is None:
        _log.warning('CIMG_DATABASE environment variable is not set.')
        database = DEFAULT_DATABASE
        # raise ValueError('CIMG_DATABASE environment variable is not set.')
    return database

@cache
def get_use_units() -> bool:
    """
    Returns the use_units flag for the cimgraph database
    Returns:
        use_units: the use_units flag for the cimgraph database
    """
    use_units = os.getenv('CIMG_USE_UNITS')
    if use_units is None:
        use_units = DEFAULT_USE_UNITS
        _log.debug('CIMG_USE_UNITS environment variable is not set. Defaulting to false.')
    return use_units.lower() == 'true'

@cache
def get_username() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        username: str
    """
    username = os.getenv('CIMG_USERNAME')
    if username is None:
        _log.warning('CIMG_USERNAME environment variable is not set.')
        username = DEFAULT_USERNAME
    return username

@cache
def get_password() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        password: str
    """
    password = os.getenv('CIMG_PASSWORD')
    if password is None:
        _log.warning('CIMG_PASSWORD environment variable is not set.')
        password = DEFAULT_PASSWORD
    return password

@cache
def get_host() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        host: str
    """
    host = os.getenv('CIMG_HOST')
    if host is None:
        _log.warning('CIMG_HOST environment variable is not set.')
        host = DEFAULT_HOST
    return host

@cache
def get_port() -> str:
    """
    Returns the CIM profile to be used for object graph
    Returns:
        port: str
    """
    port = os.getenv('CIMG_PORT')
    if port is None:
        _log.warning('CIMG_PORT environment variable is not set.')
        port = DEFAULT_PORT
    return port

@cache
def get_validation_log_level() -> str:
    '''
    Returns the log level used for validation warnings
    Returns:
        log_level: str
    '''
    log_level = getattr(logging, os.environ.get('CIMG_VALIDATION_LOG_LEVEL',
                        DEFAULT_VALIDATION_LOG_LEVEL).upper(), logging.WARNING)
    return log_level

@cache
def get_undefined_handling() -> str:
    '''
    Returns the log level used for validation warnings
    Returns:
        log_level: str
    '''
    handling = os.environ.get('CIMG_ALLOW_UNDEFINED_ATTRIBUTES',
                        DEFAULT_ALLOW_UNDEFINED_ATTRIBUTES)
    return handling.lower() == 'true'


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
    def __post_init__(self):
        _log.warning('ConnectionParameters class is deprecated and will be deleted in a future release')
        _log.warning('Set environment variables for required authentication')

@dataclass
class QueryResponse:
    response: str


class ConnectionInterface(ABC):

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
    def get_from_triple(self, subject:object, predicate:str, graph: Graph = None) -> list[object]:
        raise RuntimeError('Must have implemented query in the inherited class')

    @abstractmethod
    def create_new_graph(self, container: object, graph: Graph = None) -> Graph:
        raise RuntimeError('Must have implemented query in the inherited class')

    @abstractmethod
    def create_distributed_graph(self, area: object, graph: Graph = None) -> Graph:
        raise RuntimeError('Must have implemented query in the inherited class')

    def __init__(self):
        # clear cached env variables
        get_namespace.cache_clear()
        get_cim_profile.cache_clear()
        get_iec61970_301.cache_clear()
        get_validation_log_level.cache_clear()

        # retrieve env variables
        self.cim_profile, self.cim = get_cim_profile()
        self.namespace = get_namespace()
        self.iec61970_301 = get_iec61970_301()
        self.log_level = get_validation_log_level()

    def check_attribute(self, cim_class:type, attribute:str) -> str:
        attr_class = attribute.split('.')[0]
        attr_link = attribute.split('.')[1]
        association = None

        if attr_link in cim_class.__dataclass_fields__:
            association = attr_link
        else:
            try:
                from_class = getattr(self.cim, attr_class)

                if attr_link not in from_class.__dataclass_fields__:
                    _log.log(self.log_level, f'Association {attr_link} missing from class {attr_class} in data profile')

                else:
                    try:
                        reverse = from_class.__dataclass_fields__[attr_link].metadata['inverse']
                        reverse_assc = reverse.split('.')[1]
                        if reverse_assc in cim_class.__dataclass_fields__:
                            association = reverse_assc
                        else:
                            _log.log(self.log_level,f'Association {reverse_assc} missing from class {cim_class.__name__} in data profile')
                    except:
                        _log.log(self.log_level,f'Unable to find inverse of {attribute} for {cim_class.__name__}')
            except:
                _log.log(self.log_level,f'Unable to find {attribute} for {cim_class.__name__}')

        return association


    def create_value(self, graph: dict[type, dict[str, object]],
                    cim_class: type, identifier: UUID, attribute: str,
                    value: str) -> bool|int|float|str:

        association = self.check_attribute(cim_class, attribute)
        if association is not None:
            attribute_type = cim_class.__dataclass_fields__[association].type
            if 'List' in attribute_type or 'list' in attribute_type:
                obj_list = getattr(graph[cim_class][identifier], association)
                if value not in str(obj_list):
                    obj_list.append(value)

            elif 'bool' in attribute_type:
                if str(value).lower() == 'true' or str(value).lower() == '1':
                    value = True
                elif str(value).lower() == 'false' or str(value).lower() == '0':
                    value = False
                else:
                    _log.log(self.log_level, f'{value} for {cim_class.__name__}.{association} is not a boolean')

                setattr(graph[cim_class][identifier], association, value)


            elif 'int' in attribute_type:
                try:
                    value = int(float(value))
                except:
                    _log.log(self.log_level, f'{value} for {cim_class.__name__}.{association} is not an integer')

                setattr(graph[cim_class][identifier], association, value)

            elif 'float' in attribute_type:
                try:
                    value = float(value)
                except:
                    _log.log(self.log_level, f'{value} for {cim_class.__name__}.{association} is not a float')
                setattr(graph[cim_class][identifier], association, value)

            else:
                if get_use_units():
                    pass
                    #TODO: Implement evaluation of units
                else:
                    setattr(graph[cim_class][identifier], association, value)
        return value




    def create_edge(self, graph: dict[type, dict[str, object]],
                    cim_class: type, identifier: UUID, attribute: str,
                    edge_class: type, edge_mRID: str) -> object:

        edge_object = None
        association = self.check_attribute(cim_class, attribute)
        if association is not None:
            if association in cim_class.__dataclass_fields__:
                attribute_type = cim_class.__dataclass_fields__[association].type
                if 'List' in attribute_type or 'list' in attribute_type:
                    obj_list = getattr(graph[cim_class][identifier], association)
                    if type(obj_list) is not list:
                        obj_list = [obj_list]
                    edge_uuid = (edge_mRID.strip('_').lower())
                    # _log.warning(obj_list)
                    if edge_uuid not in str(obj_list):
                        edge_object = self.create_object(graph, edge_class, edge_mRID)
                        obj_list.append(edge_object)
                        setattr(graph[cim_class][identifier], association, obj_list)
                else:
                    # _log.warning(f'{identifier}, {attribute}, {edge_class}, {edge_mRID}, ')

                    edge_object = self.create_object(graph, edge_class, edge_mRID)
                    # _log.warning(edge_object)
                    setattr(graph[cim_class][identifier], association, edge_object)
            else:
                _log.warning(f'{cim_class.__name__} does not have attribute {association}')
        return edge_object

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
        try:
            identifier = UUID(uri.strip('_').lower())
        except:
            _log.warning(f'URI {uri} for object {class_type.__name__} is not a valid UUID')
            identifier = uri

        # Check if object exists in graph
        if identifier in graph[class_type]:
            obj = graph[class_type][identifier]

        # If not there, create a new object and add to graph
        else:
            obj = class_type(identifier = uri)
            # obj.uuid(uri = uri)
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


from cimgraph.databases.blazegraph import BlazegraphConnection
from cimgraph.databases.fileparsers import XMLFile
from cimgraph.databases.graphdb import GraphDBConnection
from cimgraph.databases.gridappsd import GridappsdConnection
from cimgraph.databases.neo4j import Neo4jConnection
from cimgraph.databases.rdflib import RDFlibConnection
