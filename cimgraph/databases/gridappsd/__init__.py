"""
This module provides functionality to interact with the GridAPPSD platform.

It attempts to import the GridAPPSD package and sets an environment variable
'CIMGRAPH_HAS_GRIDAPPSD' to '1' and HAS_GRIDAPPSD flag set to True, if the import is
successful. If the import fails, it sets a flag 'HAS_GRIDAPPSD' to False.

The module also provides a function 'get_topology_response' which sends a
request to the GridAPPSD platform to get the topology of a specific feeder.

Functions:
----------
get_topology_response(feeder_mrid: str, gapps: GridAPPSD) -> Dict:
    Sends a request to the GridAPPSD platform to get the topology of a specific feeder.

    Parameters:
    -----------
    feeder_mrid : str
        The mRID of the feeder for which the topology is requested.
    gapps : GridAPPSD
        An instance of the GridAPPSD class.

    Returns:
    --------
    dict
        A dictionary containing the response from the GridAPPSD platform.
"""
from __future__ import annotations

from gridappsd import GridAPPSD

from cimgraph.databases.gridappsd.gridappsd import GridappsdConnection


def get_topology_response(feeder_mrid: str, gapps: GridAPPSD) -> dict:
    assert feeder_mrid is not None

    topic = 'goss.gridappsd.request.data.topology'
    message = {'requestType': 'GET_SWITCH_AREAS', 'modelID': feeder_mrid, 'resultFormat': 'JSON'}

    topo_response = gapps.get_response(topic=topic, message=message, timeout=30)
    return topo_response
