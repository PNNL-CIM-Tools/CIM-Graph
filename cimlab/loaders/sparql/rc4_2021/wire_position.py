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

    mrid_list = list(typed_catalog[cim.WirePosition].keys())
    asset_list = list(typed_catalog[cim.ACLineSegment].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?sequenceNumber ?xCoord ?yCoord ?WireSpacingInfo

        WHERE {          
          ?eq r:type cim:WirePosition.
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
        ?eq cim:WirePosition.WireSpacingInfo ?wsi.
        ?wsi cim:IdentifiedObject.mRID ?WireSpacingInfo.
        ?line cim:ACLineSegment.WireSpacingInfo ?wsi.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?line cim:IdentifedObject.mRID ?ACLineSegment.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:WirePosition.sequenceNumber ?sequenceNumber.}
        OPTIONAL {?eq cim:WirePosition.xCoord ?xCoord.}
        OPTIONAL {?eq cim:WirePosition.yCoord ?yCoord.}

        }
        GROUP by ?mRID ?name ?sequenceNumber ?xCoord ?yCoord ?WireSpacingInfo
        ORDER by  ?name
        """
    return query_message