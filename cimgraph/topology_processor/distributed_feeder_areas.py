import time
import json
import importlib
import uuid

from cimgraph.topology_processor.linknet import LinkNet
from cimgraph.models import SwitchArea, SecondaryArea
# from cimgraph.models.model_parsers import add_to_graph

class DistributedFeederTopology():
    
    def __init__(self, connection, cim_profile, centralized_graph):
        self.centralized_graph = centralized_graph
        self.graph = {}
        self.connection = connection
        self.cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)

        self.Topology = LinkNet(cim_profile, self.centralized_graph)
        self.MVTopology = LinkNet(cim_profile, self.centralized_graph)
        


    def create_distributed_graph(self):
        AllNodes = list(self.centralized_graph[self.cim.ConnectivityNode].keys())
        ProcessedNodes = []
        switch_areas = []
        sa_index = -1
        boundary_classes = [self.cim.Breaker, self.cim.LoadBreakSwitch, self.cim.Recloser, self.cim.Sectionaliser]
        self.create_switch_areas(boundary_classes)
        for cim_class in boundary_classes:
            if cim_class in self.centralized_graph:
                for device in self.centralized_graph[cim_class].values():
                    node1 = device.Terminals[1].ConnectivityNode
                    if node1.ConnectivityNodeContainer is None:
                        sa_index = sa_index + 1
                        sa_area_id = list(self.centralized_graph[self.cim.Feeder].keys())[0] + '.' + str(sa_index)
                        sa_uuid = str(uuid.uuid4())
                        sa_container = self.cim.ConnectivityNodeContainer(name=sa_area_id, mRID=sa_uuid)
                        switch_areas.append(SwitchArea(area_id=sa_area_id, uuid=sa_uuid, connection=self.connection))
                        sca_index = -1
                        switch_areas[sa_index].boundary_switches.append(device.mRID)
                        node1.ConnectivityNodeContainer = sa_container

                    for node in self.MVTree[device.mRID]:
                        node.ConnectivityNodeContainer = sa_container
                        switch_areas[sa_index].connectivity_nodes.append(node.mRID)
                        add_to_graph(node, switch_areas[sa_index].graph)
                        ProcessedNodes.append(node.mRID)
                        for terminal in node.Terminals:
                            add_to_graph(terminal, switch_areas[sa_index].graph)
                            equipment = terminal.ConductingEquipment
                            add_to_graph(equipment, switch_areas[sa_index].graph)
#                             if equipment.__class__ == self.cim.PowerTransformer: #, cim.TransformerTank]:
#                                 xfmr = equipment.mRID
#                                 LVTree = self.Topology.spanning_tree(equipment.__class__, xfmr, self.MVTree, 'all')
#                                 LVTreeKeys = LVTree[xfmr]
#                                 if LVTreeKeys: 
#                                     sca_index = sca_index + 1
#                                     sca_area_id = sa_area_id + '.' + str(sca_index)
#                                     sca_uuid = uuid.uuid4()
#                                     sca_container = self.cim.ConnectivityNodeContainer(name=sca_area_id, mRID=sca_uuid)
#                                     secondary_area = SecondaryArea(area_id=sca_area_id, uuid=sca_uuid)
#                                     secondary_area.distribution_transformer.append(xfmr)
#                                     for lvnode in LVTreeKeys.values():
#                                         if lvnode.ConnectivityNodeContainer is not None:
#                                             lvnode.ConnectivityNodeContainer = sca_container
#                                             secondary_area.connectivity_nodes.append(lvnode.mRID)
#                                             add_to_graph(lvnode, secondary_area.graph)
#                                             ProcessedNodes.append(lvnode.mRID)
#                                             for lv_terminal in lvnode.Terminals:
#                                                 add_to_graph(lv_terminal, secondary_area.graph)
#                                                 equipment = terminal.ConductingEquipment
#                                                 add_to_graph(equipment, secondary_area.graph)
#                                     switch_areas[sa_index].secondary_areas.append(secondary_area)
        MissingNodes = list(set(AllNodes).difference(ProcessedNodes))
        for node_id in MissingNodes:
            node = self.centralized_graph[self.cim.ConnectivityNode][node_id]
            add_to_graph(node, self.graph)
            for terminal in node.Terminals:
                add_to_graph(terminal, self.graph)
                equipment = terminal.ConductingEquipment
                add_to_graph(equipment, self.graph)
        return switch_areas, self.graph

            
        
        
    def create_switch_areas(self, boundary_classes):

        EqTypes = [self.cim.ACLineSegment, self.cim.PowerTransformer,# self.cim.TransformerTank, 
                   self.cim.SynchronousMachine, self.cim.Fuse, self.cim.Disconnector]
        self.Topology.build_linknet(EqTypes)
        EqTypes = [self.cim.ACLineSegment, self.cim.RatioTapChanger, self.cim.SynchronousMachine, 
                   self.cim.Fuse, self.cim.Disconnector]
        self.MVTopology.build_linknet(EqTypes)
        self.MVTree = {}
        for cim_class in boundary_classes:
            if cim_class in self.centralized_graph:
                device_mrids = list(self.centralized_graph[cim_class].keys())
                self.MVTree = self.MVTopology.spanning_tree(cim_class, device_mrids , self.MVTree, 'all')
        
        
    
        
        
    def create_output_message(self):
        self.create_switch_areas()
        #Initialize output message structure
        self.DistAppStruct = {}
        self.DistAppStruct['feeders'] = {}
        self.DistAppStruct['feeders']['feeder_id'] = model_mrid
        self.DistAppStruct['feeders']['addressable_equipment'] = []
        self.DistAppStruct['feeders']['unaddressable_equipment'] = []
        self.DistAppStruct['feeders']['connectivity_node'] = []
        self.DistAppStruct['feeders']['switch_areas'] = []
        ProcessedNodes = [] # List to keep track of which nodes have been processed
        SwitchKeys = list(MVTree.keys()) # Get list of all switching devices from all CIM classes
        # Iterate through all switches
        sa_index = 0
        for i1 in range(len(SwitchKeys)):
            # Initialize switch area dictionary
            switch_area = SwitchArea
