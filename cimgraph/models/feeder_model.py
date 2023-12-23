from __future__ import annotations

import importlib
import json
import logging
import uuid
from dataclasses import dataclass, field

from cimgraph.models.distributed_area import DistributedArea, DistributedTopology
from cimgraph.models.graph_model import GraphModel, new_mrid

_log = logging.getLogger(__name__)


@dataclass
class FeederModel(GraphModel):
    """
    Knowledge graph class for distribution feeder objects. This should class
    should be used for all feeder models and distribution data.
    Args:
        container: a CIM Feeder object with specified mRID
        connection: a ConnectionInterface object, such as BlazegraphConnection
        distributed: a boolean to indicate if the graph is distributed
    Optional Args:
        distributed_hierarchy: Custom inheritance structure for defining distributed areas
        topology_message: JSON message from GridAPPS-D Topology Proccessor Service
    Returns:
        none
    Methods:
        add_to_graph(object): adds a new CIM object to the knowledge graph
        get_all_edges(cim.ClassName): universal database query to expand graph by one edge
        graph[cim.ClassName]: access to graph dictionary sorted by class and mRID
        pprint(cim.ClassName): pretty-print method for showing graph of a class type
        get_edges_query(cim.ClassName): returns query text for debugging
    """
    topology_message: dict = field(default_factory=dict)
    distributed_hierarchy: list[type] = field(default_factory=list)

    def __post_init__(self):

        if self.connection is not None:    # Check if connection has been specified
            self.cim = self.connection.cim    # Set CIM data profile
            if self.distributed:    # Check if distributed flag is true
                # Build distributed network model
                self.initialize_distributed_model(self.container)
            else:
                # Otherwise build centralized network model
                self.initialize_centralized_model(self.container)
        else:    # Log error thant no connection was specified
            _log.error('A ConnectionInterface must be specified')

    def initialize_centralized_model(self, container: object) -> None:
        # Build graph model using database-specific routine
        self.graph = self.connection.create_new_graph(container)

    def initialize_distributed_model(self, container: object) -> None:
        centralized_graph = self.connection.create_new_graph(
            container)    # Initialize centralized graph model

        # Use output from GridAPPS-D Topology Processor if given
        if self.topology_message != {}:
            # Ingest topology message
            feeder_topo = self.topology_message['feeders']
            # for feeder in self.distributed_topology["feeders"]:
            # if feeder["feeder_id"] == self.container.mRID:
            # Created DistributedArea object for feeder area
            self.FeederArea = DistributedArea(container=self.container,
                                              connection=self.connection,
                                              distributed=True)
            self.FeederArea.build_from_topo_message(feeder_topo, centralized_graph)
            self.graph = self.FeederArea.graph

            self.distributed_areas = []    # Initialize list of switch areas
            sw_counter = -1
            for switch_topo in feeder_topo['switch_areas']:
                sw_counter = sw_counter + 1
                # Create a new DistributedArea object for each switch area in message
                switch_area_id = str(self.container.mRID) + '.' + str(sw_counter)
                switch_container = self.cim.EquipmentContainer(mRID=switch_area_id)
                SwitchArea = DistributedArea(connection=self.connection,
                                             container=switch_container,
                                             distributed=True)
                SwitchArea.build_from_topo_message(switch_topo, centralized_graph)
                SwitchArea.distributed_areas = []    # Initialize secondary areas list
                self.distributed_areas.append(
                    SwitchArea)    # Add new DistributedArea class to list
                sa_counter = -1
                for secondary_topo in switch_topo['secondary_areas']:
                    sa_counter = sa_counter + 1
                    # Create a new DistributedArea object for each secondary area
                    sec_area_id = str(
                        self.container.mRID) + '.' + str(sw_counter) + '.' + str(sa_counter)
                    secondary_container = self.cim.EquipmentContainer(mRID=sec_area_id)
                    SecondaryArea = DistributedArea(connection=self.connection,
                                                    container=secondary_container,
                                                    distributed=True)
                    SecondaryArea.build_from_topo_message(secondary_topo, centralized_graph)
                    SwitchArea.distributed_areas.append(SecondaryArea)

        # If GridAPPS-D Topology Processor output is not provided, build new topology:
        else:

            if len(self.distributed_hierarchy) > 0:
                for container_class in self.distributed_hierarchy:
                    container_type = container_class.__class__.__name__
                    setattr(self, container_type + 's', [])
                    #TODO: create subclasses based on pre-defined topology
            else:
                # self.get_all_edges(self.cim.Terminal, centralized_graph)
                # self.get_all_edges(self.cim.TransformerTankEnd, centralized_graph)
                # self.get_all_edges(self.cim.PowerTransformerEnd, centralized_graph)
                # self.get_all_edges(self.cim.BaseVoltage, centralized_graph)
                self.get_all_edges(self.cim.PowerTransformer, centralized_graph)
                self.get_all_edges(self.cim.TransformerTank, centralized_graph)
                self.get_all_edges(self.cim.Asset, centralized_graph)
                self.get_all_edges(self.cim.TransformerTankInfo, centralized_graph)
                self.get_all_edges(self.cim.TransformerEndInfo, centralized_graph)

                switch_classes = [
                    self.cim.Breaker, self.cim.Sectionaliser, self.cim.Recloser,
                    self.cim.LoadBreakSwitch, self.cim.Switch
                ]    # default switch classes
                upper_boundaries = switch_classes + [self.cim.PowerTransformer]
                lower_boundaries = [self.cim.TransformerTank]

                DistTopo = DistributedTopology(connection=self.connection,
                                               centralized_graph=centralized_graph,
                                               root_classes=switch_classes,
                                               upper_boundaries=upper_boundaries,
                                               lower_boundaries=lower_boundaries)
                self.distributed_areas = DistTopo.create_distributed_areas()
