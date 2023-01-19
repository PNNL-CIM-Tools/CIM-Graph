from typing import List
from dataclasses import dataclass, field



def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?constructionKind ?diameterOverInsulation ?diameterOverJacket ?diameterOverScreen
         ?isStrandFill ?nominalTemperature ?sheathAsNeutral ?shieldMaterial
        WHERE {          
          ?eq r:type cim:CableInfo.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
         OPTIONAL {?eq cim:CableInfo.constructionKind ?constructionKind.} #CableConstructionKind
         OPTIONAL {?eq cim:CableInfo.diameterOverCore ?diameterOverCore.} #Length
         OPTIONAL {?eq cim:CableInfo.diameterOverInsulation ?diameterOverInsulation.} #Length
         OPTIONAL {?eq cim:CableInfo.diameterOverJacket ?diameterOverJacket.} #Length
         OPTIONAL {?eq cim:CableInfo.diameterOverScreen ?diameterOverScreen} #Length
         OPTIONAL {?eq cim:CableInfo.isStrandFill ?isStrandFill } #Boolean,
         OPTIONAL {?eq cim:CableInfo.nominalTemperature ?nominalTemperature.} #Temperature,
         OPTIONAL {?eq cim:CableInfo.outerJacketKind ?outerJacketKind.} #CableOuterJacketKind,
         OPTIONAL {?eq cim:CableInfo.sheathAsNeutral ?sheathAsNeutral.} #Boolean,
         OPTIONAL {?eq cim:CableInfo.shieldMaterial ?shieldMaterial.} #CableShieldMaterialKind,




        }
        ORDER by  ?name
        """
    return query_message