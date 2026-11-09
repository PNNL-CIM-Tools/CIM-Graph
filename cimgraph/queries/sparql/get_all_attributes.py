from __future__ import annotations

from uuid import UUID

from cimgraph.queries.sparql.get_all_edges import get_all_edges_sparql


def get_all_attributes_sparql(graph: dict[type, dict[UUID, object]], cim_class: type,
                              uuid_list: list[UUID]) -> str:
    """
    Return the query for every attribute and association of the objects in uuid_list.
    It is the get_all_edges query: get_all_attributes needs each referenced object's
    class too, to write the association as the reference the object is read with.
    """
    return get_all_edges_sparql(graph, cim_class, uuid_list)
