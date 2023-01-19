from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?phase ?p ?q ?PowerElectronicsConnection  
        WHERE {          
          ?eq r:type cim:PowerElectronicsConnectionPhase.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:PowerElectronicsConnectionPhase.PowerElectronicsConnection ?pec.
        ?pec cim:IdentifiedObject.mRID ?PowerElectronicsConnection.
        ?pec cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:PowerElectronicsConnectionPhase.phase ?phs.
                 bind(strafter(str(?phs),"SinglePhaseKind.") as ?phase)}

        OPTIONAL {?eq cim:PowerElectronicsConnectionPhase.p ?p.}
        OPTIONAL {?eq cim:PowerElectronicsConnectionPhase.q ?q.}

        }
        GROUP by ?mRID ?name ?phase ?p ?q ?PowerElectronicsConnection
        ?aggregate ?inService
        ORDER by  ?name
        """
    return query_message