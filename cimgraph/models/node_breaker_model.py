from __future__ import annotations

import logging
from dataclasses import dataclass, field

from cimgraph.databases import ConnectionInterface
from cimgraph.models.distributed_area import DistributedArea, create_hierarchy_level
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
        self.graph = self.connection.create_new_graph(container)
        self.add_to_graph(container)

    def initialize_distributed_model(self, container: object) -> None:

        # # Use output from GridAPPS-D Topology Processor if given
        # if self.topology_message != {}:
        #     pass
        # else:

        if self.distributed_hierarchy == []:
            feeder = {}
            feeder['container'] = 'Feeder'
            feeder['contains'] = []

            bay = {}
            bay['container'] = 'Bay'
            bay['contains'] = []

            voltage_level = {}
            voltage_level['container'] = 'VoltageLevel'
            voltage_level['contains'] = [bay]

            sub_area = {}
            sub_area['container'] = 'Substation'
            sub_area['contains'] = [voltage_level, feeder, bay]

            subregion = {}
            subregion['container'] = 'SubGeographicalRegion'
            subregion['contains'] = [sub_area]

            region = {}
            region['container'] = 'GeographicalRegion'
            region['contains'] = [subregion]

            self.distributed_hierarchy = [region]

        self.add_to_graph(self.container)
        self.get_all_edges(self.container.__class__)
        self.distributed_areas = {}
        self.distristributed_areas = create_hierarchy_level(self,
                                                            self.distributed_hierarchy,
                                                            top_level=True)
