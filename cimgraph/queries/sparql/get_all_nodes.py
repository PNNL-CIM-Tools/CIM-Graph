from __future__ import annotations

import logging

import cimgraph.data_profile.cim17v40 as cim
from cimgraph.databases import get_iec61970_301, get_namespace, get_url

_log = logging.getLogger(__name__)



def get_all_nodes_from_container(container: cim.EquipmentContainer) -> str:
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:
        container: an object instance of cim:ConnectivityNodeContainer or child classes (e.g. cim:Feeder)
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    try:
        container_uri = container.uri()
    except:
        container_uri = container.mRID

    if get_iec61970_301() > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % get_namespace()
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
        ''' % (split, split, split, get_namespace())
    # get Equipment objects associated with Container
    query_message += '''
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
        ''' % (split, split, split, get_namespace())

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


def get_all_nodes_from_area(area: object) -> str:
    """
    Generates SPARQL query string for all nodes, terminals, and conducting equipment
    Args:
        area: object of type SubSchedulingArea
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """

    area_class = area.__class__.__name__
    try:
        container_uri = area.uri()
    except:
        container_uri = area.mRID

    if get_iec61970_301() > 7:
        split = 'urn:uuid:'
    else:
        split = f'{get_url()}#'


    query_message = """
        PREFIX r:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX cim:  <%s>""" % get_namespace()
    query_message += """
        SELECT DISTINCT ?ConnectivityNode ?Terminal ?Equipment ?Measurement
        WHERE {
          """ #
    query_message += """
        VALUES ?identifier {"%s"}
        bind(iri(concat("%s", ?identifier)) as ?c).
        """ % (container_uri, split)


    # get Equipment objects associated with Container
    query_message += '''

        ?eq cim:Equipment.SubSchedulingArea ?c.
        ?eq a ?eq_cls.

        ?t cim:Terminal.ConductingEquipment ?eq.
        ?t cim:Terminal.ConnectivityNode ?node.

        OPTIONAL {?meas cim:Measurement.Terminal ?t.
        ?meas a ?m_cls.
        bind(strafter(str(?meas),"%s") as ?meas_id).
        }

        bind(strafter(str(?node),"%s") as ?ConnectivityNode).
        bind(strafter(str(?t),"%s") as ?Terminal).

        bind(strafter(str(?eq),"%s") as ?eq_id).

        bind(concat("{\\"@id\\":\\"", str(?eq_id),"\\",\\"@type\\":\\"",strafter(str(?eq_cls),"%s"), "\\"}") as ?Equipment)
        bind(concat("{\\"@id\\":\\"", str(?meas_id),"\\",\\"@type\\":\\"",strafter(str(?m_cls),"%s"), "\\"}") as ?Measurement)

    }
        ORDER by ?Equipment
        ''' % (split, split, split, split, get_namespace(), get_namespace())

    return query_message
