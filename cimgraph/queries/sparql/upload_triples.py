from __future__ import annotations

import enum
import importlib
import logging

from cimgraph.data_profile.known_problem_classes import ClassesWithManytoMany
from cimgraph.databases import ConnectionParameters

_log = logging.getLogger(__name__)


def upload_triples_sparql(obj: object, params: ConnectionParameters) -> str:
    """
    Generates SPARQL query string to upload graph model changes to database
    Args:
        obj: A valid cim object instance.
        params: ConnectionParameters object with namespace, iec61070-301 vers, etc.
    Returns:
        query_message: query string that can be used in blazegraph connection or STOMP client
    """
    cim = importlib.import_module('cimgraph.data_profile.' + params.cim_profile)
    many_to_many = ClassesWithManytoMany().attributes

    # Handling of formatting change between different 301 standard versions
    if int(params.iec61970_301) > 7: # Now use rdf:about
        rdf_resource = 'urn:uuid:'
    else: # Older versions used rdf:ID
        rdf_resource = f"""{params.url}#"""
    rdf_enum = f"""{params.namespace}"""

    prefix = 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'
    prefix += f'PREFIX cim: <{params.namespace}>\n'
    prefix += 'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n'
    triples = []
    cim_class = obj.__class__
    # Write object class description
    triple = f'\n\t<{rdf_resource}{obj.uri()}> a cim:{cim_class.__name__}.\n'
    triples.append(triple)
    # Get list of all classes from which current object inherits
    parent_classes = list(cim_class.__mro__)
    parent_classes.pop(len(parent_classes) - 1)
    # Iterate through parent classes
    for parent in parent_classes:
        # Iterate through attributes and associations inherited from each parent class
        for attribute in parent.__annotations__.keys():
            if attribute == 'identifier':
                continue

            try:
                # Check if attribute is in data profile
                attribute_type = cim_class.__dataclass_fields__[attribute].type
                rdf = f'{parent.__name__}.{attribute}'
                # Upload attributes that are many-to-one or are known problem classes
                if 'list' not in attribute_type or rdf in many_to_many:
                    edge_class = attribute_type.split('[')[1].split(']')[0]
                    edge = getattr(obj, attribute)
                    # Check if typed to a class within CIM profile
                    if edge_class in cim.__all__:
                        if edge is not None and edge != []:
                            # Check if edge is an enumeration
                            if type(edge.__class__) is enum.EnumMeta:
                                triple = f'\n\t<{rdf_resource}{obj.uri()}> cim:{parent.__name__}.{attribute} <{rdf_enum}{str(edge)}>.\n'
                            else:
                                if type(edge) == str:
                                    triple = f'\n\t<{rdf_resource}{obj.uri()}> cim:{parent.__name__}.{attribute} <{rdf_resource}{edge}>.\n'
                                    triples.append(triple)
                                elif type(edge) == list:
                                    for value in edge:
                                        if type(edge) == str:
                                            triple = f'\n\t<{rdf_resource}{obj.uri()}> cim:{parent.__name__}.{attribute} <{rdf_resource}{value}>.\n'
                                            triples.append(triple)
                                        else:
                                            triple = f'\n\t<{rdf_resource}{obj.uri()}> cim:{parent.__name__}.{attribute} <{rdf_resource}{value.uri()}>.\n'
                                            triples.append(triple)
                                else:
                                    triple = f'\n\t<{rdf_resource}{obj.uri()}> cim:{parent.__name__}.{attribute} <{rdf_resource}{edge.uri()}>.\n'
                                    triples.append(triple)
                    else:
                        if edge is not None and edge != [] and rdf != 'Identity.identifier':
                            triple = f"\n\t<{rdf_resource}{obj.uri()}> cim:{parent.__name__}.{attribute} \"{str(edge)}\".\n"
                            triples.append(triple)
            except:
                # Otherwise throw warning that attribute was invalid
                _log.warning(f'Unable to create rdf triple for {cim_class.__name__}.{attribute} = {str(edge)}')
    triples.append('}')
    query_message = prefix + 'INSERT DATA { ' + ''.join(triples)
    return query_message
