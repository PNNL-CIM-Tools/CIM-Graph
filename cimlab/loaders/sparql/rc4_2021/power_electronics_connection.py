from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?maxIFault ?maxP ?maxQ ?p ?q ?ratedS ?ratedU 
        ?aggregate ?inService
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        (group_concat(distinct ?PowerElectronicsU; separator=';') as ?PowerElectronicsUnit)  
        (group_concat(distinct ?PowerElectronicsConnectionPhase; separator=';') as ?PowerElectronicsConnectionPhases) 
        WHERE {          
          ?eq r:type cim:PowerElectronicsConnection.
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

        OPTIONAL {?eq cim:PowerElectronicsConnection.PowerElectronicsUnit ?pec.
                  ?pec cim:IdentifiedObject.mRID ?PowerElectronicsU.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.maxIFault ?maxIFault.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.p ?p.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.q ?q.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.maxP ?maxP.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.maxQ ?maxQ.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.ratedS ?ratedS.}
        OPTIONAL {?eq cim:PowerElectronicsConnection.ratedU ?ratedU.}
        
        OPTIONAL {?eq cim:Equipment.aggregate ?aggregate.}
        OPTIONAL {?eq cim:Equipment.inService ?inService.}
        #OPTIONAL {?eq cim:Equipment.networkAnalysisEnable ?networkAnalysisEnabled.}
        #OPTIONAL {?eq cim:Equipment.normallyInService ?normallyInService.}
        
        OPTIONAL {?phs cim:PowerElectronicsConnectionPhase.PowerElectronicsConnection ?eq.
                  ?phs cim:IdentifiedObject.mRID ?PowerElectronicsConnectionPhase.}
                  
        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?maxIFault ?maxP ?maxQ ?p ?q ?ratedS ?ratedU 
        ?aggregate ?inService
        ORDER by  ?name
        """
    return query_message