from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?Location ?vectorGroup ?aggregate ?inService
        (group_concat(distinct ?PowerTransformerEnd; separator=";") as ?PowerTransformerEnd) 
        (group_concat(distinct ?TransformerTank; separator=';') as ?TransformerTanks)
        (group_concat(distinct ?Terminal; separator=';') as ?Terminals)
        (group_concat(distinct ?Measurement; separator=";") as ?Measurements) 
        (group_concat(distinct ?Asset; separator=";") as ?Assets) 
        
        WHERE {          
          ?eq r:type cim:PowerTransformer.
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

        OPTIONAL {?eq cim:PowerSystemResource.Location ?loc.
        ?loc cim:IdentifiedObject.mRID ?Location.}

        OPTIONAL {?eq cim:PowerTransformer.vectorGroup ?vectorGroup.}
        OPTIONAL {?eq cim:Equipment.aggregate ?aggregate.}
        OPTIONAL {?eq cim:Equipment.inService ?inService.}
        #OPTIONAL {?eq cim:Equipment.networkAnalysisEnable ?networkAnalysisEnabled.}
        #OPTIONAL {?eq cim:Equipment.normallyInService ?normallyInService.}
        
        OPTIONAL {?asset cim:Asset.PowerSystemResources ?eq.
                  ?asset cim:IdentifiedObject.mRID ?Asset.}

        OPTIONAL {?tank cim:TransformerTank.PowerTransformer ?eq.
                  ?tank cim:IdentifiedObject.mRID ?TransformerTank.}

        OPTIONAL {?end cim:PowerTransformerEnd.PowerTransformer ?eq.
                  ?end cim:IdentifiedObject.mRID ?PowerTransformerEnd.}
                  
        OPTIONAL {?end cim:TransformerEnd.Terminal ?t.
                  ?t cim:IdentifiedObject.mRID ?Terminal.}
        OPTIONAL {?meas cim:Measurement.PowerSystemResource ?eq.
          ?meas cim:IdentifiedObject.mRID ?Measurement}
                  
        }
        GROUP by ?mRID ?name ?Location ?vectorGroup ?aggregate ?inService
        ORDER by ?name
        """
    return query_message