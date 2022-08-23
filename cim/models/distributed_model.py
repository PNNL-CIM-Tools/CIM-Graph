from __future__ import annotations

import os
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from gridappsd import GridAPPSD, topics as t

import cim.data_profile as cim
from cim.loaders import ConnectionInterface, QueryResponse


@dataclass
class DistributedModel:
    feeder: cim.Feeder
    connection: ConnectionInterface
    topology_response: QueryResponse
    addressable_equipment: Dict[str, object] = field(default_factory=dict)
    unaddressable_equipment: Dict[str, object] = field(default_factory=dict)
    connectivity_nodes: Dict[str, object] = field(default_factory=dict)
    switch_areas: List[SwitchArea] = field(default_factory=list)

    typed_catalog: dict[type, dict[str, object]] = field(default_factory=dict)
    is_loaded: Optional[set] = field(default_factory=set)

    def __post_init__(self):
        self.__initialize_network__()

    # REPLACE WITH CONNECTION OBJECT

    @staticmethod
    def add_to_catalog(obj: object, catalog: dict) -> dict:
        if obj.mRID == None:
            raise ValueError('Object must contain an mRID')
        if obj.mRID not in catalog:
            catalog[obj.mRID] = obj
        return catalog

    @staticmethod
    def add_to_typed_catalog(obj: object, typed_catalog: dict) -> dict:
        if type(obj) not in typed_catalog:
            typed_catalog[type(obj)] = {}
        if obj.mRID not in typed_catalog[type(obj)]:
            typed_catalog[type(obj)][obj.mRID] = obj
        return typed_catalog

    @staticmethod
    def get_all_by_type(typed_catalog: dict, obj_type: type) -> list[object]:
        objects = typed_catalog.get(obj_type) if typed_catalog.get(obj_type) is not None else []
        for obj in objects:
            if obj.mRID not in self.is_loaded:
                load_all_attributes(obj)

    # Initialize all CIM objects in feeder model
    def __initialize_network__(self) -> Dict[str, object]:
        # Get switch area message from Topology Processor
        # topo_message = DistributedModel.get_topology_api_response(feeder_mrid)
        # topo_message = DistributedModel.get_topology_response(feeder_mrid)

        # Initialize all CIM objects not contained in a switch area
        # def initialize_substation_equipment(feeder_mrid) -> dict(str,object):
        # for feeder_index in range(len(self.topo_message['feeders'])) #implement later
        print(self.topology_response.response)
        addr_equip = self.connection.create_default_instances(self.feeder.mRID,
                                                              self.topology_response.response['feeders'][
                                                                  'addressable_equipment'])
        for obj in addr_equip:
            DistributedModel.add_to_catalog(obj, self.addressable_equipment)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        unaddr_equip = self.connection.create_default_instances(self.feeder.mRID,
                                                                self.topology_response.response['feeders'][
                                                                    'unaddressable_equipment'])
        for obj in unaddr_equip:
            DistributedModel.add_to_catalog(obj, self.unaddressable_equipment)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        conn_nodes = self.connection.create_default_instances(self.feeder.mRID,
                                                              self.topology_response.response['feeders'][
                                                                  'connectivity_node'])
        for obj in conn_nodes:
            DistributedModel.add_to_catalog(obj, self.connectivity_nodes)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)

        # Initialize all CIM objects in a single switch area
        # def initialize_switch_areas(feeder_mrid) -> dict(str,object):
        sa_index = -1
        for switch_msg in self.topology_response.response['feeders']['switch_areas']:
            # Add switch area
            switch_area = SwitchArea(self.feeder.mRID + '.' + str(sa_index), )
            switch_area.initialize_switch_area(switch_msg)
            self.switch_areas.append(switch_area)
            # Add switch area unaddressable equipment to feeder unaddressable equipment
            self.unaddressable_equipment.update(switch_area.unaddressable_equipment)
            sa_index = sa_index + 1

    def get_terminals(self) -> list[cim.Terminal]:
        return self.typed_catalog[cim.Terminal].values()

    def get_object(self, mrid) -> object:
        return self.catalog[mrid]


from cim.models.switch_area import SwitchArea
