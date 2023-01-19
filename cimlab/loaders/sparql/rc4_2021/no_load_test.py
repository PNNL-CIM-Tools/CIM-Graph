from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?energisedEndVoltage ?excitingCurrent ?excitingCurrentZero ?loss
        ?lossZero ?basePower ?temperature ?EnergisedEnd
        WHERE {          
          ?eq r:type cim:NoLoadTest.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """          }
        #get feeder id from TransformerTank
        ?eq cim:NoLoadTest.EnergisedEnd ?end.
        ?end cim:IdentifiedObject.mRID ?EnergisedEnd.
        
        ?end cim:TransformerEndInfo.TransformerTankInfo ?tankinfo.
        ?asset cim:Asset.AssetInfo ?tankinfo.
        ?asset cim:Asset.PowerSystemResources ?tank.
        ?tank cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:NoLoadTest.energisedEndVoltage ?energisedEndVoltage.}
        OPTIONAL {?eq cim:NoLoadTest.excitingCurrent ?excitingCurrent.}
        OPTIONAL {?eq cim:NoLoadTest.excitingCurrentZero ?excitingCurrentZero.}
        OPTIONAL {?eq cim:NoLoadTest.loss ?loss.}
        OPTIONAL {?eq cim:NoLoadTest.lossZero ?lossZero.}
        OPTIONAL {?eq cim:TransformerTest.basePower ?basePower.}
        OPTIONAL {?eq cim:TransformerTest.temperature ?temperature.}
        
        }
     
        GROUP by ?mRID ?name ?energisedEndVoltage ?excitingCurrent ?excitingCurrentZero ?loss
        ?lossZero ?basePower ?temperature ?EnergisedEnd
        ORDER by ?name
          """
    return query_message