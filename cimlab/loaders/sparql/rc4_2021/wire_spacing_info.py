from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?usage ?phaseWireCount ?phaseWireSpacing ?isCable 
        (group_concat(distinct ?ACLineSegment; separator=';') as ?ACLineSegments)
        (group_concat(distinct ?WirePosition; separator=';') as ?WirePositions)
        WHERE {          
          ?eq r:type cim:WireSpacingInfo.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
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
                  ?wp cim:IdentifiedObject.mRID ?WirePosition.}
        }
        GROUP by ?mRID ?name ?usage ?phaseWireCount ?phaseWireSpacing ?isCable
        ORDER by  ?name
        """
    return query_message