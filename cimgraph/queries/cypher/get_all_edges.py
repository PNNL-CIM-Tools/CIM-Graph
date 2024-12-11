from __future__ import annotations

from uuid import UUID

from cimgraph.databases import ConnectionParameters


def get_all_edges_cypher(graph:dict[type, dict[UUID, object]], cim_class: type, uuid_list: list[UUID],
                         connection_params: ConnectionParameters) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        graph (dict[type, dict[UUID, object]]): The graph of CIM objects organized by
            class type and UUID object identifier
        cim_class (type): The CIM class type to query
        uuid_list (list[UUID]): List of UUIDs to query for
        connection_params (ConnectionParameters): Database connection parameters

    Returns:
        query_message: query string that can be used in Neo4J database
    """
    class_name = cim_class.__name__

    if int(connection_params.iec61970_301) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{connection_params.url}#'

    query_message = f"""
MATCH (n:{class_name})
WHERE n.uri IN ["""

    for uuid in uuid_list:
        query_message += f'"{split+graph[cim_class][uuid].uri()}", \n'

    query_message = query_message.rstrip(', \n')
    query_message += ''']
OPTIONAL MATCH (n) - [r] - (m)
RETURN DISTINCT n.uri as identifier,
type(r) as attribute,
m.uri as edge_id,
labels(m)[1] as edge_class'''
    # '{"@id":"' + COALESCE(m.uri ,"") + '","@type":"' + COALESCE((labels(m))[1],"") + '"}' as edge
    return query_message

def get_all_properties_cypher(graph:dict[type, dict[UUID, object]], cim_class: type, uuid_list: list[UUID],
                         connection_params: ConnectionParameters) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        graph (dict[type, dict[UUID, object]]): The graph of CIM objects organized by
            class type and UUID object identifier
        cim_class (type): The CIM class type to query
        uuid_list (list[UUID]): List of UUIDs to query for
        connection_params (ConnectionParameters): Database connection parameters

    Returns:
        query_message: query string that can be used in Neo4J database
    """
    class_name = cim_class.__name__

    if int(connection_params.iec61970_301) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{connection_params.url}#'

    query_message = f"""
        MATCH (n:{class_name})
        WHERE n.uri IN [
    """

    for uuid in uuid_list:
        query_message += f'"{split+graph[cim_class][uuid].uri()}", \n'

    query_message = query_message.rstrip(', \n')
    query_message += ''']
        RETURN DISTINCT n.uri as identifier,
        properties(n) as attributes'''
    return query_message
