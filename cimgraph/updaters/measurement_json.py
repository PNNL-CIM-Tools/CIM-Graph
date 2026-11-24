"""Measurement values as a JSON stream, as the pair to ``incremental_json``'s differences.

A difference is the wrong carrier for telemetry. It needs a before-value, so a reading
that is already current cancels out, and it has nowhere to put a value's time, source or
quality. A measurement stream carries only "this measurement read this value at this
time, from this source", keyed by the measurement's mRID.

**Payload.** The CIM4NoUtility shape (``Telemark-120/Schedule/.../*_Analog_ActivePower_2.json``
and ``*_Discrete_SwitchPosition_1.json`` in https://github.com/3lbits/CIM4NoUtility): one
list per measurement class, each measurement with its values and the attributes that
interpret them::

    {"Analog": [{"mRID": "56f7f828-...", "name": "ENGENE TotW AN7",
                 "measurementType": "ThreePhaseActivePower",
                 "phases": "http://iec.ch/TC57/CIM100#PhaseCode.ABC",
                 "unitMultiplier": "http://iec.ch/TC57/CIM100#UnitMultiplier.k",
                 "unitSymbol": "http://iec.ch/TC57/CIM100#UnitSymbol.W",
                 "ACDCTerminal": {"mRID": "83bf6035-..."},
                 "AnalogValues": [{"value": 10.1, "timeStamp": "2022-03-30T12:45:39.393725Z",
                                   "sensorAccuracy": 97.2,
                                   "MeasurementValueSource": {"mRID": "b1a076df-..."}}]}],
     "Discrete": [{..., "DiscreteValues": [{"value": 0, "timeStamp": "..."}]}]}

Values carry no mRID of their own: a reading is identified by its measurement and time.
As in CIM4NoUtility, ``Measurement.Terminal`` is written as ``ACDCTerminal`` and
``Measurement.PowerSystemResource`` as ``PowerSystemResources``.

Two departures from CIM4NoUtility:

- Its file naming (``YYYYMMDDTHHMMSSZ_Analog_ActivePower_2.json``, one measurement type
  per file over a window) is an archive layout, not a stream message, so it is not used.
  One message may mix measurement types and both classes.
- Its ``measurementType`` list is narrower than IEC 62361-102 (no shunt sections or state
  of charge). ``measurementType`` is written as the measurement has it and never checked,
  so the 62361-102 names (``StateOfChargePct``, ``TapPosition`` as an Analog) pass through.

**Units.** An ``AnalogValue.value`` is a number in its Analog's ``unitMultiplier`` and
``unitSymbol``. A value given as a ``CIMUnit`` is converted to that unit with ``.to()``
(``ActivePower(10.1, 'kW')`` on a kW Analog is written as 10.1); the reader leaves values
as given, so whoever applies them converts with the measurement's unit.
"""

from __future__ import annotations

from cimprofiles.units import CIMUnit

from cimgraph.core.attribute_utils import field_properties

__all__ = [
    'read_measurement_stream',
    'write_measurement_stream',
]

# The measurement value classes: the attribute naming the value's measurement, which is
# also the measurement's key in the payload, and the key of the measurement's values
VALUE_CLASSES = {'AnalogValue': ('Analog', 'AnalogValues'),
                 'DiscreteValue': ('Discrete', 'DiscreteValues')}
VALUE_KEYS = dict(VALUE_CLASSES.values())  # {'Analog': 'AnalogValues', 'Discrete': ...}

# Written with each measurement and each value, when the profile has the attribute and it is set
MEASUREMENT_ATTRIBUTES = ('name', 'measurementType', 'phases', 'unitMultiplier', 'unitSymbol',
                          'maxValue', 'minValue', 'normalValue',
                          'Asset', 'PowerSystemResource', 'Terminal')
VALUE_ATTRIBUTES = ('value', 'timeStamp', 'sensorAccuracy',
                    'MeasurementValueSource', 'MeasurementValueQuality')
# CIM4NoUtility names these two references by their class instead of their CIM role name
PAYLOAD_KEYS = {'Terminal': 'ACDCTerminal', 'PowerSystemResource': 'PowerSystemResources'}


# -------------------------------------------------------------------------
# Writing
# -------------------------------------------------------------------------

