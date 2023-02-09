from __future__ import annotations
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import cimlab.data_profile.rc4_2021 as cim
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

    mrid_list = list(typed_catalog[cim.TapChangerControl].keys())
    asset_list = list(typed_catalog[cim.TransformerTank].keys())


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?TapChanger ?mode ?monitoredPhase ?enabled ?discrete ?targetValue ?targetDeadband
        ?lineDropCompensation ?lineDropR ?lineDropX ?reverseLineDropR ?reverseLineDropX ?limitVoltage 
        ?Terminal
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        
        WHERE {          
          ?eq r:type cim:TapChangerControl.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    
    # add all assets
    query_message += """               }
        VALUES ?TransformerTank {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """               } 
        #get feeder id from TransformerTank
        ?tap cim:TapChanger.TapChangerControl ?eq.
        ?tap cim:RatioTapChanger.TransformerEnd ?end.
        ?tap cim:IdentifiedObject.mRID ?TapChanger.
        ?end cim:TransformerTankEnd.TransformerTank ?tank.
        ?end cim:IdentifiedObject.mRID ?TransformerEnd.
        ?tank cim:IdentifiedObject.mRID ?TransformerTank.
        ?tank cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        OPTIONAL {?eq cim:RegulatingControl.mode ?md
                 bind(strafter(str(?md),"#RegulatingControlModeKind") as ?mode).}
        OPTIONAL {?eq cim:RegulatingControl.Terminal ?term.
                  ?term cim:IdentifiedObject.mRID ?Terminal.}
        OPTIONAL {?eq cim:RegulatingControl.monitoredPhase ?phs.
                  bind(strafter(str(?phs),"#PhaseCode") as ?monitoredPhase).}
        OPTIONAL {?eq cim:RegulatingControl.enabled ?enabled.}
        OPTIONAL {?eq cim:RegulatingControl ?discrete.}
        OPTIONAL {?eq cim:RegulatingControl.targetValue ?targetValue.}
        OPTIONAL {?eq cim:RegulatingControl.targetDeadband ?targetDeadband.}
        OPTIONAL {?eq cim:TapChangerControl.lineDropCompensation ?lineDropCompensation.}
        OPTIONAL {?eq cim:TapChangerControl.lineDropR ?lineDropR.}
        OPTIONAL {?eq cim:TapChangerControl.lineDropX ?lineDropX.}
        OPTIONAL {?eq cim:TapChangerControl.reverseLineDropR ?reverseLineDropR.}
        OPTIONAL {?eq cim:TapChangerControl.reverseLineDropX ?reverseLineDropX.}
        OPTIONAL {?eq cim:TapChangerControl.limitVoltage ?limitVoltage.}

        }
        GROUP by ?mRID ?name ?TapChanger ?mode ?monitoredPhase ?enabled ?discrete ?targetValue ?targetDeadband
        ?lineDropCompensation ?lineDropR ?lineDropX ?reverseLineDropR ?reverseLineDropX ?limitVoltage 
        ?Terminal

        ORDER by  ?name
        """
    return query_message