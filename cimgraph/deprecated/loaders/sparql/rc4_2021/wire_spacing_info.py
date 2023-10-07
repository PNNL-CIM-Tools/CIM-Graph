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

    mrid_list = list(typed_catalog[cim.WireSpacingInfo].keys())
    asset_list = list(typed_catalog[cim.ACLineSegment].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?usage ?phaseWireCount ?phaseWireSpacing ?isCable 
        (group_concat(distinct ?ACLineSegment; separator=';') as ?ACLineSegments)
        (group_concat(distinct ?WirePosition; separator=';') as ?WirePositions)
        WHERE {          
          ?eq r:type cim:WireSpacingInfo.
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
        
        ?line cim:ACLineSegment.WireSpacingInfo ?eq.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?line cim:IdentifiedObject.mRID ?ACLineSegment.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        #OPTIONAL {?eq cim:WireSpacingInfo.usage ?usage.}
        OPTIONAL {?eq cim:WireSpacingInfo.phaseWireCount ?phaseWireCount.}
        OPTIONAL {?eq cim:WireSpacingInfo.phaseWireSpacing ?phaseWireSpacing.}
        OPTIONAL {?eq cim:WireSpacingInfo.isCable ?isCable.}

        OPTIONAL {?wp cim:WirePosition.WireSpacingInfo ?eq.
                  ?wp cim:IdentifiedObject.mRID ?wp_id.
                  ?wp a ?wp_cls.
                  bind(concat(str(?wp_id),",",strafter(str(?wp_cls),"CIM100#")) as ?WirePosition).}
        }
        GROUP by ?mRID ?name ?usage ?phaseWireCount ?phaseWireSpacing ?isCable
        ORDER by  ?name
        """
    return query_message