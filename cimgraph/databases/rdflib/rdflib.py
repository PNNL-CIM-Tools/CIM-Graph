from __future__ import annotations
import math
import importlib
import logging
import re
import json

from typing import Dict, List, Optional

import cimgraph.queries.rdflib as sparql
from cimgraph.databases import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from cimgraph.models.graph_model import GraphModel

from rdflib import Graph, Namespace
from rdflib.namespace import RDF

_log = logging.getLogger(__name__)

class RDFlibConnection(ConnectionInterface):
    def __init__(self, connection_params:ConnectionParameters):
        self.cim_profile = connection_params.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.namespace = connection_params.namespace
        self.iec61970_301 = connection_params.iec61970_301
        self.filename = connection_params.filename
        self.connection_params = connection_params
        self.libgraph = None

    def connect(self):
        if not self.libgraph:
            self.libgraph = Graph()
            self.libgraph.parse(self.filename)
            self.libgraph.bind("cim", Namespace(self.namespace))
            self.libgraph.bind("rdf", RDF)

    def disconnect(self):
        self.libgraph = None
        
    def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        query_output = self.libgraph.query(query_message)
        return query_output

            
    def create_new_graph(self, container:object) -> dict[type, dict[str, object]] :
        graph = {}
        # Get all nodes, terminal, and equipment by 
        sparql_message = sparql.get_all_nodes_sparql(container, self.namespace)
        query_output = self.execute(sparql_message)

        for result in query_output:
            # Parse query results
            node = result.ConnectivityNode
            terminal = result.Terminal
            eq = json.loads(result.Equipment)
            eq_id = eq["@id"]
            eq_class = eq["@type"]
            # Add each object to graph
            self.create_object(graph, self.cim.ConnectivityNode, node)
            self.create_object(graph, self.cim.Terminal, terminal)
            if eq_class in self.cim.__all__:
                eq_class = eval(f"self.cim.{eq_class}")
                obj = self.create_object(graph, eq_class, eq_id)
                
            else:
                _log.warning('object class missing from data profile:' + str(eq_class))
                continue
            # Link objects in graph
            graph[eq_class][eq_id].Terminals.append(graph[self.cim.Terminal][terminal])
            graph[self.cim.ConnectivityNode][node].Terminals.append(graph[self.cim.Terminal][terminal])
            setattr(graph[self.cim.Terminal][terminal], "ConnectivityNode", graph[self.cim.ConnectivityNode][node])
            setattr(graph[self.cim.Terminal][terminal], "ConductingEquipment", graph[eq_class][eq_id])
            
        return graph
    
    
    def get_edges_query(self, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):

        eq_mrids=list(graph[cim_class].keys())[0:100]
        sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids, self.namespace, self.iec61970_301)

        return sparql_message
    
    
    def get_all_edges(self, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        for index in range(math.ceil(len(mrid_list)/100)):
            eq_mrids = mrid_list[index*100: (index+1)*100]
            #generate SPARQL message from correct loaders>sparql python script based on class name
            sparql_message = sparql.get_all_edges_sparql(cim_class, eq_mrids, self.namespace, self.iec61970_301)
            #execute sparql query
            query_output = self.execute(sparql_message)
            self.edge_query_parser(query_output, container, graph, cim_class)

    def edge_query_parser(self, query_output, container: str | cim.ConnectivityNodeContainer, graph: dict[type, dict[str, object]], cim_class: type):
        for result in query_output:
            if 'type' not in result.attr: #skip 'type' and other single attributes
                    
                is_association = False
                is_enumeration = False
                mRID = str(result.mRID) #get mRID
                attribute = str(result.attr).split(self.namespace)[1]
                attribute = attribute.split('.') #split edge attribute
                value = str(result.val) #get edge value
                

                if self.namespace in value: #check if enumeration
                    enum_text = value.split(self.namespace)[1]
                    enum_text = enum_text.split(">")[0]
                    enum_class = enum_text.split(".")[0]
                    enum_value = enum_text.split(".")[1]
                    is_enumeration = True

                if result.edge_class is not None: #check if association
                    is_association = True
                    # edge = json.loads(result.edge)
                    # edge_mRID = edge['@id']
                    # edge_class = edge['@type']
                    edge_class = str(result.edge_class)
                    if result.edge_mRID is not None:
                        edge_mRID = str(result.edge_mRID)
                    else:
                        if self.iec61970_301 > 7:
                            edge_mRID = value.split("uuid:")[1]
                        else:
                            edge_mRID = value.split("#")[1]
                    if edge_class in self.cim.__all__:
                        edge_class = eval(f"self.cim.{edge_class}")
                    else:
                        print('unknown class', edge_class)
                        continue

                if is_association: # if association to another CIM object

                    if attribute[0] in cim_class.__dataclass_fields__: #check if first name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[0], edge_class, edge_mRID)
                        
                    elif attribute[1] in cim_class.__dataclass_fields__: #check if second name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[1], edge_class, edge_mRID)

                    elif attribute[0]+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[0]+'s', edge_class, edge_mRID)
                    
                    elif attribute[1]+'s' in cim_class.__dataclass_fields__: #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[1]+'s', edge_class, edge_mRID)
                        
                    else: #fallback: match class type until a suitable parent edge class is found
                        for node_attr in list(cim_class.__dataclass_fields__.keys()):
                            attr_str = cim_class.__dataclass_fields__[node_attr].type
                            edge_parent = attr_str.split('[')[1].split(']')[0]
                            if edge_parent in self.cim.__all__:
                                parent_class = eval(f"self.cim.{edge_parent}")
                                if issubclass(edge_class, parent_class):
                                    self.create_edge(graph, cim_class, mRID, node_attr, edge_class, edge_mRID)
                                    break

                elif is_enumeration:
                    if enum_class in self.cim.__all__: # if enumeration
                        edge_enum = eval(f"self.cim.{enum_class}(enum_value)")
                        setattr(graph[cim_class][mRID], attribute[1], edge_enum)
                else:
                    setattr(graph[cim_class][mRID], attribute[1], value)



    def create_edge(self, graph, cim_class, mRID, attribute, edge_class, edge_mRID):
        edge_object = self.create_object(graph, edge_class, edge_mRID)
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if "List" in attribute_type:
            obj_list = getattr(graph[cim_class][mRID], attribute)
            if edge_object not in obj_list:
                obj_list.append(edge_object)
                setattr(graph[cim_class][mRID], attribute, obj_list)
        else:
            setattr(graph[cim_class][mRID], attribute, edge_object)


    def create_object(self, graph, class_type, mRID):
        
        if class_type not in graph.keys():
            graph[class_type] = {}

        if mRID in graph[class_type].keys():
            obj = graph[class_type][mRID]
        else:
            obj = class_type()
            setattr(obj, "mRID", mRID)
            graph[class_type][mRID] = obj

        return obj
    
    def upload(self, graph):
        url = self.url
        
        prefix = f"""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim: <{self.namespace}>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        """
        triples = []
        for cim_class in list(graph.keys()):
            
            for obj in graph[cim_class].values():
