import unittest
from uuid import uuid4

import cimprofiles.cimhub_2023 as cim
from cimgraph.core.attribute_utils import diff_attributes
from cimgraph.databases import add_object_to_graph


def line_with_terminal(identifier, terminal_identifier, name='L1'):
    """Build an ACLineSegment and Terminal that reference each other (a cycle)."""
    line = cim.ACLineSegment(identifier=identifier, name=name)
    terminal = cim.Terminal(identifier=terminal_identifier, ConductingEquipment=line)
    line.Terminals.append(terminal)
    return line, terminal


class TestIdentityEquality(unittest.TestCase):

    def test_same_identifier_is_equal_regardless_of_attributes(self):
        identifier = uuid4()
        a = cim.ACLineSegment(identifier=identifier, name='L1')
        b = cim.ACLineSegment(identifier=identifier, name='renamed')
        self.assertEqual(a, b)
        self.assertEqual(len({a, b}), 1)

    def test_different_identifier_is_not_equal(self):
        self.assertNotEqual(cim.ACLineSegment(name='L1'), cim.ACLineSegment(name='L2'))

    def test_not_equal_to_identifier_string(self):
        line = cim.ACLineSegment()
        self.assertNotEqual(line, str(line.identifier))

    def test_cyclic_copies_compare_without_recursion(self):
        line_id, terminal_id = uuid4(), uuid4()
        _, terminal_a = line_with_terminal(line_id, terminal_id)
        _, terminal_b = line_with_terminal(line_id, terminal_id)
        self.assertEqual(terminal_a, terminal_b)

    def test_usable_as_dict_key_and_in_list_remove(self):
        line_a = cim.ACLineSegment(name='A')
        line_b = cim.ACLineSegment(name='B')
        lookup = {line_a: 'a', line_b: 'b'}
        self.assertEqual(lookup[line_b], 'b')
        objects = [line_a, line_b]
        objects.remove(cim.ACLineSegment(identifier=line_b.identifier))
        self.assertEqual(objects, [line_a])

    def test_units_keep_value_equality(self):
        self.assertEqual(cim.Voltage(1, 'kV'), cim.Voltage(1000, 'V'))
        self.assertNotEqual(cim.Voltage(1, 'kV'), cim.Voltage(1, 'V'))

    def test_merged_profile_classes_use_identity_equality(self):
        from cimprofiles.cim18gmdm import connectivity, electrical
        from cimprofiles.merge import merge_profiles
        merged = merge_profiles(connectivity, electrical)
        identifier = uuid4()
        a = merged.ACLineSegment(identifier=identifier, name='L1')
        b = merged.ACLineSegment(identifier=identifier, name='renamed')
        self.assertEqual(a, b)
        self.assertEqual(len({a, b}), 1)


class TestDiffAttributes(unittest.TestCase):

    def test_reports_changed_attribute(self):
        identifier = uuid4()
        a = cim.ACLineSegment(identifier=identifier, name='L1')
        b = cim.ACLineSegment(identifier=identifier, name='L2')
        self.assertEqual(diff_attributes(a, b), {'name': ('L1', 'L2')})

    def test_identical_copies_have_no_differences(self):
        line_id, terminal_id = uuid4(), uuid4()
        line_a, terminal_a = line_with_terminal(line_id, terminal_id)
        line_b, terminal_b = line_with_terminal(line_id, terminal_id)
        self.assertEqual(diff_attributes(line_a, line_b), {})
        self.assertEqual(diff_attributes(terminal_a, terminal_b), {})

    def test_list_order_is_ignored(self):
        identifier = uuid4()
        terminal_1, terminal_2 = cim.Terminal(), cim.Terminal()
        a = cim.ACLineSegment(identifier=identifier, Terminals=[terminal_1, terminal_2])
        b = cim.ACLineSegment(identifier=identifier, Terminals=[terminal_2, terminal_1])
        self.assertEqual(diff_attributes(a, b), {})

    def test_units_compare_by_value(self):
        identifier = uuid4()
        a = cim.ACLineSegment(identifier=identifier, length=cim.Length(1, 'km'))
        b = cim.ACLineSegment(identifier=identifier, length=cim.Length(1000, 'm'))
        self.assertEqual(diff_attributes(a, b), {})

    def test_different_classes_raise(self):
        with self.assertRaises(TypeError):
            diff_attributes(cim.ACLineSegment(), cim.Terminal())


class TestAddObjectToGraph(unittest.TestCase):

    def test_readding_same_instance_is_noop(self):
        graph = {}
        line = cim.ACLineSegment(name='L1')
        add_object_to_graph(graph, line)
        add_object_to_graph(graph, line)
        self.assertEqual(list(graph[cim.ACLineSegment].values()), [line])

    def test_identifier_collision_raises(self):
        graph = {}
        add_object_to_graph(graph, cim.ACLineSegment(mRID='LINE_1'))
        with self.assertRaises(ValueError):
            add_object_to_graph(graph, cim.ACLineSegment(mRID='LINE_1'))


if __name__ == '__main__':
    unittest.main()
