from __future__ import annotations

from cimgraph.core.serialization import rdf_identifier
from cimgraph.core.validation import validate_attribute
from cimgraph.databases import get_iec61970_552, get_url


def get_triple_cypher(subject:object, attribute:str) -> str:

    """
    Generates cypher query string to find the values of an attribute or association of an object.
    The attribute name is only compared as text (type(r) and a properties() map key), never
    written as a relationship type or property key: Neo4j warns about every relationship type
    or property key that is not in the database, and n10s stores a predicate as only one of them.
    Args:
        subject (object): The subject of the RDF triple
        attribute (str): The attribute / association to be queried
    Returns:
        query_message: query string that can be used in Neo4J. It returns no rows if the
            subject has no value for the attribute.
    """

    attribute = validate_attribute(attribute)
    if get_iec61970_552() == '552-NEW':
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = f'''MATCH (n:{subject.__class__.__name__})
WHERE n.uri = "{split+rdf_identifier(subject)}"
OPTIONAL MATCH (n) - [r] - (m)
WHERE type(r) = "{attribute}"
WITH n, m, COALESCE(properties(n)["{attribute}"], m.uri) as edge_id
WHERE edge_id IS NOT NULL
RETURN DISTINCT
n.uri as identifier,
"{attribute}" as attribute,
edge_id,
labels(m)[1] as edge_class'''
    return query_message
