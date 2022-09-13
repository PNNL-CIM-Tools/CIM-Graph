from __future__ import annotations

from cim.data_profile import Feeder


def format_terminal_all_attributes_by_feeder(feeder_id: str | Feeder) -> str:
    query_message = """
        # list all the terminals
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX c:  <http://iec.ch/TC57/CIM100#>
        SELECT ?tid ?tname ?fdrid ?cnid ?tpid ?coneqid ?txfid ?regcntl ?seq
        {
          VALUES ?fdrid {%s} 
          ?fdr c:IdentifiedObject.mRID ?fdrid.

          ?t c:Terminal.ConnectivityNode ?cn. 
          bind(strafter(str(?cn),"#") as ?cnid).

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