#             switch_area['boundary_switches'] = []
#             switch_area['addressable_equipment'] = []
#             switch_area['unaddressable_equipment'] = []
            switch_area['connectivity_node'] = []
            switch_area['secondary_areas'] = []
            # Initialize secondary area dictionary
            DistArea = {}
            DistArea['distribution_transformer'] = []
            DistArea['addressable_equipment'] = []
            DistArea['unaddressable_equipment'] = []
            DistArea['connectivity_node'] = []
            DistAreaFlag1 = True
            for i2 in range(len(MVTree[SwitchKeys[i1]])):
                # Select next medium-voltage node, append to processed list
                node = MVTree[SwitchKeys[i1]][i2]
                ProcessedNodes.append(node)
                # Add all connected equipment
                switch_area['boundary_switches'].extend(ConnNodeDict[node]['Breaker'])
                switch_area['boundary_switches'].extend(ConnNodeDict[node]['Fuse'])
                switch_area['boundary_switches'].extend(ConnNodeDict[node]['LoadBreakSwitch'])
                switch_area['boundary_switches'].extend(ConnNodeDict[node]['Recloser'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['SynchronousMachine'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['PowerElectronicsConnection'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['LinearShuntCompensator'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['RatioTapChanger'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['EnergyConsumer'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['House'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['BatteryUnit'])
                switch_area['addressable_equipment'].extend(ConnNodeDict[node]['PhotovoltaicUnit'])
                switch_area['unaddressable_equipment'].extend(ConnNodeDict[node]['ACLineSegment'])
                switch_area['unaddressable_equipment'].extend(ConnNodeDict[node]['PowerTransformer'])
                switch_area['unaddressable_equipment'].extend(ConnNodeDict[node]['TransformerTank'])
                switch_area['unaddressable_equipment'].extend(ConnNodeDict[node]['Measurement'])
                switch_area['connectivity_node'].append(node)
                # Identify PowerTransformer and TransformerTanks for secondary areas
                DistXfmrTanks = ConnNodeDict[node]['TransformerTank'] 
                DistXfmrs = ConnNodeDict[node]['PowerTransformer']
                if DistXfmrs: # Check all PowerTransformers connected to this node
                    DistAreaFlag1 = False
                    switch_area['unaddressable_equipment'].extend(DistXfmrs)
                    [switch_area, LVNodes] = self.create_dist_area(Topology, MVTree, DistXfmrs, 'PowerTransformer', switch_area.copy())
                    ProcessedNodes.extend(LVNodes)
                if DistXfmrTanks: # Check all TransformerTanks connected to this node
                    DistAreaFlag1 = False
                    switch_area['unaddressable_equipment'].extend(DistXfmrTanks)
                    [switch_area, LVNodes] = self.create_dist_area(Topology, MVTree, DistXfmrTanks, 'TransformerTank', switch_area.copy())
                    ProcessedNodes.extend(LVNodes)


            if switch_area['boundary_switches']: # Append switch area if not duplicate
                self.DistAppStruct['feeders']['switch_areas'].append(dict(switch_area))
                self.DistAppStruct['feeders']['connectivity_node'].extend(switch_area['connectivity_node'])
                self.DistAppStruct['feeders']['addressable_equipment'].extend(switch_area['boundary_switches'])
                self.DistAppStruct['feeders']['unaddressable_equipment'].extend(switch_area['unaddressable_equipment'])

        # Add missing nodes to feeder level (not in switch area or secondary area)
        AllNodes = list(ConnNodeDict.keys())
        MissingNodes = list(set(AllNodes).difference(ProcessedNodes))
        for i5 in range(len(MissingNodes)):
            node = MissingNodes[i5]
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['SynchronousMachine'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['PowerElectronicsConnection'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['LinearShuntCompensator'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['RatioTapChanger'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['EnergyConsumer'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['House'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['BatteryUnit'])
            self.DistAppStruct['feeders']['addressable_equipment'].extend(ConnNodeDict[node]['PhotovoltaicUnit'])
            self.DistAppStruct['feeders']['unaddressable_equipment'].extend(ConnNodeDict[node]['ACLineSegment'])
            self.DistAppStruct['feeders']['unaddressable_equipment'].extend(ConnNodeDict[node]['PowerTransformer'])
            self.DistAppStruct['feeders']['unaddressable_equipment'].extend(ConnNodeDict[node]['TransformerTank'])
            self.DistAppStruct['feeders']['unaddressable_equipment'].extend(ConnNodeDict[node]['Measurement'])
            self.DistAppStruct['feeders']['connectivity_node'].append(node)

        return self.DistAppStruct
    
    def create_dist_area(self, Topology, MVTree, Xfmrs, eqtype, switch_area):
        # Initialize secondary area dictionary
        ConnNodeDict = Topology.ConnNodeDict
        DistArea = {}
        DistArea['distribution_transformer'] = []
        DistArea['addressable_equipment'] = []
        DistArea['unaddressable_equipment'] = []
        DistArea['connectivity_node'] = []
        LVNodes = []
        DistAreaFlag2 = False
        # Iterate through all secondary transformers
        for i3 in range(len(Xfmrs)):
            xfmr = Xfmrs[i3]
            LVTree = Topology.spanning_tree(eqtype, [xfmr], MVTree, 'all')
            LVTreeKeys = LVTree[xfmr]
            if LVTreeKeys: 
                LVTreeKeys.pop(0) # dump first node (xfmr hi-side, duplicate)
                for i4 in range(len(LVTreeKeys)):
                    lvnode = LVTreeKeys[i4]
                    DistAreaFlag2 = True
                    LVNodes.append(lvnode)
                    DistArea['distribution_transformer'] = [xfmr]
                    DistArea['addressable_equipment'].extend(ConnNodeDict[lvnode]['SynchronousMachine'])
                    DistArea['addressable_equipment'].extend(ConnNodeDict[lvnode]['PowerElectronicsConnection'])
                    DistArea['addressable_equipment'].extend(ConnNodeDict[lvnode]['EnergyConsumer'])
                    DistArea['addressable_equipment'].extend(ConnNodeDict[lvnode]['House'])
                    DistArea['addressable_equipment'].extend(ConnNodeDict[lvnode]['BatteryUnit'])
                    DistArea['addressable_equipment'].extend(ConnNodeDict[lvnode]['PhotovoltaicUnit'])
                    DistArea['unaddressable_equipment'].extend(ConnNodeDict[lvnode]['ACLineSegment'])
                    DistArea['unaddressable_equipment'].extend(ConnNodeDict[lvnode]['Measurement'])
                    DistArea['connectivity_node'].append(lvnode)
                    switch_area['connectivity_node'].append(lvnode)
                    switch_area['unaddressable_equipment'].extend(ConnNodeDict[lvnode]['ACLineSegment'])
                    switch_area['unaddressable_equipment'].extend(ConnNodeDict[lvnode]['Measurement'])
        if DistAreaFlag2: # append secondary area if not empty
            switch_area['secondary_areas'].append((DistArea.copy()))
        return switch_area, LVNodes