import json
import logging
from dataclasses import dataclass, field

from cimgraph.models.distributed_area import DistributedArea
from cimgraph.models.graph_model import GraphModel

# from cimgraph.utils.timing import timing as time_func

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
    distributed_areas: list[DistributedArea] | None = None

    def __post_init__(self):

        if self.connection is not None:    # Check if connection has been specified
            self.cim = self.connection.cim    # Set CIM data profile
            if self.distributed:    # Check if distributed flag is true
                # Build distributed network model
                self.__initialize_distributed_model()
            else:
                # Otherwise build centralized network model
                self.__initialize_centralized_model()
        else:    # Log error thant no connection was specified
            _log.error('A ConnectionInterface must be specified')

    def __initialize_centralized_model(self) -> None:
        # Build graph model using database-specific routine
        self.graph = self.connection.create_new_graph(self.container)

    def __initialize_distributed_model(self) -> None:
        self.distributed_areas = []

        # If topology message is provided, build the distributed model from the message
        if self.topology_message is not None:
            if isinstance(self.topology_message, str):
                self.topology_message = json.loads(self.topology_message)

            if 'DistributionArea' in self.topology_message:
                # Identify cim.Feeder container from topo message
                feeder_topo_dict = self.topology_message['DistributionArea']['Substations'][0]['NormalEnergizedFeeder'][0]
            elif 'FeederArea' in self.topology_message:
                feeder_topo_dict = self.topology_message
            else:
                error_message = 'Invalid topology message. Must be a JSON message from GridAPPS-D Topology Processor'
                _log.error(error_message)
                raise ValueError(error_message)

            # try:
            self.container = self.add_jsonld_to_graph(feeder_topo_dict)
            # Identify cim.FeederArea container from topo message
            feeder_area_dict = feeder_topo_dict['FeederArea']
            feeder_area = self.add_jsonld_to_graph(feeder_area_dict)

            # Create a new DistributedArea GraphModel for the feeder area
            feeder_area_model = DistributedArea(container=feeder_area,
                                                connection=self.connection,
                                                distributed=True)
            feeder_area_model.build_from_topo_message(topology_dict=feeder_area_dict)
            # Append to distributed_areas field of FeederModel GraphModel.
            self.distributed_areas.append(feeder_area_model)

            for switch_area_dict in feeder_area_dict['SwitchAreas']:
                # Identify cim.SwitchArea container from topo message
                switch_area = feeder_area_model.add_jsonld_to_graph(switch_area_dict)

                # Create a new DistributedArea GraphModel for the switch area
                switch_area_model = DistributedArea(container=switch_area,
                                                    connection=self.connection,
                                                    distributed=True)
                switch_area_model.build_from_topo_message(switch_area_dict)
                # Append to distributed_areas field of FeederModel GraphModel.
                feeder_area_model.distributed_areas.append(switch_area_model)

                for sec_area_dict in switch_area_dict['SecondaryAreas']:
                    # Identify cim.SecondaryArea container from topo message
                    sec_area = switch_area_model.add_jsonld_to_graph(sec_area_dict)

                    # Create a new DistributedArea GraphModel for the switch area
                    sec_area_model = DistributedArea(container=sec_area,
                                                        connection=self.connection,
                                                        distributed=True)
                    sec_area_model.build_from_topo_message(sec_area_dict)
                    # Append to distributed_areas field of FeederModel GraphModel.
                    switch_area_model.distributed_areas.append(sec_area_model)

            # except:
            #     error_message = 'Invalid topology message. Must be a JSON message from GridAPPS-D Topology Processor'
            #     _log.error(error_message)
            #     raise ValueError(error_message)

        # If no topology message is provided, build the distributed model from the database
        else:

            if not isinstance(self.container, self.cim.Feeder):
                error_message = 'Invalid argument: container must be an instance of cim.Feeder'
                _log.error(error_message)
                raise TypeError(error_message)

            self.add_to_graph(self.container)

            new_edges = self.get_from_triple(self.container, 'Feeder.FeederArea')

            if not new_edges:
                error_message = f'No FeederArea defined for Feeder {self.container.uri()}. '
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
