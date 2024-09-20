from __future__ import annotations

from uuid import UUID

from cimgraph.databases import ConnectionParameters


def get_object_sparql(mrid: str, connection_params: ConnectionParameters) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        graph (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by
            class type and object mRID
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
