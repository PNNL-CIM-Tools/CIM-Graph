from typing import List
from dataclasses import dataclass, field

import cim.data_profile as cim

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?Location ?p ?q ?phase ?EnergyConsumer
        WHERE {          
          ?eq r:type cim:EnergyConsumerPhase.
          #VALUES ?fdrid {"%s"} #feeder_id association missing!
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        OPTIONAL {?eq cim:EnergyConsumerPhase.p ?p.}
        OPTIONAL {?eq cim:EnergyConsumerPhase.q ?q.}
        OPTIONAL {?eq cim:EnergyConsumerPhase.phase ?phase.}

        OPTIONAL {?eq cim:EnergyConsumerPhase.EnergyConsumer ?ec.
                  ?ec cim:IdentifiedObject.mRID ?EnergyConsumer.}
        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?p ?q ?phase ?EnergyConsumer
        ORDER by  ?name
        """
    return query_message