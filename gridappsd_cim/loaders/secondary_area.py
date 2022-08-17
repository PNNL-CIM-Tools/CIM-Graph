from __future__ import annotations

import os, json, time, sys
from typing import List
from dataclasses import dataclass, field
from gridappsd import GridAPPSD, topics as t
from gridappsd_cim import *
from shared_methods import initialize_objects

@dataclass
class SecondaryArea:
    area_id: str
    distribution_transformer: dict[str, object] = field(default_factory=dict)
    addressable_equipment: dict[str, object] = field(default_factory=dict)
    unaddressable_equipment: dict[str, object] = field(default_factory=dict)
    boundary_switches: dict[str, object] = field(default_factory=dict)
    connectivity_nodes: dict[str, object] = field(default_factory=dict)
    secondary_areas: list[object] = field(default_factory=list)
    typed_catalog: dict[type, list[object]] = field(default_factory=dict)
    
    # Initialize empty CIM objects for all equipment in secondary area
    def initialize_secondary_area(self, switch_msg: dict):
        feeder_id = self.area_id.split('.')[0] # get feeder mRID from area id
        addr_equip = initialize_objects(feeder_id, switch_msg['addressable_equipment'])
        for obj in addr_equip: DistributedModel.add_to_catalog(obj, self.addressable_equipment)
        for obj in addr_equip: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        unaddr_equip = initialize_objects(feeder_id, switch_msg['unaddressable_equipment'])
        for obj in unaddr_equip: DistributedModel.add_to_catalog(obj, self.unaddressable_equipment)
        for obj in unaddr_equip: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        conn_nodes = initialize_objects(feeder_id, switch_msg['connectivity_node'])
        for obj in conn_nodes: DistributedModel.add_to_catalog(obj, self.connectivity_nodes)
        for obj in conn_nodes: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        xfmr = initialize_objects(feeder_id, switch_msg['distribution_transformer'])
        for obj in xfmr: DistributedModel.add_to_catalog(obj, self.distribution_transformer)
        for obj in xfmr: DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)