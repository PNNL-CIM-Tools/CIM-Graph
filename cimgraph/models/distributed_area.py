import json
import logging
import importlib
import uuid

from dataclasses import dataclass, field

from cimgraph.models.graph_model import GraphModel
from cimgraph.databases import ConnectionInterface

_log = logging.getLogger(__name__)

@dataclass
class DistributedArea(GraphModel):

    def __post_init__(self):
        self.cim_profile = self.connection.cim_profile
        self.cim = self.connection.cim    
        self.graph = {}

    def build_from_topo_message(self, topology_dict, centralized_graph):
        for node_mrid in topology_dict["connectivity_node"]:
            # try:
            node = centralized_graph[self.cim.ConnectivityNode][node_mrid]
            # except:
            # _log.warning("node " + node_mrid + " not in feeder")
                # continue
            self.add_to_graph(node)
            for terminal in node.Terminals:
                self.add_to_graph(terminal)
                self.add_to_graph(terminal.ConductingEquipment)
