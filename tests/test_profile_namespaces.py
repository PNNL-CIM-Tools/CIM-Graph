"""Serializers take XML prefixes from the profile module's NAMESPACES (cimantic-graphs.xsl)."""
import sys
import types
from xml.etree import ElementTree

import pytest

from cimgraph.core.serialization import profile_namespaces


def _class_in_module(module_name, namespaces=None):
    module = types.ModuleType(module_name)
    if namespaces is not None:
        module.NAMESPACES = namespaces
    sys.modules[module_name] = module
    cls = type('Thing', (), {'__module__': module_name})
    return cls


def test_profile_namespaces_adds_the_serialization_namespaces():
    cls = _class_in_module('stub_profile_with_namespaces', {'cim': 'http://cim#', 'gad': 'http://gad#'})
    namespaces = profile_namespaces([cls])
    assert namespaces['cim'] == 'http://cim#'
    assert namespaces['gad'] == 'http://gad#'
    assert namespaces['rdf'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
    assert list(namespaces)[0] == 'cim'


def test_profile_without_namespaces_raises():
    cls = _class_in_module('stub_profile_without_namespaces')
    with pytest.raises(ValueError, match='stub_profile_without_namespaces declares no NAMESPACES'):
        profile_namespaces([cls])


def test_write_xml_declares_the_cim18v17_namespaces(tmp_path, monkeypatch):
    """No namespaces argument: the header comes from cim18v17's NAMESPACES."""
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cim18v17')
    from cimgraph.core.env_vars import get_cim_profile
    from cimgraph.databases import XMLFile
    from cimgraph.models import FeederModel
    from cimgraph.utils import write_xml
    get_cim_profile.cache_clear()
    _, cim = get_cim_profile()

    network = FeederModel(connection=XMLFile(filename=str(tmp_path / 'missing.xml')),
                          container=cim.Feeder(mRID='fdr_1'), distributed=False)
    network.add_to_graph(cim.ACLineSegment(mRID='ln_1', name='line 1'))
    out = tmp_path / 'out.xml'
    write_xml(network, str(out))

    text = out.read_text(encoding='utf-8')
    assert 'xmlns:cim="http://cim.ucaiug.io/cim101/draft#"' in text
    assert 'xmlns:gad="http://gridappsd.org/CIM/extension#"' in text
    root = ElementTree.parse(out).getroot()
    assert root.find('{http://cim.ucaiug.io/cim101/draft#}ACLineSegment') is not None
    get_cim_profile.cache_clear()


_CIM18V17_NAMESPACES = {'cim': 'http://cim.ucaiug.io/cim101/draft#',
                        'gad': 'http://gridappsd.org/CIM/extension#',
                        'nc': 'http://entsoe.eu/ns/nc#',
                        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}


def test_extension_class_is_tagged_with_its_own_namespace():
    """BatteryInfo is a GridAPPS-D extension class: gad:BatteryInfo, not cim:BatteryInfo."""
    from cimgraph.core import object_to_json_ld, object_to_xml
    from cimprofiles.cim18.cim18v17 import ACLineSegment, BatteryInfo

    battery = BatteryInfo(mRID='bat_1')
    xml = object_to_xml(battery, _CIM18V17_NAMESPACES)
    assert xml.startswith('<gad:BatteryInfo ') and xml.endswith('</gad:BatteryInfo>\n')
    assert object_to_json_ld(battery, _CIM18V17_NAMESPACES)['@type'] == 'gad:BatteryInfo'
    assert object_to_xml(ACLineSegment(mRID='ln_1'), _CIM18V17_NAMESPACES).startswith('<cim:ACLineSegment ')
