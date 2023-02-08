from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import cimlab.data_profile.rc4_2021 as cim
def get_all_attributes(feeder_mrid: str, typed_catalog: dict[type, dict[str, object]]) -> str: 
    """ Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    mrid_list = list(typed_catalog[cim.PowerElectronicsConnection].keys())

    
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
          VALUES ?mRID {"""%feeder_mrid
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