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

    mrid_list = list(typed_catalog[cim.SynchronousMachine].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?p ?q ?ratedS ?ratedU ?ratedPowerFactor ?ikk ?maxQ ?minQ
            (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
            (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        WHERE {          
          ?eq r:type cim:SynchronousMachine.
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

        OPTIONAL {?meas cim:Measurement.Terminal ?t.
        ?meas cim:IdentifiedObject.mRID ?meas_id.
        ?meas a ?meas_cls.
        bind(concat(str(?meas_id),",",strafter(str(?meas_cls),"CIM100#")) as ?Measurement).}
        
        OPTIONAL {?eq cim:SynchronousMachine.ikk ?ikk.}
        OPTIONAL {?eq cim:SynchronousMachine.maxQ ?maxQ.}
        OPTIONAL {?eq cim:SynchronousMachine.minQ ?minQ.}
        # operatingMode
        # type

        # IN UML, THESE ATTRIBUTES BELONG TO ROTATINGMACHINE NOT SYNCHRNONOUSMACHINE
        OPTIONAL {?eq cim:SynchronousMachine.p ?p.}
        OPTIONAL {?eq cim:SynchronousMachine.q ?q.}
        OPTIONAL {?eq cim:SynchronousMachine.ratedS ?ratedS.}
        OPTIONAL {?eq cim:SynchronousMachine.ratedU ?ratedU.}
        OPTIONAL {?eq cim:SynchronousMachine.ratedPowerFactor ?ratedPowerFactor.}


        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?p ?q ?ratedS ?ratedU ?ratedPowerFactor ?ikk ?maxQ ?minQ
        ORDER by  ?name
        """
    return query_message