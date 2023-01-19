from typing import List
from dataclasses import dataclass, field


def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?ratedCurrent ?normalOpen ?open ?retained
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        (group_concat(distinct ?Switch_Phase; separator=";") as ?SwitchPhase) 

        WHERE {          
          ?eq r:type cim:Disconnector.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:ConductingEquipment.BaseVoltage ?bv.
        ?bv cim:IdentifiedObject.mRID ?BaseVoltage.}

        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        ?t cim:Terminal.ConductingEquipment ?eq.
        ?t cim:IdentifiedObject.mRID ?Terminal

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?eq.
          ?meas cim:IdentifiedObject.mRID ?Measurement}

        OPTIONAL {?eq cim:Switch.ratedCurrent ?ratedCurrent.}
        OPTIONAL {?eq cim:Switch.normalOpen ?normalOpen.}
        OPTIONAL {?eq cim:Switch.open ?open.}
        OPTIONAL {?eq cim:Switch.retained ?retained.}

        OPTIONAL {?phs cim:SwitchPhase.Switch ?eq.
                  ?phs cim:IdentifiedObject ?Switch_Phase.}
        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?ratedCurrent ?normalOpen ?open ?retained

        ORDER by  ?name
        """
    return query_message