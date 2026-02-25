from __future__ import annotations

import importlib
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, is_dataclass
from functools import cache
from uuid import UUID

from cimgraph.core import (get_cim_profile, get_database, get_host, get_iec61970_301,
                           get_namespace, get_password, get_port, get_undefined_handling, get_url,
                           get_use_units, get_username, get_validation_log_level)

_log = logging.getLogger(__name__)

Graph = dict[type, dict[UUID, object]]

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
                    value: str, datatype_uri: str = None) -> bool|int|float|str|object:
        association = self.check_attribute(cim_class, attribute)
        if association is not None and association != 'identifier':
            attribute_type = cim_class.__dataclass_fields__[association].type

            # Handle datatype if present
            if datatype_uri is not None:
                unit_class = self._extract_unit_class_from_datatype(datatype_uri)
                if unit_class is not None:
                    try:
                        # Extract unit information from datatype URI
                        unit_info = self._parse_datatype_uri(datatype_uri)
                        unit_instance = unit_class(value=float(value),
                                                input_unit=unit_info['unit'],
                                                input_multiplier=unit_info.get('multiplier'))
                        setattr(graph[cim_class][identifier], association, unit_instance)
                        return unit_instance
                    except Exception as e:
                        _log.warning(f'Failed to create unit instance from datatype {datatype_uri}: {e}')
                        # Fall through to standard handling

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
                setattr(graph[cim_class][identifier], association, value)
        return value

    def _extract_unit_class_from_datatype(self, datatype_uri: str) -> type:
        """
        Extract the CIM unit class from a datatype URI.
        Example: "http://cim.ucaiug.io/CIM101/draft#ApparentPower.MVA" -> ApparentPower
        """
        try:
            # Extract class name from URI (e.g., "ApparentPower.MVA" or "ApparentPower")
            datatype_part = datatype_uri.split('#')[-1]
            class_name = datatype_part.split('.')[0]

            # Try to get the class from the cim module
            if hasattr(self.cim, class_name):
                unit_class = getattr(self.cim, class_name)
                # Verify it's a CIMUnit subclass
                if hasattr(unit_class, '__pint__'):
                    return unit_class
        except Exception as e:
            _log.debug(f'Could not extract unit class from datatype URI {datatype_uri}: {e}')
        return None

    def _parse_datatype_uri(self, datatype_uri: str) -> dict:
        """
        Parse a datatype URI to extract unit and multiplier information.
        Examples:
        - "http://example.com#ApparentPower.MVA" -> {'unit': 'VA', 'multiplier': 'M'}
        - "http://example.com#ApparentPower" -> {'unit': 'VA', 'multiplier': None}
        """
        unit_info = {'unit': None, 'multiplier': None}

        try:
            datatype_part = datatype_uri.split('#')[-1]
            parts = datatype_part.split('.')

            if len(parts) > 1:
                # Has unit specification (e.g., "ApparentPower.MVA")
                unit_with_mult = parts[1]

                # Parse multiplier and unit
                # Common multipliers: k, M, G, T, m, µ, n, p
                multipliers = {'k': 'k', 'M': 'M', 'G': 'G', 'T': 'T',
                            'm': 'm', 'µ': 'µ', 'u': 'µ', 'n': 'n', 'p': 'p'}

                if unit_with_mult[0] in multipliers:
                    unit_info['multiplier'] = multipliers[unit_with_mult[0]]
                    unit_info['unit'] = unit_with_mult[1:]
                else:
                    unit_info['unit'] = unit_with_mult
        except Exception as e:
            _log.debug(f'Could not parse datatype URI {datatype_uri}: {e}')

        return unit_info




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
            # _log.warning(f'URI {uri} for object {class_type.__name__} is not a valid UUID')
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
from cimgraph.databases.fileparsers import JSONLDFile, XMLFile
from cimgraph.databases.graphdb import GraphDBConnection
from cimgraph.databases.gridappsd import GridappsdConnection
from cimgraph.databases.neo4j import Neo4jConnection
from cimgraph.databases.rdflib import RDFlibConnection
from cimgraph.databases.sparql_endpoint import SPARQLEndpointConnection
