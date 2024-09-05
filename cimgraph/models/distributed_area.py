import importlib
import logging
from dataclasses import dataclass, field
from uuid import UUID

from cimgraph.databases import ConnectionInterface
from cimgraph.models.graph_model import GraphModel, new_mrid

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

    def build_from_topo_message(self, topology_dict: dict, centralized_graph: dict = {}):
        AddrEquip = AddressableEquipment(self.cim)
        UnaddrEquip = UnaddressableEquipment(self.cim)
        if centralized_graph:
            for node_mrid in topology_dict['connectivity_node']:
                try:
                    uuid = UUID(node_mrid.strip('_').lower())
                    node = centralized_graph[self.cim.ConnectivityNode][uuid]
                    self.add_to_graph(node)
                    for terminal in node.Terminals:
                        self.add_to_graph(terminal)
                        self.add_to_graph(terminal.ConductingEquipment)
                except:
                    _log.warning('node ' + str(uuid) + ' not in feeder')


        else:
            node_list = topology_dict['connectivity_node']
            self.connection.build_graph_from_list(self.graph, node_list)
            self.addressable_equipment = {}
            self.unaddressable_equipment = {}
            AddrEquip.identify_addressable(addressable_equipment=self.addressable_equipment, graph=self.graph)
            UnaddrEquip.identify_unaddressable(unaddressable_equipment=self.unaddressable_equipment, graph=self.graph)

            if 'switch_areas' in topology_dict:
                sw_counter = -1
                for switch_topo in topology_dict['switch_areas']:
                    sw_counter = sw_counter + 1
                    node_list = switch_topo['connectivity_node']
                    self.connection.build_graph_from_list(self.graph, node_list)
                    # Create a new DistributedArea object for each switch area in message
                    switch_area_id = str(
                        self.container.mRID) + '.' + str(sw_counter)
                    switch_container = self.cim.EquipmentContainer(mRID=switch_area_id)
                    SwitchArea = DistributedArea(connection=self.connection,
                                                 container=switch_container,
                                                 distributed=True)
                    SwitchArea.build_from_topo_message(switch_topo, self.graph)
                    # Identify addressable and unaddressable
                    SwitchArea.addressable_equipment = {}
                    SwitchArea.unaddressable_equipment = {}
                    UnaddrEquip.identify_unaddressable(
                        unaddressable_equipment=self.unaddressable_equipment,
                        graph=SwitchArea.graph)
                    UnaddrEquip.identify_unaddressable(
                        unaddressable_equipment=SwitchArea.
                        unaddressable_equipment,
                        graph=SwitchArea.graph)
                    AddrEquip.identify_addressable(
                        addressable_equipment=SwitchArea.addressable_equipment,
                        graph=SwitchArea.graph)
                    AddrEquip.identify_addressable(
                        addressable_equipment=self.unaddressable_equipment,
                        graph=SwitchArea.graph)
                    # Add to FeederArea
                    SwitchArea.distributed_areas = [
                    ]  # Initialize secondary areas list
                    self.distributed_areas.append(
                        SwitchArea)  # Add new DistributedArea class to list

                    if 'secondary_areas' in switch_topo:
                        sa_counter = -1
                        for secondary_topo in switch_topo['secondary_areas']:
                            sa_counter = sa_counter + 1
                            node_list = secondary_topo['connectivity_node']
                            self.connection.build_graph_from_list(
                                self.graph, node_list)
                            sec_area_id = str(self.container.mRID) + '.' + str(
                                sw_counter) + '.' + str(sa_counter)
                            secondary_container = self.cim.EquipmentContainer(
                                mRID=sec_area_id)
                            SecondaryArea = DistributedArea(
                                connection=self.connection,
                                container=secondary_container,
                                distributed=True)
                            SecondaryArea.build_from_topo_message(
                                secondary_topo, self.graph)
                            SwitchArea.distributed_areas.append(SecondaryArea)
                            SecondaryArea.addressable_equipment = {}
                            SecondaryArea.unaddressable_equipment = {}
                            UnaddrEquip.identify_unaddressable(
                                unaddressable_equipment=self.
                                unaddressable_equipment,
                                graph=SecondaryArea.graph)
                            UnaddrEquip.identify_unaddressable(
                                unaddressable_equipment=SwitchArea.
                                unaddressable_equipment,
                                graph=SecondaryArea.graph)
                            UnaddrEquip.identify_unaddressable(
                                unaddressable_equipment=SecondaryArea.
                                unaddressable_equipment,
                                graph=SecondaryArea.graph)
                            AddrEquip.identify_addressable(
                                addressable_equipment=self.
                                unaddressable_equipment,
                                graph=SecondaryArea.graph)
                            AddrEquip.identify_addressable(
                                addressable_equipment=SwitchArea.
                                unaddressable_equipment,
                                graph=SecondaryArea.graph)
                            AddrEquip.identify_addressable(
                                addressable_equipment=SecondaryArea.
                                addressable_equipment,
                                graph=SecondaryArea.graph)

            if 'secondary_areas' in topology_dict:
                sa_counter = -1
                for secondary_topo in topology_dict['secondary_areas']:
                    sa_counter = sa_counter + 1
                    node_list = secondary_topo['connectivity_node']
                    self.connection.build_graph_from_list(
                        self.graph, node_list)
                    secondary_container = self.cim.EquipmentContainer(
                        mRID=self.container.mRID + '.' + str(sa_counter))
                    SecondaryArea = DistributedArea(
                        connection=self.connection,
                        container=secondary_container,
                        distributed=True)
                    SecondaryArea.build_from_topo_message(
                        secondary_topo, self.graph)
                    SecondaryArea.addressable_equipment = {}
                    SecondaryArea.unaddressable_equipment = {}
                    UnaddrEquip.identify_unaddressable(
                        unaddressable_equipment=self.unaddressable_equipment,
                        graph=SecondaryArea.graph)
                    UnaddrEquip.identify_unaddressable(
                        unaddressable_equipment=SecondaryArea.
                        unaddressable_equipment,
                        graph=SecondaryArea.graph)
                    AddrEquip.identify_addressable(
                        addressable_equipment=self.unaddressable_equipment,
                        graph=SecondaryArea.graph)
                    AddrEquip.identify_addressable(
                        addressable_equipment=SecondaryArea.
                        addressable_equipment,
                        graph=SecondaryArea.graph)
                    self.distributed_areas.append(SecondaryArea)


