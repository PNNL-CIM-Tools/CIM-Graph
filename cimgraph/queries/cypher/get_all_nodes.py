from __future__ import annotations

from cimgraph.databases import ConnectionParameters


def get_all_nodes_from_container(container: object, namespace: str):
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    uri = container.uri()

    query_message = f"""MATCH (container:{container_class})
WHERE container.uri = "{uri}"
MATCH (eq) - [:`Equipment.EquipmentContainer`] - (container)
OPTIONAL MATCH (cnode) - [:`Terminal.ConnectivityNode`] - (term:Terminal) - [:`Terminal.ConductingEquipment`] -> (eq)
RETURN DISTINCT
cnode.`IdentifiedObject.mRID` as ConnectivityNode,
term.`IdentifiedObject.mRID` as Terminal,
eq.`IdentifiedObject.mRID` as eq_id,
LABELS(eq)[1] as eq_class"""

    return query_message


def get_all_nodes_from_area(container: object, namespace: str):
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    uri = container.uri()

    query_message = f"""MATCH (container:{container_class})
WHERE container.uri = "{uri}"
MATCH (eq) - [:`Equipment.SubSchedulingArea`] - (container)
OPTIONAL MATCH (cnode) - [:`Terminal.ConnectivityNode`] - (term:Terminal) - [:`Terminal.ConductingEquipment`] -> (eq)
RETURN DISTINCT
cnode.`IdentifiedObject.mRID` as ConnectivityNode,
term.`IdentifiedObject.mRID` as Terminal,
eq.`IdentifiedObject.mRID` as eq_id,
LABELS(eq)[1] as eq_class"""

    return query_message
