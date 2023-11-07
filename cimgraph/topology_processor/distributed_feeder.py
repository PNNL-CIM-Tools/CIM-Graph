import time
import json
import logging

_log = logging.getLogger(__name__)

from cimgraph.databases import ConnectionInterface
from cimgraph.models.graph_model import GraphModel, new_mrid
from cimgraph.models.distributed_area import DistributedArea


class DistributedFeederTopology():

    def __init__(self, connection: ConnectionInterface, switch_classes: list[type] = None):
        self.connection = connection
        self.cim = self.connection.cim
        if switch_classes is None:
            self.switch_classes = [
                self.cim.Breaker, self.cim.Sectionaliser, self.cim.Recloser,
                self.cim.LoadBreakSwitch, self.cim.Switch
            ]    # default switch classes
        else:
            self.switch_classes = switch_classes
        self.boundary_classes - self.switch_classes.append(self.cim.PowerTransformer)

    def build_distributed_feeder(self, centralized_graph):
        distributed_areas = []    # List of distributed graphs

        # Iterate through all types of switches
        for boundary_class in self.switch_classes:
            # Iterate through all instances of a switch class
            if boundary_class in centralized_graph:
                for switch in centralized_graph[boundary_class].values():
                    # Iterate through both terminals of each switch
                    for terminal in switch.Terminals:
                        parsed = False
                        for DistArea in distributed_areas:
                            # Check if this terminal has been parsed in any other graphs
                            if terminal.ConnectivityNode.mRID in DistArea.graph[
                                    self.cim.ConnectivityNode].keys():
                                parsed = True
                        if not parsed:    # If not parsed, build switch areas from this switch
                            NewArea = self.build_distributed_area(centralized_graph,
                                                                  terminal.ConnectivityNode)
                            distributed_areas.append(NewArea)

        return distributed_areas

    def build_distributed_area(self, centralized_graph, root_node):
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
        NewArea = DistributedArea(connection=self.connection,
                                  container=container,
                                  distributed=True)
        NewArea.graph = {}
        NewArea.add_to_graph(root_node)

        parsed_nodes = set()
        all_nodes = set(NewArea.graph[self.cim.ConnectivityNode].keys())
        # all_nodes.append(node)

        while parsed_nodes != all_nodes:
            for node_mrid in list(all_nodes - parsed_nodes):
                node = NewArea.graph[self.cim.ConnectivityNode][node_mrid]
                if node.mRID not in parsed_nodes:
                    # print('start', node.mRID)

                    for terminal in node.Terminals:
                        equipment = terminal.ConductingEquipment
                        NewArea.add_to_graph(terminal)
                        NewArea.add_to_graph(equipment)

                        if type(equipment) in [self.cim.TransformerTank]:
                            if equipment.TransformerEndInfo is not None:
                                voltages = []
                                # Iterate through xfmr ends to get winding voltage
                                for end in equipment.TransformerTankInfo.TransformerEndInfos:
                                    voltages.append(end.ratedU)
                                # If all xfmr ends have the same voltage, then it is a regulator
                                if len(set(voltages)) == 1:
                                    self.get_topo_edges(equipment, NewArea)

                        elif type(equipment) not in self.boundary_devices:
                            self.get_topo_edges(equipment, NewArea)

                    parsed_nodes.add(node.mRID)

            all_nodes = set(NewArea.graph[self.cim.ConnectivityNode].keys())
        return NewArea

    def get_topo_edges(self, equipment, DistArea):
        for next_terminal in equipment.Terminals:
            next_node = next_terminal.ConnectivityNode
            if next_node not in DistArea.graph[self.cim.ConnectivityNode]:
                DistArea.add_to_graph(next_node)
                DistArea.add_to_graph(next_terminal)

    def build_topo_island(self, root_node):
        """
        Creates graph for a topological island
            Args:
                container_mRID (str | Feeder object): The mRID of the feeder or feeder object
                graph (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by
                    class type and object mRID
                cim_class (type): The CIM class type (e.g. cim:ACLineSegment)
            Returns:
                graph
            none
        """

        area = DistributedArea()
        area.graph = {}
        area.add_to_graph(root_node)

        parsed_nodes = set()
        all_nodes = set(area.graph[self.cim.ConnectivityNode].keys())
        # all_nodes.append(node)

        while parsed_nodes != all_nodes:
            for node_mrid in list(all_nodes - parsed_nodes):
                node = area.graph[self.cim.ConnectivityNode][node_mrid]
                if node.mRID not in parsed_nodes:
                    # print('start', node.mRID)

                    for terminal in node.Terminals:
                        equipment = terminal.ConductingEquipment
                        just_parsed = [terminal]
                        area.add_to_graph(terminal)
                        area.add_to_graph(equipment)
                        if type(equipment) in self.switch_classes:
                            if equipment.open == 'false':
                                for next_terminal in equipment.Terminals:
                                    next_node = next_terminal.ConnectivityNode

                                    if next_node.mRID not in area.graph[
                                            self.cim.ConnectivityNode].keys():
                                        area.add_to_graph(next_node)
                                        area.add_to_graph(next_terminal)
                                        just_parsed.append(next_terminal)
