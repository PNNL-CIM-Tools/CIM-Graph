from __future__ import annotations
import math
import importlib
import logging
import re
import json
import enum
import uuid

from cimgraph.models.graph_model import GraphModel, json_dump
_log = logging.getLogger(__name__)


def write_xml(network:GraphModel, filename:str) -> None:
    namespace = network.connection.namespace
    iec61970_301 = network.connection.iec61970_301

    if int(iec61970_301) > 7:
        rdf_header = """rdf:about="urn:uuid:"""
        rdf_resource = """urn:uuid:"""
    else:
        rdf_header = """rdf:ID=\""""
        rdf_resource = """#"""

    f = open(filename, 'w', encoding='utf-8')
    header = f"""<?xml version="1.0" encoding="utf-8"?>
<!-- un-comment this line to enable validation
-->
<rdf:RDF xmlns:cim="{namespace}" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<!--
-->"""
    f.write(header)

    for cim_class in list(network.graph.keys()):

        for obj in network.graph[cim_class].values():
            header = f"""
<cim:{cim_class.__name__} {rdf_header}{obj.mRID}">"""
            f.write(header)

            parent_classes = list(cim_class.__mro__)
            parent_classes.pop(len(parent_classes) - 1)

            for pclass in parent_classes:
                attribute_list = list(pclass.__annotations__.keys())
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
                        if attribute_class in network.cim.__all__:
                            attr_obj = getattr(obj, attribute)
                            if attr_obj is not None:
                                if type(type(attr_obj)) is not enum.EnumMeta:
                                    value = """rdf:resource=\"""" + rdf_resource + attr_obj.mRID
                                else:
                                    value = """rdf:resource=\"""" + namespace + str(attr_obj)
                                body = f"""
  <cim:{pclass.__name__}.{attribute} {value}"/>"""

                                f.write(body)

                        else:
                            value = json_dump(getattr(obj, attribute), network.cim)
                            if value:
                                body = f"""
  <cim:{pclass.__name__}.{attribute}>{value}</cim:{pclass.__name__}.{attribute}>"""
                                f.write(body)
            tail = f"""
</cim:{cim_class.__name__}>"""
            f.write(tail)

    f.write("""
</rdf:RDF>""")
