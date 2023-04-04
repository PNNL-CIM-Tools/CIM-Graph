from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import cimgraph.data_profile.rc4_2021 as cim


def get_all_attributes(feeder_mrid: str, typed_catalog: dict[type, dict[str, object]]) -> str: 
    """ Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    mrid_list = list(typed_catalog[cim.EnergyConsumerPhase].keys())
    asset_list = list(typed_catalog[cim.EnergyConsumer].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?p ?q ?phase ?EnergyConsumer  
        WHERE {          
          ?eq r:type cim:EnergyConsumerPhase.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:EnergyConsumerPhase.EnergyConsumer ?ec.
        ?ec cim:IdentifiedObject.mRID ?EnergyConsumer.
        ?ec cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        OPTIONAL {?eq cim:EnergyConsumerPhase.p ?p.}
        OPTIONAL {?eq cim:EnergyConsumerPhase.q ?q.}
        OPTIONAL {?eq cim:EnergyConsumerPhase.phase ?phs
                 bind(strafter(str(?phs),"SinglePhaseKind.") as ?phase)}

        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?p ?q ?phase ?EnergyConsumer
        ORDER by  ?name
        """
    return query_message