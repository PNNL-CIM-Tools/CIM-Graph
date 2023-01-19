from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?energisedEndStep ?groundedEndStep ?leakageImpedance ?leakageImpedanceZero ?loss
        ?lossZero ?basePower ?temperature ?EnergisedEnd
        (group_concat(distinct ?GroundedEnd; separator=";") as ?GroundedEnds)
        WHERE {          
          ?eq r:type cim:ShortCircuitTest.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """          }
        #get feeder id from TransformerTank
        ?eq cim:ShortCircuitTest.GroundedEnds ?gends.
        ?gends cim:IdentifiedObject.mRID ?GroundedEnd.
        ?eq cim:ShortCircuitTest.EnergisedEnd ?eend.
        ?eend cim:IdentifiedObject.mRID ?EnergisedEnd.
        
        { {?gends cim:TransformerEndInfo.TransformerTankInfo ?tankinfo. } UNION 
         {?eend cim:TransformerEndInfo.TransformerTankInfo ?tankinfo. } }
        ?asset cim:Asset.AssetInfo ?tankinfo.
        ?asset cim:Asset.PowerSystemResources ?tank.
        ?tank cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:ShortCircuitTest.energisedEndStep ?energisedEndStep.}
        OPTIONAL {?eq cim:ShortCircuitTest.groundedEndStep ?groundedEndStep.}
        OPTIONAL {?eq cim:ShortCircuitTest.leakageImpedance ?leakageImpedance.}
        OPTIONAL {?eq cim:ShortCircuitTest.leakageImpedanceZero ?leakageImpedanceZero.}
        OPTIONAL {?eq cim:ShortCircuitTest.loss ?loss.}
        OPTIONAL {?eq cim:ShortCircuitTest.lossZero ?lossZero.}
        OPTIONAL {?eq cim:TransformerTest.basePower ?basePower.}
        OPTIONAL {?eq cim:TransformerTest.temperature ?temperature.}
        
        }
     
        GROUP by ?mRID ?name ?energisedEndStep ?groundedEndStep ?leakageImpedance ?leakageImpedanceZero ?loss
        ?lossZero ?basePower ?temperature ?EnergisedEnd
        ORDER by ?name
          """
    return query_message