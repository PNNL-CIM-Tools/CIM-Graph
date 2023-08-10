from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional


def get_all_nodes_sparql(container, namespace):
    """ 
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:
         
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    container_mRID = container.mRID

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  %s"""%namespace
    query_message += """
        SELECT  ?ConnectivityNode ?Terminal ?Equipment
        WHERE {          
          ?c r:type cim:%s."""%container_class
    query_message += """
        VALUES ?cid {"%s"}"""%container_mRID

    # add all attributes
    query_message += """
        ?c cim:IdentifiedObject.mRID ?cid.
        ?node cim:ConnectivityNode.ConnectivityNodeContainer ?c.
        ?node cim:IdentifiedObject.mRID ?ConnectivityNode.

        ?t cim:Terminal.ConnectivityNode ?node.
        ?t cim:IdentifiedObject.mRID ?Terminal.
        ?t cim:Terminal.ConductingEquipment ?eq.

        ?eq cim:IdentifiedObject.mRID ?eq_id.
        ?eq a ?eq_cls.
        bind(concat(str(?eq_id),";",strafter(str(?eq_cls),"CIM100#")) as ?Equipment)     
        }
        """
    return query_message