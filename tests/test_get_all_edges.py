import os

import pytest

from cimgraph.databases.gridappsd import GridappsdConnection
from cimgraph.models import FeederModel, GraphModel


@pytest.fixture
def env_setup():
    original_env = {
        'CIMG_CIM_PROFILE': os.getenv('CIMG_CIM_PROFILE'),
        'CIMG_URL': os.getenv('CIMG_URL'),
        'CIMG_DATABASE': os.getenv('CIMG_DATABASE'),
        'CIMG_HOST': os.getenv('CIMG_HOST'),
        'CIMG_PORT': os.getenv('CIMG_PORT'),
        'CIMG_USERNAME': os.getenv('CIMG_USERNAME'),
        'CIMG_PASSWORD': os.getenv('CIMG_PASSWORD'),
        'CIMG_NAMESPACE': os.getenv('CIMG_NAMESPACE'),
        'CIMG_IEC61970_301': os.getenv('CIMG_IEC61970_301'),
        'CIMG_USE_UNITS': os.getenv('CIMG_USE_UNITS'),
    }

    # Set environment variables for testing
    os.environ['CIMG_CIM_PROFILE'] = 'cimhub_2023'
    os.environ['CIMG_URL'] = 'http://localhost:8889/bigdata/namespace/kb/sparql'
    os.environ['CIMG_DATABASE'] = 'powergridmodel'
    os.environ['CIMG_HOST'] = 'localhost'
    os.environ['CIMG_PORT'] = '61613'
    os.environ['CIMG_USERNAME'] = 'test_app_user'
    os.environ['CIMG_PASSWORD'] = '4Test'
    os.environ['CIMG_NAMESPACE'] = 'http://iec.ch/TC57/CIM100#'
    os.environ['CIMG_IEC61970_301'] = '8'
    os.environ['CIMG_USE_UNITS'] = 'False'

    yield

    for key, value in original_env.items():
        if value is not None:
            os.environ[key] = value
        else:
            os.environ.pop(key, None)

@pytest.fixture(params=[{
    'connection': GridappsdConnection,
    'mrid': '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62',
    'distributed': False
    }])
def network(env_setup, request) -> GraphModel:

    connection, mrid, distributed = request.param['connection'](), request.param['mrid'], request.param['distributed']

    feeder = connection.get_object(mrid=mrid)
    assert feeder, 'Feeder object not found.'
    yield FeederModel(connection=connection, container=feeder, distributed=distributed)

    connection.disconnect()

@pytest.fixture
def cim():
    cim_profile = 'cimhub_2023'
    # cim_profile = 'rc4_2021'
    # import cimgraph.data_profile.rc4_2021 as cim
    import cimgraph.data_profile.cimhub_2023 as cim
    return cim



def test_get_all_edges(network, cim):
    network.get_all_edges(cim.ACLineSegment)
    network.get_all_edges(cim.ACLineSegmentPhase)
    network.get_all_edges(cim.PerLengthPhaseImpedance)
    network.get_all_edges(cim.PhaseImpedanceData)
    network.get_all_edges(cim.WireSpacingInfo)
    network.get_all_edges(cim.WirePosition)
    network.get_all_edges(cim.OverheadWireInfo)
    network.get_all_edges(cim.ConcentricNeutralCableInfo)
    network.get_all_edges(cim.TapeShieldCableInfo)

    network.get_all_edges(cim.PowerTransformer)
    network.get_all_edges(cim.TransformerTank)
    network.get_all_edges(cim.TransformerTankEnd)
    network.get_all_edges(cim.TransformerTankInfo)
    network.get_all_edges(cim.TransformerEndInfo)
    network.get_all_edges(cim.PowerTransformerEnd)
    network.get_all_edges(cim.PowerTransformerInfo)
    network.get_all_edges(cim.TransformerCoreAdmittance)
    network.get_all_edges(cim.TransformerMeshImpedance)
    network.get_all_edges(cim.TransformerStarImpedance)
    network.get_all_edges(cim.ShortCircuitTest)
    network.get_all_edges(cim.NoLoadTest)
    network.get_all_edges(cim.RatioTapChanger)
    network.get_all_edges(cim.TapChanger)
    network.get_all_edges(cim.TapChangerControl)
    network.get_all_edges(cim.TapChangerInfo)

    network.get_all_edges(cim.EnergyConsumer)
    network.get_all_edges(cim.EnergyConsumerPhase)
    network.get_all_edges(cim.EnergySource)

    network.get_all_edges(cim.ConnectivityNode)
    network.get_all_edges(cim.Terminal)

    network.get_all_edges(cim.OperationalLimitSet)
    network.get_all_edges(cim.OperationalLimitType)
    network.get_all_edges(cim.VoltageLimit)
    network.get_all_edges(cim.CurrentLimit)
    network.get_all_edges(cim.Feeder)
    network.get_all_edges(cim.BaseVoltage)
    network.get_all_edges(cim.CoordinateSystem)
    network.get_all_edges(cim.Location)
    network.get_all_edges(cim.PositionPoint)
