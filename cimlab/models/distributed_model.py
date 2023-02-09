from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import json

import cimlab.data_profile as cim
from cimlab.loaders import ConnectionInterface, QueryResponse
from cimlab.models.model_parsers import add_to_catalog, add_to_typed_catalog, cim_dump
from cimlab.models.switch_area import SwitchArea


@dataclass
class DistributedModel:
    feeder: cim.Feeder
    connection: ConnectionInterface
    topology: Dict
    addressable_equipment: Dict[str, object] = field(default_factory=dict)
    unaddressable_equipment: Dict[str, object] = field(default_factory=dict)
    connectivity_nodes: Dict[str, object] = field(default_factory=dict)
    switch_areas: List[SwitchArea] = field(default_factory=list)
    assets: List[str] = field(default_factory=list)
    typed_catalog: dict[type, dict[str, object]] = field(default_factory=dict)
    is_loaded: Optional[set] = field(default_factory=set)

    def __post_init__(self):
        self.__initialize_network__()

    # REPLACE WITH CONNECTION OBJECT



    # Initialize all CIM objects in feeder model
    def __initialize_network__(self) -> Dict[str, object]:
        # Get switch area message from Topology Processor
        # topo_message = DistributedModel.get_topology_api_response(feeder_mrid)
        # topo_message = DistributedModel.get_topology_response(feeder_mrid)

        # Initialize all CIM objects not contained in a switch area
        addr_equip = self.connection.create_default_instances(self.feeder.mRID, self.topology['addressable_equipment'])
        for obj in addr_equip:
            add_to_catalog(obj, self.addressable_equipment)
            add_to_typed_catalog(obj, self.typed_catalog)
        unaddr_equip = self.connection.create_default_instances(self.feeder.mRID,
                                                                self.topology['unaddressable_equipment'])
        for obj in unaddr_equip:
            add_to_catalog(obj, self.unaddressable_equipment)
            add_to_typed_catalog(obj, self.typed_catalog)
        conn_nodes = self.connection.create_default_instances(self.feeder.mRID,
                                                              self.topology['connectivity_node'])
        for obj in conn_nodes:
            add_to_catalog(obj, self.connectivity_nodes)
            add_to_typed_catalog(obj, self.typed_catalog)

        # Initialize all CIM objects in a single switch area
        # def initialize_switch_areas(feeder_mrid) -> dict(str,object):
        sa_index = -1
        for switch_msg in self.topology['switch_areas']:
            # Add switch area
            switch_area = SwitchArea(self.feeder.mRID + '.' + str(sa_index), self.connection)
            switch_area.initialize_switch_area(switch_msg)
            self.switch_areas.append(switch_area)
            # Add switch area unaddressable equipment to feeder unaddressable equipment
            self.unaddressable_equipment.update(switch_area.unaddressable_equipment)
            sa_index = sa_index + 1


    def get_all_attributes(self, cim_class):
        if cim_class in self.typed_catalog:
            self.connection.get_all_attributes(self.feeder.mRID, self.typed_catalog, cim_class)
        else:
            print('warning: no instances of ', cim_class.__name__, ' found in catalog.')
#             return self.__dumps__(cim_class)

    def get_attributes_query(self, cim_class):
        if cim_class in self.typed_catalog:
            sparql_message = self.connection.get_attributes_query(self.feeder.mRID, self.typed_catalog, cim_class)
        else:
            print('warning: no instances of ', cim_class.__name__, ' found in catalog.')
            sparql_message = ''
        return sparql_message

    def __dumps__(self, cim_class):
        if cim_class in self.typed_catalog:
            json_dump = cim_dump(self.typed_catalog, cim_class)
        else:
            json_dump = {}
            print('warning: no instances of ', cim_class.__name__, ' found in catalog.')

        return json_dump
    
    