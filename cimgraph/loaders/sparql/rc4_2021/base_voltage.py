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
        sparql_message: query string that can be used in blazegraph connection or STOMP client
    """
    
    mrid_list = list(typed_catalog[cim.BaseVoltage].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?nominalVoltage
        (group_concat(distinct ?ConductingEq; separator=';') as ?ConductingEquipment)
        (group_concat(distinct ?TransformerEnd; separator=';') as ?TransformerEnds)
        (group_concat(distinct ?TopoNode; separator=';') as ?TopologicalNode)
        (group_concat(distinct ?VoltLevel; separator=';') as ?VoltageLevel)
        (group_concat(distinct ?NetworkAsset; separator=';') as ?NetworkAssetDeployment)
        WHERE {          
          ?eq r:type cim:BaseVoltage.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?condeq cim:ConductingEquipment.BaseVoltage ?eq.
        ?condeq cim:IdentifiedObject.mRID ?ConductingEq.
        ?condeq cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        OPTIONAL {?eq cim:BaseVoltage.nominalVoltage ?nominalVoltage.}

                  
        OPTIONAL {?xfend cim:TransformerEnd.BaseVoltage ?eq.
                  ?xfend cim:IdentifiedObject.mRID ?TransformerEnd.}
                  
        OPTIONAL {?level cim:VoltageLevel.BaseVoltage ?eq.
                  ?level cim:IdentifiedObject.mRID ?VoltLevel.}
                  
        OPTIONAL {?asset cim:AssetDeployment.BaseVoltage ?eq.
                  ?asset cim:IdentifiedObject.mRID ?NetworkAsset.}

        }
        GROUP by  ?name ?mRID ?nominalVoltage
        ORDER by  ?name
        """
    return query_message