import json

import cimgraph.data_profile.rc4_2021 as cim
from cimgraph.loaders import ConnectionParameters, Parameter
from cimgraph.loaders.blazegraph.blazegraph import BlazegraphConnection
from cimgraph.loaders.gridappsd import (GridappsdConnection,
                                        get_topology_response)
from cimgraph.models import DistributedModel


# print line name, phase, and bus
def get_lines_buses(network_area):
    print('\n \n EXAMPLE 1: GET ALL LINE PHASES AND BUSES')
    if cim.ACLineSegment in network_area.typed_catalog:
        network_area.get_all_attributes(cim.ACLineSegment)
        network_area.get_all_attributes(cim.ACLineSegmentPhase)
        network_area.get_all_attributes(cim.Terminal)
        
        line_ids = list(network_area.typed_catalog[cim.ACLineSegment].keys())
        for line_id in line_ids:
            line = network_area.typed_catalog[cim.ACLineSegment][line_id]
            print('\n line mrid: ',line_id)
            print('line name:', line.name)
            print('bus 1: ', line.Terminals[0].ConnectivityNode.name, line.Terminals[0].ConnectivityNode.mRID)
            print('bus 2: ', line.Terminals[1].ConnectivityNode.name, line.Terminals[1].ConnectivityNode.mRID)
            for line_phs in line.ACLineSegmentPhases:
                print('phase ', line_phs.phase, ': ', line_phs.mRID)
    else:
        print('no ACLineSegment objects in area')

# get line impedances and conductor geometry:

def get_line_impedances(network_area):
    print('\n \n EXAMPLE 2: GET ALL LINE IMPEDANCE ATTRIBUTES')
    if cim.ACLineSegment in network_area.typed_catalog:
        network_area.get_all_attributes(cim.ACLineSegment)
        network_area.get_all_attributes(cim.ACLineSegmentPhase)
        network_area.get_all_attributes(cim.PerLengthPhaseImpedance)
        network_area.get_all_attributes(cim.PhaseImpedanceData)

        network_area.get_all_attributes(cim.WireSpacingInfo)
        network_area.get_all_attributes(cim.WirePosition)
        network_area.get_all_attributes(cim.OverheadWireInfo)
        network_area.get_all_attributes(cim.ConcentricNeutralCableInfo)
        network_area.get_all_attributes(cim.TapeShieldCableInfo)
        network_area.get_all_attributes(cim.Terminal)

# sort data by line phase
def sort_impedance_by_line(network_area):
    print('\n \n EXAMPLE 3: SORT IMPEDANCE BY LINE PHASE')
    if cim.ACLineSegment in network_area.typed_catalog:
        for line in network_area.typed_catalog[cim.ACLineSegment].values():
            print('\n line mrid: ', line.mRID)
            print('line name:', line.name)
            print('bus 1: ', line.Terminals[0].ConnectivityNode.mRID)
            print('bus 2: ', line.Terminals[1].ConnectivityNode.mRID)

            for line_phs in line.ACLineSegmentPhases:
                print('phase ', line_phs.phase, ': ', line_phs.mRID)
                if line_phs.WireInfo is not None:
                    print('type: ', line_phs.WireInfo.__class__.__name__)
                    print('gmr: ', line_phs.WireInfo.gmr)
                    print('insulated: ', line_phs.WireInfo.insulated)

            if line.WireSpacingInfo is not None:
                for position in line.WireSpacingInfo.WirePositions:
                    print('seq:', position.sequenceNumber, ' x:', position.xCoord, ' y:', position.yCoord)    

            if line.PerLengthImpedance is not None:
                for data in line.PerLengthImpedance.PhaseImpedanceData:
                    print('row:', data.row, 'col:', data.column, 'r:', data.r, 'x:', data.x, 'b:', data.b)
    else:
        print('info: no ACLineSegment objects in area')


