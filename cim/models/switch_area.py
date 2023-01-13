from __future__ import annotations

import os, json, time, sys
from typing import List
from dataclasses import dataclass, field

import cim.data_profile as cim
from cim.loaders import ConnectionInterface
from cim.models.model_parsers import add_to_catalog, add_to_typed_catalog
from cim.models.secondary_area import SecondaryArea



@dataclass
class SwitchArea:
    area_id: str
    connection: ConnectionInterface
    addressable_equipment: dict[str, object] = field(default_factory=dict)
    unaddressable_equipment: dict[str, object] = field(default_factory=dict)
    boundary_switches: dict[str, object] = field(default_factory=dict)
    connectivity_nodes: dict[str, object] = field(default_factory=dict)
    secondary_areas: list[object] = field(default_factory=list)
    typed_catalog: dict[type, dict[str, object]] = field(default_factory=dict)

    # Initialize empty CIM objects for all equipment in switch area
    def initialize_switch_area(self, switch_msg: dict):
        self.feeder_mrid = self.area_id.split('.')[0]  # get feeder mRID from area id
        addr_equip = self.connection.create_default_instances(self.feeder_mrid, switch_msg['addressable_equipment'])
        for obj in addr_equip:
            add_to_catalog(obj, self.addressable_equipment)
            add_to_typed_catalog(obj, self.typed_catalog)
        unaddr_equip = self.connection.create_default_instances(self.feeder_mrid, switch_msg['unaddressable_equipment'])
        for obj in unaddr_equip:
            add_to_catalog(obj, self.unaddressable_equipment)
            add_to_typed_catalog(obj, self.typed_catalog)
        conn_nodes = self.connection.create_default_instances(self.feeder_mrid, switch_msg['connectivity_node'])
        for obj in conn_nodes:
            add_to_catalog(obj, self.connectivity_nodes)
            add_to_typed_catalog(obj, self.typed_catalog)
        bound_sw = self.connection.create_default_instances(self.feeder_mrid, switch_msg['boundary_switches'])
        for obj in bound_sw:
            add_to_catalog(obj, self.boundary_switches)
            add_to_typed_catalog(obj, self.typed_catalog)

        sa_index = -1
        for sec_area_msg in switch_msg['secondary_areas']:
            # Add switch area
            sec_area = SecondaryArea(self.area_id + '.' + str(sa_index), self.connection)
            sec_area.initialize_secondary_area(sec_area_msg)
            self.secondary_areas.append(sec_area)
            # Add switch area unaddressable equipment to feeder unaddressable equipment
            self.unaddressable_equipment.update(sec_area.unaddressable_equipment)
            sa_index = sa_index + 1

    def get_all_attributes(self, cim_class):
        if cim_class in self.typed_catalog:
            self.connection.get_all_attributes(self.feeder_mrid, self.typed_catalog, cim_class)
#             return self.__dumps__(cim_class)
        
    def __dumps__(self, cim_class):
        mrid_list = list(self.typed_catalog[cim_class].keys())
        attribute_list = list(cim_class().__dict__.keys())
        json_dump = {}

        for mrid in mrid_list:
            json_dump[mrid] = {}
            for attribute in attribute_list:
                value = getattr(self.typed_catalog[cim_class][mrid], attribute)

                if type(value) in [str, list]:
                    json_dump[mrid][attribute] = value
                elif value is None:
                    json_dump[mrid][attribute] = ''
                else:
                    json_dump[mrid][attribute] = value.__dict__

        return json.dumps(json_dump)