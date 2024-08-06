from __future__ import annotations
from cimgraph.databases import ConnectionInterface


def get_all_nodes_from_container(container: object, connection_params: ConnectionInterface) -> str:
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    container_class = container.__class__.__name__
    try:
        container_uri = container.uri()
    except:
        container_uri = container.mRID

    if int(connection_params.iec61970_301) > 7:
        split = 'urn:uuid:'
    else:
        split = f'{connection_params.url}#'


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % connection_params.namespace
    query_message += """
        SELECT DISTINCT ?ConnectivityNode ?Terminal ?Equipment
        WHERE {
          """ #
    query_message += """
        VALUES ?identifier {"%s"}
        bind(iri(concat("%s", ?identifier)) as ?c).
        """ % (container_uri, split)

    # get ConnectivityNode objects associated with Container
    query_message += '''     {
        
        ?node cim:ConnectivityNode.ConnectivityNodeContainer ?c.
        ?t cim:Terminal.ConnectivityNode ?node.
        ?t cim:Terminal.ConductingEquipment ?eq.
        ?eq a ?eq_cls.

        bind(strafter(str(?node),"%s") as ?ConnectivityNode).
        bind(strafter(str(?t),"%s") as ?Terminal).
        bind(strafter(str(?eq),"%s") as ?eq_id).

        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"%s"), "\\"}") as ?Equipment)
        }
        ''' % (split, split, split, connection_params.namespace)
    # get Equipment objects associated with Container
    query_message += '''
        UNION
        {
        ?eq cim:Equipment.EquipmentContainer ?c.
        ?t cim:Terminal.ConductingEquipment ?eq.
        ?t cim:Terminal.ConnectivityNode ?node.
        ?eq a ?eq_cls.
          
        bind(strafter(str(?node),"%s") as ?ConnectivityNode).
        bind(strafter(str(?t),"%s") as ?Terminal).
        bind(strafter(str(?eq),"%s") as ?eq_id).

        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"%s"), "\\"}") as ?Equipment)
        }
        }
        ORDER by ?ConnectivityNode
        ''' % (split, split, split, connection_params.namespace)

    return query_message


def get_all_nodes_from_list(mrid_list: list[str], namespace: str) -> str:
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:

    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    query_message = f"""
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <{namespace}>"""
    query_message += """
        SELECT DISTINCT ?ConnectivityNode ?Terminal ?Equipment
        WHERE {
          ?c r:type cim:ConnectivityNode"""
    query_message += """
        VALUES ?ConnectivityNode {"""
    # add all equipment mRID
    for mrid in mrid_list:
        query_message += f' "{mrid}" \n'
    query_message += '               }'

    # add all attributes
    query_message += """
                {
        ?node cim:IdentifiedObject.mRID ?ConnectivityNode.

        ?t cim:Terminal.ConnectivityNode ?node.
        ?t cim:IdentifiedObject.mRID ?Terminal.
        ?t cim:Terminal.ConductingEquipment ?eq.

        ?eq cim:IdentifiedObject.mRID ?eq_id.
        ?eq a ?eq_cls.
        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"%s"), "\\"}") as ?Equipment)
        }
        }
        """ % namespace

    return query_message
