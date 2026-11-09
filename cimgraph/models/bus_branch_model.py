from __future__ import annotations

import importlib
import json
import logging
from collections import defaultdict
from dataclasses import dataclass, field

from cimgraph.core import get_cim_profile
from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


@dataclass
class BusBranchModel(GraphModel):

    def __post_init__(self):
        if self.connection is not None:
            self.cim = self.connection.cim
        else:
            _, self.cim = get_cim_profile()
        if not self.graph:
            self.graph = defaultdict(lambda: defaultdict(dict))

        if self.connection is not None:
            if self.distributed:
                self.initialize_distributed_model(self.container)
            else:
                self.initialize_centralized_model(self.container)
        else:
            _log.debug('No ConnectionInterface: in-memory model, built with add_to_graph')
        self.set_default_bases()    # after loading: the graph's BasePower sets base_power

    def initialize_centralized_model(self, container) -> None:
        # Pass self.graph so objects the caller already built are preserved
        # instead of being replaced by the query result (matches FeederModel).
        self.graph = self.connection.create_new_graph(container, self.graph)

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
