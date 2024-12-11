from __future__ import annotations

from uuid import UUID

from cimgraph.databases import ConnectionParameters


def get_triple_cypher(obj:object, attribute:str, connection_params: ConnectionParameters) -> str:

    """
    Generates cypher query string to find the type of an object from its uri
    Args:
        mrid (str): The mRID or uri of the  object
        connection_params (ConnectionParameters): Database connection parameters
    Returns:
        query_message: query string that can be used in Neo4J
    """

    if int(connection_params.iec61970_301) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{connection_params.url}#'

    query_message = f'''MATCH (n:{obj.__class__.__name__})
WHERE n.uri = "{split+obj.uri()}"
OPTIONAL MATCH (n) - [:`{attribute}`] - (m)
RETURN DISTINCT
n.uri as identifier,
"{attribute}" as attribute,
COALESCE(n.`{attribute}`,m.uri) as edge_id,
labels(m)[1] as edge_class'''
    # '{"@id":"' + COALESCE(m.uri ,"") + '","@type":"' + COALESCE((labels(m))[1],"") + '"}' as edge
    return query_message
