from typing import List
from dataclasses import dataclass, field


def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?maxP ?minP ?ratedE ?storedE ?batteryState ?PowerElectronicsConnection ?inService 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
 
        WHERE {          
          ?eq r:type cim:PowerElectronicsConnection.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?pec cim:PowerElectronicsConnection.PowerElectronicsUnit ?eq.
        ?pec cim:IdentifiedObject.mRID ?PowerElectronicsConnection.
        ?pec cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?eq.
          ?meas cim:IdentifiedObject.mRID ?Measurement}

        OPTIONAL {?eq cim:PowerElectronicsUnit.maxP ?maxP.}
        OPTIONAL {?eq cim:PowerElectronicsUnit.minP ?maxQ.}
        OPTIONAL {?eq cim:BatteryUnit.ratedE ?ratedE.}
        OPTIONAL {?eq cim:BatteryUnit.storedE ?storedE.}
        OPTIONAL {?eq cim:BatteryUnit.batteryState ?state.
                  bind(strafter(str(?phs),"BatteryState.") as ?batteryState)}
        
        #OPTIONAL {?eq cim:Equipment.aggregate ?aggregate.}
        OPTIONAL {?eq cim:Equipment.inService ?inService.}
        #OPTIONAL {?eq cim:Equipment.networkAnalysisEnable ?networkAnalysisEnabled.}
        #OPTIONAL {?eq cim:Equipment.normallyInService ?normallyInService.}

                  
        }
        GROUP by ?mRID ?name ?maxP ?minP ?ratedE ?storedE ?batteryState ?PowerElectronicsConnection ?inService
        ORDER by  ?name
        """
    return query_message