def _mrid(reference) -> str:
    """A referenced object's uri() (as cimgraph's writers identify it), or an unresolved
    reference's text as given."""
    return reference if isinstance(reference, str) else reference.uri()


def _payload_value(prop) -> object:
    """A Property as the payload writes it: a reference as {"mRID": ...}, an enumeration
    as its IRI, a CIMUnit as the number it stores, anything else as it is."""
    if prop.kind == 'reference':
        return {'mRID': _mrid(prop.value)}
    if prop.kind == 'enum':
        return f'{prop.namespace}{prop.value}'
    if prop.kind == 'unit':
        return prop.value.value
    return prop.value


def _entry(obj, attributes: tuple[str, ...]) -> dict:
    """The payload entry of an object's attributes that are set. Each is single-valued."""
    cim_class = type(obj)
    entry = {}
    for attribute in attributes:
        if attribute not in cim_class.__dataclass_fields__:
            continue  # not in this profile, e.g. unitSymbol in cimhub_2023
        for prop in field_properties(cim_class, attribute, getattr(obj, attribute)):
            entry[PAYLOAD_KEYS.get(attribute, attribute)] = _payload_value(prop)
    return entry


def _value_class(value) -> str:
    """'AnalogValue' or 'DiscreteValue': the measurement value class value is or specializes."""
    for parent in type(value).__mro__:
        if parent.__name__ in VALUE_CLASSES:
            return parent.__name__
    raise TypeError(f'{type(value).__name__} is not an AnalogValue or DiscreteValue; '
                    f'a measurement stream carries only those')


def _measurement_unit(measurement) -> str:
    """The pint unit of a measurement's values: its multiplier and symbol ('kW')."""
    symbol = getattr(measurement, 'unitSymbol', None)
    if symbol is None:
        raise ValueError(f'{type(measurement).__name__} {measurement.uri()} has no unitSymbol, so '
                         f'a CIMUnit value cannot be converted to its unit. Set the unitSymbol '
                         f'(and unitMultiplier), or give the value as a number.')
    multiplier = getattr(measurement, 'unitMultiplier', None)
    if multiplier is None or multiplier.value == 'none':
        return symbol.value
    return multiplier.value + symbol.value


def _value_entry(value, measurement, source, timestamp: str | None) -> dict:
    """The payload entry of one measurement value, with the message's source and
    timestamp where the value has none."""
    entry = _entry(value, VALUE_ATTRIBUTES)
    if isinstance(value.value, CIMUnit):
        entry['value'] = value.value.to(_measurement_unit(measurement))
    if 'value' not in entry:
        raise ValueError(f'{type(value).__name__} {value.uri()} of {measurement.uri()} has no value')
    if timestamp is not None:
        entry.setdefault('timeStamp', timestamp)
    if 'timeStamp' not in entry:
        raise ValueError(f'{type(value).__name__} {value.uri()} of {measurement.uri()} has no '
                         f'timeStamp; set it, or pass timestamp= for the whole message')
    if source is not None:
        entry.setdefault('MeasurementValueSource', {'mRID': _mrid(source)})
    return entry


def write_measurement_stream(values, *, source=None, timestamp: str | None = None) -> dict:
    """Build a measurement stream message from measurement values.

    Args:
        values: ``AnalogValue`` and ``DiscreteValue`` objects, each linked to its measurement
            (``AnalogValue.Analog``, ``DiscreteValue.Discrete``). Values of one measurement
            are grouped under it, in the order given; measurements are in the order first seen.
        source: the ``MeasurementValueSource`` (or its mRID) of values that have none.
        timestamp: the ISO 8601 ``timeStamp`` of values that have none, e.g. one per tick.

    Returns:
        The message, with an ``Analog`` and/or ``Discrete`` list.

    Raises:
        TypeError: for a value that is not an AnalogValue or DiscreteValue.
        ValueError: if there are no values, or a value has no measurement, no value or no
            timeStamp, or is a CIMUnit whose Analog has no unitSymbol. A message that
            cannot say what was measured is never sent as a plausible empty one.
    """
    measurements: dict[str, tuple[str, dict]] = {}  # mRID: (payload key, entry)
    for value in values:
        class_key, values_key = VALUE_CLASSES[_value_class(value)]
        measurement = getattr(value, class_key)
        if measurement is None:
            raise ValueError(f'{type(value).__name__} {value.uri()} has no {class_key}; '
                             f'a value is identified by its measurement')
        mrid = measurement.uri()
        if mrid not in measurements:
            entry = {'mRID': mrid, **_entry(measurement, MEASUREMENT_ATTRIBUTES), values_key: []}
            measurements[mrid] = (class_key, entry)
        measurements[mrid][1][values_key].append(_value_entry(value, measurement, source, timestamp))

    if not measurements:
        raise ValueError('No measurement values to write')
    message: dict[str, list[dict]] = {}
    for class_key, entry in measurements.values():
        message.setdefault(class_key, []).append(entry)
    return message


