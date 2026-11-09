"""Every database adapter reads the same objects as XMLFile from the same file: the databases
in docker-compose.yml hold tests/test_models/ieee13.xml (tests/seed_databases.py)."""
import pytest
from cimprofiles.identity import Identity, as_uuid

from cimgraph import utils
from cimgraph.core.attribute_utils import diff_attributes
from cimgraph.databases import XMLFile
from cimgraph.models import FeederModel

MODEL = 'tests/test_models/ieee13.xml'
FEEDER_MRID = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'
ENV = {
    'CIMG_CIM_PROFILE': 'cimhub_2023',
    'CIMG_NAMESPACE': 'http://iec.ch/TC57/CIM100#',
    'CIMG_IEC61970_552': '552-NEW',
    'CIMG_USE_UNITS': 'true',
}
BACKENDS = [
    pytest.param('BlazegraphConnection', {'CIMG_URL': 'http://localhost:8889/bigdata/namespace/kb/sparql'},
                 marks=pytest.mark.integration('blazegraph'), id='blazegraph'),
    pytest.param('GraphDBConnection', {'CIMG_URL': 'http://localhost:7200/repositories/powergrid_models'},
                 marks=pytest.mark.integration('graphdb'), id='graphdb'),
    pytest.param('Neo4jConnection', {'CIMG_URL': 'neo4j://localhost:7687', 'CIMG_DATABASE': 'neo4j',
                                     'CIMG_USERNAME': 'neo4j', 'CIMG_PASSWORD': 'test1234'},
                 marks=pytest.mark.integration('neo4j'), id='neo4j'),
]
# ieee13.xml links one OperationalLimitSet to several terminals and nodes, but the profile
# allows one, so which one a reader keeps depends on the order its results arrive in
AMBIGUOUS = {('OperationalLimitSet', 'Terminal'), ('OperationalLimitSet', 'ConnectivityNode')}


def _feeder_model(connection) -> FeederModel:
    feeder = connection.cim.Feeder(mRID=FEEDER_MRID)
    return FeederModel(connection=connection, container=feeder, distributed=False)


def _same_reference(database_value, xml_value) -> bool:
    """A reference the adapter left as identifier text, because its object is not in the
    graph, to the object XMLFile read (it reads the whole file). Text keeps the database's
    case, and UUIDs are case-insensitive."""
    return (isinstance(database_value, str) and isinstance(xml_value, Identity)
            and as_uuid(database_value) == xml_value.identifier)


@pytest.mark.parametrize(('connection_name', 'connection_env'), BACKENDS)
def test_database_reads_the_objects_xml_reads(monkeypatch, connection_name, connection_env):
    for key, value in {**ENV, **connection_env}.items():
        monkeypatch.setenv(key, value)
    import cimgraph.databases
    connection = getattr(cimgraph.databases, connection_name)()
    xml_network = _feeder_model(XMLFile(filename=MODEL))
    network = _feeder_model(connection)
    utils.get_all_data(network)

    differences = []
    for cim_class, objects in network.graph.items():
        for identifier, obj in objects.items():
            xml_obj = xml_network.graph.get(cim_class, {}).get(identifier)
            if xml_obj is None:
                differences.append(f'{cim_class.__name__} {identifier} is not in {MODEL}')
                continue
            for attribute, (value, xml_value) in diff_attributes(obj, xml_obj).items():
                if (cim_class.__name__, attribute) in AMBIGUOUS or _same_reference(value, xml_value):
                    continue
                differences.append(f'{cim_class.__name__}.{attribute} of {obj.name!r}: '
                                   f'{value!r} != {xml_value!r}')
    connection.disconnect()
    assert sum(len(objects) for objects in network.graph.values()) > 400
    assert differences == []
