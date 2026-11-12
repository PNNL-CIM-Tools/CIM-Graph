"""Integration tests need a live service: mark them with @pytest.mark.integration('<service>')
(or a module-level pytestmark). They are skipped when nothing listens on the service's port,
and CI deselects them all with -m "not integration"."""
import os
import socket
from functools import cache

import pytest

from cimgraph.core import get_model_authority, get_model_name

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


@pytest.fixture(autouse=True)
def restore_model_scope():
    """Reading a file with a model header sets the model scope process-wide
    (set_model_scope); restore it after each test so tests don't depend on their order."""
    saved = {name: os.environ.get(name) for name in ('CIMG_MODEL_AUTHORITY', 'CIMG_MODEL_NAME')}
    yield
    for name, value in saved.items():
        if value is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = value
    get_model_authority.cache_clear()
    get_model_name.cache_clear()
