import os
import sqlite3
import unittest

import pytest

from cimgraph import utils
from cimgraph.databases import MySQLConnection, XMLFile
from cimgraph.databases.mysql.schema import build_schema
from cimgraph.models import FeederModel

FEEDER_MRID = '_49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'

ENV = {
    'CIMG_CIM_PROFILE': 'rc4_2021',
    'CIMG_HOST': '127.0.0.1',
    'CIMG_PORT': '3306',
    'CIMG_USERNAME': 'root',
    'CIMG_PASSWORD': 'password',
    'CIMG_DATABASE': 'tier5_ieee13',
    'CIMG_USE_UNITS': 'true',
}


class TestSqlSchema(unittest.TestCase):
    """Schema metadata parsing, no database required."""

    def setUp(self):
        columns = [
            {'TABLE_NAME': 'IdentifiedObject', 'COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'IdentifiedObject', 'COLUMN_NAME': 'name'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'phases'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'ConductingEquipment'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'Compound'},
            {'TABLE_NAME': 'Switch', 'COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'Breaker', 'COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'PhaseCode', 'COLUMN_NAME': 'name'},
        ]
        keys = [
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'mRID',
             'REFERENCED_TABLE_NAME': 'IdentifiedObject', 'REFERENCED_COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'Switch', 'COLUMN_NAME': 'mRID',
             'REFERENCED_TABLE_NAME': 'IdentifiedObject', 'REFERENCED_COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'Breaker', 'COLUMN_NAME': 'mRID',
             'REFERENCED_TABLE_NAME': 'Switch', 'REFERENCED_COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'ConductingEquipment',
             'REFERENCED_TABLE_NAME': 'Switch', 'REFERENCED_COLUMN_NAME': 'mRID'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'phases',
             'REFERENCED_TABLE_NAME': 'PhaseCode', 'REFERENCED_COLUMN_NAME': 'name'},
            {'TABLE_NAME': 'Terminal', 'COLUMN_NAME': 'Compound',
             'REFERENCED_TABLE_NAME': 'SomeCompound', 'REFERENCED_COLUMN_NAME': 'id'},
        ]
        self.schema = build_schema(columns, keys)

    def test_class_tables_exclude_enums(self):
        self.assertNotIn('PhaseCode', self.schema.columns)
        self.assertEqual(self.schema.columns['Terminal'], ['phases', 'ConductingEquipment'])

    def test_hierarchy(self):
        self.assertEqual(self.schema.ancestry('Breaker'), ['Breaker', 'Switch', 'IdentifiedObject'])
        self.assertEqual(self.schema.descendants('Switch'), ['Switch', 'Breaker'])
        self.assertEqual(self.schema.roots(), ['IdentifiedObject'])

    def test_associations(self):
        # Enum keys are plain columns; the unsupported compound key is dropped
        self.assertEqual(self.schema.associations, {('Terminal', 'ConductingEquipment'): 'Switch'})


# A small CIMTool-style database for offline tests: one feeder holding one line with two
# terminals and nodes, keyed by mRIDs stored with a leading underscore like tier5_ieee13.
# Each table: (parent table, {association column: target table}, rows of (mRID, values...)).
LINE_MRID = '_0BBD0EA3-F665-465B-86FD-FC8B8466AD53'
TABLES = {
    'IdentifiedObject': (None, {'name': None}, [
        (FEEDER_MRID, 'ieee13'), (LINE_MRID, '645646'),
        ('_T1', 't1'), ('_T2', 't2'), ('_N1', 'n1'), ('_N2', 'n2')]),
    'Feeder': ('IdentifiedObject', {}, [(FEEDER_MRID,)]),
    'Equipment': ('IdentifiedObject', {'EquipmentContainer': 'Feeder'}, [(LINE_MRID, FEEDER_MRID)]),
    'ACLineSegment': ('Equipment', {}, [(LINE_MRID,)]),
    'ConnectivityNode': ('IdentifiedObject', {}, [('_N1',), ('_N2',)]),
    'Terminal': ('IdentifiedObject', {'ConductingEquipment': 'Equipment',
                                      'ConnectivityNode': 'ConnectivityNode'},
                 [('_T1', LINE_MRID, '_N1'), ('_T2', LINE_MRID, '_N2')]),
}
# Terminal and node mRIDs must be UUIDs to be read as the same objects in every style
UUIDS = {'_T1': '_1F8A2C0E-2B9C-4C59-9E0A-5D0D6B7E8A01', '_T2': '_1F8A2C0E-2B9C-4C59-9E0A-5D0D6B7E8A02',
         '_N1': '_1F8A2C0E-2B9C-4C59-9E0A-5D0D6B7E8A03', '_N2': '_1F8A2C0E-2B9C-4C59-9E0A-5D0D6B7E8A04'}


