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

    mrid_list = list(typed_catalog[cim.PowerTransformerInfo].keys())
    asset_list = list(typed_catalog[cim.TransformerTank].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name
        (group_concat(distinct ?Asset; separator=";") as ?Assets) 
        (group_concat(distinct ?TransformerTankInfo; separator=";") as ?TransformerTankInfos) 

        WHERE {          
          ?eq r:type cim:PowerTransformerInfo.
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
    query_message += """          }
        #get feeder id from TransformerTank
        ?asset cim:Asset.AssetInfo ?tankinfo.
        ?asset cim:Asset.PowerSystemResources ?tank.
        ?tank cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        ?tank cim:IdentifiedObject.mRID ?TransformerTank.
        ?asset cim:IdentifiedObject.mRID ?Asset.
        
        ?tankinfo cim:TransformerTankInfo.PowerTransformerInfo ?eq.
        ?tankinfo cim:IdentifiedObject.mRID ?TransformerTankInfo.
       
        }
        GROUP by ?mRID ?name 
        ORDER by ?name
          """
    return query_message