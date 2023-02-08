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

    mrid_list = list(typed_catalog[cim.PowerElectronicsConnectionPhase].keys())

    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?phase ?p ?q ?PowerElectronicsConnection  
        WHERE {          
          ?eq r:type cim:PowerElectronicsConnectionPhase.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
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