def _sqlite_connection(monkeypatch, style: str) -> MySQLConnection:
    """A MySQLConnection reading TABLES from an in-memory SQLite database (which also
    takes double-quoted identifiers), in the given CIMG_IEC61970_552 style."""
    for key, value in {**ENV, 'CIMG_IEC61970_552': style}.items():
        monkeypatch.setenv(key, value)
    database = sqlite3.connect(':memory:')
    column_rows, key_rows = [], []
    for table, (parent, columns, rows) in TABLES.items():
        names = ['mRID', *columns]
        database.execute(f'CREATE TABLE "{table}" ({", ".join(f"{name!r}" for name in names)})')
        values = [tuple(UUIDS.get(value, value) for value in row) for row in rows]
        database.executemany(f'INSERT INTO "{table}" VALUES ({", ".join("?" * len(names))})', values)
        column_rows += [{'TABLE_NAME': table, 'COLUMN_NAME': name} for name in names]
        references = {'mRID': parent, **columns}
        key_rows += [{'TABLE_NAME': table, 'COLUMN_NAME': column, 'REFERENCED_TABLE_NAME': target,
                      'REFERENCED_COLUMN_NAME': 'mRID'}
                     for column, target in references.items() if target is not None]

    def execute(query_message: str, params: tuple = ()) -> list[dict]:
        cursor = database.execute(query_message.replace('%s', '?'), params)
        names = [description[0] for description in cursor.description]
        return [dict(zip(names, row)) for row in cursor.fetchall()]

    connection = MySQLConnection()
    connection.connection = database  # connect() then uses it instead of a MySQL server
    connection.schema = build_schema(column_rows, key_rows)
    monkeypatch.setattr(connection, 'execute', execute)
    return connection


@pytest.mark.parametrize('style', ['552-NEW', '552-LEGACY', 'CGMES'])
def test_lookups_match_the_stored_mrid_in_every_style(monkeypatch, style):
    """The mRID column keeps the source model's '_<uuid>' whatever CIMG_IEC61970_552 is."""
    connection = _sqlite_connection(monkeypatch, style)
    cim = connection.cim
    feeder = connection.get_object(FEEDER_MRID)
    network = FeederModel(connection=connection, container=feeder, distributed=False)
    line = network.first(cim.ACLineSegment)
    assert len(network.list_by_class(cim.Terminal)) == 2
    assert len(network.list_by_class(cim.ConnectivityNode)) == 2

    assert network.get_from_triple(line, 'IdentifiedObject.name') == ['645646']
    terminals = network.get_from_triple(line, 'ConductingEquipment.Terminals')
    assert len(terminals) == 2 and set(terminals) == set(line.Terminals)
    network.get_all_attributes(cim.Terminal)
    assert sorted(terminal.name for terminal in line.Terminals) == ['t1', 't2']
    connection.disconnect()


