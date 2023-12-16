from __future__ import annotations

from cimgraph.data_profile.known_problem_classes import ClassesWithoutMRID


def get_all_edges_cypher(cim_class: str, mrid_list: list, namespace: str) -> str:
    """
    Generates Cypher query string for a given CIM class, list of mRIDs, and namespace
    Args:
        cim_class (CIM object): CIM Class Object to be queried
        mrid_list (list[str]): List of mRID of objects
        name_space

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    class_name = cim_class.__name__
    classes_without_mrid = ClassesWithoutMRID()

    query_message = f"""MATCH (eq:{class_name})
    """

    if class_name not in classes_without_mrid.classes:
        query_message += f"""WHERE eq.`IdentifiedObject.mRID` in {mrid_list}
        MATCH (eq:{class_name}) - [edge] - (edge_node)
        RETURN eq.`IdentifiedObject.mRID` as mRID, eq, type(edge) as attribute, (COALESCE(edge_node.`IdentifiedObject.mRID`,edge_node.uri)) as edge_mrid, labels(edge_node) as edge_class"""
    else:
        index = 0
        for mrid in mrid_list:
            index = index + 1
            if index == 1:
                query_message += f"""WHERE eq.uri contains "{mrid}" OR
                """
            elif 1 < index < len(mrid_list):
                query_message += f"""eq.uri contains "{mrid}" OR
                """
            else:
                query_message += f"""eq.uri contains "{mrid}"
                """

        query_message += f"""MATCH (eq:{class_name}) - [edge] - (edge_node)
        RETURN eq.uri as mRID, eq, type(edge) as attribute, (COALESCE(edge_node.`IdentifiedObject.mRID`,edge_node.uri)) as edge_mrid, labels(edge_node) as edge_class"""

    return query_message
