from __future__ import annotations

from dataclasses import dataclass, field


def get_all_nodes_from_container(container: object, namespace: str):
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    container_mRID = container.mRID

    query_message = f"""MATCH (container:{container_class})  <- [:`ConnectivityNode.ConnectivityNodeContainer`]
    - (cnode:ConnectivityNode) - [:`Terminal.ConnectivityNode`] - (term:Terminal)
    - [:`Terminal.ConductingEquipment`] -> (eq)
    WHERE container.`IdentifiedObject.mRID` in ["{container_mRID}"]
    RETURN cnode.`IdentifiedObject.mRID` as ConnectivityNode, term.`IdentifiedObject.mRID` as Terminal, eq.`IdentifiedObject.mRID` as eq_id, LABELS(eq) as eq_class"""

    return query_message
