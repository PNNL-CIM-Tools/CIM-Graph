import importlib
import logging
from dataclasses import dataclass, field
from uuid import UUID

from cimgraph.databases import ConnectionInterface
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


def create_subgeographical_area(
        connection: ConnectionInterface,
        subgeographicalregion: object,
        distributed: bool = True,
        aggregate_lower: bool = True) -> DistributedArea:
    cim_profile = connection.connection_params.cim_profile
    cim = importlib.import_module(f'cimgraph.data_profile.{cim_profile}')
    SubGeographicalArea = DistributedArea(connection=connection,
                                          container=subgeographicalregion,
                                          distributed=distributed)
    SubGeographicalArea.get_all_edges(cim.SubGeographicalRegion)
    # SubGeographicalArea.get_all_edges(cim.ConnectivityNode)
    # SubstationArea.connection.create_new_graph(substation)

    if distributed:
        SubGeographicalArea.distributed_areas = {}
        # Create nested Substation areas
        if cim.Substation in SubGeographicalArea.graph:
            SubGeographicalArea.distributed_areas[cim.Substation] = {}
            for substation in SubGeographicalArea.graph[
                    cim.Substation].values():
                SubstationArea = create_substation_area(connection, substation)
                SubGeographicalArea.distributed_areas[cim.Substation][
                    substation.mRID] = SubstationArea
                if aggregate_lower:
                    aggregate_equipment(SubGeographicalArea.graph,
                                        SubstationArea.graph)

    return SubGeographicalArea


def create_substation_area(connection: ConnectionInterface,
                           substation: object,
                           distributed=True,
                           aggregate_lower=True) -> DistributedArea:
    cim_profile = connection.connection_params.cim_profile
    cim = importlib.import_module(f'cimgraph.data_profile.{cim_profile}')
    SubstationArea = DistributedArea(connection=connection,
                                     container=substation,
                                     distributed=distributed)
    SubstationArea.get_all_edges(cim.Substation)
    SubstationArea.get_all_edges(cim.ConnectivityNode)
    SubstationArea.connection.create_new_graph(substation)

    if distributed:
        # Create nested VoltageLevel areas
        if cim.VoltageLevel in SubstationArea.graph:
            for voltage_level in SubstationArea.graph[
                    cim.VoltageLevel].values():
                VoltageLevelArea = create_voltage_level_area(
                    connection, voltage_level)
                SubstationArea.distributed_areas.append(VoltageLevelArea)
                if aggregate_lower:
                    aggregate_equipment(SubstationArea.graph,
                                        VoltageLevelArea.graph)
        # Create nested Bay areas
        if cim.Bay in SubstationArea.graph:
            for bay in SubstationArea.graph[cim.Bay].values():
                BayArea = create_bay_area(connection, bay)
                SubstationArea.distributed_areas.append(BayArea)
                if aggregate_lower:
                    aggregate_equipment(SubstationArea.graph, BayArea.graph)

        # Create nested Feeder areas
        if cim.Feeder in SubstationArea.graph:
            for feeder in SubstationArea.graph[cim.Feeder].values():
                FeederArea = create_feeder_area(connection, feeder)
                SubstationArea.distributed_areas.append(FeederArea)

    return SubstationArea


def create_voltage_level_area(connection: ConnectionInterface,
                              voltage_level: object,
                              distributed=True,
                              aggregate_lower=True) -> DistributedArea:
    cim_profile = connection.connection_params.cim_profile
    cim = importlib.import_module(f'cimgraph.data_profile.{cim_profile}')
    VoltageLevelArea = DistributedArea(connection=connection,
                                       container=voltage_level,
                                       distributed=distributed)
    VoltageLevelArea.get_all_edges(cim.VoltageLevel)
    # VoltageLevelArea.get_all_edges(cim.ConnectivityNode)
    # VoltageLevelArea.connection.create_new_graph(voltage_level)

    if distributed:
        if cim.Bay in VoltageLevelArea.graph:
            for bay in VoltageLevelArea.graph[cim.Bay].values():
                BayArea = DistributedArea(connection=connection,
                                          container=bay,
                                          distributed=True)
                VoltageLevelArea.distributed_areas.append(BayArea)
                if aggregate_lower:
                    aggregate_equipment(VoltageLevelArea.graph, BayArea.graph)

    return VoltageLevelArea


def create_bay_area(connection: ConnectionInterface,
                    bay: object,
                    distributed=True) -> DistributedArea:
    cim_profile = connection.connection_params.cim_profile
    cim = importlib.import_module(f'cimgraph.data_profile.{cim_profile}')
    BayArea = DistributedArea(connection=connection,
                              container=bay,
                              distributed=distributed)
    BayArea.get_all_edges(cim.Bay)
    BayArea.get_all_edges(cim.ConnectivityNode)
    # VoltageLevelArea.connection.create_new_graph(bay)
    return BayArea


def create_feeder_area(connection: ConnectionInterface,
                       feeder: object,
                       distributed=True) -> DistributedArea:
    cim_profile = connection.connection_params.cim_profile
    cim = importlib.import_module(f'cimgraph.data_profile.{cim_profile}')
    FeederArea = DistributedArea(connection=connection,
                                 container=feeder,
                                 distributed=distributed)
    FeederArea.get_all_edges(cim.Feeder)
    FeederArea.get_all_edges(cim.ConnectivityNode)
    # FeederArea.connection.create_new_graph(feeder)

    # if distributed:
    #     for switch in FeederArea.graph[cim.LoadBreakSwitch]:
    #         create_switch_area()
    return FeederArea


def aggregate_equipment(parent_graph: DistributedArea,
                        child_graph: DistributedArea) -> None:
    for cim_class in child_graph:
        if cim_class not in parent_graph:
            parent_graph[cim_class] = {}
        parent_graph[cim_class].update(child_graph[cim_class])

        # for obj in child_area.graph[cim_class].values():
        #     parent_area.add_to_graph(obj)


def create_switch_area():
    pass


def create_secondary_area():
    pass
