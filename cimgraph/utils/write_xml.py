from __future__ import annotations

import enum
import importlib
import json
import logging
import math
import uuid

from cimgraph.data_profile.known_problem_classes import ClassesWithManytoMany
from cimgraph.models.graph_model import GraphModel

_log = logging.getLogger(__name__)


def write_xml(network: GraphModel, filename: str) -> None:
    namespace = network.connection.namespace
    iec61970_301 = network.connection.iec61970_301
    classes_with_many_to_many = ClassesWithManytoMany()
    many_to_many = classes_with_many_to_many.attributes
    # Handling of formatting change between different 301 standard versions
    if int(iec61970_301) > 7:
        rdf_header = 'rdf:about="urn:uuid:'
        rdf_resource = 'urn:uuid:'
    else:
        rdf_header = 'rdf:ID="'
        rdf_resource = '#'
    f = open(filename, 'w', encoding='utf-8')
    header = '<?xml version="1.0" encoding="utf-8"?>\n'
    header += '<!-- un-comment this line to enable validation\n'
    header += '-->\n'
    header += f'<rdf:RDF xmlns:cim="{namespace}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
    header += '<!--\n'
    header += '-->\n'
    f.write(header)
    for root_class in list(network.graph.keys()):
        counter = 0
        for obj in network.graph[root_class].values():
            cim_class = obj.__class__
            header = f'<cim:{cim_class.__name__} {rdf_header}{obj.uri()}">\n'
            f.write(header)
            parent_classes = list(cim_class.__mro__)
            parent_classes.pop(len(parent_classes) - 1)
            for parent in parent_classes:
                for attribute in parent.__annotations__.keys():
                    # Check if attribute is in data profile
                    attribute_type = cim_class.__dataclass_fields__[attribute].type
                    rdf = f'{parent.__name__}.{attribute}'
                    if attribute == 'identifier':
                        continue
                    # Upload attributes that are many-to-one or are known problem classes
                    if 'list' not in attribute_type or rdf in many_to_many:
                        edge_class = attribute_type.split('[')[1].split(']')[0]
                        edge = getattr(obj, attribute)
                        # Check if attribute is association to a class object
                        if edge_class in network.connection.cim.__all__:
                            if edge is not None and edge != []:
                                if type(edge.__class__) is enum.EnumMeta:
                                    resource = f'rdf:resource="{namespace}{str(edge)}"'
                                    row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                    f.write(row)
                                elif type(edge) is str or type(edge) is bool or type(edge) is float:
                                    row = f'  <cim:{parent.__name__}.{attribute}>{str(edge)}</cim:{parent.__name__}.{attribute}>\n'
                                    f.write(row)
                                elif type(edge) is list:
                                    for value in edge:
                                        #TODO: lookup how to handle multiple rows of same value
                                        if type(value.__class__) is enum.EnumMeta:
                                            resource = f'rdf:resource="{namespace}{str(edge)}"'
                                            row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                            f.write(row)
                                        elif type(value) is str or type(value) is bool or type(value) is float:
                                            row = f'  <cim:{parent.__name__}.{attribute}>{str(value)}</cim:{parent.__name__}.{attribute}>\n'
                                            f.write(row)
                                        else:
                                            resource = f'rdf:resource="{rdf_resource}{value.uri()}"'
                                            row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                            f.write(row)
                                else:
                                    # try:
                                        resource = f'rdf:resource="{rdf_resource}{edge.uri()}"'
                                        row = f'  <cim:{parent.__name__}.{attribute} {resource}/>\n'
                                        f.write(row)
                                    # except:
                                    #     _log.warning(obj.__dict__)
                        else:
                            if edge is not None and edge != [] and rdf != 'Identity.identifier':
                                row = f'  <cim:{parent.__name__}.{attribute}>{str(edge)}</cim:{parent.__name__}.{attribute}>\n'
                                f.write(row)
            tail = f'</cim:{cim_class.__name__}>\n'
            f.write(tail)
            counter = counter + 1
        _log.info(f'wrote {counter} {cim_class.__name__} objects')
    f.write('</rdf:RDF>')
    f.close()
