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

    mrid_list = list(typed_catalog[cim.TransformerEndInfo].keys())
    asset_list = list(typed_catalog[cim.TransformerTank].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?ratedS ?ratedU ?r ?connectionKind ?phaseAngleClock ?endNumber
        ?shortTermS ?emergencyS ?insulationU ?GroundedEndShortCircuitTests ?EnergisedEndShortCircuitTests
        ?EnergisedEndNoLoadTests ?FromMeshImpedance ?ToMeshImpedance ?CoreAdmittance ?TransformerTankInfo
        (group_concat(distinct ?Asset; separator=";") as ?Assets) 

        WHERE {          
          ?eq r:type cim:TransformerEndInfo.
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
        ?eq cim:TransformerEndInfo.TransformerTankInfo ?tankinfo.
        ?asset cim:Asset.AssetInfo ?tankinfo.
        ?asset cim:Asset.PowerSystemResources ?tank.
        ?tank cim:IdentifiedObject.mRID ?TransformerTank.
        ?tank cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        ?tankinfo cim:IdentifiedObject.mRID ?TransformerTankInfo.
        ?asset cim:IdentifiedObject.mRID ?Asset
       
        OPTIONAL {?eq cim:TransformerEndInfo.endNumber ?endNumber.}
        OPTIONAL {?eq cim:TransformerEndInfo.connectionKind ?conn.
                  bind(strafter(str(?conn),"WindingConnection.") as ?connectionKind).}
        OPTIONAL {?eq cim:TransformerEndInfo.phaseAngleClock ?phaseAngleClock.}
        OPTIONAL {?eq cim:TransformerEndInfo.ratedU ?ratedU.}
        OPTIONAL {?eq cim:TransformerEndInfo.ratedS ?ratedS.}
        OPTIONAL {?eq cim:TransformerEndInfo.shortTermS ?shortTermS.}
        OPTIONAL {?eq cim:TransformerEndInfo.emergencyS ?emergencyS.}
        OPTIONAL {?eq cim:TransformerEndInfo.r ?r.}
        OPTIONAL {?eq cim:TransformerEndInfo.insulationU ?insulationU.}
        
        OPTIONAL {?gsct cim:ShortCircuitTest.GroundedEnds ?eq.
                  ?gsct cim:IdentifiedObject.mRID ?GroundedEndShortCircuitTests.}
                  
        OPTIONAL {?esct cim:ShortCircuitTest.EnergisedEnd ?eq.
                  ?esct cim:IdentifiedObject.mRID ?EnergisedEndShortCircuitTests.}
                  
        OPTIONAL {?enol cim:NoLoadTest.EnergisedEnd ?eq.
                  ?enol cim:IdentifiedObject.mRID ?EnergisedEndNoLoadTests.}
                  
        OPTIONAL {?tac cim:TransformerCoreAdmittace.TransformerEnd ?eq.
                  ?tac cim:IdentifiedObject.mRID ?CoreAdmittance.}
          
        OPTIONAL {?frmesh cim:TransformerMeshImpedance.FromTransformerEnd ?eq.
                  ?frmesh cim:IdentifiedObject.mRID ?FromMeshImpedance.}
          
        OPTIONAL {?frmesh cim:TransformerMeshImpedance.ToTransformerEnd ?eq.
                  ?frmesh cim:IdentifiedObject.mRID ?ToMeshImpedance.}
        }
     
        GROUP by ?mRID ?name ?ratedS ?ratedU ?r ?connectionKind ?phaseAngleClock ?endNumber
        ?shortTermS ?emergencyS ?insulationU ?GroundedEndShortCircuitTests ?EnergisedEndShortCircuitTests
        ?EnergisedEndNoLoadTests ?FromMeshImpedance ?ToMeshImpedance ?CoreAdmittance ?TransformerTankInfo
        ORDER by ?name
          """
    return query_message