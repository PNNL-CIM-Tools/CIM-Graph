from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?Location ?Switch ?closed ?normalOpen ?phaseSide1 ?phaseSide2
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 


        WHERE {          
          ?eq r:type cim:Fuse.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:SwitchPhase.Switch ?sw.
        ?sw cim:IdentifiedObject ?Switch.
        ?sw cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        OPTIONAL {?t cim:Terminal.ConductingEquipment ?eq.
                  ?t cim:IdentifiedObject.mRID ?Terminal.}

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?switch.
                  ?meas cim:Measurement.phases ?measphs.
                  ?meas cim:IdentifiedObject.mRID ?Measurement.}

        OPTIONAL {?eq cim:SwitchPhase.closed ?closed>
        OPTIONAL {?eq cim:SwitchPhase.normalOpen ?normalOpen>
        OPTIONAL {?eq cim:SwitchPhase.phaseSide1 ?phs1.
                 bind(strafter(str(?phs1),"SinglePhaseKind.") as ?phaseSide1)}
        OPTIONAL {?eq <cim:SwitchPhase.phaseSide2 ?ph2.
                 bind(strafter(str(?phs2),"SinglePhaseKind.") as ?phaseSide2)}

        FILTER regex(STR(?measphs), ?phase)

        OPTIONAL {
        }
        GROUP by ?mRID ?name ?Location ?Switch ?closed ?normalOpen ?phaseSide1 ?phaseSide2

        ORDER by  ?name
        """
    return query_message