import logging
from dataclasses import dataclass, field

from cimgraph.models.distributed_area import DistributedArea
from cimgraph.models.graph_model import GraphModel

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
    distributed_areas: list[DistributedArea] | None = None

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
        self.distributed_areas = []

        if not isinstance(container, self.cim.Feeder):
            error_message = 'Invalid argument: container must be an instance of cim.Feeder'
            _log.error(error_message)
            raise TypeError(error_message)

        self.add_to_graph(container)
        new_edges = self.get_from_triple(container, 'Feeder.FeederArea')

        if not new_edges:
            error_message = f'No FeederArea defined for Feeder {container.uri()}. '
            error_message += 'Rebuild the model with the create_distributed_feeder() method'
            error_message += 'from the CIM-Graph-Topology-Processor library.'
            _log.error(error_message)
            raise ValueError(error_message)

        feeder_area = new_edges[0]
        # Create a new DistributedArea GraphModel for the feeder area
        feeder_area_model = DistributedArea(container=feeder_area,
                                              connection=self.connection,
                                              distributed=True)

        # Initialize DistributedArea with equipment, nodes, terminals, and measurements
        feeder_area_model.get_all_edges(self.cim.FeederArea)
        feeder_area_model.build_from_area()
        # Append to distributed_areas field of FeederModel GraphModel.
        self.distributed_areas.append(feeder_area_model)

        for switch_area in feeder_area.SwitchAreas:
            # Create a new DistributedArea GraphModel for each switch area
            switch_area_model = DistributedArea(container=switch_area,
                                              connection=self.connection,
                                              distributed=True)
            # Initialize DistributedArea with equipment, nodes, terminals, and measurements
            switch_area_model.get_all_edges(self.cim.SwitchArea)
            switch_area_model.build_from_area()
            # Add switch area context object to list of dist areas for feeder area context
            feeder_area_model.distributed_areas.append(switch_area_model)

            for secondary_area in switch_area.SecondaryAreas:
                # Create new DistributedArea GraphModel for each secondary area
                secondary_area_model = DistributedArea(container=secondary_area,
                                                connection=self.connection,
                                                distributed=True)
                # Initialize DistributedArea with equipment, nodes, terminals, and measurements
                secondary_area_model.build_from_area()
                # Add secondary area context to list of dist areas for switch area context
                switch_area_model.distributed_areas.append(secondary_area_model)
