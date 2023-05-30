from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import cimgraph.data_profile.rc4_2021 as cim


def get_all_attributes(feeder_mrid: str, typed_catalog: dict[type, dict[str, object]]) -> str: 
    """ Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    mrid_list = list(typed_catalog[cim.ConnectivityNode].keys())

    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?ConnectivityNodeContainer ?TopologicalNode ?OperationalLimitSet
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        WHERE {          
          ?eq r:type cim:ConnectivityNode.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        #get feeder id from connectivity node

        ?eq cim:ConnectivityNode.ConnectivityNodeContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?fdr cim:IdentifiedObject.mRID ?ConnectivityNodeContainer.
        
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?t cim:Terminal.ConnectivityNode ?eq.
                  ?t cim:IdentifiedObject.mRID ?Terminal}
        
        OPTIONAL {?eq cim:ConnectivityNode.TopologicalNode ?tp.
                  ?tp cim:IdentifiedObject.mRID ?TopologicalNode.}
                  
        OPTIONAL {?eq cim:ConnectivityNode.OperationalLimitSet ?ol.
                  ?ol cim:IdentifiedObject.mRID ?OperationalLimitSet.}
                  
        #SvInjection
        #SvVoltage
       
        }
        GROUP BY  ?mRID ?name ?ConnectivityNodeContainer ?TopologicalNode ?OperationalLimitSet
        ORDER by  ?name 
    """

    return query_message
