from __future__ import annotations

from cimgraph.databases import get_iec61970_301, get_namespace, get_url


def get_all_nodes_sparql(container: object) -> str:
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    container_mRID = container.mRID
    namespace = get_namespace()

    try:
        container_uri = container.uri()
    except:
        container_uri = container.mRID

    if get_iec61970_301() > 7:
        split = 'urn:uuid:'
    else:
        split = 'rdf:id:'

    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % namespace
    query_message += """
        SELECT  ?ConnectivityNode ?Terminal ?Equipment
        WHERE {
          ?c r:type cim:%s.""" % container_class
    query_message += """
        VALUES ?identifier {"%s"}
        bind(iri(concat("%s", ?identifier)) as ?c).
        """ % (container_uri, split)

    # add all attributes
    query_message += """
                {
        ?node cim:ConnectivityNode.ConnectivityNodeContainer ?c.
        ?t cim:Terminal.ConnectivityNode ?node.
        ?t cim:Terminal.ConductingEquipment ?eq.
        ?eq a ?eq_cls.

        bind(strafter(str(?node),"%s") as ?ConnectivityNode).
        bind(strafter(str(?t),"%s") as ?Terminal).
        bind(strafter(str(?eq),"%s") as ?eq_id).

        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"%s"), "\\"}") as ?Equipment)
        }
        """ % (split, split, split, get_namespace())
    # get Equipment objects associated with Container
    query_message += """
       UNION
        {
        {?eq cim:Equipment.EquipmentContainer ?c.}
        UNION
        {?eq cim:Equipment.AdditionalEquipmentContainer ?c.}
        OPTIONAL {
            ?t cim:Terminal.ConductingEquipment ?eq.
            ?t cim:Terminal.ConnectivityNode ?node.
            }
        ?eq a ?eq_cls.

        bind(strafter(str(?node),"%s") as ?ConnectivityNode).
        bind(strafter(str(?t),"%s") as ?Terminal).
        bind(strafter(str(?eq),"%s") as ?eq_id).

        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"%s"), "\\"}") as ?Equipment)
        }
        }
        ORDER by ?ConnectivityNode
        """ % (split, split, split, get_namespace())

    return query_message
