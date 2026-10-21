from __future__ import annotations

import logging
from collections import defaultdict
from enum import Enum

import mysql.connector

from cimgraph.core import get_database, get_host, get_password, get_port, get_username
from cimgraph.core.serialization import mrid_text
from cimgraph.databases import ConnectionInterface, Graph
from cimgraph.databases.mysql.schema import SqlSchema, build_schema

_log = logging.getLogger(__name__)


def _database_mrid(obj) -> str:
    """The object's key in the database's "mRID" column, in the CIMG_IEC61970_552 style."""
    return mrid_text(obj, getattr(obj, 'mRID', None) or obj.uri())

BATCH_SIZE = 100


def _batches(items: list, size: int = BATCH_SIZE) -> list[list]:
    return [items[index:index + size] for index in range(0, len(items), size)]


def _placeholders(values: list) -> str:
    return ', '.join(['%s'] * len(values))


class MySQLConnection(ConnectionInterface):
    """
    Read-only connection to a MySQL database using a CIMTool-generated SQL schema.

    Each CIM class is a table keyed by "mRID", with subclass rows sharing the
    parent row's mRID. Only the single-valued end of an association is stored
    as a column, so list ends (e.g. ConductingEquipment.Terminals) are rebuilt
    by reverse lookup using the inverse metadata of the CIM data profile.
    """

    def __init__(self):
        get_host.cache_clear()
        get_port.cache_clear()
        get_username.cache_clear()
        get_password.cache_clear()
        get_database.cache_clear()
        super().__init__()
        self.host = get_host()
        self.port = get_port()
        self.username = get_username()
        self.password = get_password()
        self.database = get_database()
        self.connection = None
        self.schema: SqlSchema | None = None
        # Cache of mRID -> most-derived class table
        self._table_cache: dict[str, str] = {}

    # -------------------------------------------------------------------------
    # Connection management methods
    # -------------------------------------------------------------------------

    def connect(self) -> None:
        """Connect to MySQL and read the schema metadata."""
        if self.connection is None:
            self.connection = mysql.connector.connect(host=self.host, port=self.port,
                                                      user=self.username,
                                                      password=self.password,
                                                      database=self.database)
            # CIMTool schemas use double-quoted identifiers
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SET SESSION sql_mode = CONCAT(@@SESSION.sql_mode, ',ANSI_QUOTES')")
            self.schema = self._read_schema()

    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
        self.connection = None
        self.schema = None

    def execute(self, query_message: str, params: tuple = ()) -> list[dict]:
        """
        Execute a SQL query with bound %s parameters.

        Returns:
            rows: list of dicts keyed by column name
        """
        self.connect()
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query_message, params)
            return cursor.fetchall()

    def _read_schema(self) -> SqlSchema:
        column_rows = self.execute(
            'SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.COLUMNS '
            'WHERE TABLE_SCHEMA = %s ORDER BY TABLE_NAME, ORDINAL_POSITION', (self.database,))
        key_rows = self.execute(
            'SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME '
            'FROM information_schema.KEY_COLUMN_USAGE '
            'WHERE TABLE_SCHEMA = %s AND REFERENCED_TABLE_NAME IS NOT NULL', (self.database,))
        return build_schema(column_rows, key_rows)

    def upload(self, graph: Graph) -> None:
        raise NotImplementedError('MySQL upload is not supported; MySQLConnection is read-only')

    # -------------------------------------------------------------------------
    # Class resolution
    # -------------------------------------------------------------------------

    def _resolve_classes(self, base_tables: list[str], mrids: list[str]) -> dict[str, type]:
        """
        Find the concrete CIM class of each mRID.

        An object has a row in every table of its class hierarchy, so its class
        is the deepest table containing its mRID. Only the base tables and their
        subclass tables are searched.

        Returns:
            classes: dict of mRID -> CIM class for mRIDs found in the database
                and present in the data profile
        """
        unknown = [mrid for mrid in set(mrids) if mrid not in self._table_cache]
        tables = [table for base in base_tables for table in self.schema.descendants(base)]
        for batch in _batches(unknown):
            query = ' UNION ALL '.join(
                f'SELECT "mRID", \'{table}\' AS cls FROM "{table}" '
                f'WHERE "mRID" IN ({_placeholders(batch)})' for table in tables)
            for row in self.execute(query, tuple(batch) * len(tables)):
                current = self._table_cache.get(row['mRID'])
                if current is None or self.schema.depth(row['cls']) > self.schema.depth(current):
                    self._table_cache[row['mRID']] = row['cls']

        classes = {}
        for mrid in set(mrids):
            table = self._table_cache.get(mrid)
            if table is None:
                _log.log(self.log_level, f'{mrid} not found in tables {base_tables}')
            elif table not in self.cim.__all__:
                _log.warning(f'object class missing from data profile: {table}')
            else:
                classes[mrid] = getattr(self.cim, table)
        return classes

    # -------------------------------------------------------------------------
    # Object retrieval methods
    # -------------------------------------------------------------------------

    def get_object(self, mRID: str, graph: Graph = None) -> object:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.connect()
        classes = self._resolve_classes(self.schema.roots(), [mRID])
        if mRID not in classes:
            return None
        return self.create_object(graph, classes[mRID], mRID)

    def get_from_triple(self, subject: object, predicate: str, graph: Graph = None) -> list[object]:
        """
        Retrieve the values of one CIM property of the subject, such as
        `Terminal.ConnectivityNode` or `ConductingEquipment.Terminals`.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(obj=subject, graph=graph)
        self.connect()
        association = self.check_attribute(subject.__class__, predicate)
        if association is None:
            return []
        return self._load(graph, subject.__class__, {_database_mrid(subject): subject.identifier},
                          expand_graph=True, only_field=association)

    # -------------------------------------------------------------------------
    # Graph creation methods
    # -------------------------------------------------------------------------

    def create_new_graph(self, container: object, graph: Graph = None) -> Graph:
        """
        Create a graph of all equipment in the container, with their terminals
        and connectivity nodes.
        """
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.add_to_graph(graph=graph, obj=container)
        self._add_equipment_and_nodes(graph, 'EquipmentContainer', _database_mrid(container))
        return graph

    def create_distributed_graph(self, area: object, graph: Graph = None) -> Graph:
        if graph is None:
            graph = defaultdict(lambda: defaultdict(dict))
        self.connect()
        if 'SubSchedulingArea' not in self.schema.columns.get('Equipment', []):
            raise ValueError(f'Database {self.database} has no Equipment.SubSchedulingArea '
                             'column; distributed graphs are not supported')
        if not isinstance(area, self.cim.SubSchedulingArea):
            raise TypeError('Area object is not a SubSchedulingArea')
        self.add_to_graph(graph=graph, obj=area)
        self._add_equipment_and_nodes(graph, 'SubSchedulingArea', _database_mrid(area))
        return graph

    def _add_equipment_and_nodes(self, graph: Graph, column: str, mrid: str) -> None:
        """Add equipment where Equipment.<column> = mrid, plus their terminals and nodes."""
        rows = self.execute(
            'SELECT e."mRID" AS equipment, t."mRID" AS terminal, t."ConnectivityNode" AS node '
            'FROM "Equipment" e LEFT JOIN "Terminal" t ON t."ConductingEquipment" = e."mRID" '
            f'WHERE e."{column}" = %s', (mrid,))
        classes = self._resolve_classes(['Equipment'], [row['equipment'] for row in rows])

        for row in rows:
            eq_class = classes.get(row['equipment'])
            if eq_class is None:
                continue
            equipment = self.create_object(graph, eq_class, row['equipment'])
            if row['node'] is None:
                continue
            node = self.create_object(graph, self.cim.ConnectivityNode, row['node'])
            terminal = self.create_object(graph, self.cim.Terminal, row['terminal'])

            if terminal not in equipment.Terminals:
                equipment.Terminals.append(terminal)
            if terminal not in node.Terminals:
                node.Terminals.append(terminal)
            terminal.ConnectivityNode = node
            terminal.ConductingEquipment = equipment

    # -------------------------------------------------------------------------
    # Edge and attribute retrieval methods
    # -------------------------------------------------------------------------

    def get_all_edges(self, graph: Graph, cim_class: type) -> None:
        """
        Expand the graph by one edge for all instances of cim_class. Associated
        objects are added to the graph as new CIM objects.
        """
        self._load(graph, cim_class, self._identifiers(graph, cim_class), expand_graph=True)

    def get_all_attributes(self, graph: Graph, cim_class: type) -> None:
        """
        Retrieve all stored attributes for instances of cim_class. Associations
        are set as mRID strings instead of new CIM objects.
        """
        self._load(graph, cim_class, self._identifiers(graph, cim_class), expand_graph=False)

    def get_edges_query(self, graph: Graph, cim_class: type) -> str:
        """Return the SQL used to read the class tables of cim_class, for debugging."""
        self.connect()
        batch = list(self._identifiers(graph, cim_class))[:BATCH_SIZE]
        return ';\n'.join(self._forward_query(table, batch)
                          for table in self.schema.ancestry(cim_class.__name__))

    def _identifiers(self, graph: Graph, cim_class: type) -> dict:
        """Map the database mRID of each object of cim_class to its graph identifier."""
        return {_database_mrid(obj): identifier for identifier, obj in graph[cim_class].items()}

    def _forward_query(self, table: str, batch: list[str]) -> str:
        return f'SELECT * FROM "{table}" WHERE "mRID" IN ({_placeholders(batch)})'

    def _load(self, graph: Graph, cim_class: type, identifiers: dict, expand_graph: bool,
              only_field: str = None) -> list[object]:
        """
        Read the stored columns of each object, and (if expand_graph) the
        associations stored on the other end. Restrict to one dataclass field
        with only_field.

        Returns:
            new_values: the objects and values that were set
        """
        self.connect()
        if cim_class.__name__ not in self.schema.columns:
            _log.warning(f'Class {cim_class.__name__} has no table in database {self.database}')
            return []

        new_values = []
        for batch in _batches(list(identifiers)):
            new_values += self._load_columns(graph, cim_class, identifiers, batch,
                                             expand_graph, only_field)
            if expand_graph:
                new_values += self._load_reverse(graph, cim_class, identifiers, batch,
                                                 only_field)
        return new_values

    def _load_columns(self, graph: Graph, cim_class: type, identifiers: dict, batch: list[str],
                      expand_graph: bool, only_field: str) -> list[object]:
        """Set values from the columns of every table in the class hierarchy."""
        new_values = []
        for table in self.schema.ancestry(cim_class.__name__):
            columns = [column for column in self.schema.columns[table]
                       if only_field is None
                       or self.check_attribute(cim_class, f'{table}.{column}') == only_field]
            if not columns:
                continue
            rows = self.execute(self._forward_query(table, batch), tuple(batch))

            # Resolve the classes of all association targets in bulk
            edge_classes = {}
            if expand_graph:
                for column in columns:
                    target_table = self.schema.associations.get((table, column))
                    if target_table is not None:
                        mrids = [row[column] for row in rows if row[column] is not None]
                        edge_classes.update(self._resolve_classes([target_table], mrids))

            for row in rows:
                identifier = identifiers[row['mRID']]
                for column in columns:
                    value = row[column]
                    if value is None:
                        continue
                    attribute = f'{table}.{column}'
                    if expand_graph and (table, column) in self.schema.associations:
                        if value in edge_classes:
                            new_values.append(self.create_edge(graph, cim_class, identifier,
                                                               attribute, edge_classes[value],
                                                               value))
                    else:
                        new_values.append(self._set_value(graph, cim_class, identifier,
                                                          attribute, value))
        return new_values

    def _set_value(self, graph: Graph, cim_class: type, identifier: object, attribute: str,
                   value: object) -> object:
        """Set a plain column value, converting enum literals (e.g. 'ABC') to the profile enum."""
        association = self.check_attribute(cim_class, attribute)
        if association is None:
            return None
        enum_class = self._enum_class(cim_class.__dataclass_fields__[association].type)
        if enum_class is None:
            return self.create_value(graph, cim_class, identifier, attribute, value)
        enum_value = enum_class(value)
        setattr(graph[cim_class][identifier], association, enum_value)
        return enum_value

    def _enum_class(self, attribute_type: str) -> type | None:
        """Return the profile Enum named by a type string like 'Optional[PhaseCode]'."""
        type_name = attribute_type.removeprefix('Optional[').removesuffix(']').strip()
        enum_class = getattr(self.cim, type_name, None)
        if isinstance(enum_class, type) and issubclass(enum_class, Enum):
            return enum_class
        return None

    def _load_reverse(self, graph: Graph, cim_class: type, identifiers: dict, batch: list[str],
                      only_field: str) -> list[object]:
        """
        Set associations stored on the other end, found by looking up the
        inverse association column (e.g. ConductingEquipment.Terminals is
        rebuilt from the Terminal."ConductingEquipment" column).
        """
        new_edges = []
        for field_name, field in cim_class.__dataclass_fields__.items():
            if only_field is not None and field_name != only_field:
                continue
            inverse = field.metadata.get('inverse')
            if inverse is None:
                continue
            source_table, column = inverse.split('.')
            if (source_table, column) not in self.schema.associations:
                continue

            rows = self.execute(
                f'SELECT "mRID", "{column}" AS target FROM "{source_table}" '
                f'WHERE "{column}" IN ({_placeholders(batch)})', tuple(batch))
            edge_classes = self._resolve_classes([source_table], [row['mRID'] for row in rows])
            for row in rows:
                if row['mRID'] in edge_classes:
                    new_edges.append(self.create_edge(graph, cim_class, identifiers[row['target']],
                                                      f'{cim_class.__name__}.{field_name}',
                                                      edge_classes[row['mRID']], row['mRID']))
        return new_edges
