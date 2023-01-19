from typing import List
from dataclasses import dataclass, field

# import cim.data_profile as cim

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?Location ?phase ?sequenceNumber ?ACLineSegment ?WireInfo
        #(group_concat(distinct ?ACLineSegment; separator=';') as ?ACLineSegments)
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        WHERE {          
          ?eq r:type cim:ACLineSegmentPhase.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        
        #trace back up to EquipmentContainer via ACLineSegment
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?eq cim:ACLineSegmentPhase.ACLineSegment ?line.
        ?line cim:IdentifiedObject.mRID ?ACLineSegment.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
                  ?loc cim:IdentifiedObject.mRID ?Location.}

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?line.
                  ?meas cim:Measurement.phases ?measphs.
                  ?meas cim:IdentifiedObject.mRID ?Measurement.}
        
        OPTIONAL {?eq cim:ACLineSegmentPhase.phase ?phs.
                 bind(strafter(str(?phs),"SinglePhaseKind.") as ?phase)}
        OPTIONAL {?eq cim:ACLineSegmentPhase.sequenceNumber ?sequenceNumber.}
        OPTIONAL {?eq cim:ACLineSegmentPhase.WireInfo ?wire.
                  ?wire cim:IdentifiedObject.mRID ?WireInfo.}

        FILTER regex(STR(?measphs), ?phase)

        }
        GROUP by ?mRID ?name ?Location ?phase ?sequenceNumber ?ACLineSegment ?WireInfo ?measphs
        ORDER by  ?name

        """
    return query_message