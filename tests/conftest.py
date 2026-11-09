"""Integration tests need a live service: mark them with @pytest.mark.integration('<service>')
(or a module-level pytestmark). They are skipped when nothing listens on the service's port,
and CI deselects them all with -m "not integration"."""
import socket
from functools import cache

import pytest

# service -> (host, port) the integration tests connect to (see docker-compose.yml)
SERVICES = {
    'blazegraph': ('localhost', 8889),
    'graphdb': ('localhost', 7200),
    'gridappsd': ('localhost', 61613),
    'mysql': ('127.0.0.1', 3306),
    'neo4j': ('localhost', 7687),
}


@cache
def service_is_running(service: str) -> bool:
    try:
        socket.create_connection(SERVICES[service], timeout=1).close()
        return True
    except OSError:
        return False


def pytest_runtest_setup(item: pytest.Item) -> None:
    for marker in item.iter_markers('integration'):
        if len(marker.args) != 1 or marker.args[0] not in SERVICES:
            raise ValueError(f'{item.nodeid}: integration marker needs one of {sorted(SERVICES)}')
        service = marker.args[0]
        if not service_is_running(service):
            host, port = SERVICES[service]
            pytest.skip(f'{service} is not running on {host}:{port}')
