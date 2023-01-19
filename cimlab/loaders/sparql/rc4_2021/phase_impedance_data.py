from typing import List
from dataclasses import dataclass, field

def get_all_attributes(feeder_id: str, mrid_list: List[str]):
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?PhaseImpedance ?row ?column ?r ?x ?b 

        WHERE {          
          ?eq r:type cim:PhaseImpedanceData.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
        ?eq cim:PhaseImpedanceData.PhaseImpedance ?pli.
        ?line cim:ACLineSegment.PerLengthImpedance ?pli.
        ?pli cim:IdentifiedObject.mRID ?PhaseImpedance.
        ?line cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.
        #?eq c:IdentifiedObject.mRID ?mRID. #mRID MISSING FROM XML
        bind(strafter(str(?eq),"sparql#") as ?mRID).
        #?eq cim:IdentifiedObject.name ?name.

        OPTIONAL {?eq cim:PhaseImpedanceData.row ?row.}
        OPTIONAL {?eq cim:PhaseImpedanceData.column ?column.}
        OPTIONAL {?eq cim:PhaseImpedanceData.r ?r.}
        OPTIONAL {?eq cim:PhaseImpedanceData.x ?x.}
        OPTIONAL {?eq cim:PhaseImpedanceData.b ?b.}

        }
        GROUP by ?mRID ?name ?PhaseImpedance ?row ?column ?r ?x ?b 
        ORDER by  ?name
        """
    return query_message