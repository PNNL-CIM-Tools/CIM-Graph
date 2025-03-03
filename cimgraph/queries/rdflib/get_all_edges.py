from __future__ import annotations

from cimgraph.data_profile.known_problem_classes import ClassesWithoutMRID


def get_all_edges_sparql(cim_class: str, mrid_list: list[str], namespace: str,
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
        split = 'rdf:id:'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % namespace

    query_message += """
        SELECT DISTINCT ?mRID ?attr ?val ?edge_class ?edge_mRID ?eq
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
        {?eq (cim:|!cim:) ?val.
         ?eq ?attr ?val.}
        UNION
        {?val (cim:|!cim:) ?eq.
         ?val ?attr ?eq.}

        # {bind(strafter(str(?attr),"#") as ?attribute).}
        # {bind(strafter(str(?val),"%s") as ?uri).}
        # {bind(if(?uri = "", ?val, ?uri) as ?value).}

        OPTIONAL {?val a ?classraw.
                  bind(strafter(str(?classraw),"%s") as ?edge_class).}
        OPTIONAL {?val cim:IdentifiedObject.mRID ?edge_mRID.
                #   {bind(if(EXISTS(?edge_id), ?val, ?edge_id)) as ?edge_mRID)}.
                #   bind(concat("{\\"@id\\":\\"", ?edge_mRID,"\\",\\"@type\\":\\"", ?edge_class, "\\"}") as ?edge)
                  }
        }

        ORDER by  ?mRID ?attribute
        """ % (split, namespace)
    return query_message