# sort lines by impedance info
def sort_line_by_impedance(network_area):
    print('EXAMPLE 4: SORT LINES BY IMPEDANCE AND GEOMETRY')
    #OverheadWireInfo
    if cim.OverheadWireInfo in network_area.typed_catalog:
        for oh_wire in network_area.typed_catalog[cim.OverheadWireInfo].values():
            print('\n name: ', oh_wire.name)
            print('gmr: ', oh_wire.gmr)
            print('insulated:', oh_wire.insulated)
            for line_phs in oh_wire.ACLineSegmentPhases:
                node1 = line_phs.ACLineSegment.Terminals[0].ConnectivityNode
                node2 = line_phs.ACLineSegment.Terminals[1].ConnectivityNode
                print('Buses:', node1.name, node2.name)
                print('Line Phase: ', line_phs.name, line_phs.mRID)
    else:
        print('info: no OverheadWireInfo objects in area')

    #TapeShieldCableInfo
    if cim.TapeShieldCableInfo in network_area.typed_catalog:
        for cable in network_area.typed_catalog[cim.TapeShieldCableInfo].values():
            print('name: ', cable.name)
            print('gmr: ', cable.gmr)
            print('insulated:', cable.insulated)
            print('tape thickness', cable.tapeThickness)
            for line_phs in cable.ACLineSegmentPhases:
                node1 = line_phs.ACLineSegment.Terminals[0].ConnectivityNode
                node2 = line_phs.ACLineSegment.Terminals[1].ConnectivityNode
                print('Line Phase: ', line_phs.name, line_phs.mRID)
                print('Buses:', node1.name, node2.name, node1.mRID, node2.mRID)
    else:
        print('info: no TapeShieldCableInfo objects in area')

    #PerLengthPhaseImpedance
    if cim.PerLengthPhaseImpedance in network_area.typed_catalog:
        for impedance in network_area.typed_catalog[cim.PerLengthPhaseImpedance].values():
            print('\n name:', impedance.name)
            for data in impedance.PhaseImpedanceData:
                    print('row:', data.row, 'col:', data.column, 'r:', data.r, 'x:', data.x, 'b:', data.b)
            for line in impedance.ACLineSegments:
                node1 = line.Terminals[0].ConnectivityNode
                node2 = line.Terminals[1].ConnectivityNode
                print('Line: ', line.name, line.mRID)
                print('Buses:', node1.name, node2.name, node1.mRID, node2.mRID)
    else:
        print('no PerLengthPhaseImpedance objects in area')

        
# get transformertank data
def get_tank_impedances(network_area):
    print('EXAMPLE 5: GET TRANSFORMER TANK IMPEDANCES')
    #OverheadWireInfo
    if cim.TransformerTank in network_area.typed_catalog:
        network_area.get_all_attributes(cim.TransformerTank)
        network_area.get_all_attributes(cim.TransformerTankEnd)
        network_area.get_all_attributes(cim.TransformerTankInfo)
        network_area.get_all_attributes(cim.TransformerEndInfo)
        network_area.get_all_attributes(cim.ShortCircuitTest)
        network_area.get_all_attributes(cim.NoLoadTest)
        network_area.get_all_attributes(cim.Terminal)
        
        for tank in network_area.typed_catalog[cim.TransformerTank].values():
            print('\n name:', tank.name)
            for end in tank.TransformerTankEnds:
                print('end number:', end.endNumber)
                node = end.Terminal.ConnectivityNode
                print('bus: ', node.name, node.mRID)

            for end_info in tank.TransformerTankInfo.TransformerEndInfos:

                print('end number', end_info.endNumber)
                print('rated voltage:', end_info.ratedU)
                print('resistance:', end_info.r)
                for no_load_test in end_info.EnergisedEndNoLoadTests:
                    print('exciting current:', no_load_test.excitingCurrent)

                for short_circuit_test in end_info.EnergisedEndShortCircuitTests:
                    print('energisedEndStep:', short_circuit_test.energisedEndStep)
                    print('groundedEndStep:', short_circuit_test.groundedEndStep)
                    print('leakageImpedance:', short_circuit_test.leakageImpedance)

                for short_circuit_test in end_info.GroundedEndShortCircuitTests:
                    print('energisedEndStep:', short_circuit_test.energisedEndStep)
                    print('groundedEndStep:', short_circuit_test.groundedEndStep)
                    print('leakageImpedance:', short_circuit_test.leakageImpedance)
        
        
# sort PowerElectronicsUnits
def get_inverter_buses(network_area):
    if cim.PowerElectronicsConnection in network_area.typed_catalog:
        network_area.get_all_attributes(cim.PowerElectronicsConnection)
        network_area.get_all_attributes(cim.PowerElectronicsConnectionPhase)
        network_area.get_all_attributes(cim.Terminal)
        network_area.get_all_attributes(cim.Analog)
        
        print('\n \n EXAMPLE 6: GET ALL INVERTER PHASES AND BUSES')
        for pec in network_area.typed_catalog[cim.PowerElectronicsConnection].values():
            print('\n name: ', pec.name, pec.mRID)
            print('p = ', pec.p, 'q = ', pec.q)
            node1 = pec.Terminals[0].ConnectivityNode
            print('bus: ', node1.name, node1.mRID)
            for pec_phs in pec.PowerElectronicsConnectionPhases:
                print('phase ', pec_phs.phase, ': ', pec_phs.mRID)
                
            for meas in pec.Measurements:
                print('Measurement: ', meas.name, meas.mRID)
                print('type:', meas.measurementType, 'phases:', meas.phases)
            
