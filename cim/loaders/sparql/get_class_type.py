def get_class_type_sparql(feeder_mrid, mrid_list, add_prefix=True):
    prefix = """
            PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX c:  <http://iec.ch/TC57/CIM100#>
            """
    query_message = """
                SELECT ?mRID ?name ?class
                {
                  VALUES ?fdrid {"%s"}
                  VALUES ?mRID {""" % feeder_mrid
        
    if add_prefix:
        query_message = prefix+query_message
        
    for mrid in mrid_list:
        query_message += ' "%s" \n' % mrid

    query_message += """               } 
                  ?fdr c:IdentifiedObject.mRID ?fdrid.
                  ?eq c:IdentifiedObject.name ?name.
                  ?eq c:IdentifiedObject.mRID ?mRID.
                  ?eq a ?classraw.
                  bind(strafter(str(?classraw),"CIM100#") as ?class)
                }
                GROUP BY  ?mRID ?name ?class
                ORDER by  ?fdrid
                """
    return query_message