class DistributedTopology():

    def __init__(self, connection: ConnectionInterface, centralized_graph,
                 root_classes: list[type], upper_boundaries: list[type],
                 lower_boundaries: list[type]):
        self.connection = connection
        self.cim = self.connection.cim
        self.centralized_graph = centralized_graph
        self.root_classes = root_classes
        self.upper_boundaries = upper_boundaries
        self.lower_boundaries = lower_boundaries

    def create_distributed_areas(self):
        distributed_areas = []
        # Iterate through all types of switches
        for root_class in self.root_classes:
            distributed_areas = self.expand_area(root_class, distributed_areas)
        # for DistArea in distributed_areas:
        #     for lower_bound_class in self.lower_boundaries:

        return distributed_areas

    def expand_area(
            self, root_class: type,
            distributed_areas: list[DistributedArea]) -> list[DistributedArea]:
        # Iterate through all instances of a switch class
        if root_class in self.centralized_graph:
            for equipment in self.centralized_graph[root_class].values():
                # Iterate through both terminals of each switch
                for terminal in equipment.Terminals:
                    parsed = False
                    for DistArea in distributed_areas:
                        # Check if this terminal has been parsed in any other graphs
                        if terminal.ConnectivityNode.mRID in DistArea.graph[
                                self.cim.ConnectivityNode].keys():
                            parsed = True
                    if not parsed:  # If not parsed, build switch areas from this switch
                        NewArea = self.expand_node(terminal.ConnectivityNode)
                        distributed_areas.append(NewArea)
        return distributed_areas

    def expand_node(self, root_node: object) -> DistributedArea:
        """
        Creates graph for a switch area
            Args:
                container_mRID (str | Feeder object): The mRID of the feeder or feeder object
                graph (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by
                    class type and object mRID
                cim_class (type): The CIM class type (e.g. cim:ACLineSegment)
            Returns:
                graph
            none
        """
        container = self.cim.EquipmentContainer(mRID=new_mrid())
        DistArea = DistributedArea(connection=self.connection,
                                   container=container,
                                   distributed=True)
        DistArea.graph = {}
        DistArea.add_to_graph(root_node)

        parsed_nodes = set()
        all_nodes = set(DistArea.graph[self.cim.ConnectivityNode].keys())
        # all_nodes.append(node)

        while parsed_nodes != all_nodes:
            for node_mrid in list(all_nodes - parsed_nodes):
                node = DistArea.graph[self.cim.ConnectivityNode][node_mrid]
                if node.mRID not in parsed_nodes:

                    for terminal in node.Terminals:
                        equipment = terminal.ConductingEquipment
                        DistArea.add_to_graph(terminal)
                        DistArea.add_to_graph(equipment)

                        if equipment.__class__ == self.cim.PowerTransformer:
                            found_voltages = False
                            voltages = []
                            if equipment.PowerTransformerEnd is not None:
                                for end in equipment.PowerTransformerEnd:
                                    voltages.append(end.ratedU)
                                    found_voltages = True
                                if len(set(voltages)) == 1:
                                    self.expand_terminal(terminal, DistArea)

                            if equipment.TransformerTanks is not None and not found_voltages:
                                for tank in equipment.TransformerTanks:
                                    if 'TransformerTankInfo' in self.cim.TransformerTank.__dataclass_fields__.keys(
                                    ):
                                        if tank.TransformerTankInfo is not None:
                                            # Iterate through xfmr ends to get winding voltage
                                            for end in tank.TransformerTankInfo.TransformerEndInfos:
                                                voltages = end.ratedU
                                                found_voltages = True
                                            if len(set(voltages)) == 1:
                                                self.expand_terminal(
                                                    terminal, DistArea)

                                    if tank.Assets is not None and not found_voltages:
                                        for asset in tank.Assets:
                                            if asset.AssetInfo is not None:
                                                for end in asset.AssetInfo.TransformerEndInfos:
                                                    voltages.append(end.ratedU)
                                                    found_voltages = True
                                                if len(set(voltages)) == 1:
                                                    self.expand_terminal(
                                                        terminal, DistArea)

                        # if terminal.TransformerEnd is not None:
                        #     voltages = []
                        #     for end in terminal.TransformerEnd:
                        #         voltages.append(end.BaseVoltage.nominalVoltage)
                        #         # If all xfmr ends have the same voltage, then it is a regulator
                        #         if len(set(voltages)) == 1:
                        #             self.expand_terminal(terminal, DistArea)
                        #         else:
                        #             continue

                        if type(equipment) in self.lower_boundaries:
                            lower_container = self.cim.EquipmentContainer(
                                mRID=new_mrid())
                            LowerArea = DistributedArea(
                                container=lower_container,
                                connection=self.connection,
                                distributed=True)
                            self.expand_terminal(terminal, LowerArea)
                            DistArea.distributed_areas.append(LowerArea)

                        elif type(equipment) in self.upper_boundaries:
                            pass

                        elif type(equipment):
                            self.expand_terminal(terminal, DistArea)

                    parsed_nodes.add(node.mRID)

            all_nodes = set(DistArea.graph[self.cim.ConnectivityNode].keys())
        return DistArea

    def expand_equipment(self, equipment, DistArea):
        for next_terminal in equipment.Terminals:
            next_node = next_terminal.ConnectivityNode
            if next_node not in DistArea.graph[self.cim.ConnectivityNode]:
                DistArea.add_to_graph(next_node)
                DistArea.add_to_graph(next_terminal)

    def expand_terminal(self, root_terminal, DistArea):
        equipment = root_terminal.ConductingEquipment
        for next_terminal in equipment.Terminals:
            if next_terminal != root_terminal:
                next_node = next_terminal.ConnectivityNode
                if next_node.mRID not in DistArea.graph[
                        self.cim.ConnectivityNode].keys():
                    DistArea.add_to_graph(next_node)
                    DistArea.add_to_graph(next_terminal)


