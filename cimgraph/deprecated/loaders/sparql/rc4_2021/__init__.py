#a
import cimgraph.deprecated.loaders.sparql.rc4_2021.ac_dc_terminal as ACDCTerminalSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.ac_line_segment as ACLineSegmentSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.ac_line_segment_phase as ACLineSegmentPhaseSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.analog as AnalogSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.asset as AssetSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.asset_info as AssetInfoSPARQL
#b
import cimgraph.deprecated.loaders.sparql.rc4_2021.base_voltage as BaseVoltageSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.battery_unit as BatteryUnitSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.breaker as BreakerSPARQL
# import cimgraph.loaders.sparql.rc4_2021.bus_bar_section as BusBarSectionSPARQL
# import cimgraph.loaders.sparql.rc4_2021.bus_bar_section_info as BusBarSectionInfoSPARQL
#c
import cimgraph.deprecated.loaders.sparql.rc4_2021.cable_info as CableInfoSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.concentric_neutral_cable_info as ConcentricNeutralCableInfoSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.connectivity_node as ConnectivityNodeSPARQL
#d
import cimgraph.deprecated.loaders.sparql.rc4_2021.disconnector as DisconnectorSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.discrete as DiscreteSPARQL
#e
import cimgraph.deprecated.loaders.sparql.rc4_2021.energy_consumer as EnergyConsumerSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.energy_consumer_phase as EnergyConsumerPhaseSPARQL
#f
import cimgraph.deprecated.loaders.sparql.rc4_2021.fuse as FuseSPARQL
#l
import cimgraph.deprecated.loaders.sparql.rc4_2021.linear_shunt_compensator as LinearShuntCompensatorSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.linear_shunt_compensator_phase as LinearShuntCompensatorPhaseSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.load_break_switch as LoadBreakSwitchSPARQL
#n
import cimgraph.deprecated.loaders.sparql.rc4_2021.no_load_test as NoLoadTestSPARQL
#o
import cimgraph.deprecated.loaders.sparql.rc4_2021.overhead_wire_info as OverheadWireInfoSPARQL
#p
import cimgraph.deprecated.loaders.sparql.rc4_2021.per_length_phase_impedance as PerLengthPhaseImpedanceSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.per_length_sequence_impedance as PerLengthSequenceImpedanceSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.phase_impedance_data as PhaseImpedanceDataSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.photovoltaic_unit as PhotovoltaicUnitSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.power_electronics_connection as PowerElectronicsConnectionSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.power_electronics_connection_phase as PowerElectronicsConnectionPhaseSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.power_transformer as PowerTransformerSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.power_transformer_end as PowerTransformerEndSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.power_transformer_info as PowerTransformerInfoSPARQL
#r
import cimgraph.deprecated.loaders.sparql.rc4_2021.ratio_tap_changer as RatioTapChangerSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.recloser as RecloserSPARQL
#s
import cimgraph.deprecated.loaders.sparql.rc4_2021.sectionaliser as SectionaliserSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.short_circuit_test as ShortCircuitTestSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.shunt_compensator_phase as ShuntCompensatorPhaseSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.switch_phase as SwitchPhaseSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.synchronous_machine as SynchronousMachineSPARQL
#t
import cimgraph.deprecated.loaders.sparql.rc4_2021.tap_changer_control as TapChangerControlSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.tape_shield_cable_info as TapeShieldCableInfoSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.terminal as TerminalSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.transformer_core_admittance as TransformerCoreAdmittanceSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.transformer_end_info as TransformerEndInfoSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.transformer_mesh_impedance as TransformerMeshImpedanceSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.transformer_tank as TransformerTankSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.transformer_tank_end as TransformerTankEndSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.transformer_tank_info as TransformerTankInfoSPARQL
#w
import cimgraph.deprecated.loaders.sparql.rc4_2021.wire_position as WirePositionSPARQL
import cimgraph.deprecated.loaders.sparql.rc4_2021.wire_spacing_info as WireSpacingInfoSPARQL

from cimgraph.deprecated.loaders.sparql.rc4_2021.get_class_type import get_class_type_sparql