# -------------------------------------------------------------------------
# Reading
# -------------------------------------------------------------------------

def _plain(item: object, where: str) -> object:
    """A payload item as a plain value: a reference {"mRID": ...} as its mRID."""
    if not isinstance(item, dict):
        return item
    if 'mRID' not in item:
        raise ValueError(f'{where} is an object without an mRID: {item}')
    return item['mRID']


def _required(entry: dict, key: str, where: str) -> object:
    if not isinstance(entry, dict):
        raise ValueError(f'{where} is not an object: {entry!r}')
    if key not in entry:
        raise ValueError(f'{where} has no {key!r}')
    return entry[key]


def _list(items: object, where: str) -> list:
    if not isinstance(items, list):
        raise ValueError(f'{where} is not a list: {items!r}')
    return items


def _reading_value(item: dict, where: str) -> dict:
    """One value of a measurement, with its references as mRIDs."""
    _required(item, 'value', where)
    _required(item, 'timeStamp', where)
    return {key: _plain(field, f'{where}.{key}') for key, field in item.items()}


def read_measurement_stream(message: dict) -> dict:
    """Read a measurement stream message into its readings, keyed by measurement mRID.

    The message is the shape :func:`write_measurement_stream` builds. Each reading is the
    measurement's payload attributes, with references as their mRIDs, its ``class``
    ('Analog' or 'Discrete') and its ``values``::

        {'56f7f828-...': {'class': 'Analog', 'measurementType': 'ThreePhaseActivePower',
                          'unitMultiplier': '...#UnitMultiplier.k', 'unitSymbol': '...#UnitSymbol.W',
                          'ACDCTerminal': '83bf6035-...', ...,
                          'values': [{'value': 10.1, 'timeStamp': '2022-03-30T12:45:39.393725Z',
                                      'MeasurementValueSource': 'b1a076df-...'}]}}

    Values are left as given, in the measurement's unit (see the module notes); they are
    not resolved against a model. A measurement listed twice has its values joined.

    Raises:
        ValueError: if the message has no ``Analog`` or ``Discrete`` list, has any other
            key, or a measurement or value misses ``mRID``, its values, ``value`` or
            ``timeStamp``. A message that cannot be read is never one that read nothing.
    """
    if not isinstance(message, dict):
        raise ValueError(f'A measurement stream message is an object, not {type(message).__name__}')
    unknown = sorted(set(message) - set(VALUE_KEYS))
    if unknown:
        raise ValueError(f'Unknown keys {unknown} in the message; a measurement stream has '
                         f'only {sorted(VALUE_KEYS)} lists')
    if not message:
        raise ValueError(f'No {" or ".join(sorted(VALUE_KEYS))} list in the message')

    readings: dict[str, dict] = {}
    for class_key, values_key in VALUE_KEYS.items():
        for index, entry in enumerate(_list(message.get(class_key, []), class_key)):
            where = f'{class_key}[{index}]'
            mrid = _required(entry, 'mRID', where)
            items = _list(_required(entry, values_key, where), f'{where}.{values_key}')
            reading = {'class': class_key}
            for key, field in entry.items():
                if key not in ('mRID', values_key):
                    reading[key] = _plain(field, f'{where}.{key}')
            values = [_reading_value(item, f'{where}.{values_key}[{number}]')
                      for number, item in enumerate(items)]

            if mrid not in readings:
                readings[mrid] = {**reading, 'values': values}
                continue
            previous = {key: field for key, field in readings[mrid].items() if key != 'values'}
            if previous != reading:
                raise ValueError(f'{where} lists measurement {mrid} again, with other '
                                 f'attributes: {reading} and {previous}')
            readings[mrid]['values'].extend(values)
    return readings
