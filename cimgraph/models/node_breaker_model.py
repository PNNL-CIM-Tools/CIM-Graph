from __future__ import annotations

import json
import logging
import importlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from cimgraph.databases import ConnectionInterface
from cimgraph.models.graph_model import GraphModel
from cimgraph.models.model_parsers import add_to_graph, cim_dump, cim_print
from cimgraph.topology_processor.linknet import LinkNet
from cimgraph.topology_processor.distributed_feeder_areas import DistributedFeederTopology
from pprint import pprint as pypprint

_log = logging.getLogger(__name__)

@dataclass
class NodeBreakerModel(GraphModel):
    container: cim.ConnectivityNodeContainer
    connection: ConnectionInterface = None
    write_connection: ConnectionInterface = None
    distributed: bool = field(default_factory=False) #TODO: cannot find correct typing class
    distributed_hierarchy: list[type] = field(default_factory=list)
    graph: dict[type, dict[str, object]] = field(default_factory=dict)
    cim_profile: str = field(default_factory='rc4_2021')
    
    def __post_init__(self):
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)

        if self.connection is not None:
            if self.distributed:
                self.initialize_distributed_model(self.container)
            else:
                self.initialize_centralized_model(self.container)



    def initialize_centralized_model(self, container) -> None:
        self.graph = self.connection.create_new_graph(container)

        
    def initialize_distributed_model(self, container) -> None:
        if len(self.distributed_hierarchy) > 0:
            for container_class in self.distributed_hierarchy:
                container_type = container_class.__class__.__name__
                setattr(self, container_type + 's', []) 
                #TODO: create subclasses based on pre-defined topology        
        else:
            centralized_graph = self.connection.create_new_graph(container)
            self.get_all_edges(self.cim.Substation, centralized_graph)
            self.get_all_edges(self.cim.VoltageLevel, centralized_graph)
            self.get_all_edges(self.cim.Bay, centralized_graph)
            self.get_all_edges(self.cim.PowerTransformer, centralized_graph)
            self.get_all_edges(self.cim.TransformerTank, centralized_graph)
            self.get_all_edges(self.cim.BaseVoltage, centralized_graph)
            
            DistTopo = DistributedFeederTopology(self.connection, self.cim_profile, centralized_graph)
            self.switch_areas, self.graph = DistTopo.create_distributed_graph()
#             self.linknet = LinkNet(self.cim_profile, centralized_graph)
#             self.linknet.build_linknet([self.cim.ACLineSegment])

    
        
            