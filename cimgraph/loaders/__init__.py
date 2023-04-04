from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List



@dataclass
class Parameter:
    key: Any
    value: Any


@dataclass
class ConnectionParameters:
    parameters: List[Parameter] = field(default_factory=list)


@dataclass
class QueryResponse:
    response: Any


@dataclass
class ConnectionInterface:
    connection_params: ConnectionParameters

    def connect(self):
        raise RuntimeError("Must have implemented connect in inherited class")

    def disconnect(self):
        raise RuntimeError("Must have implemented disconnect in inherited class")

    def load_attributes(self, obj: object):
        raise RuntimeError("Must have implemented load_attributes in inherited class")

    def create_default_instances(self, feeder_mrid: str | Feeder, mrid_list: List[str]):
        raise RuntimeError("Must have implemented retrieve_instance from inherited class")

    def execute(self, query: str) -> QueryResponse:
        raise RuntimeError("Must have implemented query in the inherited class")
