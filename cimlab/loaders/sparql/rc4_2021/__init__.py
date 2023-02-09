from cimlab.loaders.sparql.rc4_2021.get_class_type import get_class_type_sparql
#a
import cimlab.loaders.sparql.rc4_2021.ac_dc_terminal as ACDCTerminalSPARQL
import cimlab.loaders.sparql.rc4_2021.ac_line_segment as ACLineSegmentSPARQL
import cimlab.loaders.sparql.rc4_2021.ac_line_segment_phase as ACLineSegmentPhaseSPARQL
import cimlab.loaders.sparql.rc4_2021.asset as AssetSPARQL
import cimlab.loaders.sparql.rc4_2021.asset_info as AssetInfoSPARQL
#b
import cimlab.loaders.sparql.rc4_2021.base_voltage as BaseVoltageSPARQL
import cimlab.loaders.sparql.rc4_2021.battery_unit as BatteryUnitSPARQL
import cimlab.loaders.sparql.rc4_2021.breaker as BreakerSPARQL
# import cimlab.loaders.sparql.rc4_2021.bus_bar_section as BusBarSectionSPARQL
# import cimlab.loaders.sparql.rc4_2021.bus_bar_section_info as BusBarSectionInfoSPARQL
#c
import cimlab.loaders.sparql.rc4_2021.cable_info as CableInfoSPARQL
import cimlab.loaders.sparql.rc4_2021.concentric_neutral_cable_info as ConcentricNeutralCableInfoSPARQL
#d
import cimlab.loaders.sparql.rc4_2021.disconnector as DisconnectorSPARQL
#e
import cimlab.loaders.sparql.rc4_2021.energy_consumer as EnergyConsumerSPARQL
import cimlab.loaders.sparql.rc4_2021.energy_consumer_phase as EnergyConsumerPhaseSPARQL
#f
import cimlab.loaders.sparql.rc4_2021.fuse as FuseSPARQL

#l
import cimlab.loaders.sparql.rc4_2021.linear_shunt_compensator as LinearShuntCompensatorSPARQL
import cimlab.loaders.sparql.rc4_2021.load_break_switch as LoadBreakSwitchSPARQL

#n
import cimlab.loaders.sparql.rc4_2021.no_load_test as NoLoadTestSPARQL
#o
import cimlab.loaders.sparql.rc4_2021.overhead_wire_info as OverheadWireInfoSPARQL

#p
import cimlab.loaders.sparql.rc4_2021.per_length_phase_impedance as PerLengthPhaseImpedanceSPARQL
import cimlab.loaders.sparql.rc4_2021.per_length_sequence_impedance as PerLengthSequenceImpedanceSPARQL
import cimlab.loaders.sparql.rc4_2021.phase_impedance_data as PhaseImpedanceDataSPARQL
import cimlab.loaders.sparql.rc4_2021.power_electronics_connection as PowerElectronicsConnectionSPARQL
import cimlab.loaders.sparql.rc4_2021.power_electronics_connection_phase as PowerElectronicsConnectionPhaseSPARQL
import cimlab.loaders.sparql.rc4_2021.power_transformer as PowerTransformerSPARQL
import cimlab.loaders.sparql.rc4_2021.power_transformer_end as PowerTransformerEndSPARQL
import cimlab.loaders.sparql.rc4_2021.power_transformer_info as PowerTransformerInfoSPARQL
#r
import cimlab.loaders.sparql.rc4_2021.ratio_tap_changer as RatioTapChangerSPARQL
import cimlab.loaders.sparql.rc4_2021.recloser as RecloserSPARQL
#s
import cimlab.loaders.sparql.rc4_2021.sectionaliser as SectionaliserSPARQL
import cimlab.loaders.sparql.rc4_2021.short_circuit_test as ShortCircuitTestSPARQL
import cimlab.loaders.sparql.rc4_2021.switch_phase as SwitchPhaseSPARQL
#t
import cimlab.loaders.sparql.rc4_2021.tap_changer_control as TapChangerControlSPARQL
import cimlab.loaders.sparql.rc4_2021.tape_shield_cable_info as TapeShieldCableInfoSPARQL
import cimlab.loaders.sparql.rc4_2021.terminal as TerminalSPARQL
import cimlab.loaders.sparql.rc4_2021.transformer_end_info as TransformerEndInfoSPARQL
import cimlab.loaders.sparql.rc4_2021.transformer_tank as TransformerTankSPARQL
import cimlab.loaders.sparql.rc4_2021.transformer_tank_end as TransformerTankEndSPARQL
import cimlab.loaders.sparql.rc4_2021.transformer_tank_info as TransformerTankInfoSPARQL
import cimlab.loaders.sparql.rc4_2021.transformer_mesh_impedance as TransformerMeshImpedanceSPARQL
import cimlab.loaders.sparql.rc4_2021.transformer_core_admittance as TransformerCoreAdmittanceSPARQL

#w
import cimlab.loaders.sparql.rc4_2021.wire_position as WirePositionSPARQL
import cimlab.loaders.sparql.rc4_2021.wire_spacing_info as WireSpacingInfoSPARQL