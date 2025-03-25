from __future__ import annotations

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_triple_sparql(obj:object, attribute:str) -> str:
    """
    Generates SPARQL query string to find predicate for RDF triple
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    mrid = obj.uri()

    if int(get_iec61970_301()) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % get_namespace()

    query_message += """
        SELECT DISTINCT ?identifier ?attribute ?value ?edge
        WHERE {
          """

    query_message += '''
    VALUES ?identifier {"%s"}''' %mrid
    # add all equipment mRID

    query_message += f'''
        bind(iri(concat("{split}", ?identifier)) as ?eq)'''

    query_message += """

        ?eq cim:%s ?val.

        {bind("%s" as ?attribute)}
        {bind(strafter(str(?val),"%s") as ?uri)}
        {bind(if(?uri = "", ?val, ?uri) as ?value)}

        OPTIONAL {?val a ?classraw.
                  bind(strafter(str(?classraw),"%s") as ?edge_class)
                  {bind(strafter(str(?val),"%s") as ?uri)}

                  bind(concat("{\\"@id\\":\\"", ?uri,"\\",\\"@type\\":\\"", ?edge_class, "\\"}") as ?edge)}
        }

        ORDER by  ?identifier ?attribute
        """ % (attribute, attribute, split, get_namespace(), split)
    return query_message
