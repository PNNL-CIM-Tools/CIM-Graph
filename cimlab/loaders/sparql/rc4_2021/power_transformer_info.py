from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name
        (group_concat(distinct ?Asset; separator=";") as ?Assets) 
        (group_concat(distinct ?TransformerTankInfo; separator=";") as ?TransformerTankInfos) 

        WHERE {          
          ?eq r:type cim:PowerTransformerInfo.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
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