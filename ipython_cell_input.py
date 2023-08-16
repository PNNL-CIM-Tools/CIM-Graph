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

# Neo4J Connection
params = ConnectionParameters(url = "neo4j://localhost:7687/neo4j", database="neo4j", cim_profile='rc4_2021')
neo4j = Neo4jConnection(params)

feeder_mrid = "EE71F6C9-56F0-4167-A14E-7F4C71F10EAA" #9500 node
feeder = cim.Feeder(mRID=feeder_mrid)

network = FeederModel(connection=neo4j, container=feeder, distributed=False, cim_profile = 'rc4_2021')
