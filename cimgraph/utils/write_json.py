from __future__ import annotations

import enum
import json
import logging
from dataclasses import dataclass, field, is_dataclass

from cimgraph.data_profile.known_problem_classes import ClassesWithManytoMany
from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def write_json_ld(network: GraphModel, filename: str, namespaces: dict=None, indent:int=4) -> None:
    """
    Write the network graph to an XML file.

    Args:
        network (GraphModel): The network graph to be written to an XML file.
        namespaces (dict): A dictionary of namespaces to be used in the XML file. The key is the namespace prefix and the value is the namespace URI. Defaults to CIM100.

    Returns:
        None

    """
    if namespaces is None:
        namespaces = {'cim': 'http://iec.ch/TC57/CIM100#',
                      'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}

    # Create reverse lookup for namespace
    reverse_ns_lookup = {v: k for k, v in namespaces.items()}

    classes_with_many_to_many = ClassesWithManytoMany()
    many_to_many = classes_with_many_to_many.attributes

    # Write XML header and namespace declarations
    f = open(filename, 'w', encoding='utf-8')
    f.write('{\n')

    context = {
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'cim': 'http://ucaiug.org/ns/CIM#',
        'eu': 'http://iec.ch/TC57/CIM100-European#',
        'dcterms': 'http://purl.org/dc/terms/',
        'dcat': 'http://www.w3.org/ns/dcat#',
        'prov': 'http://www.w3.org/ns/prov#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#'
        }
    f.write(' '*indent + '"@context": ')
    f.write(json.dumps(context, indent=indent).replace('\n', '\n' + ' '*indent)+',\n')

    # TODO: Add support for PROV, DCAT, and timestamping of model data

    f.write(' '*indent + '"@graph": [\n')

    # Write each object in the network graph to the XML file
    for root_class in list(network.graph.keys()):
        counter = 0
        for obj in network.graph[root_class].values():

            cim_class = obj.__class__
            dump = {}
            dump['@id'] = 'urn:uuid:'+obj.uri()
            dump['@type'] = f'cim:{cim_class.__name__}'
            parent_classes = list(cim_class.__mro__)
            parent_classes.pop(len(parent_classes) - 1)
            for parent in parent_classes:
                for attribute in parent.__annotations__.keys():
                    # Skip over Identity.identifier attribute
                    if attribute == 'identifier':
                        continue
                    attribute_type = cim_class.__dataclass_fields__[attribute].type
                    rdf = f'{parent.__name__}.{attribute}'
                    attr_ns = cim_class.__dataclass_fields__[attribute].metadata['namespace']
                    ns_prefix = reverse_ns_lookup[attr_ns]

                    # Upload attributes that are many-to-one or are known problem classes
                    if 'list' not in attribute_type or rdf in many_to_many:
                        edge_class = attribute_type.split('[')[1].split(']')[0]
                        edge = getattr(obj, attribute)
                        # Check if attribute is association to a class object
                        if edge_class in network.connection.cim.__all__:
                            if edge is not None and edge != []:
                                if type(edge.__class__) is enum.EnumMeta:
                                    dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = f'{attr_ns}:{str(edge)}'
                                elif type(edge) is str or type(edge) is bool or type(edge) is float:
                                    dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = str(edge)
                                elif type(edge) is list:
                                    for value in edge:
                                        if type(edge.__class__) is enum.EnumMeta:
                                            dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = f'{attr_ns}:{str(value)}'
                                        elif type(edge) is str or type(edge) is bool or type(edge) is float:
                                            dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = str(value)
                                        else:
                                            dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = json.loads(value.__repr__())
                                else:
                                    dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = json.loads(edge.__repr__())
                        else:
                            if edge is not None and edge != [] and rdf != 'Identity.identifier':
                                dump[f'{ns_prefix}:{parent.__name__}.{attribute}'] = str(edge)

            f.write(' '*indent*2 + json.dumps(dump, indent=indent).replace('\n', '\n' + ' '*indent*2)+',\n')
        counter = counter + 1
        _log.info(f'wrote {counter} {cim_class.__name__} objects')
    f.close()
    # Remove the last two characters before the closing bracket
    f = open(filename, 'rb+')
    f.seek(-2, 2)
    f.truncate()
    f = open(filename, 'a', encoding='utf-8')
    f.write('\n'+' '*indent + ']\n'+'}')
    f.close()
