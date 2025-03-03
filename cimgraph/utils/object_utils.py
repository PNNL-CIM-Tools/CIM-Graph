import json
import logging
from uuid import UUID

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
        graph: an LPG graph from a GraphModel object
        class_type: a dataclass type, such as cim.ACLineSegment
        uri: the RDF ID or mRID of the object
    Returns:
        obj: a dataclass instance with the correct identifier
    """
    # Convert uri string to a uuid
    try:
        identifier = UUID(uri.strip('_').lower())
    except:
        _log.warning(f'URI {uri} for object {class_type.__name__} is not a valid UUID')
        identifier = uri

    if graph is None:
        graph = {}

    # Add class type to graph keys if not there
    if class_type not in graph:
        graph[class_type] = {}

    # Check if object exists in graph
    if identifier in graph[class_type]:
        obj = graph[class_type][identifier]

    # If not there, create a new object and add to graph
    else:
        obj = class_type()
        obj.uuid(uri = uri)
        graph[class_type][identifier] = obj

    return obj