#                 obj_triple = "<{url}#_{mRID}> a cim:{class_type}."
                obj_triple = """
        <urn:uuid:{mRID}> a cim:{class_type}.
                """
                triple = obj_triple.format(url = url, mRID = obj.mRID, class_type = cim_class.__name__)
                triples.append(triple)
                parent_classes = list(cim_class.__mro__)
                parent_classes.pop(len(parent_classes)-1)
                for class_type in parent_classes:
                    attribute_list = list(class_type.__annotations__.keys())
                    for attribute in attribute_list:
                        
                        try: #check if attribute is in data profile
                            attribute_type = cim_class.__dataclass_fields__[attribute].type
                        except:
                            #replace with warning message                       
                            _log.warning('attribute '+str(attribute) +' missing from '+str(cim_class.__name__))
                        
                        if 'List' not in attribute_type: #check if attribute is association to a class object
                            if '\'' in attribute_type: #handling inconsistent '' marks in data profile
                                at_cls = re.match(r'Optional\[\'(.*)\']',attribute_type)
                                attribute_class = at_cls.group(1)
                            else:        
                                at_cls = re.match(r'Optional\[(.*)]',attribute_type)
                                attribute_class = at_cls.group(1)

                            if attribute_class in self.cim.__all__:
                                attr_obj = getattr(obj,attribute)
                                if attr_obj is not None:
                                    value = attr_obj.mRID
                                    attr = """
        <urn:uuid:{mRID}> cim:{class_type}.{att} <urn:uuid:{value}>.
                                    """

                                    triple = attr.format(url = url, mRID = obj.mRID, class_type = class_type.__name__, att = attribute, value = value)
                                    triples.append(triple)

                            else:
                                value = GraphModel.item_dump(getattr(obj, attribute))
                                if value:
        #                              <{url}#_{mRID}> cim:{class_type}.{attr} \"{value}\".
                                    attr = """
        <urn:uuid:{mRID}> cim:{class_type}.{attr} \"{value}\".
                                     """
                                    triple = attr.format(url = url, mRID = obj.mRID, class_type = class_type.__name__, attr = attribute, value = value)
                                    triples.append(triple)
        triples.append ('}')
        query = prefix + ' INSERT DATA { ' + ''.join(triples)

        self.execute(query)
        return query


            
