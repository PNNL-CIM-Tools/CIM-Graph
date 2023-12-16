from __future__ import annotations

import importlib
import json
import logging
from dataclasses import dataclass, field

from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


@dataclass
class BusBranchModel(GraphModel):

    distributed_hierarchy: list[type] = field(default_factory=list)

    def __post_init__(self):
        self.cim_profile = self.connection.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)

        if self.connection is not None:
            if self.distributed:
                self.initialize_distributed_model(self.container)
            else:
                self.initialize_centralized_model(self.container)
        else:
            _log.error('A ConnectionInterface must be specified')

    def initialize_centralized_model(self, container) -> None:
        self.graph = self.connection.create_new_graph(container)

    def initialize_distributed_model(self, container) -> None:
        pass
        # if len(self.distributed_hierarchy) > 0:
        #     for container_class in self.distributed_hierarchy:
        #         container_type = container_class.__class__.__name__
        #         setattr(self, container_type + 's', [])
        #         #TODO: create subclasses based on pre-defined topology
        # else:
        #     centralized_graph = self.connection.create_new_graph(container)
        #     self.get_all_edges(self.cim.PowerTransformer, centralized_graph)
        #     self.get_all_edges(self.cim.TransformerTank, centralized_graph)
        #     self.get_all_edges(self.cim.BaseVoltage, centralized_graph)


#             self.linknet = LinkNet(self.cim_profile, centralized_graph)
#             self.linknet.build_linknet([self.cim.ACLineSegment])
