from __future__ import annotations
import math
import importlib
import logging
import re
import json
import enum
import uuid

from cimgraph.models.graph_model import GraphModel, json_dump
_log = logging.getLogger(__name__)

def write_csv(network:GraphModel, destination) -> None:

    for cim_class in list(network.graph.keys()):
        attributes = list(cim_class.__dataclass_fields__.keys())

        with open(f'{destination}/{cim_class.__name__}.csv', 'w') as csv_file:
            header = ','.join(attributes)
            csv_file.write(header)
