import json
import logging
import importlib
from math import dist
import uuid

from dataclasses import dataclass, field

from cimgraph.models.graph_model import GraphModel, new_mrid
from cimgraph.databases import ConnectionInterface

_log = logging.getLogger(__name__)

@dataclass
class DistributedArea(GraphModel):

    def __post_init__(self):
        self.cim_profile = self.connection.cim_profile
        self.cim = self.connection.cim    
        self.graph = {}
        self.distributed_areas = []

    def build_from_topo_message(self, topology_dict, centralized_graph):
        for node_mrid in topology_dict["connectivity_node"]:
            try:
                node = centralized_graph[self.cim.ConnectivityNode][node_mrid]
            except:
                _log.warning("node " + str(node_mrid) + " not in feeder")

            self.add_to_graph(node)
            for terminal in node.Terminals:
                self.add_to_graph(terminal)
                self.add_to_graph(terminal.ConductingEquipment)


            


class DistributedTopology():
    def __init__(self, connection:ConnectionInterface, centralized_graph,
                 root_classes:list[type],
                  upper_boundaries:list[type], lower_boundaries:list[type]):
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
    
    def expand_area(self, root_class, distributed_areas):
        # Iterate through all instances of a switch class
        if root_class in self.centralized_graph:
            for equipment in self.centralized_graph[root_class].values(): 
                # Iterate through both terminals of each switch
                for terminal in equipment.Terminals: 
                    parsed = False
                    for DistArea in distributed_areas: 
                        # Check if this terminal has been parsed in any other graphs
                        if terminal.ConnectivityNode.mRID in DistArea.graph[self.cim.ConnectivityNode].keys():
                            parsed = True
                    if not parsed: # If not parsed, build switch areas from this switch
                        NewArea = self.expand_node(terminal.ConnectivityNode)
                        distributed_areas.append(NewArea)
        return distributed_areas
    
    def expand_node(self, root_node):
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
        container = self.cim.EquipmentContainer(mRID = new_mrid())
        DistArea = DistributedArea(connection=self.connection, container=container, distributed=True)
        DistArea.graph = {}
        DistArea.add_to_graph(root_node)

        parsed_nodes = set()
        all_nodes = set(DistArea.graph[self.cim.ConnectivityNode].keys())
            # all_nodes.append(node)

        while parsed_nodes != all_nodes:
            for node_mrid in list(all_nodes - parsed_nodes):
                node = DistArea.graph[self.cim.ConnectivityNode][node_mrid]
                if node.mRID not in parsed_nodes:
                    # print('start', node.mRID)

                    for terminal in node.Terminals:
                        equipment = terminal.ConductingEquipment
                        DistArea.add_to_graph(terminal)
                        DistArea.add_to_graph(equipment)

                        if equipment.__class__ == self.cim.PowerTransformer:
                            print(equipment.name)
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
                                    # print('tank', tank.name)
                                    if "TransformerTankInfo" in self.cim.TransformerTank.__dataclass_fields__.keys():
                                        if tank.TransformerTankInfo is not None:
                                            # Iterate through xfmr ends to get winding voltage
                                            for end in equipment.TransformerTankInfo.TransformerEndInfos:
                                                voltages = end.ratedU
                                                found_voltages = True
                                            if len(set(voltages)) == 1:
                                                self.expand_terminal(terminal, DistArea)
                                    
                                    if tank.Assets is not None and not found_voltages:
                                        for asset in tank.Assets:
                                            # print(asset.name)
                                            if asset.AssetInfo is not None:
                                                for end in asset.AssetInfo.TransformerEndInfos:
                                                    print(end.ratedU)
                                                    voltages.append(end.ratedU)
                                                    found_voltages = True
                                                if len(set(voltages)) == 1:
                                                    print('regulator')
                                                    self.expand_terminal(terminal, DistArea)

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
                            lower_container = self.cim.EquipmentContainer(mRID = new_mrid())
                            LowerArea = DistributedArea(container = lower_container, connection=self.connection, distributed = True)
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
                if next_node.mRID not in DistArea.graph[self.cim.ConnectivityNode].keys():
                    DistArea.add_to_graph(next_node)
                    DistArea.add_to_graph(next_terminal)

def create_hierarchy_level(network:GraphModel, hierarchy:dict, top_level:bool):
    for level in hierarchy:
        try:
            container_type = level["container"]
            lower_hierarchy = level["contains"]
        except:
            _log.error("""distributed hierarchy must contain "container" and "contains" keys""")
        # Determine container class
        try:
            container_class = eval(f"""network.cim.{container_type}""")
        except:
            _log.error("container is not a valid CIM class")
        
        
        network.get_all_edges(container_class)
        if container_class in network.graph:
            for container in network.graph[container_class].values():
                if not top_level:
                    _log.info("creating new area for " + container_type + ' ' + container.name)
                    NewArea = DistributedArea(container = container, connection=network.connection, distributed = True)
                    NewArea.distributed_areas = {}
                    if container_class not in network.distributed_areas:
                        network.distributed_areas[container_class] = {}
                    network.distributed_areas[container_class][container.mRID] = NewArea
                    NewArea.add_to_graph(container)  
                else:
                    NewArea = network

                NewArea.get_all_edges(container_class)
                if lower_hierarchy is not None and lower_hierarchy != []:
                    NewArea.distributed_areas = create_hierarchy_level(NewArea, lower_hierarchy, top_level=False)
    return network.distributed_areas