from __future__ import annotations

from uuid import UUID

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_all_edges_ontotext(graph:dict[type, dict[UUID, object]], cim_class: type, uuid_list: list[UUID]) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        graph (dict[type, dict[UUID, object]]): The graph of CIM objects organized by
            class type and UUID object identifier
        cim_class (type): The CIM class type to query
        uuid_list (list[UUID]): List of UUIDs to query for

    Returns:
        query_message: query string that can be used in GraphDB connection or STOMP client
    """
    class_name = cim_class.__name__
    namespace = get_namespace()

    if int(get_iec61970_301()) > 7:
        split = 'urn:uuid:'
    else:
        split = '#'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % namespace

    query_message += """
        SELECT DISTINCT ?mRID ?attribute ?value ?edge
        WHERE {
          ?eq r:type cim:%s.""" % class_name
    # query_message += """
    #     VALUES ?fdrid {"%s"}
    #     {?fdr cim:IdentifiedObject.mRID ?fdrid.
    #     {?eq (cim:|!cim:)?  [ cim:Equipment.EquipmentContainer ?fdr]}
    #      UNION
    #      {[cim:Equipment.EquipmentContainer ?fdr] (cim:|!cim:)?  ?eq}}.
    #       """ %feeder_mrid

    query_message += """
    VALUES ?identifier {"""
    # add all equipment mRID
    for uuid in uuid_list:
        query_message += ' "%s" \n' % graph[cim_class][uuid].uri()
    query_message += '               }'
    query_message += f'''
        bind(iri(concat("{split}", ?identifier)) as ?eq)'''

    # add all attributes
    query_message += """
        SERVICE <http://www.ontotext.com/path#search> {
        <urn:path> path:findPath path:allPaths ;
                   path:sourceNode ?eq ;
                   path:destinationNode ?dst ;
                   path:minPathLength 1 ;
                   path:maxPathLength 1 ;
                   path:endNode ?value ;
                   path:propertyBinding ?attr ;
                   path:bidirectional true ;
                   path:pathIndex ?path .
        }

        {bind(strafter(str(?attr),"#") as ?attribute)}
        {bind(strafter(str(?val),"%s") as ?uri)}
        {bind(if(?uri = "", ?val, ?uri) as ?value)}

        OPTIONAL {?val a ?classraw.
                  bind(strafter(str(?classraw),"%s") as ?edge_class)
                  {bind(strafter(str(?val),"%s") as ?uri)}

                  bind(concat("{\\"@id\\":\\"", ?uri,"\\",\\"@type\\":\\"", ?edge_class, "\\"}") as ?edge)}
        }

        ORDER by  ?identifier ?attribute
        """ % (split, namespace, split)
    return query_message
