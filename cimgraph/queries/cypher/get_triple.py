from __future__ import annotations

from uuid import UUID

from cimgraph.databases import get_iec61970_301, get_url


def get_triple_cypher(subject:object, attribute:str) -> str:

    """
    Generates cypher query string to find the type of an object from its uri
    Args:
        subject (object): The subject of the RDF triple
        attribute (str): The attribute / association to be queried
    Returns:
        query_message: query string that can be used in Neo4J
    """

    if int(get_iec61970_301()) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = f'''MATCH (n:{subject.__class__.__name__})
WHERE n.uri = "{split+subject.uri()}"
OPTIONAL MATCH (n) - [:`{attribute}`] - (m)
RETURN DISTINCT
n.uri as identifier,
"{attribute}" as attribute,
COALESCE(n.`{attribute}`,m.uri) as edge_id,
labels(m)[1] as edge_class'''
    # '{"@id":"' + COALESCE(m.uri ,"") + '","@type":"' + COALESCE((labels(m))[1],"") + '"}' as edge
    return query_message
