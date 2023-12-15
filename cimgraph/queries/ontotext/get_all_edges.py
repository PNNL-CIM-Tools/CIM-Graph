from __future__ import annotations

from dataclasses import dataclass, field

from cimgraph.data_profile.known_problem_classes import ClassesWithoutMRID


def get_all_edges_ontotext(cim_class: type, mrid_list: list[str], namespace: str,
                           iec61970_301: int) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        graph (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    class_name = cim_class.__name__
    classes_without_mrid = ClassesWithoutMRID()

    if int(iec61970_301) > 7:
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

    if class_name not in classes_without_mrid.classes:
        query_message += """
        VALUES ?mRID {"""
        # add all equipment mRID
        for mrid in mrid_list:
            query_message += ' "%s" \n' % mrid
        query_message += """               }
        ?eq cim:IdentifiedObject.mRID ?mRID."""
    else:
        query_message += """
        VALUES ?eq {"""
        # add all equipment mRID
        for mrid in mrid_list:
            query_message += """ <%s%s> \n""" % (split, mrid)
        query_message += """               }
        {bind(strafter(str(?eq),"%s") as ?mRID)}.""" % split

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
                  OPTIONAL {?val cim:IdentifiedObject.mRID ?edge_id.}
                  bind(exists{?val cim:IdentifiedObject.mRID ?edge_id} as ?mRID_exists)
                 {bind(if(?mRID_exists, ?edge_id, ?uri) as ?edge_mRID)}.

                  bind(concat("{\\"@id\\":\\"", ?edge_mRID,"\\",\\"@type\\":\\"", ?edge_class, "\\"}") as ?edge)}
        }

        ORDER by  ?mRID ?attribute
        """ % (split, namespace, split)
    return query_message
