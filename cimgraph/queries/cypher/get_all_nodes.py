from __future__ import annotations

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_all_nodes_from_container(container: object):
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    uri = container.uri()

    if get_iec61970_301() > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = f"""MATCH (container:{container_class})
WHERE container.uri = "{split}{uri}"
MATCH (eq) - [:`Equipment.EquipmentContainer`] - (container)
OPTIONAL MATCH (cnode) - [:`Terminal.ConnectivityNode`] - (term:Terminal) - [:`Terminal.ConductingEquipment`] -> (eq)
RETURN DISTINCT
REPLACE(cnode.uri, "{split}", "") as ConnectivityNode,
REPLACE(term.uri, "{split}", "") as Terminal,
REPLACE(eq.uri, "{split}", "") as eq_id,
LABELS(eq)[1] as eq_class"""

    return query_message


def get_all_nodes_from_area(container: object):
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
