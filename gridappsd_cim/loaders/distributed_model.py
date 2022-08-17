from __future__ import annotations

import os, json, time, sys
from typing import List
from dataclasses import dataclass, field
from gridappsd import GridAPPSD, topics as t
from gridappsd_cim import *
from shared_methods import initialize_objects

@dataclass
class DistributedModel:
    feeder: Feeder
    addressable_equipment: dict[str, object] = field(default_factory=dict)
    unaddressable_equipment: dict[str, object] = field(default_factory=dict)
    connectivity_nodes: dict[str, object] = field(default_factory=dict)
    switch_areas: list[obj] = field(default_factory=list)
        
    typed_catalog: dict[type, dict[str,object]] = field(default_factory=dict)
    is_loaded: optional[set] = field(default_factory=set)
    __connection__: optional[connection] = None

    # REPLACE WITH CONNECTION OBJECT
    os.environ['GRIDAPPSD_APPLICATION_ID'] = 'gridappsd-cim-profile'
    os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
    os.environ['GRIDAPPSD_USER'] = 'app_user'
    os.environ['GRIDAPPSD_PASSWORD'] = '1234App'
    gapps = GridAPPSD()
    assert gapps.connected
    
    def add_to_catalog(obj:object, catalog:dict) -> dict:
        if obj.mRID == None: raise ValueError('Object must contain an mRID')
        if obj.mRID not in catalog: catalog[obj.mRID] = obj
        return catalog

    def add_to_typed_catalog(obj:object, typed_catalog:dict) -> dict:
        if type(obj) not in typed_catalog: typed_catalog[type(obj)] = []
        if obj not in typed_catalog[type(obj)]: typed_catalog[type(obj)][obj.mRID] = obj
        return typed_catalog
    
    def get_all_by_type(typed_catalog:dict, obj_type:type) -> list[object]:
        objects = typed_catalog.get(obj_type) if typed_catalog.get(obj_type) is not None else []
        for obj in objects:
            if obj.mRID not in self.is_loaded:
                load_all_attributes(obj)

        
            
    # Get distributed switch areas through GridAPPS-D API call
    def get_topology_api_response(self) -> dict:
        topic = "goss.gridappsd.request.data.topology"
        message = {
           "requestType": "GET_SWITCH_AREAS",
           "modelID": self.feeder.mRID,
           "resultFormat": "JSON"
        }
        self.topo_message = self.gapps.get_response(topic, message, timeout=30)
        return self.topo_message

    # Get distributed switch areas from Topology Library
    def get_topology_response(self) -> dict:
        DistTopo = DistributedTopology(gapps, feeder.mRID)
        self.topo_message = DistTopo.create_switch_areas(feeder_mrid)
        return self.topo_message
    
    
    # Initialize all CIM objects in feeder model   
    def initialize_network(self) -> dict(str,object):
        # Get switch area message from Topology Processor
        #topo_message = DistributedModel.get_topology_api_response(feeder_mrid)
        #topo_message = DistributedModel.get_topology_response(feeder_mrid)
        
    # Initialize all CIM objects not contained in a switch area
    #def initialize_substation_equipment(feeder_mrid) -> dict(str,object):
        # for feeder_index in range(len(self.topo_message['feeders'])) #implement later
        addr_equip = initialize_objects(self.feeder.mRID, self.topo_message['feeders']['addressable_equipment'])
        for obj in addr_equip: DistributedModel.add_to_catalog(obj, self.addressable_equipment)
        for obj in addr_equip: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        unaddr_equip = initialize_objects(self.feeder.mRID, self.topo_message['feeders']['unaddressable_equipment'])
        for obj in unaddr_equip: DistributedModel.add_to_catalog(obj, self.unaddressable_equipment)
        for obj in unaddr_equip: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        conn_nodes = initialize_objects(self.feeder.mRID, self.topo_message['feeders']['connectivity_node'])
        for obj in conn_nodes: DistributedModel.add_to_catalog(obj, self.connectivity_nodes)
        for obj in conn_nodes: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)

    # Initialize all CIM objects in a single switch area
    #def initialize_switch_areas(feeder_mrid) -> dict(str,object):
        sa_index = -1
        for switch_msg in self.topo_message['feeders']['switch_areas']:
            # Add switch area
            switch_area = SwitchArea(feeder_mrid + '.' + str(sa_index))
            switch_area.initialize_switch_area(switch_msg)
            self.switch_areas.append(switch_area)
            # Add switch area unaddressable equipment to feeder unaddressable equipment
            self.unaddressable_equipment.update(switch_area.unaddressable_equipment)
            sa_index = sa_index + 1
            

    def get_terminals() -> list[Terminal]:
        return self.typed_catalog[Terminal]
    
    
    def get_object(self, mrid) -> object:
        return self.catalog[mrid]

    