from cim.loaders import Parameter, ConnectionParameters
from cim.loaders.blazegraph import BlazegraphConnection
from cim.loaders.gridappsd import GridappsdConnection, get_topology_response
from cim.models.distributed_model import DistributedModel
import cim.data_profile as cim

params = ConnectionParameters([Parameter(key="url", value="http://blazegraph:8080/bigdata/namespace/kb/sparql")])


feeder_mrid = "_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"

bg = BlazegraphConnection(params)
topology_response = get_topology_response(feeder_mrid)
feeder_mrid = "_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"
feeder = cim.Feeder(mRID=feeder_mrid)
network = DistributedModel(connection=bg, feeder=feeder, topology_response=topology_response)

print(network.addressable_equipment)



# bg.load_attributes()
# bg.create_default_instances(feeder_mrid=feeder)
