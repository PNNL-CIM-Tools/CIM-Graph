from __future__ import annotations

import logging
import cimgraph.data_profile.cim18gmdm.canonical as cim
from cimgraph.models.graph_model import GraphModel
from cimgraph.databases import get_validation_log_level

_log = logging.getLogger(__name__)
log_level = get_validation_log_level()

def query_class_list(network: GraphModel, classes:list[str]):
    cim:cim = network.connection.cim
    for class_name in classes:
        try:
            cim_class = getattr(cim, class_name)
            network.get_all_edges(cim_class)
        except:
            pass
            # _log.log(log_level, f'{class_name} not in profile')


def get_all_line_data(network: GraphModel) -> None:
    classes = ['ACLineSegment',
    'ACLineSegment',
    'ACLineSegmentPhase',
    'PerLengthPhaseImpedance',
    'PhaseImpedanceData',
    'WireSpacingInfo',
    'WirePosition',
    'OverheadWireInfo',
    'ConcentricNeutralCableInfo',
    'TapeShieldCableInfo']
    query_class_list(network, classes)

            


def get_all_transformer_data(network: GraphModel) -> None:
    classes = ['PowerTransformer',
    'TransformerTank',
    'Asset',
    'TransformerTankEnd',
    'TransformerTankInfo',
    'TransformerEndInfo',
    'PowerTransformerEnd',
    'PowerTransformerInfo',
    'TransformerCoreAdmittance',
    'TransformerMeshImpedance',
    'TransformerStarImpedance',
    'ShortCircuitTest',
    'NoLoadTest',
    'RatioTapChanger',
    'TapChanger',
    'TapChangerControl',
    'TapChangerInfo']
    query_class_list(network, classes)


def get_all_load_data(network: GraphModel) -> None:
    cim:cim = network.connection.cim
    classes = ['EnergySource',
    'EnergyConsumer',
    'ConformLoad',
    'NonConformLoad',
    'EnergyConsumerPhase',
    'House',
    'ThermostatController']
    query_class_list(network, classes)
    
    network.get_all_attributes(cim.LoadResponseCharacteristic)
    network.get_all_attributes(cim.PowerCutZone)

def get_all_generator_data(network:GraphModel) -> None:
    classes = ['AsynchronousMachine',
    'SynchronousMachine',
    'ThermalGeneratingUnit',
    'WindGeneratingUnit'
    'FossilFuel']
    query_class_list(network, classes)



def get_all_inverter_data(network: GraphModel) -> None:
    classes = ['PowerElectronicsConnection',
    'PowerElectronicsConnectionPhase',
    'BatteryUnit',
    'PowerElectronicsWindUnit',
    'PowerElectronicsThermalUnit'
    'PhotoVoltaicUnit',# handling inconsistent case
    'PhotovoltaicUnit']
    query_class_list(network, classes)



def get_all_switch_data(network: GraphModel) -> None:
    classes = [
    'Switch',
    'Sectionaliser',
    'Jumper',
    'Fuse',
    'Disconnector',
    'GroundDisconnector',
    'ProtectedSwitch',
    'Breaker',
    'Recloser',
    'LoadBreakSwitch',
    'SwitchPhase']
    query_class_list(network, classes)
    


def get_all_bus_data(network: GraphModel) -> None:
    classes = [
    'ConnectivityNode',
    'Terminal',
    'TopologicalNode',
    'TopologicalIsland']
    query_class_list(network, classes)
    


def get_all_measurement_data(network: GraphModel) -> None:
    classes = [
    'Measurement',
    'Analog',
    'Discrete',
    'Accumlator',
    'StringMeasurement',]
    query_class_list(network, classes)
    


def get_all_limit_data(network: GraphModel) -> None:
    classes = [
    'OperationalLimitSet',
    'ActivePowerLimit',
    'ApparentPowerLimit',
    'VoltageLimit',
    'CurrentLimit',
    'OperationalLimitType']
    query_class_list(network, classes)
    


def get_all_location_data(network: GraphModel):
    cim:cim = network.connection.cim
    network.get_all_attributes(cim.CoordinateSystem)
    network.get_all_edges(cim.Location)
    network.get_all_edges(cim.PositionPoint)
    
def get_all_capacitor_data(network: GraphModel):
    classes = ['ShuntCompensator',
    'LinearShuntCompensator',
    'LinearShuntCompensatorPhase',
    ]
    query_class_list(network, classes)


def get_all_data(network: GraphModel):
    cim:cim = network.connection.cim

    # Get base data
    get_all_bus_data(network)
    get_all_line_data(network)
    get_all_transformer_data(network)
    get_all_load_data(network)
    get_all_inverter_data(network)
    get_all_limit_data(network)
    get_all_location_data(network)
    get_all_measurement_data(network)

    attr_only = [
        cim.BaseVoltage, cim.Substation, cim.SubGeographicalRegion,
        cim.GeographicalRegion, cim.LoadResponseCharacteristic
    ]

    # Do recursive search for missing data
    all_classes = []
    parsed_classes = []
    for class_type in list(network.graph.keys()):
        all_classes.append(class_type.__name__)

    while set(parsed_classes) != set(all_classes):
        for class_name in all_classes:
            if class_name not in parsed_classes:
                class_type = getattr(cim, class_name)
                if class_type not in attr_only:
                    # print('edges', class_name)
                    network.get_all_edges(class_type)

                else:
                    # print('attributes', class_name)
                    network.get_all_attributes(class_type)

                parsed_classes.append(class_name)
                all_classes = []
                for class_type in list(network.graph.keys()):
                    all_classes.append(class_type.__name__)
