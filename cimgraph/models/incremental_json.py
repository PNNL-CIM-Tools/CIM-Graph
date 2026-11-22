"""JSON difference messages, as the pair to ``incremental_builder``'s RDF/XML.

``incremental_builder`` reads and writes differences as RDF/XML files. A message
bus carries JSON, so an application that wants to publish or apply a difference
over a bus has had to build that JSON itself. Doing so by hand loses the two
things ``GraphModel.modify`` provides -- the attribute is validated against the
profile, and the prior value is recorded automatically -- so the usual result is
hand-tracked "previous value" state and attribute names spelled as plain field
names, which a consumer silently ignores.

Both directions here go through the same helpers ``write_incremental`` and
``apply_incremental`` use, so a JSON difference means exactly what an RDF/XML one
means.

**Flavors.** The GridAPPS-D shape is implemented. JSON-LD is a stub: see
:func:`read_incremental_jsonld`.

**Two shapes, deliberately not unified.** A difference exists in two forms in
cimgraph, and this module converts between them rather than inventing a third:

``model.incrementals`` -- keyed by class, then URI, with *field* names, as
:func:`~cimgraph.models.incremental_builder.record_difference` records it and
``write_incremental`` consumes it::

    {'forwardDifferences': {cim.ACLineSegment: {uri: {'length': Length(10, 'm')}}}}

the applied form -- keyed by URI, with qualified ``Class.attribute`` names, as
``read_incremental_xml`` returns it and ``apply_incremental`` consumes it::

    {'forwardDifferences': {uri: {'Conductor.length': '10.0'}}}

The class key is what makes the qualified name derivable: ``length`` is declared
on ``Conductor``, not on ``ACLineSegment``, so the name cannot be reconstructed
from a field name alone. :func:`write_incremental_gridappsd` therefore reuses
``field_properties``, which resolves the declaring class, instead of formatting
the name itself.

Values are left as text or numbers in the applied form, matching
``read_incremental_xml`` (which yields ``'10.0'``, not ``Length(10, 'm')``);
``apply_incremental`` converts and validates them against each attribute's
datatype.
"""

from __future__ import annotations

import logging
from collections import defaultdict

from cimgraph.core.attribute_utils import field_properties

_log = logging.getLogger(__name__)

__all__ = [
    'read_incremental_gridappsd',
    'read_incremental_jsonld',
    'write_incremental_gridappsd',
    'write_incremental_jsonld',
]


# -------------------------------------------------------------------------
# GridAPPS-D difference messages
# -------------------------------------------------------------------------

def _statements(differences: dict) -> list[dict]:
    """The ``{object, attribute, value}`` statements of a class-keyed difference.

    ``field_properties`` resolves the declaring class for the ``Class.attribute``
    name a consumer routes on, and classifies the value: a referenced object
    becomes its URI, and a ``CIMUnit`` becomes the plain number it stores, which
    is in base SI units. A list attribute yields one statement per item, and a
    value of None or ``[]`` yields none -- the same rule ``_difference_row``
    applies when writing XML.
    """
    statements = []
    for cim_class, objects in differences.items():
        for uri, difference in objects.items():
            for attribute, value in difference.items():
                if attribute == 'rdf:type':
                    # Creates and deletes are carried by forward/reverse rdf:type in
                    # RDF/XML. A GridAPPS-D message has no equivalent, so they are
                    # rejected in write_incremental_gridappsd rather than dropped here.
                    continue
                for prop in field_properties(cim_class, attribute, value):
                    text = prop.value.value if prop.kind == 'unit' else prop.value
                    statements.append({'object': uri, 'attribute': prop.name, 'value': text})
    return statements


def _creates_or_deletes(differences: dict) -> list[str]:
    """The URIs whose difference creates or deletes the object."""
    return [uri for objects in differences.values() for uri, difference in objects.items()
            if difference.get('rdf:type') is not None]


