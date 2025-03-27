from __future__ import annotations

from uuid import UUID

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_object_sparql(mRID: str) -> str:
    """
    Generates SPARQL query string to find the type of an object from its uri
    Args:
        mRID (str): The mRID or uri of the  object
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    if get_iec61970_301() > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % get_namespace()

    query_message += """
        SELECT DISTINCT ?identifier ?obj_class
        WHERE {
          """

    query_message += '''
    VALUES ?identifier {"%s"}''' %mRID
    # add all equipment mRID

    query_message += f'''
        bind(iri(concat("{split}", ?identifier)) as ?eq)'''

    query_message += """

        ?eq a ?classraw.
        bind(strafter(str(?classraw),"%s") as ?obj_class)
        }
        ORDER by  ?identifier
        """ % (get_namespace())
    return query_message
