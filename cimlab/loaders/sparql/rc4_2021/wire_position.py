from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?sequenceNumber ?xCoord ?yCoord ?WireSpacingInfo

        WHERE {          
          ?eq r:type cim:WirePosition.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:WirePosition.WireSpacingInfo ?wsi.
        ?wsi cim:IdentifiedObject.mRID ?WireSpacingInfo.
        ?line cim:ACLineSegment.WireSpacingInfo ?wsi.
        ?line cim:Equipment.EquipmentContainer ?fdr.
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