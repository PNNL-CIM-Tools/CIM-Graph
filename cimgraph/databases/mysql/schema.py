from __future__ import annotations

import logging
from dataclasses import dataclass, field

_log = logging.getLogger(__name__)


@dataclass
class SqlSchema:
    """
    Metadata for a CIMTool-generated SQL schema, read from information_schema.

    Each CIM class is its own table keyed by "mRID". A subclass row shares the
    mRID of its parent row, so the class hierarchy is the set of mRID -> mRID
    foreign keys. Association columns are foreign keys to another class table's
    "mRID". Enum columns store the literal value and are read as plain columns
    (their foreign keys to enum tables are not always generated).
    """
    parent: dict[str, str] = field(default_factory=dict)
    columns: dict[str, list[str]] = field(default_factory=dict)
    associations: dict[tuple[str, str], str] = field(default_factory=dict)

    def ancestry(self, table: str) -> list[str]:
        """Return the table followed by all of its parent tables up to the root."""
        tables = [table]
        while tables[-1] in self.parent:
            tables.append(self.parent[tables[-1]])
        return tables

    def descendants(self, table: str) -> list[str]:
        """Return the table followed by all of its subclass tables."""
        tables = [table]
        for child, parent in self.parent.items():
            if parent == table:
                tables.extend(self.descendants(child))
        return tables

    def roots(self) -> list[str]:
        """Return the class tables with no parent table (e.g. IdentifiedObject)."""
        return [table for table in self.columns if table not in self.parent]

    def depth(self, table: str) -> int:
        return len(self.ancestry(table))


def build_schema(column_rows: list[dict], key_rows: list[dict]) -> SqlSchema:
    """
    Build an SqlSchema from information_schema query results.

    Args:
        column_rows: rows of information_schema.COLUMNS with TABLE_NAME, COLUMN_NAME
        key_rows: rows of information_schema.KEY_COLUMN_USAGE with TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME for all foreign keys
    Returns:
        schema: SqlSchema describing class tables, hierarchy and associations
    """
    schema = SqlSchema()

    all_columns: dict[str, list[str]] = {}
    for row in column_rows:
        all_columns.setdefault(row['TABLE_NAME'], []).append(row['COLUMN_NAME'])

    # Class tables are keyed by mRID. Enum tables only have a "name" column.
    for table, columns in all_columns.items():
        if 'mRID' in columns:
            schema.columns[table] = [column for column in columns if column != 'mRID']

    for row in key_rows:
        table = row['TABLE_NAME']
        column = row['COLUMN_NAME']
        target = row['REFERENCED_TABLE_NAME']
        target_column = row['REFERENCED_COLUMN_NAME']
        if column == 'mRID' and target_column == 'mRID':
            schema.parent[table] = target
        elif target_column == 'mRID':
            schema.associations[(table, column)] = target
        elif target_column != 'name':    # "name" keys reference enum tables
            _log.warning(f'Ignoring unsupported foreign key {table}.{column} -> '
                         f'{target}.{target_column}')
            if column in schema.columns.get(table, []):
                schema.columns[table].remove(column)

    return schema
