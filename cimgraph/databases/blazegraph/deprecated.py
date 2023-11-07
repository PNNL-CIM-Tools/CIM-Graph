from __future__ import annotations
import math
import importlib
import logging
import re
import json

from typing import Dict, List, Optional

import cimgraph.queries.sparql as sparql

_log = logging.getLogger(__name__)


def query_list_parser(self, container, graph: Dict, class_name: type, mRID: str, query: List,
                      attribute: str, attribute_class: str, separator: str):
    value = query[attribute]['value']
    values = value.split(separator)
    obj_list = []
    #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
    if attribute_class in self.cim.__all__:
        for value in values:
            value = value.split(',')
            obj_mrid = value[0]
            try:
                obj_class = value[1]
            except:
                obj_class = attribute_class
            class_type = eval(f'self.cim.{obj_class}')
            if type(class_type) is type and len(obj_mrid) > 0:
                result = self.create_object(graph, class_type, obj_mrid)
                obj_list.append(result)

    else:
        obj_list = values
    #set attribute of queried object to list parsed from query results
    setattr(graph[class_name][mRID], attribute, obj_list)


def get_all_attributes(self, container, graph: dict[type, dict[str, object]], cim_class: type):
    """ Populates all available attribute fields of CIM objects in the typed catalog of a specified CIM class.
    This method uses pre-defined UML paths for specific container to class and edges
    Objects are stored in memory, so no values are returned.
    Args:
    container: a CIM container object inheriting from ConnectivityNodeContainer
    graph: The graph catalog of CIM objects organized by class type and object mRID
    cim_class: The CIM class type (e.g. cim:ACLineSegment)
    Returns:
    none
    """
    mrid_list = list(graph[cim_class].keys())
    num_nodes = len(mrid_list)
    container_mRID = container.mRID
    for index in range(math.ceil(len(mrid_list) / 100)):
        eq_mrids = mrid_list[index * 100:(index + 1) * 100]
        #generate SPARQL message from correct loaders>sparql python script based on class name
        # sparql_message = self.get_attributes_query(container, cim_class, eq_mrids, self.namespace)
        sparql_func = getattr(self.legacy_sparql, f'{cim_class.__name__}SPARQL')
        sparql_message = sparql_func.get_all_attributes(container, graph, mrid_list)
        #execute sparql query

        query_output = self.execute(sparql_message)
        self.edge_query_parser(query_output, container, graph, cim_class)

        # #generate SPARQL message from correct loaders>sparql python script based on class name
        # sparql_message = self.get_attributes_query(container_mRID, graph, cim_class)
        # #execute sparql query
        # query_output = self.execute(sparql_message)

        for result in query_output['results']['bindings']:    #iterate through rows of response
            attribute_list = result.keys()
            mRID = result['mRID']['value']
            for attribute in attribute_list:
                try:    #check if attribute is in data profile
                    attribute_type = cim_class.__dataclass_fields__[attribute].type
                except:
                    #replace with warning message
                    _log.warning('attribute ' + str(attribute) + ' missing from ' +
                                 str(cim_class.__name__))

                if 'List' in attribute_type:    #check if attribute is association to a list of class objects
                    if '\'' in attribute_type:    #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'List\[\'(.*)\']', attribute_type)
                        attribute_class = at_cls.group(1)
                    else:
                        at_cls = re.match(r'List\[(.*)]', attribute_type)
                        attribute_class = at_cls.group(1)
                    # pass query response of associated objects to list parser
                    self.query_list_parser(container_mRID, graph, cim_class, mRID, result,
                                           attribute, attribute_class, ';')
                elif 'Optional' in attribute_type:    #check if attribute is association to a class object
                    if '\'' in attribute_type:    #handling inconsistent '' marks in data profile
                        at_cls = re.match(r'Optional\[\'(.*)\']', attribute_type)
                        attribute_class = at_cls.group(1)
                    else:
                        at_cls = re.match(r'Optional\[(.*)]', attribute_type)
                        attribute_class = at_cls.group(1)

                    # pass query response of associated objects to list parser
                    self.query_parser(container_mRID, graph, cim_class, mRID, result, attribute,
                                      attribute_class, ';')
                else:    #otherwise assign query response

                    self.query_parser(container_mRID, graph, cim_class, mRID, result, attribute,
                                      attribute_class, ';')


def get_attributes_query(self, container, graph: dict[type, dict[str, object]], cim_class: type):
    """ Generates SPARQL edges query for a given catalog of objects and feeder id
    Args:
        container_mRID (str | Feeder object): The mRID of the feeder or feeder object
        graph (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by
            class type and object mRID
        cim_class (type): The CIM class type (e.g. cim:ACLineSegment)
    Returns:
        sparql_message: query string that can be used in blazegraph connection or STOMP client
    none
    """
    mrid_list = list(graph[cim_class].keys())
    eq_mrids = mrid_list[0:100]
    sparql_func = getattr(self.legacy_sparql, f'{cim_class.__name__}SPARQL')
    sparql_message = sparql_func.get_all_attributes(container, graph, eq_mrids)

    return sparql_message


def query_parser(self, container, graph: Dict, class_name: str, mRID: str, query: List,
                 attribute: str, attribute_class: str, separator: str) -> object | str:
    value = query[attribute]['value']
    #if attribute is CIM class, then build CIM objects. otherwise assign to obj_list
    if attribute_class in self.cim.__all__:
        value = value.split(',')
        obj_mrid = value[0]
        try:
            obj_class = value[1]
        except:
            obj_class = attribute_class
        class_type = eval(f'self.cim.{obj_class}')
        if type(class_type) is type and len(obj_mrid) > 0:
            result = self.create_object(graph, class_type, obj_mrid)

        else:
            result = value

    else:
        result = value
    setattr(graph[class_name][mRID], attribute, result)
