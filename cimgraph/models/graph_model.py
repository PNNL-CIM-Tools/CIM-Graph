from __future__ import annotations
import re
import json
import logging
import importlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from cimgraph.loaders import ConnectionInterface


_log = logging.getLogger(__name__)

@dataclass
class GraphModel:
   
    def add_to_graph(obj: object, graph: Dict) -> Dict:
        if type(obj) not in graph:
            graph[type(obj)] = {}
        if obj.mRID not in graph[type(obj)]:
            graph[type(obj)][obj.mRID] = obj
        return graph

    def get_all_edges(self, cim_class, graph=None):
        if graph is None:
            graph = self.graph
        if cim_class in graph:
            self.read_connection.get_all_edges(self.container.mRID, graph, cim_class)
        else:
            _log.info('no instances of '+str(cim_class.__name__)+' found in graph.')
    
    def pprint(self, cim_class):
        if cim_class in self.graph:
            json_dump = self.cim_print(self.graph, cim_class)
        else:
            json_dump = {}
            _log.info('no instances of '+str(cim_class.__name__)+' found in graph.')
        print(json.dumps(json_dump,indent=4))
    
    def get_attributes_query(self, cim_class):
        if cim_class in self.graph:
            sparql_message = self.read_connection.get_attributes_query(self.container.mRID, self.graph, cim_class)
        else:
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')
            sparql_message = ''
        return sparql_message
    
    def get_edges_query(self, cim_class):
        if cim_class in self.graph:
            sparql_message = self.read_connection.get_edges_query(self.container.mRID, self.graph, cim_class)
            
        else:
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')
            sparql_message = ''
        return sparql_message

    def __dumps__(self, cim_class):
        if cim_class in self.graph:
            json_dump = cim_dump(self.graph, cim_class)
        else:
            json_dump = {}
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')

        return json_dump
    
    def upload(self):
        query = self.write_connection.upload(self.graph)
#         return query
    
    def write_xml(self, filename, schema):
        
        f = open(filename, "w", encoding="utf-8")
        header="""
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="{schema}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
"""
        f.write(header.format(schema = schema))
        for cim_class in list(self.graph.keys()):

            for obj in self.graph[cim_class].values():
                header = """
<cim:{class_name} rdf:about="urn:uuid:{mRID}">"""         
                f.write(header.format(class_name=cim_class.__name__, mRID = obj.mRID))

                parent_classes = list(cim_class.__mro__)
                parent_classes.pop(len(parent_classes)-1)

                for pclass in parent_classes:
                    attribute_list = list(pclass.__annotations__.keys())
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
                                    body = """
  <cim:{pclass}.{attr} rdf:resource="urn:uuid:{value}"/>"""

                                    f.write(body.format(pclass=pclass.__name__, attr=attribute, value = value))

                            else:
                                value = self.item_dump(getattr(obj, attribute))
                                if value:
                                    body = """
  <cim:{pclass}.{attr}>{value}</cim:{pclass}.{attr}>"""
                                    f.write(body.format(pclass=pclass.__name__, attr = attribute, value = value))
                tail = """
</cim:{class_name}>"""
                f.write(tail.format(class_name = cim_class.__name__))
        
        f.write("""
</rdf:RDF>""")
        



    def cim_print(self, graph:Dict, cim_class:type):
        mrid_list = list(graph[cim_class].keys())
        attribute_list = list(cim_class().__dict__.keys())
        json_dump = {}

        for mrid in mrid_list:
            json_dump[mrid] = {}
            for attribute in attribute_list:
                value = getattr(graph[cim_class][mrid], attribute)
                if value is not None and value != []:
                    json_dump[mrid][attribute] = self.item_dump(value)
        return json_dump
                            
    def item_dump(self, value):
        if type(value) is str:
            result = value
        elif type(value) is float:
            result = value
        elif type(value) is list:
            result = []
            for item in value:
                result.append(self.item_dump(item))
        elif value is None:
            result = ''
        elif type(type(value)) is type:
            result = value.mRID
        else:
            result = str(value)
        return result

    def cim_dump(self, graph:Dict, cim_class:type):
        mrid_list = list(graph[cim_class].keys())
        attribute_list = list(cim_class().__dict__.keys())
        json_dump = {}

        for mrid in mrid_list:
            json_dump[mrid] = {}
            for attribute in attribute_list:
                value = getattr(graph[cim_class][mrid], attribute)
                json_dump[mrid][attribute] = self.item_dump(value)
        return (json_dump)