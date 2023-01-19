from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?PowerTransformer ?ratedS ?ratedU ?r ?connectionKind ?phaseAngleClock ?endNumber
        ?grounded ?rground ?xground ?Terminal ?BaseVoltage ?PhaseTapChanger ?RatioTapChanger
        ?FromMeshImpedance ?ToMeshImpedance ?CoreAdmittance
        WHERE {          
          ?eq r:type cim:PowerTransformerEnd.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """          }
        #get feeder id from PowerTransformer
        ?eq cim:PowerTransformerEnd.PowerTransformer ?pxf.
        ?pxf cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        ?pxf cim:IdentifiedObject.mRID ?PowerTransformer.

        OPTIONAL {?eq cim:PowerTransformerEnd.ratedS ?ratedS.}
        OPTIONAL {?eq cim:PowerTransformerEnd.ratedU ?ratedU.}
        OPTIONAL {?eq cim:PowerTransformerEnd.r ?r.}
        OPTIONAL {?eq cim:PowerTransformerEnd.connectionKind ?conn.
                  bind(strafter(str(?conn),"WindingConnection.") as ?connectionKind).}
        OPTIONAL {?eq cim:PowerTransformerEnd.phaseAngleClock ?phaseAngleClock.}
  
        OPTIONAL {?eq cim:TransformerEnd.endNumber ?endNumber.}
        OPTIONAL {?eq cim:TransformerEnd.grounded ?grounded.}
        OPTIONAL {?eq cim:TransformerEnd.rground ?rground.}
        OPTIONAL {?eq cim:TransformerEnd.xground ?xground.}
        OPTIONAL {?eq cim:TransformerEnd.Terminal ?t.
                  ?t cim:IdentifiedObject.mRID ?Terminal.}
        OPTIONAL {?eq cim:TransformerEnd.BaseVoltage ?bv.
                  ?bv cim:IdentifiedObject.mRID ?BaseVoltage.}
        
        OPTIONAL {?ptc cim:PhaseTapChanger.TransformerEnd ?eq.
                  ?ptc cim:IdentifiedObject.mRID ?PhaseTapChanger.}
        
        OPTIONAL {?rtc cim:RatioTapChanger.TransformerEnd ?eq.
                  ?rtc cim:IdentifiedObject.mRID ?RatioTapChanger.}
                  
        OPTIONAL {?tac cim:TransformerCoreAdmittace.TransformerEnd ?eq.
                  ?tac cim:IdentifiedObject.mRID ?CoreAdmittance.}
          
        OPTIONAL {?frmesh cim:TransformerMeshImpedance.FromTransformerEnd ?eq.
                  ?frmesh cim:IdentifiedObject.mRID ?FromMeshImpedance.}
          
        OPTIONAL {?frmesh cim:TransformerMeshImpedance.ToTransformerEnd ?eq.
                  ?frmesh cim:IdentifiedObject.mRID ?ToMeshImpedance.}
        }
        GROUP by ?mRID ?name ?PowerTransformer ?ratedS ?ratedU ?r ?connectionKind ?phaseAngleClock ?endNumber
        ?grounded ?rground ?xground ?Terminal ?BaseVoltage ?PhaseTapChanger ?RatioTapChanger
        ?FromMeshImpedance ?ToMeshImpedance ?CoreAdmittance
        ORDER by ?name
          """
    return query_message