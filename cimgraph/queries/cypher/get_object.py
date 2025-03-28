from __future__ import annotations

from uuid import UUID

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_object_cypher(mRID: str) -> str:
    """
    Generates cypher query string to find the type of an object from its uri
    Args:
        mrid (str): The mRID or uri of the  object
    Returns:
        query_message: query string that can be used in Neo4J
    """


    if int(get_iec61970_301()) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = f'''
MATCH(n)
WHERE n.uri = "{split+mRID}"
RETURN DISTINCT n.uri as identifier,
labels(n)[1] as class'''
    # '{"@id":"' + COALESCE(m.uri ,"") + '","@type":"' + COALESCE((labels(m))[1],"") + '"}' as edge
    return query_message
