from __future__ import annotations

from uuid import UUID

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_all_edges_sparql(graph:dict[type, dict[UUID, object]], cim_class: type, uuid_list: list[UUID]) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        graph (dict[type, dict[UUID, object]]): The graph of CIM objects organized by
            class type and UUID object identifier
        cim_class (type): The CIM class type to query
        uuid_list (list[UUID]): List of UUIDs to query for
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    class_name = cim_class.__name__

    if get_iec61970_301() > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % get_namespace()

    query_message += """
        SELECT DISTINCT ?identifier ?attr ?val ?edge_class
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


        OPTIONAL {?val a ?classraw.
                  bind(strafter(str(?classraw),"%s") as ?edge_class)
                  {bind(strafter(str(?val),"%s") as ?uri)}

                #   bind(concat("{\\"@id\\":\\"", ?uri,"\\",\\"@type\\":\\"", ?edge_class, "\\"}") as ?edge)
        }
        }
        ORDER by  ?identifier ?attribute
        """ % (class_name,  get_namespace(), split)
    return query_message
