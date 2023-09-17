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

    connection: ConnectionInterface
    distributed: bool
    distributed_hierarchy: list[type] = field(default_factory=list)
    graph: dict[type, dict[str, object]] = field(default_factory=dict)

    def __post_init__(self):
        self.cim_profile = self.connection.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.container = self.cim.EquipmentContainer(mRID = str(uuid.uuid4()))

    

