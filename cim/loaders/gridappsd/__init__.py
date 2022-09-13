from __future__ import annotations

import atexit
import os
from typing import List

import cim.data_profile as cim
from cim.loaders import ConnectionInterface, ConnectionParameters, Parameter, QueryResponse
from gridappsd import GridAPPSD

# os.environ["GRIDAPPSD_ADDRESS"] = "gridappsd"
# os.environ["GRIDAPPSD_PORT"] = "61613"
os.environ['GRIDAPPSD_APPLICATION_ID'] = 'gridappsd-cim-profile'
os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
os.environ['GRIDAPPSD_USER'] = 'app_user'
os.environ['GRIDAPPSD_PASSWORD'] = '1234App'
__gapps__ = GridAPPSD()


# assert gapps.connected


class GridappsdConnection(ConnectionInterface):

    def connect(self):
        pass

    def disconnect(self):
        assert self.connection_params

    def connect(self):
        assert self.connection_params

    def disconnect(self):
        assert self.connection_params

    def load_attributes(self, obj: object):
        if isinstance(obj, cim.Terminal):
            # load terminal stuff here
            pass

    def create_default_instances(self, feeder_mrid: str | cim.Feeder, mrid_list: List[str]):
        raise RuntimeError("Must have implemented retrieve_instance from inherited class")

    def execute(self, **kwargs) -> QueryResponse:
        for x in ('topic', 'message', 'timeout'):
            if x not in kwargs:
                raise ValueError(f"Parameter {x} required")

        response = QueryResponse(__gapps__.get_response(**kwargs))
        return response


def get_topology_response(feeder_mrid: str) -> QueryResponse:
    assert feeder_mrid is not None

    gapps = GridAPPSD()
    topic = "goss.gridappsd.request.data.topology"
    message = {
        "requestType": "GET_SWITCH_AREAS",
        "modelID": feeder_mrid,
        "resultFormat": "JSON"
    }

    topo_response = gapps.get_response(topic=topic, message=message, timeout=30)
    return topo_response

# Close gridappsd connection when exiting program.
atexit.register(lambda: __gapps__.disconnect())
