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

    mrid_list = list(typed_catalog[cim.ShuntCompensatorPhase].keys())
    asset_list = list(typed_catalog[cim.LinearShuntCompensator].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?Location ?phase ?ShuntCompensator
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        WHERE {          
          ?eq r:type cim:ShuntCompensatorPhase.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
        
    # add all assets
    query_message += """               }
        VALUES ?ShuntCompensator {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """               } 
        
        #trace back up to EquipmentContainer via ShuntCompensator
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?cap cim:Equipment.EquipmentContainer ?fdr.
        ?eq cim:ShuntCompensatorPhase.ShuntCompensator ?cap.
        ?cap cim:IdentifiedObject.mRID ?ShuntCompensator.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
                  ?loc cim:IdentifiedObject.mRID ?Location.}

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?line.
                  ?meas cim:Measurement.phases ?measphs.
                  ?meas cim:IdentifiedObject.mRID ?meas_id.
                  ?meas a ?meas_cls.
                  bind(concat(str(?meas_id),",",strafter(str(?meas_cls),"CIM100#")) as ?Measurement).}
        
        OPTIONAL {?eq cim:ShuntCompensatorPhase.phase ?phs.
                 bind(strafter(str(?phs),"SinglePhaseKind.") as ?phase)}

        #FILTER regex(STR(?measphs), ?phase)

        }
        GROUP by ?mRID ?name ?Location ?phase ?ShuntCompensator ?measphs
        ORDER by  ?name

        """
    return query_message