from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import cimlab.data_profile.rc4_2021 as cim
def get_all_attributes(feeder_mrid: str, typed_catalog: dict[type, dict[str, object]]) -> str: 
    """ Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    mrid_list = list(typed_catalog[cim.PerLengthSequenceImpedance].keys())
    asset_list = list(typed_catalog[cim.ACLineSegment].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?bch ?r ?x ?gch ?b0ch ?r0 ?x0 ?g0ch 
        (group_concat(distinct ?ACLineSegment; separator=';') as ?ACLineSegments)  
        WHERE {          
          ?eq r:type cim:PerLengthSequenceImpedance.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
        
    # add all assets
    query_message += """               }
        VALUES ?ACLineSegment {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """               } 
        ?line cim:ACLineSegment.PerLengthImpedance ?eq.
        ?line cim:IdentifiedObject.mRID ?ACLineSegment.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.bch ?bch.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.r ?r0.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedancet.x ?x0.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.g ?r0.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.b0ch ?b0.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.r0 ?r0.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.x0 ?x0.}
        OPTIONAL {?eq cim:PerLengthSequenceImpedance.g0ch ?b0.}

        }
        GROUP by ?mRID ?name  ?bch ?r ?x ?gch ?b0ch ?r0 ?x0 ?g0ch 
        ORDER by  ?name
        """
    return query_message