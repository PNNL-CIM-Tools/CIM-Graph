"""Measurement value streams (cimgraph.updaters.measurement_json).

The writer builds the CIM4NoUtility payload from AnalogValue / DiscreteValue objects, and
the reader gives back every value with its time, source and unit attributes, so values
read and written again give the same message.
"""
import json

import cimprofiles.cim17.cim17v40 as cim
import pytest

from cimgraph.updaters.measurement_json import read_measurement_stream, write_measurement_stream

CIM = 'http://iec.ch/TC57/CIM100#'
ANALOG = '56f7f828-73d8-405a-a725-4dfbe88c371d'
TERMINAL = '83bf6035-97b6-4433-b5f9-bb455444a983'
SOURCE = 'b1a076df-b20d-490d-81a5-6e55efbf403c'
DISCRETE = '0d7c2f54-3d0b-4b41-9a8e-6f1c2b3a4d5e'
SWITCH = '9e8d7c6b-5a49-4382-a1b0-c9d8e7f6a5b4'

# Telemark-120/Schedule/2022/03/30/20220330T230000Z_Analog_ActivePower_2.json of CIM4NoUtility
CIM4NOUTILITY_ACTIVE_POWER = {'Analog': [{
    'mRID': ANALOG, 'name': 'ENGENE TotW AN7', 'measurementType': 'ThreePhaseActivePower',
    'phases': f'{CIM}PhaseCode.ABC', 'unitMultiplier': f'{CIM}UnitMultiplier.k',
    'unitSymbol': f'{CIM}UnitSymbol.W', 'ACDCTerminal': {'mRID': TERMINAL},
    'AnalogValues': [
        {'value': 10.1, 'timeStamp': '2022-03-30T12:45:39.393725Z', 'sensorAccuracy': 97.2,
         'MeasurementValueSource': {'mRID': SOURCE}},
        {'value': 10.3, 'timeStamp': '2022-03-30T13:45:39.393725Z', 'sensorAccuracy': 97.2,
         'MeasurementValueSource': {'mRID': SOURCE}},
    ]}]}


@pytest.fixture
def register():
    """The CIM4NoUtility active power Analog and a switch position Discrete."""
    source = cim.MeasurementValueSource(mRID=SOURCE)
    analog = cim.Analog(mRID=ANALOG, name='ENGENE TotW AN7', measurementType='ThreePhaseActivePower',
                        phases=cim.PhaseCode.ABC, unitMultiplier=cim.UnitMultiplier.k,
                        unitSymbol=cim.UnitSymbol.W, Terminal=cim.Terminal(mRID=TERMINAL))
    discrete = cim.Discrete(mRID=DISCRETE, name='T1E SWITCH POSITION', measurementType='SwitchPosition',
                            maxValue=3, minValue=0, normalValue=0,
                            PowerSystemResource=cim.Breaker(mRID=SWITCH))
    return source, analog, discrete


def _analog_values(analog, source):
    return [cim.AnalogValue(Analog=analog, value=value, timeStamp=time, sensorAccuracy=97.2,
                            MeasurementValueSource=source)
            for value, time in ((10.1, '2022-03-30T12:45:39.393725Z'), (10.3, '2022-03-30T13:45:39.393725Z'))]


def _values_from(readings, measurements, sources):
    """Measurement value objects from read readings: what applying them to the register does."""
    values = []
    for mrid, reading in readings.items():
        value_class = cim.AnalogValue if reading['class'] == 'Analog' else cim.DiscreteValue
        for item in reading['values']:
            value = value_class(value=item['value'], timeStamp=item['timeStamp'],
                                sensorAccuracy=item.get('sensorAccuracy'),
                                MeasurementValueSource=sources.get(item.get('MeasurementValueSource')))
            setattr(value, reading['class'], measurements[mrid])
            values.append(value)
    return values


def test_writes_the_cim4noutility_payload(register):
    source, analog, _ = register
    assert write_measurement_stream(_analog_values(analog, source)) == CIM4NOUTILITY_ACTIVE_POWER