#sort EnergyConsumers
def get_load_buses(network_area):
    if cim.EnergyConsumer in network_area.typed_catalog:
        network_area.get_all_attributes(cim.EnergyConsumer)
        network_area.get_all_attributes(cim.EnergyConsumerPhase)
        network_area.get_all_attributes(cim.Terminal)
        network_area.get_all_attributes(cim.Analog)

        print('\n \n EXAMPLE 7: GET ALL LOAD PHASES AND BUSES')

        for load in network_area.typed_catalog[cim.EnergyConsumer].values():
            print('name: ', load.name, load.mRID)
            print('p = ', load.p, 'q = ', load.q)
            node1 = load.Terminals[0].ConnectivityNode
            print('bus: ', node1.name, node1.mRID)
            
            for load_phs in load.EnergyConsumerPhase:
                print('phases: ', load_phs.phase)
                print('p = ', load_phs.p, 'q = ', load_phs.q)
                
            for meas in load.Measurements:
                print('Measurement: ', meas.name, meas.mRID)
                print('type:', meas.measurementType, 'phases:', meas.phases)
                
                
def get_power_transformers(network_area):
    if cim.PowerTransformer in network_area.typed_catalog:
        network_area.get_all_attributes(cim.PowerTransformer)
        network_area.get_all_attributes(cim.PowerTransformerInfo)
        network_area.get_all_attributes(cim.PowerTransformerEnd)
        network_area.get_all_attributes(cim.TransformerMeshImpedance)
        network_area.get_all_attributes(cim.TransformerCoreAdmittance)
        network_area.get_all_attributes(cim.Terminal)
        network_area.get_all_attributes(cim.Analog)
        network_area.get_all_attributes(cim.Discrete)
        

        for xfmr in network_area.typed_catalog[cim.PowerTransformer].values():
            print('\n name: ', xfmr.name, xfmr.mRID)
            for end in xfmr.PowerTransformerEnd:
                print('end number:', end.endNumber)
                print('bus:', end.Terminal.ConnectivityNode.name)
                print('connection:', end.connectionKind)
                print('voltage:', end.ratedU)

                for mesh_imp in end.ToMeshImpedance:
                    print('r:', mesh_imp.r)
                    print('x:', mesh_imp.x)
                if end.CoreAdmittance is not None:
                    print('g:', end.CoreAdmittance.g)
                    print('b:', end.CoreAdmittance.b)
            for meas in xfmr.Measurements:
                print('Measurement: ', meas.name, meas.mRID)
                print('type:', meas.measurementType, 'phases:', meas.phases)
                
def _main():
    #feeder_mrid = "_C1C3E687-6FFD-C753-582B-632A27E28507"  # 123 bus
    feeder_mrid = "_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"  # 13 bus
    #feeder_mrid = "_5B816B93-7A5F-B64C-8460-47C17D6E4B0F" # 13 bus asets
    #feeder_mrid = "_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"  # 8500 node
    #feeder_mrid = "_67AB291F-DCCD-31B7-B499-338206B9828F" # J1
    #feeder_mrid = "_9CE150A8-8CC5-A0F9-B67E-BBD8C79D3095"  # R2 12.47 3
    #feeder_mrid = "_EE71F6C9-56F0-4167-A14E-7F4C71F10EAA" #9500 node
    
    # Get Topology Message
    gapps = GridappsdConnection(feeder_mrid)
    topology_response = get_topology_response(feeder_mrid)
    
    
    # Blazegraph connection for running outside the container
    params = ConnectionParameters([Parameter(key="url", value="http://localhost:8889/bigdata/namespace/kb/sparql")])
    bg = BlazegraphConnection(params, 'rc4_2021')
    
    # Initialize Model
    feeder = cim.Feeder(mRID=feeder_mrid)
    network = DistributedModel(connection=bg, feeder=feeder, topology=topology_response['feeders'])
    
    # Run examples
    switch_area = network.switch_areas[0]
    # EXAMPLE 1 - Get phase, bus info about ACLineSegments
    get_lines_buses(switch_area)

    # EXAMPLE 2 - Get all line impedance data
    get_line_impedances(switch_area)

    # EXAMPLE 3 - Sort all line impedance by line phase:
    sort_impedance_by_line(switch_area)

    # Example 4 - Sort all lines by impedance
    sort_line_by_impedance(switch_area)

    # Example 5 - Get TransformerTank impedances
    get_tank_impedances(switch_area)

    # Example 6 - Get inverter buses and phases
    get_inverter_buses(switch_area)

    # Example 7 - Get load buses and phases
    get_load_buses(switch_area)

if __name__ == "__main__":

    _main()

