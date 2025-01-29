import importlib
import logging
from dataclasses import dataclass, field
from uuid import UUID

from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


@dataclass
class DistributedArea(GraphModel):

    def __post_init__(self):
        self.cim_profile = self.connection.cim_profile
        self.cim = self.connection.cim
        self.graph = {}
        self.add_to_graph(self.container)
        self.distributed_areas = []
        self.boundaries = []

    def build_from_area(self) -> None:
        self.get_all_edges(self.container.__class__)
        self.connection.create_distributed_graph(area=self.container, graph=self.graph)


    # Build the distributed model from a topology message from GridAPPS-D
    def build_from_topo_message(self, topology_dict:dict):
        # Set base as
        self.container = self.add_jsonld_to_graph(topology_dict)

        # builder for Feeder, Substation, VoltageLevel, and Bay
        if isinstance(self.container, self.cim.EquipmentContainer):
            for addr_eq in topology_dict['AddressableEquipment']:
                equipment = self.add_jsonld_to_graph(addr_eq)
                equipment.EquipmentContainer = self.container

            for unaddr_eq in topology_dict['AddressableEquipment']:
                equipment = self.add_jsonld_to_graph(unaddr_eq)
                equipment.EquipmentContainer = self.container

            for meas in topology_dict['Measurements']:
                self.add_jsonld_to_graph(meas)


        elif isinstance(self.container, self.cim.SubSchedulingArea):
            for boundary in topology_dict['BoundaryTerminals']:
                terminal = self.add_jsonld_to_graph(boundary)
                self.container.BoundaryTerminals.append(terminal)

            for addr_eq in topology_dict['AddressableEquipment']:
                equipment = self.add_jsonld_to_graph(addr_eq)
                equipment.SubSchedulingArea = self.container

            for unaddr_eq in topology_dict['AddressableEquipment']:
                equipment = self.add_jsonld_to_graph(unaddr_eq)
                equipment.SubSchedulingArea = self.container

            for meas in topology_dict['Measurements']:
                self.add_jsonld_to_graph(meas)
