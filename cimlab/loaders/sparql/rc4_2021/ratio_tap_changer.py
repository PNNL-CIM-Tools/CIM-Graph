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

    mrid_list = list(typed_catalog[cim.RatioTapChanger].keys())
    asset_list = list(typed_catalog[cim.TransformerTank].keys())


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?BaseVoltage ?Location ?TransformerEnd ?highStep ?lowStep ?neutralStep 
        ?normalStep ?neutralU ?initialDelay ?subsequentDelay ?ltcFlag ?controlEnabled 
        ?tculControlMode ?tapChangerControl
        (group_concat(distinct ?Terminal; separator=";") as ?Terminals) 
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        
        WHERE {          
          ?eq r:type cim:RatioTapChanger.
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
        ?eq cim:RatioTapChanger.TransformerEnd ?end.
        ?end cim:TransformerTankEnd.TransformerTank ?tank.
        ?end cim:IdentifiedObject.mRID ?TransformerEnd.
        ?tank cim:IdentifiedObject.mRID ?TransformerTank.
        ?tank cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        
        OPTIONAL {?eq cim:ConductingEquipment.BaseVoltage ?bv.
        ?bv cim:IdentifiedObject.mRID ?BaseVoltage.}

        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        ?t cim:Terminal.ConductingEquipment ?eq.
        ?t cim:IdentifiedObject.mRID ?Terminal

        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?eq.
          ?meas cim:IdentifiedObject.mRID ?Measurement}

        OPTIONAL {?eq cim:TapChanger.TapChangerControl ?cntrl.
                  ?cntrl cim:IdentifiedObject.mRID ?TapChangerControl.}
                  
        OPTIONAL {?eq cim:RatioTapChanger.stepVoltageIncrement ?stepVoltageIncrement.}
        OPTIONAL {?eq RatioTapChanger.tculControlMode ?tcul.
               bind(strafter(str(?tcul),"#TransformerControlMode") as ?tculControlMode).}
               
        OPTIONAL {?eq cim:TapChanger.highStep ?highStep.}
        OPTIONAL {?eq cim:TapChanger.lowStep ?lowStep.}
        OPTIONAL {?eq cim:TapChanger.neutralStep ?neutralStep.}
        OPTIONAL {?eq cim:TapChanger.normalStep ?normalStep.}
        OPTIONAL {?eq cim:TapChanger.neutralU ?neutralU.}
        OPTIONAL {?eq cim:TapChanger.initialDelay ?initialDelay.}
        OPTIONAL {?eq cim:TapChanger.subsequentDelay ?subsequentDelay.}
        OPTIONAL {?eq cim:TapChanger.ltcFlag ?ltcFlag.}
        OPTIONAL {?eq cim:TapChanger.controlEnabled ?controlEnabled.}
        OPTIONAL {?eq cim:TapChanger.step ?step.}

        }
        GROUP by ?mRID ?name ?BaseVoltage ?Location ?TransformerEnd ?highStep ?lowStep ?neutralStep 
        ?normalStep ?neutralU ?initialDelay ?subsequentDelay ?ltcFlag ?controlEnabled 
        ?tculControlMode ?tapChangerControl

        ORDER by  ?name
        """
    return query_message