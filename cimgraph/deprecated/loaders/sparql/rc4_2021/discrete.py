from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import cimgraph.data_profile.rc4_2021 as cim


def get_all_attributes(feeder_mrid: str, typed_catalog: dict[type, dict[str, object]]) -> str: 
    """ 
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        typed_catalog (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by 
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    mrid_list = list(typed_catalog[cim.Discrete].keys())


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?PowerSystemResource ?measurementType ?phases ?Terminal 
        ?minValue ?maxValue ?normalValue ?positiveFlowIn
        (group_concat(distinct ?Location; separator=';') as ?Locations)

        WHERE {          
          ?eq r:type cim:Discrete.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:Measurement.PowerSystemResource ?psr.
        ?psr cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        ?eq cim:Measurement.Terminal ?t.
        ?t cim:IdentifiedObject.mRID ?Terminal.

        OPTIONAL {?eq cim:Measurement.phases ?phs.
                 bind(strafter(str(?phs),"PhaseCode.") as ?phases)}
                 
        OPTIONAL {?psr cim:PowerSystemResource.Location ?loc.
                  ?loc cim:IdentifiedObject.mRID ?Location.}
        
        OPTIONAL {?eq cim:Measurement.measurementType ?measurementType.}
        OPTIONAL {?eq cim:Measurement.minValue ?minValue.}
        OPTIONAL {?eq cim:Measurement.maxValue ?maxValue.}
        OPTIONAL {?eq cim:Measurement.normalValue ?normalValue.}
        OPTIONAL {?eq cim:Measurement.positiveFlowIn ?postiveFlowIn.}
        # AnalogValues
        # LimitSets
        # Procedures

       

        }
        GROUP by ?mRID ?name ?PowerSystemResource ?Location ?measurementType ?phases ?Terminal 
        ?minValue ?maxValue ?normalValue ?positiveFlowIn
        
        ORDER by  ?name
        """
    return query_message