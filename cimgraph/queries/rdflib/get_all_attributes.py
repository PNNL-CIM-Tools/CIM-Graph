from __future__ import annotations

from uuid import UUID

from cimgraph.data_profile.known_problem_classes import ClassesWithoutMRID
from cimgraph.databases import get_cim_profile, get_iec61970_301, get_namespace, get_url


def get_all_attributes_sparql(graph:dict[type, dict[UUID, object]], cim_class: str, uuid_list: list[UUID]) -> str:
    """
    Generates SPARQL query string for a given catalog of objects and feeder id
    Args:
        feeder_mrid (str | Feeder object): The mRID of the feeder or feeder object
        graph (dict[type, dict[str, object]]): The typed catalog of CIM objects organized by
            class type and object mRID
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    namespace = get_namespace()
    iec61970_301 = get_iec61970_301()
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
        {?eq (cim:|!cim:) ?val.
         ?eq ?attr ?val.}
        UNION
        {?val (cim:|!cim:) ?eq.
         ?val ?attr ?eq.}

        # {bind(strafter(str(?attr),"#") as ?attribute).}
        # {bind(strafter(str(?val),"%s") as ?uri).}
        # {bind(if(?uri = "", ?val, ?uri) as ?value).}
        }


        ORDER by  ?identifier ?attribute
        """ % split
    return query_message
