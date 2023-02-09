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

    mrid_list = list(typed_catalog[cim.TransformerMeshImpedance].keys())
    asset_list = list(typed_catalog[cim.PowerTransformer].keys())
    
    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <http://iec.ch/TC57/CIM100#>
        SELECT ?mRID ?name ?r ?r0 ?x ?x0 ?FromTransformerEnd ?ToTransformerEnd 
        # ?FromTransformerEndInfo ?ToPowerTransformerEndInfos
        WHERE {          
          ?eq r:type cim:TransformerMeshImpedance.
          VALUES ?fdrid {"%s"}
          VALUES ?mRID {"""%feeder_mrid
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += ' "%s" \n'%mrid
        
    # add all assets
    query_message += """               }
        VALUES ?PowerTransformer {"""
    for asset_mrid in asset_list:
        query_message += ' "%s" \n' % asset_mrid
        
    # add all attributes
    query_message += """          }
        #get feeder id from PowerTransformer
        ?eq cim:TransformerMeshImpedance.FromTransformerEnd ?end1.
        ?eq cim:TransformerMeshImpedance.ToTransformerEnd ?end2.
        ?end1 cim:PowerTransformerEnd.PowerTransformer ?pxf.
        ?pxf cim:Equipment.EquipmentContainer ?fdr.
        ?fdr cim:IdentifiedObject.mRID ?fdrid.

        ?eq cim:IdentifiedObject.mRID ?mRID.
        ?eq cim:IdentifiedObject.name ?name.
        
        ?end1 cim:IdentifiedObject.mRID ?FromTransformerEnd.
        ?end2 cim:IdentifiedObject.mRID ?ToTransformerEnd.
        ?pxf cim:IdentifiedObject.mRID ?PowerTransformer.


        OPTIONAL {?eq cim:TransformerMeshImpedance.r ?r.}
        OPTIONAL {?eq cim:TransformerMeshImpedance.r0 ?r0.}
        OPTIONAL {?eq cim:TransformerMeshImpedance.x ?x.}
        OPTIONAL {?eq cim:TransformerMeshImpedance.x0 ?x0.}
        
       
        }
        GROUP by ?mRID ?name ?r ?r0 ?x ?x0 ?FromTransformerEnd ?ToTransformerEnd
        ORDER by ?name
          """
    return query_message