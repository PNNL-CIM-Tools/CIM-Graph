import json
import logging
from uuid import UUID

from cimgraph.databases import create_graph_object

_log = logging.getLogger(__name__)

jsonld = dict['@id':str(UUID),'@type':str(type)]
Graph = dict[type, dict[UUID, object]]



# def jsonld_to_obj(cim:cim, json_ld:jsonld|str[jsonld]) -> object:

#     if type(json_ld) == str:
#         json_ld = json.loads(json_ld)
#     elif type(json_ld) == dict:
#         pass
#     else:
#         raise TypeError('json_ld input must be string or dict')



def create_object(class_type:type, uri:str, graph:Graph = None) -> object:
    """
    Method for creating new objects and adding them to the graph
    Required Args:
        class_type: a dataclass type, such as cim.ACLineSegment
        uri: the RDF ID or mRID of the object
    Optional Args:
        graph: an LPG graph from a GraphModel object, default a new graph
    Returns:
        obj: the object from the graph, else a new one added to it under its identifier
    """
    if graph is None:
        graph = {}
    return create_graph_object(graph, class_type, uri)
