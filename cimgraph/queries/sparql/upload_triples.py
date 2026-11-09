from __future__ import annotations

from cimgraph.core.serialization import object_to_sparql_triples


def upload_triples_sparql(obj: object) -> str:
    """
    Generates a SPARQL INSERT DATA query that uploads one CIM object.

    Args:
        obj: A valid cim object instance.
    Returns:
        query_message: query string that can be used in a SPARQL update or STOMP client
    """
    triples = '\n\t'.join(object_to_sparql_triples(obj))
    return f'INSERT DATA {{\n\t{triples}\n}}'
