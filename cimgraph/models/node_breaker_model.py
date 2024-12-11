from __future__ import annotations

import logging
from dataclasses import dataclass, field

from cimgraph.databases import ConnectionInterface
from cimgraph.models.distributed_area import DistributedArea
from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


@dataclass
class NodeBreakerModel(GraphModel):
    """
    Knowledge graph class for transmission node-breaker models. This should class
    should be used for all models with detailed substation representations.
    Args:
        container: a CIM object inheriting from EquipmentContainer with specified mRID
        connection: a ConnectionInterface object, such as BlazegraphConnection
        distributed: a boolean to indicate if the graph is distributed
    Optional Args:
        distributed_hierarchy: Custom inheritance structure for defining distributed areas
        topology_message: JSON message from GridAPPS-D Topology Proccessor Service
    Returns:
        none
    Methods:
        graph[cim.ClassName]: access to graph dictionary sorted by class and mRID
        add_to_graph(object): adds a new CIM object to the knowledge graph
        get_all_edges(cim.ClassName): universal database query to expand graph by one edge
        get_all_attributes(cim.ClassName): universal query to get attributes without expanding graph
        get_edges_query(cim.ClassName): returns query text for debugging
        pprint(cim.ClassName): pretty-print method for showing graph of a class type

    """
    # topology_message: dict = field(default_factory=dict)
    # distributed_hierarchy: list[type] = field(default_factory=list)
    aggregate_lower_areas: bool = field(default=True)

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
        self.graph = self.connection.create_new_graph(container)
        self.add_to_graph(container)

    def initialize_distributed_model(self, container: object) -> None:
        self.graph = {}
        self.add_to_graph(self.container)
        self.distributed_areas = {}

        # if container.__class__ == self.cim.GeographicalRegion:
        #     self.get_all_edges(self.cim.GeographicalRegion)
        #     self.distributed_areas[self.cim.SubGeographicalRegion] = {}
        #     self.distributed_areas[self.cim.Substation] = {}
        #     sub_geo_list = list(
        #         self.graph[self.cim.SubGeographicalRegion].keys())
        #     for sub_geo_mrid in sub_geo_list:
        #         sub_geo = self.graph[
        #             self.cim.SubGeographicalRegion][sub_geo_mrid]
        #         SubGeographicalArea = create_subgeographical_area(
        #             self.connection, sub_geo)
        #         self.distributed_areas[self.cim.SubGeographicalRegion][
        #             sub_geo_mrid] = SubGeographicalArea
        #         if self.aggregate_lower_areas:
        #             aggregate_equipment(self.graph, SubGeographicalArea.graph)
        #             self.distributed_areas.update(
        #                 SubGeographicalArea.distributed_areas)

        # elif container.__class__ == self.cim.SubGeographicalRegion:
        #     self.get_all_edges(self.cim.SubGeographicalRegion)

        #     for substation in self.graph[self.cim.Substation].values():
        #         SubstationArea = create_substation_area(
        #             self.connection, substation)
        #         self.distributed_areas.append(SubstationArea)
        #         if self.aggregate_lower_areas:
        #             aggregate_equipment(self.graph, SubstationArea.graph)

        # self.distristributed_areas = create_hierarchy_level(self, self.distributed_hierarchy, top_level=True)
