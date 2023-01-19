from __future__ import annotations

import os, json, time, sys
from typing import List
from dataclasses import dataclass, field

import cimlab.data_profile as cim
from cimlab.loaders import ConnectionInterface
from cimlab.models.model_parsers import add_to_catalog, add_to_typed_catalog, cim_dump
from cimlab.models.secondary_area import SecondaryArea



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
        else:
            print('warning: no instances of ', cim_class.__name__, ' found in catalog.')
#             return self.__dumps__(cim_class)

    def get_attributes_query(self, cim_class):
        if cim_class in self.typed_catalog:
            sparql_message = self.connection.get_attributes_query(self.feeder_mrid, self.typed_catalog, cim_class)
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