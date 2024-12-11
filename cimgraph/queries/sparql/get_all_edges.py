from __future__ import annotations

from uuid import UUID

from cimgraph.databases import ConnectionParameters


def get_all_edges_sparql(graph:dict[type, dict[UUID, object]], cim_class: type, uuid_list: list[UUID],
                         connection_params: ConnectionParameters) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        graph (dict[type, dict[UUID, object]]): The graph of CIM objects organized by
            class type and UUID object identifier
        cim_class (type): The CIM class type to query
        uuid_list (list[UUID]): List of UUIDs to query for
        connection_params (ConnectionParameters): Database connection parameters

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    class_name = cim_class.__name__

    if int(connection_params.iec61970_301) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{connection_params.url}#'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % connection_params.namespace

    query_message += """
        SELECT DISTINCT ?identifier ?attribute ?value ?edge
        WHERE {
          """

    query_message += """
    VALUES ?identifier {"""
    # add all equipment mRID
    for uuid in uuid_list:
        query_message += ' "%s" \n' % graph[cim_class][uuid].uri()
    query_message += '               }'
    query_message += f'''
        bind(iri(concat("{split}", ?identifier)) as ?eq)'''

    query_message += """

        ?eq r:type cim:%s.

        {?eq (cim:|!cim:) ?val.
         ?eq ?attr ?val.}
        UNION
        {?val (cim:|!cim:) ?eq.
         ?val ?attr ?eq.}

        {bind(strafter(str(?attr),"#") as ?attribute)}
        {bind(strafter(str(?val),"%s") as ?uri)}
        {bind(if(?uri = "", ?val, ?uri) as ?value)}

        OPTIONAL {?val a ?classraw.
                  bind(strafter(str(?classraw),"%s") as ?edge_class)
                  {bind(strafter(str(?val),"%s") as ?uri)}

                  bind(concat("{\\"@id\\":\\"", ?uri,"\\",\\"@type\\":\\"", ?edge_class, "\\"}") as ?edge)}
        }

        ORDER by  ?identifier ?attribute
        """ % (class_name, split, connection_params.namespace, split)
    return query_message
