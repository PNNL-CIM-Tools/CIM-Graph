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

    mrid_list = list(typed_catalog[cim.LoadBreakSwitch].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?inTransitTime ?breakingCapacity ?ratedCurrent ?normalOpen 
        ?open ?retained
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        (group_concat(distinct ?Switch_Phase; separator=";") as ?SwitchPhase) 

        WHERE {          
          ?eq r:type cim:LoadBreakSwitch.
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
        
        OPTIONAL {?eq cim:ProtectedSwitch.breakingCapacity ?breakingCapacity.}
        OPTIONAL {?eq cim:Switch.ratedCurrent ?ratedCurrent.}
        OPTIONAL {?eq cim:Switch.normalOpen ?normalOpen.}
        OPTIONAL {?eq cim:Switch.open ?open.}
        OPTIONAL {?eq cim:Switch.retained ?retained.}

        OPTIONAL {?phs cim:SwitchPhase.Switch ?eq.
                  ?phs cim:IdentifiedObject ?Switch_Phase.}
        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?inTransitTime ?breakingCapacity ?ratedCurrent ?normalOpen
        ?open ?retained

        ORDER by  ?name
        """
    return query_message