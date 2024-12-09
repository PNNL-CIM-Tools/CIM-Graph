from __future__ import annotations

from uuid import UUID

from cimgraph.databases import ConnectionParameters


def get_object_cypher(mrid: str, connection_params: ConnectionParameters) -> str:
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

    query_message = f'''
MATCH(n)
WHERE n.uri = {split+mrid}
RETURN DISTINCT n.uri as identifier,
labels(n)[1] as class'''
    # '{"@id":"' + COALESCE(m.uri ,"") + '","@type":"' + COALESCE((labels(m))[1],"") + '"}' as edge
    return query_message