def create_hierarchy_level(network: GraphModel, hierarchy: dict,
                           top_level: bool) -> list[DistributedArea]:
    for level in hierarchy:
        try:
            container_type = level['container']
            lower_hierarchy = level['contains']
        except:
            _log.error(
                """distributed hierarchy must contain "container" and "contains" keys"""
            )
        # Determine container class
        try:
            container_class = eval(f"""network.cim.{container_type}""")
        except:
            _log.error('container is not a valid CIM class')

        network.get_all_edges(container_class)
        if container_class in network.graph:
            containers = list(network.graph[container_class].keys())
            for container_id in containers:
                container = network.graph[container_class][container_id]
                if not top_level:
                    _log.info('creating new area for ' + container_type + ' ' +
                              container.name)
                    NewArea = DistributedArea(container=container,
                                              connection=network.connection,
                                              distributed=True)
                    NewArea.distributed_areas = {}
                    if container_class not in network.distributed_areas:
                        network.distributed_areas[container_class] = {}
                    network.distributed_areas[container_class][
                        container.mRID] = NewArea
                    NewArea.add_to_graph(container)
                else:
                    NewArea = network

                NewArea.get_all_edges(container_class)
                if lower_hierarchy is not None and lower_hierarchy != []:
                    NewArea.distributed_areas = create_hierarchy_level(
                        NewArea, lower_hierarchy, top_level=False)
    return network.distributed_areas


@dataclass
class AddressableEquipment:

    def __init__(self, cim):
        self.cim = cim
        self.addressable_classes = [
            self.cim.AsynchronousMachine, self.cim.Breaker,
            self.cim.Disconnector, self.cim.EnergyConsumer,
            self.cim.LinearShuntCompensator, self.cim.LoadBreakSwitch,
            self.cim.PowerElectronicsConnection, self.cim.RatioTapChanger,
            self.cim.Sectionaliser, self.cim.ShuntCompensator, self.cim.Switch,
            self.cim.SynchronousMachine
        ]

    def identify_addressable(self, addressable_equipment: dict,
                             graph: dict) -> None:
        for class_type in self.addressable_classes:
            if class_type in graph:
                if class_type not in addressable_equipment:
                    addressable_equipment[class_type] = {}
                for mrid in graph[class_type]:
                    addressable_equipment[class_type][mrid] = graph[
                        class_type][mrid]


@dataclass
class UnaddressableEquipment:

    def __init__(self, cim):
        self.cim = cim
        self.unaddressable_classes = [
            self.cim.ACLineSegment, self.cim.EnergySource, self.cim.Fuse,
            self.cim.PowerTransformer, self.cim.TransformerTank
        ]

    def identify_unaddressable(self, unaddressable_equipment: dict,
                               graph: dict) -> None:
        for class_type in self.unaddressable_classes:
            if class_type in graph:
                if class_type not in unaddressable_equipment:
                    unaddressable_equipment[class_type] = {}
                for mrid in graph[class_type]:
                    unaddressable_equipment[class_type][mrid] = graph[
                        class_type][mrid]


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