@pytest.mark.integration('mysql')
class TestMySQLConnection(unittest.TestCase):

    def setUp(self):
        self.original_env = {key: os.getenv(key) for key in ENV}
        os.environ.update(ENV)
        self.database = MySQLConnection()
        self.cim = self.database.cim
        feeder = self.database.get_object(FEEDER_MRID)
        self.network = FeederModel(connection=self.database, container=feeder, distributed=False)

    def tearDown(self):
        self.database.disconnect()
        for key, value in self.original_env.items():
            if value is not None:
                os.environ[key] = value
            else:
                os.environ.pop(key, None)

    def test_connection_with_env_vars(self):
        self.assertEqual(self.database.cim_profile, 'rc4_2021')
        self.assertEqual(self.database.host, '127.0.0.1')
        self.assertEqual(self.database.port, 3306)
        self.assertEqual(self.database.database, 'tier5_ieee13')

    def test_get_object(self):
        feeder = self.database.get_object(FEEDER_MRID)
        self.assertIsInstance(feeder, self.cim.Feeder)
        self.assertIsNone(self.database.get_object('_not-an-mrid'))

    def test_get_object_resolves_most_derived_class(self):
        breaker = self.network.first(self.cim.Breaker)
        self.assertIsInstance(self.database.get_object(breaker.uri()), self.cim.Breaker)

    def test_feeder_model_connectivity(self):
        terminals = self.network.list_by_class(self.cim.Terminal)
        self.assertEqual(len(terminals), 69)
        self.assertEqual(len(self.network.list_by_class(self.cim.ConnectivityNode)), 22)
        for terminal in terminals:
            self.assertIsNotNone(terminal.ConnectivityNode)
            self.assertIn(terminal, terminal.ConductingEquipment.Terminals)

    def test_get_all_edges_reverse_associations(self):
        self.network.get_all_edges(self.cim.ACLineSegment)
        self.assertEqual(len(self.network.list_by_class(self.cim.ACLineSegmentPhase)), 26)
        for line in self.network.list_by_class(self.cim.ACLineSegment):
            self.assertIsInstance(line.BaseVoltage, self.cim.BaseVoltage)
            self.assertTrue(line.ACLineSegmentPhases)

    def test_values_enums_booleans_units(self):
        self.network.get_all_edges(self.cim.EnergyConsumer)
        self.network.get_all_edges(self.cim.Breaker)
        self.network.get_all_edges(self.cim.ACLineSegment)
        for consumer in self.network.list_by_class(self.cim.EnergyConsumer):
            self.assertIsInstance(consumer.phaseConnection, self.cim.PhaseShuntConnectionKind)
        breaker = self.network.first(self.cim.Breaker)
        self.assertIs(type(breaker.normalOpen), bool)
        line = self.network.graph[self.cim.ACLineSegment]
        lengths = sorted(round(obj.length.to('m'), 2) for obj in line.values())
        self.assertIn(91.44, lengths)

    def test_get_all_attributes_does_not_expand_graph(self):
        self.network.get_all_attributes(self.cim.ACLineSegment)
        self.assertNotIn(self.cim.ACLineSegmentPhase, self.network.graph)
        line = self.network.first(self.cim.ACLineSegment)
        self.assertIsInstance(line.BaseVoltage, str)

    def test_dangling_reference_is_skipped(self):
        # RatioTapChanger.TransformerEnd points at TransformerTankEnds, which are not in the schema
        rows = self.database.execute('SELECT "mRID" FROM "RatioTapChanger"')
        changers = [self.database.get_object(row['mRID'], self.network.graph) for row in rows]
        self.network.get_all_edges(self.cim.RatioTapChanger)
        for changer in changers:
            self.assertIsNone(changer.TransformerEnd)

    def test_get_from_triple(self):
        terminal = self.network.first(self.cim.Terminal)
        nodes = self.database.get_from_triple(terminal, 'Terminal.ConnectivityNode')
        self.assertEqual(nodes, [terminal.ConnectivityNode])
        line = self.network.first(self.cim.ACLineSegment)
        terminals = self.database.get_from_triple(line, 'ConductingEquipment.Terminals')
        self.assertEqual(len(terminals), 2)
        names = self.database.get_from_triple(line, 'IdentifiedObject.name')
        self.assertEqual(names, [line.name])

    def test_matches_xml_file(self):
        xml = XMLFile(filename='tests/test_models/ieee13_2021.xml')
        xml_network = FeederModel(connection=xml, container=self.cim.Feeder(mRID=FEEDER_MRID),
                                  distributed=False)
        utils.get_all_data(self.network)
        # Every class read from MySQL has the same objects as the XML file
        for cim_class, objects in self.network.graph.items():
            self.assertEqual(len(objects), len(xml_network.graph[cim_class]), cim_class.__name__)
        for terminal in self.network.list_by_class(self.cim.Terminal):
            xml_terminal = xml_network.graph[self.cim.Terminal][terminal.identifier]
            self.assertEqual(xml_terminal.ConnectivityNode.identifier,
                             terminal.ConnectivityNode.identifier)

    def test_upload_not_supported(self):
        with self.assertRaises(NotImplementedError):
            self.database.upload(self.network.graph)


if __name__ == '__main__':
    unittest.main()
