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
    
    mrid_list = list(typed_catalog[cim.BatteryUnit].keys())
    asset_list = list(typed_catalog[cim.PowerElectronicsConnection].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?maxP ?minP ?ratedE ?storedE ?batteryState ?PowerElectronicsConnection ?inService 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
 
        WHERE {          
          ?eq r:type cim:BatteryUnit.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
        
    # add all assets
    query_message += """               }
        VALUES ?PowerElectronicsConnection {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """               } 
        ?pec cim:PowerElectronicsConnection.PowerElectronicsUnit ?eq.
        ?pec cim:IdentifiedObject.mRID ?PowerElectronicsConnection.
        ?pec cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?eq.
                  ?meas cim:IdentifiedObject.mRID ?meas_id.
                  ?meas a ?meas_cls.
                  bind(concat(str(?meas_id),",",strafter(str(?meas_cls),"CIM100#")) as ?Measurement).}

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