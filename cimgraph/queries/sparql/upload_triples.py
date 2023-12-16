from __future__ import annotations

import enum
import importlib
import logging
import re

from cimgraph.databases import ConnectionInterface
from cimgraph.models.graph_model import json_dump

_log = logging.getLogger(__name__)


def upload_triples_sparql(obj: object, params: ConnectionInterface) -> str:
    """
    Generates SPARQL query string to upload graph model changes to database
    Args:
        obj: A valid cim profile dataclass.
        params: ConnectionParameters object with namespace, iec61070-301 vers, etc.
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    cim = importlib.import_module('cimgraph.data_profile.' + params.cim_profile)
    if int(params.iec61970_301) > 7:
        rdf_header = 'rdf:about="urn:uuid:'
        rdf_resource = 'rdf:resource:urn:uuid:'
        rdf_triple = 'urn:uuid:'
    else:
        rdf_header = """rdf:ID=\""""
        rdf_resource = f"""{params.url}#"""
        rdf_triple = f"""{params.url}#"""
    rdf_enum = f"""{params.namespace}"""

    prefix = 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'
    prefix += f'PREFIX cim: <{params.namespace}>\n'
    prefix += 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n'
    triples = []
    cim_class = type(obj)

    triple = f'\n\t<{rdf_triple}{obj.mRID}> a cim:{cim_class.__name__}.\n'
    triples.append(triple)

    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    for class_type in parent_classes:
        attribute_list = list(class_type.__annotations__.keys())
        for attribute in attribute_list:

            try:    #check if attribute is in data profile
                attribute_type = cim_class.__dataclass_fields__[attribute].type
            except:
                #replace with warning message
                _log.warning('attribute ' + str(attribute) + ' missing from ' +
                             str(cim_class.__name__))

            if 'List' not in attribute_type:    #check if attribute is association to a class object
                if '\'' in attribute_type:    #handling inconsistent '' marks in data profile
                    at_cls = re.match(r'Optional\[\'(.*)\']', attribute_type)
                    attribute_class = at_cls.group(1)
                else:
                    at_cls = re.match(r'Optional\[(.*)]', attribute_type)
                    attribute_class = at_cls.group(1)

                if attribute_class in cim.__all__:
                    attr_obj = getattr(obj, attribute)
                    if attr_obj is not None:
                        if type(attr_obj.__class__) is enum.EnumMeta:
                            value = str(attr_obj)
                            triple = f'\n\t<{rdf_triple}{obj.mRID}> cim:{class_type.__name__}.{attribute} <{rdf_enum}{value}>.\n'
                        else:
                            value = attr_obj.mRID
                            triple = f'\n\t<{rdf_triple}{obj.mRID}> cim:{class_type.__name__}.{attribute} <{rdf_resource}{value}>.\n'
                        triples.append(triple)

                else:
                    value = str(json_dump(getattr(obj, attribute), cim, json_ld=False))
                    if value:
                        triple = f"\n\t<{rdf_triple}{obj.mRID}> cim:{class_type.__name__}.{attribute} \"{value}\".\n"

                        triples.append(triple)
    triples.append('}')
    query_message = prefix + 'INSERT DATA { ' + ''.join(triples)
    return query_message
