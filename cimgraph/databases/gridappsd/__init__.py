from __future__ import annotations
from gridappsd import GridAPPSD

from cimgraph.databases.gridappsd.gridappsd import GridappsdConnection


def get_topology_response(feeder_mrid: str, gapps: GridAPPSD) -> dict:
    assert feeder_mrid is not None

    topic = 'goss.gridappsd.request.data.topology'
    message = {'requestType': 'GET_SWITCH_AREAS', 'modelID': feeder_mrid, 'resultFormat': 'JSON'}

    topo_response = gapps.get_response(topic=topic, message=message, timeout=30)
    return topo_response
