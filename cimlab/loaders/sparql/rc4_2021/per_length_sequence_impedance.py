from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?bch ?r ?x ?gch ?b0ch ?r0 ?x0 ?g0ch 
        (group_concat(distinct ?ACLineSegment; separator=';') as ?ACLineSegments)  
        WHERE {          
          ?eq r:type cim:PerLengthSequenceImpedance.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
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