def write_incremental_gridappsd(reverse: dict | None, forward: dict | None, *,
                                simulation_id: str, timestamp: int) -> dict | None:
    """Build a GridAPPS-D difference message from a model's ``incrementals``.

    Pass ``model.incrementals['reverseDifferences']`` and
    ``['forwardDifferences']``, as with ``write_incremental``.

    Returns None when there is nothing to publish, so a caller can skip
    publishing rather than send an empty update. Note that
    ``record_difference`` already removes an attribute set back to its original
    value, so a change and its undo leave nothing to send.

    Raises:
        ValueError: if a difference creates or deletes an object. A GridAPPS-D
            message updates attributes of existing objects only; it has no
            representation for an object's class, so publishing a create as a
            bare attribute update would silently drop the object itself. Write
            RDF/XML for those (``write_incremental``), or publish JSON-LD once
            :func:`write_incremental_jsonld` exists.
    """
    forward = forward or {}
    reverse = reverse or {}
    structural = _creates_or_deletes(forward) + _creates_or_deletes(reverse)
    if structural:
        raise ValueError(
            f'A GridAPPS-D difference message can only update attributes, but these objects '
            f'are created or deleted: {", ".join(sorted(set(structural)))}. Use '
            f'write_incremental for an RDF/XML difference model, which carries rdf:type.')

    forward_statements = _statements(forward)
    if not forward_statements:
        return None
    return {
        'command': 'update',
        'input': {
            'simulation_id': str(simulation_id),
            'message': {
                'timestamp': int(timestamp),
                'reverse_differences': _statements(reverse),
                'forward_differences': forward_statements,
            },
        },
    }


def _difference_of(statements: list, direction: str) -> dict:
    """Group ``{object, attribute, value}`` statements by URI, repeats into a list."""
    difference: dict = defaultdict(dict)
    for index, statement in enumerate(statements):
        for key in ('object', 'attribute', 'value'):
            if key not in statement:
                raise ValueError(f'{direction}[{index}] has no {key!r}: {statement}')
        uri, attribute, value = statement['object'], statement['attribute'], statement['value']
        existing = difference[uri].get(attribute)
        if existing is None:
            difference[uri][attribute] = value
        elif isinstance(existing, list):
            existing.append(value)
        else:
            difference[uri][attribute] = [existing, value]
    return dict(difference)


def read_incremental_gridappsd(message: dict) -> dict:
    """Read a GridAPPS-D difference message into the form ``apply_incremental`` takes.

    The message is the shape :func:`write_incremental_gridappsd` builds, either
    whole or just its inner ``message`` (what a bus subscriber usually receives).
    Values are left as given; ``apply_incremental`` converts and validates them.

    Apply one to a model with::

        apply_incremental(model, read_incremental_gridappsd(message))

    which needs no file, unlike ``GraphModel.from_incremental``. The model and
    its ``incrementals`` end up as if the changes had been made on it.

    Raises:
        ValueError: if the message has neither difference list, or a statement
            is missing ``object``, ``attribute`` or ``value``. A difference that
            cannot be read is never a difference that changes nothing.
    """
    inner = message.get('input', {}).get('message', message)
    forward, reverse = inner.get('forward_differences'), inner.get('reverse_differences')
    if forward is None and reverse is None:
        raise ValueError(
            "No 'forward_differences' or 'reverse_differences' in the message. A GridAPPS-D "
            'difference message holds them under input.message, or is that inner message.')
    return {
        'forwardDifferences': _difference_of(forward or [], 'forward_differences'),
        'reverseDifferences': _difference_of(reverse or [], 'reverse_differences'),
    }


# -------------------------------------------------------------------------
# JSON-LD differences
# -------------------------------------------------------------------------

# TODO(#230): a second flavor, to carry what a GridAPPS-D message cannot -- an
# object's class, so creates and deletes survive a round trip, and namespaces, so
# an extension class is not confused with a cim: one.
#
# JSON-LD is the recommended shape over Apache Avro: CIM has published JSON-LD
# context conventions, cimgraph already serializes namespace-prefixed RDF
# (`profile_namespaces`, `_prefix`) and already reads JSON-LD models
# (`tests/test_jsonld_roundtrip.py`), so this is a re-serialization of a shape
# the library has rather than a new one. Avro would add a schema registry and a
# code-generation step to buy compactness that a difference message -- a handful
# of attributes -- does not need.
#
# Both functions raise rather than return a plausible-looking empty difference:
# an unimplemented writer that returns None reads to a caller exactly like
# "nothing changed", which is the silent failure this module exists to remove.

_JSONLD_TODO = ('JSON-LD differences are not implemented yet (cimgraph issue #230). Use '
                'read/write_incremental_gridappsd, or write_incremental for RDF/XML.')


def write_incremental_jsonld(reverse: dict | None, forward: dict | None, **kwargs) -> dict:
    """Not implemented: see the note above and :data:`_JSONLD_TODO`."""
    raise NotImplementedError(_JSONLD_TODO)


def read_incremental_jsonld(message: dict) -> dict:
    """Not implemented: see the note above and :data:`_JSONLD_TODO`."""
    raise NotImplementedError(_JSONLD_TODO)