def test_reads_the_cim4noutility_payload():
    reading = read_measurement_stream(CIM4NOUTILITY_ACTIVE_POWER)[ANALOG]
    assert reading['class'] == 'Analog'
    assert reading['unitMultiplier'] == f'{CIM}UnitMultiplier.k'
    assert reading['ACDCTerminal'] == TERMINAL
    assert reading['values'][0] == {'value': 10.1, 'timeStamp': '2022-03-30T12:45:39.393725Z',
                                    'sensorAccuracy': 97.2, 'MeasurementValueSource': SOURCE}


def test_write_read_write_is_byte_identical(register):
    source, analog, discrete = register
    switch = cim.DiscreteValue(Discrete=discrete, value=0)
    first = write_measurement_stream([*_analog_values(analog, source), switch],
                                     timestamp='2026-11-23T10:00:00Z', source=source)
    readings = read_measurement_stream(json.loads(json.dumps(first)))
    again = write_measurement_stream(_values_from(readings, {ANALOG: analog, DISCRETE: discrete},
                                                  {SOURCE: source}))
    assert json.dumps(again) == json.dumps(first)
    assert first['Discrete'][0]['PowerSystemResources'] == {'mRID': SWITCH}
    assert first['Discrete'][0]['DiscreteValues'] == [
        {'value': 0, 'timeStamp': '2026-11-23T10:00:00Z', 'MeasurementValueSource': {'mRID': SOURCE}}]


def test_a_unit_value_is_converted_to_its_analogs_unit(register):
    _, analog, _ = register
    analog.unitMultiplier = cim.UnitMultiplier.M
    value = cim.AnalogValue(Analog=analog, value=cim.ActivePower(10.1, 'kW'), timeStamp='t')
    assert write_measurement_stream([value])['Analog'][0]['AnalogValues'][0]['value'] == pytest.approx(0.0101)

    analog.unitSymbol = None
    with pytest.raises(ValueError, match='no unitSymbol'):
        write_measurement_stream([value])


@pytest.mark.parametrize('value, error', [
    (cim.AnalogValue(value=1.0, timeStamp='t'), 'has no Analog'),
    (cim.AnalogValue(Analog=cim.Analog(), timeStamp='t'), 'has no value'),
    (cim.DiscreteValue(Discrete=cim.Discrete(), value=1), 'has no timeStamp'),
])
def test_write_raises_on_a_value_it_cannot_carry(value, error):
    with pytest.raises(ValueError, match=error):
        write_measurement_stream([value])


def test_write_raises_on_no_values_or_another_class():
    with pytest.raises(ValueError, match='No measurement values'):
        write_measurement_stream([])
    with pytest.raises(TypeError, match='not an AnalogValue or DiscreteValue'):
        write_measurement_stream([cim.AccumulatorValue(value=1)])


@pytest.mark.parametrize('message, error', [
    ({}, 'No Analog or Discrete'),
    ({'Analog': [], 'Accumulator': []}, 'Unknown keys'),
    ({'Analog': [{'AnalogValues': []}]}, r"Analog\[0\] has no 'mRID'"),
    ({'Analog': [{'mRID': ANALOG}]}, "has no 'AnalogValues'"),
    ({'Discrete': [{'mRID': DISCRETE, 'DiscreteValues': [{'value': 1}]}]}, "has no 'timeStamp'"),
    ({'Analog': [{'mRID': ANALOG, 'AnalogValues': [{'timeStamp': 't'}]}]}, "has no 'value'"),
    ({'Analog': {'mRID': ANALOG}}, 'is not a list'),
])
def test_read_raises_on_a_message_it_cannot_read(message, error):
    with pytest.raises(ValueError, match=error):
        read_measurement_stream(message)


def test_a_measurement_listed_twice_has_its_values_joined():
    first, second = (CIM4NOUTILITY_ACTIVE_POWER['Analog'][0] | {'AnalogValues': [value]}
                     for value in CIM4NOUTILITY_ACTIVE_POWER['Analog'][0]['AnalogValues'])
    readings = read_measurement_stream({'Analog': [first, second]})
    assert [value['value'] for value in readings[ANALOG]['values']] == [10.1, 10.3]
    with pytest.raises(ValueError, match='again, with other attributes'):
        read_measurement_stream({'Analog': [first, second | {'name': 'other'}]})
