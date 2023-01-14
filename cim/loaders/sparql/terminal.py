from __future__ import annotations

from cim.data_profile import Feeder


def get_all_attributes(feeder_id: str | Feeder) -> str:
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name 
        WHERE {          
          ?eq r:type cim:Terminal.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_id
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    # add all attributes
    query_message += """               } 
          ?eq c:Terminal.ConnectivityNode ?node. 
          ?node IdentifiedObject.mRID ?ConnectivityNode

          ?t c:Terminal.ConductingEquipment ?coneq.
          bind(strafter(str(?coneq),"#") as ?coneqid).

          OPTIONAL {?t c:Terminal.TransformerEnd ?txf.
          bind(strafter(str(?txf),"#") as ?txfid).} 

          OPTIONAL {?t c:Terminal.RegulatingControl ?regcntl}


          ?t c:IdentifiedObject.name ?tname.
          bind(strafter(str(?t),"#") as ?tid).

          ?cn c:ConnectivityNode.TopologicalNode ?tp.
          bind(strafter(str(?tp),"#") as ?tpid).

          ?t c:ACDCTerminal.sequenceNumber ?seq.


        }
        GROUP BY  ?tid ?tname ?fdrid ?cnid ?tpid ?coneqid ?txfid ?regcntl ?seq
        ORDER by  ?fdrid 
    """ % feeder_id

    return query_message
