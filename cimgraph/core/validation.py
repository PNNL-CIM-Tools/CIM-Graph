from __future__ import annotations

import re

# Identifier characters allowed in an XML rdf:ID (NCName letters, digits, '_', '.', '-').
# Covers UUIDs with or without a leading underscore and legacy IDs such as '_LINE_650632'.
# Excludes quotes, backticks, braces and whitespace, so a valid identifier cannot break
# out of a quoted SPARQL or Cypher string.
_IDENTIFIER = re.compile(r'[A-Za-z0-9_.\-]+')

# An attribute or association name: 'name' or 'Class.name'.
_ATTRIBUTE = re.compile(r'[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)?')


def validate_identifier(value: str) -> str:
    """
    Return an mRID or rdf:ID unchanged if it is safe to put in a query, otherwise raise.

    Call this on every caller-supplied identifier before it is interpolated into a
    SPARQL or Cypher query.
    """
    if not isinstance(value, str) or _IDENTIFIER.fullmatch(value) is None:
        raise ValueError(f'Invalid identifier {value!r}: expected a UUID or rdf:ID '
                         'containing only letters, digits, "_", "." and "-"')
    return value


def validate_attribute(value: str) -> str:
    """Return an attribute name ('name' or 'Class.name') unchanged if valid, otherwise raise."""
    if not isinstance(value, str) or _ATTRIBUTE.fullmatch(value) is None:
        raise ValueError(f'Invalid attribute name {value!r}: expected "name" or "Class.name"')
    return value


# Characters an RDF IRI may not contain (RFC 3987 / SPARQL IRIREF); any of them would
# also break out of an rdf:resource attribute or a SPARQL <...> IRI.
_IRI_FORBIDDEN = re.compile(r'[<>"{}|^`\\\x00-\x20]')


def validate_iri_text(value: str) -> str:
    """Return a reference IRI or identifier unchanged if it is a valid IRI, otherwise raise."""
    if not isinstance(value, str) or not value or _IRI_FORBIDDEN.search(value):
        raise ValueError(f'Invalid IRI or identifier {value!r}: it is empty or contains a '
                         'character not allowed in an IRI (<>"{}|^`\\ or whitespace)')
    return value
