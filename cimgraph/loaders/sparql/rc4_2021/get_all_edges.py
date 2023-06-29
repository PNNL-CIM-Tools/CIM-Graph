from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import cimgraph.data_profile.rc4_2021 as cim


def get_all_edges_sparql(feeder_mrid: str, typed_catalog: dict[type, dict[str, object]], cim_class: str) -> str: 
    """ 
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    class_name = cim_class.__name__
    mrid_list = list(typed_catalog[cim_class].keys())


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?attribute ?value ?edge_mRID ?edge_class
        WHERE {          
          ?eq r:type cim:%s."""%class_name
    query_message += """
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:Equipment.EquipmentContainer ?fdr.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        {?eq (cim:|!cim:) ?value.
         ?eq ?attr ?value.}
        UNION
        {?value (cim:|!cim:) ?eq.
         ?value ?attr ?eq.}
        
        {bind(strafter(str(?attr),"#") as ?attribute)}
          
        OPTIONAL {?value cim:IdentifiedObject.mRID ?edge_mRID.
                  ?value a ?classraw.
                  bind(strafter(str(?classraw),"CIM100#") as ?edge_class)}
        }

        ORDER by  ?name ?attribute
        """
    return query_message