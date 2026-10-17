import unittest
import xml.etree.ElementTree as ElementTree

import cimgraph.data_profile.cimhub_2023 as cim
from cimgraph.core import object_to_json_ld, object_to_sparql_triples, object_to_xml
from cimgraph.core.serialization import RDF_XML_CLOSE, rdf_xml_open
from cimgraph.queries.sparql import upload_triples_sparql

CIM_NS = 'http://iec.ch/TC57/CIM100#'


class TestSerialization(unittest.TestCase):

    def setUp(self):
        self.line = cim.ACLineSegment(name='line1', length=cim.Length(91.44, 'm'))
        self.terminal = cim.Terminal(name='t1', connected=True, ConductingEquipment=self.line)
        self.line.Terminals.append(self.terminal)
        self.end = cim.PowerTransformerEnd(name='end1', connectionKind=cim.WindingConnection.D)

    def test_references_follow_serialize_metadata(self):
        terminal_xml = object_to_xml(self.terminal)
        self.assertIn(f'<cim:Terminal.ConductingEquipment rdf:resource="urn:uuid:{self.line.uri()}"/>',
                      terminal_xml)
        # ConductingEquipment.Terminals is serialize=False: written from the Terminal end only
        self.assertNotIn('ConductingEquipment.Terminals', object_to_xml(self.line))

    def test_units_enums_and_booleans(self):
        self.assertIn(f'<cim:Conductor.length rdf:datatype="{CIM_NS}UnitSymbol.meter">91.44</cim:Conductor.length>',
                      object_to_xml(self.line))
        self.assertIn('<cim:ACDCTerminal.connected>true</cim:ACDCTerminal.connected>',
                      object_to_xml(self.terminal))
        enum_resource = f'{CIM_NS}WindingConnection.D'
        self.assertIn(f'rdf:resource="{enum_resource}"', object_to_xml(self.end))
        self.assertEqual(object_to_json_ld(self.end)['cim:PowerTransformerEnd.connectionKind'],
                         'cim:WindingConnection.D')

    def test_sparql_includes_enums(self):
        triples = object_to_sparql_triples(self.end)
        self.assertIn(f'<{CIM_NS}PowerTransformerEnd.connectionKind> <{CIM_NS}WindingConnection.D> .',
                      ' '.join(triples))
        self.assertTrue(upload_triples_sparql(self.end).startswith('INSERT DATA {'))

    def test_json_ld_repeated_properties_become_lists(self):
        location = cim.Location(name='loc')
        location.Measurements = [cim.Analog(name='a1'), cim.Analog(name='a2')]
        node = object_to_json_ld(location)
        expected = [{'@id': f'urn:uuid:{m.uri()}'} for m in location.Measurements]
        self.assertEqual(node['cim:Location.Measurements'], expected)

    def test_literals_are_escaped(self):
        line = cim.ACLineSegment(name='A & B <"x">')
        document = rdf_xml_open() + object_to_xml(line) + RDF_XML_CLOSE
        root = ElementTree.fromstring(document)
        names = [element.text for element in root.iter(f'{{{CIM_NS}}}IdentifiedObject.name')]
        self.assertEqual(names, ['A & B <"x">'])
        self.assertIn('"A & B <\\"x\\">"', ' '.join(object_to_sparql_triples(line)))


if __name__ == '__main__':
    unittest.main()
