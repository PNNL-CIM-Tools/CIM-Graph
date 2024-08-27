from __future__ import annotations

import logging

from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def get_all_line_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.ACLineSegment)
    network.get_all_edges(cim.ACLineSegmentPhase)
    network.get_all_edges(cim.PerLengthPhaseImpedance)
    network.get_all_edges(cim.PhaseImpedanceData)
    network.get_all_edges(cim.WireSpacingInfo)
    network.get_all_edges(cim.WirePosition)
    network.get_all_edges(cim.OverheadWireInfo)
    network.get_all_edges(cim.ConcentricNeutralCableInfo)
    network.get_all_edges(cim.TapeShieldCableInfo)


def get_all_transformer_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.PowerTransformer)
    network.get_all_edges(cim.TransformerTank)
    network.get_all_edges(cim.Asset)
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


def get_all_load_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.EnergySource)
    network.get_all_edges(cim.EnergyConsumer)
    network.get_all_edges(cim.ConformLoad)
    network.get_all_edges(cim.NonConformLoad)
    network.get_all_edges(cim.EnergyConsumerPhase)
    network.get_all_attributes(cim.LoadResponseCharacteristic)
    network.get_all_attributes(cim.PowerCutZone)
    if 'House' in cim.__all__:
        network.get_all_edges(cim.House)
        network.get_all_edges(cim.ThermostatController)


def get_all_inverter_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.PowerElectronicsConnection)
    network.get_all_edges(cim.PowerElectronicsConnectionPhase)
    network.get_all_edges(cim.BatteryUnit)
    network.get_all_edges(cim.PowerElectronicsWindUnit)
    if 'PhotoVoltaicUnit' in cim.__all__:    # handling inconsistent case
        network.get_all_edges(cim.PhotoVoltaicUnit)
    elif 'PhotovoltaicUnit' in cim.__all__:    # handling inconsistent case
        network.get_all_edges(cim.PhotovoltaicUnit)


def get_all_switch_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.Switch)
    network.get_all_edges(cim.Sectionaliser)
    network.get_all_edges(cim.Jumper)
    network.get_all_edges(cim.Fuse)
    network.get_all_edges(cim.Disconnector)
    network.get_all_edges(cim.GroundDisconnector)
    network.get_all_edges(cim.ProtectedSwitch)
    network.get_all_edges(cim.Breaker)
    network.get_all_edges(cim.Recloser)
    network.get_all_edges(cim.LoadBreakSwitch)
    network.get_all_edges(cim.SwitchPhase)


def get_all_bus_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.ConnectivityNode)
    network.get_all_edges(cim.Terminal)
    network.get_all_edges(cim.TopologicalNode)
    network.get_all_edges(cim.TopologicalIsland)


def get_all_measurement_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.Terminal)
    network.get_all_edges(cim.Measurement)
    network.get_all_edges(cim.Analog)
    network.get_all_edges(cim.Discrete)
    # network.get_all_edges(cim.Accumlator)
    network.get_all_edges(cim.StringMeasurement)


def get_all_limit_data(network: GraphModel) -> None:
    cim = network.connection.cim
    network.get_all_edges(cim.OperationalLimitSet)
    network.get_all_edges(cim.ActivePowerLimit)
    network.get_all_edges(cim.ApparentPowerLimit)
    network.get_all_edges(cim.VoltageLimit)
    network.get_all_edges(cim.CurrentLimit)
    network.get_all_edges(cim.OperationalLimitType)


def get_all_location_data(network: GraphModel):
    cim = network.connection.cim
    network.get_all_edges(cim.CoordinateSystem)
    network.get_all_edges(cim.Location)
    network.get_all_edges(cim.PositionPoint)

def get_all_data(network: GraphModel):
    cim = network.connection.cim

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
                class_type = eval(f'cim.{class_name}')
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
