from typing import List
from dataclasses import dataclass, field

import cim.data_profile as cim


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

 <cim:IdentifiedObject.mRID>_9EE93180-5EA6-42FC-8EC5-35B82D4F4D8C</cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>ts_1/0</cim:IdentifiedObject.name>
  <cim:WireInfo.sizeDescription>TSData_ts_1/0</cim:WireInfo.sizeDescription>
  <cim:WireInfo.gmr>0.00338328</cim:WireInfo.gmr>
  <cim:WireInfo.radius>0.0046736</cim:WireInfo.radius>
  <cim:WireInfo.rDC20>0.00059092798</cim:WireInfo.rDC20>
  <cim:WireInfo.rAC25>0.00060274654</cim:WireInfo.rAC25>
  <cim:WireInfo.rAC50>0.00060274654</cim:WireInfo.rAC50>
  <cim:WireInfo.rAC75>0.00060274654</cim:WireInfo.rAC75>
  <cim:WireInfo.ratedCurrent>165</cim:WireInfo.ratedCurrent>
  <cim:WireInfo.strandCount>0</cim:WireInfo.strandCount>
  <cim:WireInfo.coreStrandCount>0</cim:WireInfo.coreStrandCount>
  <cim:WireInfo.coreRadius>0</cim:WireInfo.coreRadius>
  <cim:WireInfo.insulated>true</cim:WireInfo.insulated>
  <cim:WireInfo.insulationThickness>0.005588</cim:WireInfo.insulationThickness>
  <cim:WireInfo.insulationMaterial rdf:resource="http://iec.ch/TC57/CIM100#WireInsulationKind.crosslinkedPolyethylene"/>
  <cim:CableInfo.isStrandFill>false</cim:CableInfo.isStrandFill>
  <cim:CableInfo.diameterOverCore>0.009652</cim:CableInfo.diameterOverCore>
  <cim:CableInfo.diameterOverInsulation>0.020828</cim:CableInfo.diameterOverInsulation>
  <cim:CableInfo.diameterOverJacket>0.026924</cim:CableInfo.diameterOverJacket>
  <cim:CableInfo.nominalTemperature>90</cim:CableInfo.nominalTemperature>
  <cim:CableInfo.diameterOverScreen>0.022098</cim:CableInfo.diameterOverScreen>
  <cim:TapeShieldCableInfo.tapeLap>20</cim:TapeShieldCableInfo.tapeLap>
  <cim:TapeShieldCableInfo.tapeThickness>0.000127</cim:TapeShieldCableInfo.tapeThickness>
  <cim:CableInfo.sheathAsNeutral>true</cim:CableInfo.sheathAsNeutral>


        }
        ORDER by  ?name
        """
    return query_message