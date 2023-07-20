from __future__ import annotations

import json
import logging
import importlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from cimgraph.loaders import ConnectionInterface
from cimgraph.models.model_parsers import add_to_graph, cim_dump, cim_print

from pprint import pprint as pypprint

_log = logging.getLogger(__name__)

@dataclass
class GraphModel:
   
    
    def get_all_edges(self, cim_class, graph=None):
        if graph is None:
            graph = self.graph
        if cim_class in graph:
            self.connection.get_all_edges(self.container.mRID, graph, cim_class)
        else:
            _log.info('no instances of '+str(cim_class.__name__)+' found in graph.')
    
    def pprint(self, cim_class):
        if cim_class in self.graph:
            json_dump = cim_print(self.graph, cim_class)
        else:
            json_dump = {}
            _log.info('no instances of '+str(cim_class.__name__)+' found in graph.')
        print(json.dumps(json_dump,indent=4))
    
    
        
            