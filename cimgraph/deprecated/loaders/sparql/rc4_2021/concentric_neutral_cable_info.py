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

    mrid_list = list(typed_catalog[cim.ConcentricNeutralCableInfo].keys())
    asset_list = list(typed_catalog[cim.ACLineSegment].keys())
    
    query_message = """
        PREFIX r: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim: <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?coreRadius ?coreStrandCount ?gmr ?insulated ?insulationMaterial 
         ?insulationThickness ?material ?rAC25 ?rAC50 ?rAC75 ?rDC20 ?radius ?ratedCurrent ?strandCount
         ?sizeDescription ?constructionKind ?diameterOverInsulation ?diameterOverJacket ?diameterOverScreen
         ?isStrandFill ?nominalTemperature ?sheathAsNeutral ?shieldMaterial ?diameterOverNeutral
          ?neutralStrandRadius ?neutralStrandGmr ?neutralStrandRDC20 ?neutralStrandCount
         (group_concat(distinct ?ACLineSegmentPhase; separator=';') as ?ACLineSegmentPhases)
        WHERE {          
          ?eq r:type cim:ConcentricNeutralCableInfo.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
        
    # add all assets
    query_message += """               }
        VALUES ?ACLineSegment {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """               } 
        #trace back up to EquipmentContainer via ACLineSegment
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?linephase cim:ACLineSegmentPhase.ACLineSegment ?line.
        ?linephase cim:ACLineSegmentPhase.WireInfo ?eq.
        ?linephase cim:IdentifiedObject.mRID ?ACLineSegmentPhase.
        ?line cim:IdentifiedObject.mRID ?ACLineSegment.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        #collect inherited WireInfo attributes
        OPTIONAL {?eq cim:WireInfo.coreRadius ?coreRadius.}
        OPTIONAL {?eq cim:WireInfo.coreStrandCount ?coreStrandCount.}        
        OPTIONAL {?eq cim:WireInfo.gmr ?gmr.}
        OPTIONAL {?eq cim:WireInfo.insulated ?insulated.} 
        OPTIONAL {?eq cim:WireInfo.insulationMaterial ?ins.
                  bind(strafter(str(?ins),"WireInsulationKind.") as ?insulationMaterial).}
        OPTIONAL {?eq cim:WireInfo.insulationThickness ?insulationThickness.}
        OPTIONAL {?eq cim:WireInfo.material ?material.}
        OPTIONAL {?eq cim:WireInfo.rAC25 ?rAC25.}
        OPTIONAL {?eq cim:WireInfo.rAC50 ?rAC50.}
        OPTIONAL {?eq cim:WireInfo.rAC75 ?rAC75.}
        OPTIONAL {?eq cim:WireInfo.rDC20 ?rDC20.}
        OPTIONAL {?eq cim:WireInfo.radius ?radius.}
        OPTIONAL {?eq cim:WireInfo.ratedCurrent ?ratedCurrent.}
        OPTIONAL {?eq cim:WireInfo.strandCount ?strandCount.}
        OPTIONAL {?eq cim:WireInfo.sizeDescription ?sizeDescription.}

        #collect inherited CableInfo attributes
        OPTIONAL {?eq cim:CableInfo.constructionKind ?constructionKind.}
        OPTIONAL {?eq cim:CableInfo.diameterOverCore ?diameterOverCore.}
        OPTIONAL {?eq cim:CableInfo.diameterOverInsulation ?diameterOverInsulation.}
        OPTIONAL {?eq cim:CableInfo.diameterOverJacket ?diameterOverJacket.}
        OPTIONAL {?eq cim:CableInfo.diameterOverScreen ?diameterOverScreen.}
        OPTIONAL {?eq cim:CableInfo.isStrandFill ?isStrandFill.}
        OPTIONAL {?eq cim:CableInfo.nominalTemperature ?nominalTemperature.}
        OPTIONAL {?eq cim:CableInfo.outerJacketKind ?outerJacketKind.}
        OPTIONAL {?eq cim:CableInfo.sheathAsNeutral ?sheathAsNeutral.}
        OPTIONAL {?eq cim:CableInfo.shieldMaterial ?shieldMaterial.}
        
        #collect TapeShieldCableInfo attributes
        OPTIONAL {?eq cim:ConcentricNeutralCableInfo.diameterOverNeutral ?diameterOverNeutral.}
        OPTIONAL {?eq cim:ConcentricNeutralCableInfo.neutralStrandRadius ?neutralStrandRadius.}
        OPTIONAL {?eq cim:ConcentricNeutralCableInfo.neutralStrandGmr ?neutralStrandGmr.}
        OPTIONAL {?eq cim:ConcentricNeutralCableInfo.neutralStrandRDC20 ?neutralStrandRDC20.}
        OPTIONAL {?eq cim:ConcentricNeutralCableInfo.neutralStrandCount ?neutralStrandCount.}

        }
        GROUP BY ?mRID ?name ?coreRadius ?coreStrandCount ?gmr ?insulated ?insulationMaterial 
         ?insulationThickness ?material ?rAC25 ?rAC50 ?rAC75 ?rDC20 ?radius ?ratedCurrent ?strandCount
         ?sizeDescription ?constructionKind ?diameterOverInsulation ?diameterOverJacket ?diameterOverScreen
         ?isStrandFill ?nominalTemperature ?sheathAsNeutral ?shieldMaterial ?diameterOverNeutral
         ?neutralStrandRadius ?neutralStrandGmr ?neutralStrandRDC20 ?neutralStrandCount
         
        ORDER by  ?name
        """
    return query_message