from __future__ import annotations

from uuid import UUID

from cimgraph.databases import ConnectionParameters


def get_object_sparql(mrid: str, connection_params: ConnectionParameters) -> str:
    """
    Generates SPARQL query string to find the type of an object from its uri
    Args:
        mrid (str): The mRID or uri of the  object
        connection_params (ConnectionParameters): Database connection parameters
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    if int(connection_params.iec61970_301) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{connection_params.url}#'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % connection_params.namespace

    query_message += """
        SELECT DISTINCT ?identifier ?obj_class
        WHERE {
          """

    query_message += '''
    VALUES ?identifier {"%s"}''' %mrid
    # add all equipment mRID

    query_message += f'''
        bind(iri(concat("{split}", ?identifier)) as ?eq)'''

    query_message += """

        ?eq a ?classraw.
        bind(strafter(str(?classraw),"%s") as ?obj_class)
        }
        ORDER by  ?identifier
        """ % (connection_params.namespace)
    return query_message
