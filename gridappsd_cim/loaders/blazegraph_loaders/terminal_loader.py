import os, json, time
from __future__ import annotations
from typing import List

from gridappsd import GridAPPSD, topics as t
from gridappsd_cim import Terminal, ConnectivityNode

class BlazegraphConnection(ConnectionInterface):
 # insert blazegraph url for direct access

 
class GridappsdConnection(ConnectionInterface):

    def __init__(self):
        os.environ['GRIDAPPSD_APPLICATION_ID'] = 'gridappsd-cim-profile'
        os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
        os.environ['GRIDAPPSD_USER'] = 'app_user'
        os.environ['GRIDAPPSD_PASSWORD'] = '1234App'
        gapps = GridAPPSD()
        assert gapps.connected
        self.gapps = gapps
        self.log = self.gapps.get_logger()
        
        self.log.info('Terminal loader started')
        
    def execute(string):
        pass
    def next_result():
        pass
    def num_ressults():
        pass
        

class TerminalLoader:
    def __init__(self, conn: ConnectionInteface):
        self._con = conn
        _log.debug(f"Conn is {type(self._con)}")

        
    def load_terminal_all_attributes_by_feeder(feeder_id: str | Feeder) -> List[Terminal]:
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
        """%feeder_id
        
        results = gapps.query_data(query = QueryMeasurementMessage, timeout = 60)
        output = results['data']['results']['bindings']
        
        
        
    def load_terminal_by_connectivity_node(conducting: str | ConductingEquipment) -> List[Terminal]:
        query_message = """
        
        """