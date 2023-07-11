from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import json
import logging
import re

from cimgraph.loaders import ConnectionInterface, QueryResponse
from cimgraph.models.model_parsers import add_to_catalog, add_to_typed_catalog, cim_dump, item_dump, cim_print

_log = logging.getLogger(__name__)

@dataclass
class NewModel:
    connection: ConnectionInterface
    typed_catalog: dict[type, dict[str, object]] = field(default_factory=dict)
       
    def __post_init__(self):
        self.__initialize_network__()

    # Initialize all CIM objects in feeder model
    def __initialize_network__(self) -> Dict[str, object]:
        self.cim = self.connection.cim
    
    def add_to_typed_catalog(self, obj_list: List[object]) -> Dict:
        if type(obj_list) is not list:
            obj_list = [obj_list]

        for obj in obj_list:
            if type(obj) not in self.typed_catalog:
                self.typed_catalog[type(obj)] = {}
            if obj.mRID not in self.typed_catalog[type(obj)]:
                self.typed_catalog[type(obj)][obj.mRID] = obj

        
    def get_all_attributes(self, cim_class):
        if cim_class in self.typed_catalog:
            self.connection.get_all_attributes(self.feeder.mRID, self.typed_catalog, cim_class)
        else:
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')


    def get_attributes_query(self, cim_class):
        if cim_class in self.typed_catalog:
            sparql_message = self.connection.get_attributes_query(self.feeder.mRID, self.typed_catalog, cim_class)
        else:
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')
            sparql_message = ''
        return sparql_message

    def __dumps__(self, cim_class):
        if cim_class in self.typed_catalog:
            json_dump = cim_dump(self.typed_catalog, cim_class)
        else:
            json_dump = {}
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')

        return json_dump

    def pprint(self, cim_class):
        if cim_class in self.typed_catalog:
            json_dump = cim_print(self.typed_catalog, cim_class)
        else:
            json_dump = {}
            _log.info('no instances of '+str(cim_class.__name__)+' found in catalog.')

        print(json_dump)
    
    def upload(self):
        query = self.connection.upload(self.typed_catalog)
#         return query
    
    def write_xml(self, filename, schema):
        
        f = open(filename, "w", encoding="utf-8")
        header="""
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="{schema}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
"""
        f.write(header.format(schema = schema))
        for cim_class in list(self.typed_catalog.keys()):

            for obj in self.typed_catalog[cim_class].values():
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
                                value = item_dump(getattr(obj, attribute))
                                if value:
                                    body = """
  <cim:{pclass}.{attr}>{value}</cim:{pclass}.{attr}>"""
                                    f.write(body.format(pclass=pclass.__name__, attr = attribute, value = value))
                tail = """
</cim:{class_name}>"""
                f.write(tail.format(class_name = cim_class.__name__))
        
        f.write("""
</rdf:RDF>""")
        