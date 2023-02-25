from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import json
import logging
import cimlab.data_profile as cim
from cimlab.loaders import ConnectionInterface, QueryResponse
from cimlab.models.model_parsers import add_to_catalog, add_to_typed_catalog, cim_dump, item_dump

_log = logging.getLogger(__name__)

@dataclass
class NewModel:
    connection: ConnectionInterface
    typed_catalog: dict[type, dict[str, object]] = field(default_factory=dict)
       
    def __post_init__(self):
        self.__initialize_network__()

    # Initialize all CIM objects in feeder model
    def __initialize_network__(self) -> Dict[str, object]:
        pass
    
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
    
    def upload(self):
        query = self.connection.upload(self.typed_catalog)
        return query
        