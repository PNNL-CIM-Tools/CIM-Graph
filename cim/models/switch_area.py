from __future__ import annotations

import os, json, time, sys
from typing import List
from dataclasses import dataclass, field
from gridappsd import GridAPPSD, topics as t

from cim.loaders import ConnectionInterface
from cim.models.distributed_model import DistributedModel
from cim.models.secondary_area import SecondaryArea
from gridappsd_cim import *


@dataclass
class SwitchArea:
    area_id: str
    addressable_equipment: dict[str, object] = field(default_factory=dict)
    unaddressable_equipment: dict[str, object] = field(default_factory=dict)
    boundary_switches: dict[str, object] = field(default_factory=dict)
    connectivity_nodes: dict[str, object] = field(default_factory=dict)
    secondary_areas: list[object] = field(default_factory=list)
    typed_catalog: dict[type, dict[str, object]] = field(default_factory=dict)

    # Initialize empty CIM objects for all equipment in switch area
    def initialize_switch_area(self, switch_msg: dict, connection: ConnectionInterface):
        feeder_id = self.area_id.split('.')[0]  # get feeder mRID from area id
        cn = connection
        addr_equip = cn.create_default_instances(feeder_id, switch_msg['addressable_equipment'])
        for obj in addr_equip:
            DistributedModel.add_to_catalog(obj, self.addressable_equipment)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        unaddr_equip = cn.create_default_instances(feeder_id, switch_msg['unaddressable_equipment'])
        for obj in unaddr_equip:
            DistributedModel.add_to_catalog(obj, self.unaddressable_equipment)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        conn_nodes = cn.create_default_instances(feeder_id, switch_msg['connectivity_node'])
        for obj in conn_nodes:
            DistributedModel.add_to_catalog(obj, self.connectivity_nodes)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)
        bound_sw = cn.create_default_instances(feeder_id, switch_msg['boundary_switches'])
        for obj in bound_sw:
            DistributedModel.add_to_catalog(obj, self.boundary_switches)
            DistributedModel.add_to_typed_catalog(obj, self.typed_catalog)

        # sa_index = -1
        # for sec_area_msg in switch_msg['secondary_areas']:
        #     # Add switch area
        #     sec_area = SecondaryArea(self.feeder.mRID + '.' + str(sa_index))
        #     sec_area.initialize_secondary_area(sec_area_msg)
        #     self.secondary_areas.append(sec_area)
        #     # Add switch area unaddressable equipment to feeder unaddressable equipment
        #     self.unaddressable_equipment.update(sec_area.unaddressable_equipment)
        #     sa_index = sa_index + 1
