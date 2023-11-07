from __future__ import annotations
import re
import json
import logging
import importlib
import enum
import uuid

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from cimgraph.databases import ConnectionInterface

_log = logging.getLogger(__name__)


def new_mrid():
    mRID = str(uuid.uuid4())
    return mRID


def json_dump(value, cim: __package__, json_ld: bool = False):
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

    def add_to_graph(self, obj: object, graph: GraphModel = None) -> Dict:
        if graph is None:
            graph = self.graph
        if type(obj) not in graph.keys():
            graph[type(obj)] = {}
        if obj.mRID not in graph[type(obj)].keys():
            graph[type(obj)][obj.mRID] = obj

    def get_all_edges(self, cim_class, graph: GraphModel = None):
        if graph is None:
            graph = self.graph
        if cim_class in graph:
            self.connection.get_all_edges(self.container.mRID, graph, cim_class)
        else:
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in graph.')

    def get_edges_query(self, cim_class):
        if cim_class in self.graph:
            sparql_message = self.connection.get_edges_query(self.container.mRID, self.graph,
                                                             cim_class)

        else:
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in catalog.')
            sparql_message = ''
        return sparql_message

    def pprint(self, cim_class: type, show_empty: bool = False, json_ld: bool = False):
        if cim_class in self.graph:
            json_dump = self.__dumps__(cim_class, show_empty, json_ld)
        else:
            json_dump = {}
            _log.info('no instances of ' + str(cim_class.__name__) + ' found in graph.')
        print(json.dumps(json_dump, indent=4))

    def upload(self):
        self.connection.upload(self.graph)

    def write_xml(self, filename):
        namespace = self.connection.namespace
        iec61970_301 = self.connection.iec61970_301

        if int(iec61970_301) > 7:
            rdf_header = """rdf:about="urn:uuid:"""
            rdf_resource = """urn:uuid:"""
        else:
            rdf_header = """rdf:ID=\""""
            rdf_resource = """#"""

        f = open(filename, 'w', encoding='utf-8')
        header = f"""
<?xml version="1.0" encoding="utf-8"?>
<!-- un-comment this line to enable validation
-->
<rdf:RDF xmlns:cim="{namespace}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<!--
-->
"""
        f.write(header)

        for cim_class in list(self.graph.keys()):

            for obj in self.graph[cim_class].values():
                header = f"""
<cim:{cim_class.__name__} {rdf_header}{obj.mRID}">"""
                f.write(header)

                parent_classes = list(cim_class.__mro__)
                parent_classes.pop(len(parent_classes) - 1)

                for pclass in parent_classes:
                    attribute_list = list(pclass.__annotations__.keys())
                    for attribute in attribute_list:

                        try:    #check if attribute is in data profile
                            attribute_type = cim_class.__dataclass_fields__[attribute].type
                        except:
                            #replace with warning message
                            _log.warning('attribute ' + str(attribute) + ' missing from ' +
                                         str(cim_class.__name__))

                        if 'List' not in attribute_type:    #check if attribute is association to a class object
                            if '\'' in attribute_type:    #handling inconsistent '' marks in data profile
                                at_cls = re.match(r'Optional\[\'(.*)\']', attribute_type)
                                attribute_class = at_cls.group(1)
                            else:
                                at_cls = re.match(r'Optional\[(.*)]', attribute_type)
                                attribute_class = at_cls.group(1)
                            if attribute_class in self.cim.__all__:
                                attr_obj = getattr(obj, attribute)
                                if attr_obj is not None:
                                    if type(type(attr_obj)) is not enum.EnumMeta:
                                        value = """rdf:resource=\"""" + rdf_resource + attr_obj.mRID
                                    else:
                                        value = """rdf:resource=\"""" + namespace + str(attr_obj)
                                    body = f"""
  <cim:{pclass.__name__}.{attribute} {value}"/>"""

                                    f.write(body)

                            else:
                                value = json_dump(getattr(obj, attribute), self.cim)
                                if value:
                                    body = f"""
  <cim:{pclass.__name__}.{attribute}>{value}</cim:{pclass.__name__}.{attribute}>"""
                                    f.write(body)
                tail = f"""
</cim:{cim_class.__name__}>"""
                f.write(tail)

        f.write("""
</rdf:RDF>""")

    def __dumps__(self, cim_class: type, show_empty: bool = False, json_ld: bool = True):
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
