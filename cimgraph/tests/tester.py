import importlib
cim_profile = 'rc4_2021'
cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)

from cimgraph.databases import Parameter, ConnectionParameters
from cimgraph.databases.blazegraph.blazegraph import BlazegraphConnection
from cimgraph.databases.graphdb.graphdb import GraphDBConnection
from cimgraph.databases.neo4j.neo4j import Neo4jConnection
from cimgraph.models import FeederModel
import json
import time



def _main():
    #feeder_mrid = "_C1C3E687-6FFD-C753-582B-632A27E28507"  # 123 bus
    feeder_mrid = "_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"  # 13 bus
    #feeder_mrid = "_5B816B93-7A5F-B64C-8460-47C17D6E4B0F" # 13 bus asets
    #feeder_mrid = "_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"  # 8500 node
    #feeder_mrid = "_67AB291F-DCCD-31B7-B499-338206B9828F" # J1
    #feeder_mrid = "_9CE150A8-8CC5-A0F9-B67E-BBD8C79D3095"  # R2 12.47 3
    #feeder_mrid = "_EE71F6C9-56F0-4167-A14E-7F4C71F10EAA" #9500 node


    # Neo4J Connection
    params = ConnectionParameters(url = "neo4j://localhost:7687/neo4j", database="neo4j", cim_profile='rc4_2021')
    neo4j = Neo4jConnection(params)

    feeder_mrid = "EE71F6C9-56F0-4167-A14E-7F4C71F10EAA" #9500 node
    feeder = cim.Feeder(mRID=feeder_mrid)

    network = FeederModel(connection=neo4j, container=feeder, distributed=False, cim_profile = 'rc4_2021')

    network_area = network
    # network_area.get_all_edges(cim.ACLineSegment)
    # network_area.get_all_edges(cim.ACLineSegmentPhase)
    # network_area.get_all_edges(cim.PerLengthPhaseImpedance)
    # network_area.get_all_edges(cim.PhaseImpedanceData)
    # network_area.get_all_edges(cim.WireSpacingInfo)
    # network_area.get_all_edges(cim.WirePosition)
    # network_area.get_all_edges(cim.OverheadWireInfo)
    # network_area.get_all_edges(cim.ConcentricNeutralCableInfo)
    # network_area.get_all_edges(cim.TapeShieldCableInfo)

    # network_area.get_all_edges(cim.PowerTransformer)
    # network_area.get_all_edges(cim.TransformerTank)
    # network_area.get_all_edges(cim.TransformerTankEnd)
    # network_area.get_all_edges(cim.TransformerTankInfo)
    # network_area.get_all_edges(cim.TransformerEndInfo)
    # network_area.get_all_edges(cim.ShortCircuitTest)
    # network_area.get_all_edges(cim.NoLoadTest)
    # network_area.get_all_edges(cim.RatioTapChanger)

if __name__ == "__main__":
    _main()
