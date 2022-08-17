from __future__ import annotations

import os, json, time, sys
from typing import List
from dataclasses import dataclass, field
from gridappsd import GridAPPSD, topics as t
from gridappsd_cim import *


def initialize_objects(feeder_id, mrid_list):
    
    
    os.environ['GRIDAPPSD_APPLICATION_ID'] = 'gridappsd-cim-profile'
    os.environ['GRIDAPPSD_APPLICATION_STATUS'] = 'STARTED'
    os.environ['GRIDAPPSD_USER'] = 'app_user'
    os.environ['GRIDAPPSD_PASSWORD'] = '1234App'
    gapps = GridAPPSD()
    assert gapps.connected

    log = gapps.get_logger()

    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX c:  <http://iec.ch/TC57/CIM100#>
        SELECT ?eqid ?eqname ?class
        {
          VALUES ?fdrid {"%s"}
          VALUES ?eqid {"""%feeder_id
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
    
    query_message += """               } 
          ?fdr c:IdentifiedObject.mRID ?fdrid.
          ?eq c:IdentifiedObject.name ?eqname.
          ?eq c:IdentifiedObject.mRID ?eqid.
          ?eq a ?classraw.
          bind(strafter(str(?classraw),"CIM100#") as ?class)
        }
        GROUP BY  ?eqid ?eqname ?class
        ORDER by  ?fdrid
        """
    print(query_message)
    results = gapps.query_data(query = query_message, timeout = 60)
    output = results['data']['results']['bindings']

    #if self.sparql is None:
    #    self.sparql = SPARQLWrapper(self.url)
    #    self.sparql.setReturnFormat(JSON)
    #self.sparql.setQuery(sparql)

    #ret = self.sparql.query().convert()
    objects = []
    for result in output:
        cls = result['class']['value']
        mrid = result['eqid']['value']
        try:
            objects.append(eval(f"{cls}(mRID='{mrid}')"))
            print(cls)
        except:
            print('warning: object class missing:', cls)
    return objects