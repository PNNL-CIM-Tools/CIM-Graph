from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?RegulatingControl ?aVRDelay ?b0PerSection 
        ?bPerSection ?controlEnabled ?g0PerSection ?gPerSection ?grounded ?maximumSections ?nomU 
        ?normalSections ?phaseConnection ?sections ?Terminals ?ShuntCompensatorPhase 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        WHERE { 
          ?eq r:type cim:LinearShuntCompensator.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:Equipment.EquipmentContainer ?fdr. #filter by feeder
        ?fdr cim:IdentifiedObject.mRID ?fdrid. #filter by feeder
        ?eq cim:IdentifiedObject.mRID ?mRID. #get cap mrid
        ?eq cim:IdentifiedObject.name ?name. #get cap name

        ?eq cim:ConductingEquipment.BaseVoltage ?bv. #get basevoltage object
        ?bv cim:IdentifiedObject.mRID ?BaseVoltage. 

        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc. #get location object
            ?loc cim:IdentifiedObject.mRID ?Location.} #get location mrid

        OPTIONAL {?ctl cim:RegulatingControl.RegulatingCondEq ?eq. #get control
            ?ctl cim:RegulatingControl.enabled ?controlEnabled. #get enabled
            ?ctl cim:IdentifiedObject.mRID ?RegulatingControl} #get control mrid

        ?t cim:Terminal.ConductingEquipment ?eq.
        ?t cim:IdentifiedObject.mRID ?Terminals
        OPTIONAL {?meas cim:Measurement.Terminal ?t.
            ?meas cim:IdentifiedObject.mRID ?Measurement}

        OPTIONAL {?eq cim:ShuntCompensator.grounded ?grounded.}
        OPTIONAL {?eq cim:ShuntCompensator.maximumSections ?maximumSections.}
        OPTIONAL {?eq cim:ShuntCompensator.nomU ?nomU.}
        OPTIONAL {?eq cim:ShuntCompensator.normalSections ?normalSections.}
        OPTIONAL {?eq cim:ShuntCompensator.aVRDelay ?aVRDelay.}
        OPTIONAL {?eq cim:ShuntCompensator.phaseConnection ?phaseConn.
            bind(strafter(str(?phaseConn),"CIM100#") as ?phaseConnection)}
        OPTIONAL {?spc cim:ShuntCompensatorPhase.ShuntCompensator ?eq.
            ?spc cim:IdentifiedObject.mRID ?ShuntCompensatorPhase.}

        OPTIONAL {?eq cim:LinearShuntCompensator.b0PerSection ?b0PerSection.}
        OPTIONAL {?eq cim:LinearShuntCompensator.bPerSection ?bPerSection.}
        OPTIONAL {?eq cim:LinearShuntCompensator.g0PerSection ?g0PerSection.}
        OPTIONAL {?eq cim:LinearShuntCompensator.gPerSection ?gPerSection.}
        }
        GROUP by  ?mRID ?name ?BaseVoltage ?Location ?RegulatingControl ?aVRDelay ?b0PerSection 
        ?bPerSection ?controlEnabled ?g0PerSection ?gPerSection ?grounded ?maximumSections ?nomU
        ?normalSections ?phaseConnection ?sections ?Terminals ?ShuntCompensatorPhase
        ORDER by  ?name
        """
    return query_message