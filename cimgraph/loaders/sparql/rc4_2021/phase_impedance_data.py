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

    mrid_list = list(typed_catalog[cim.PhaseImpedanceData].keys())
    asset_list = list(typed_catalog[cim.ACLineSegment].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?PhaseImpedance ?row ?column ?r ?x ?b 

        WHERE {          
          ?eq r:type cim:PhaseImpedanceData.
          VALUES ?fdrid {"%s"}
          """%feeder_mrid
    # add all equipment mRID
#     for mrid in mrid_list:
#         query_message += ' "%s" \n'%mrid
        
    # add all assets
    query_message += """               
        VALUES ?ACLineSegment {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """               } 
        ?eq cim:PhaseImpedanceData.PhaseImpedance ?pli.
        ?line cim:ACLineSegment.PerLengthImpedance ?pli.
        ?pli cim:IdentifiedObject.mRID ?PhaseImpedance.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?line cim:IdentifiedObject.mRID ?ACLineSegment.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        #?eq c:IdentifiedObject.mRID ?mRID. #mRID MISSING FROM XML
        bind(strafter(str(?eq),"sparql#") as ?mRID).
        #?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:PhaseImpedanceData.row ?row.}
        OPTIONAL {?eq cim:PhaseImpedanceData.column ?column.}
        OPTIONAL {?eq cim:PhaseImpedanceData.r ?r.}
        OPTIONAL {?eq cim:PhaseImpedanceData.x ?x.}
        OPTIONAL {?eq cim:PhaseImpedanceData.b ?b.}

        }
        GROUP by ?mRID ?name ?PhaseImpedance ?row ?column ?r ?x ?b 
        ORDER by  ?name
        """
    return query_message