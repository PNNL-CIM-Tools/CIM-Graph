"""Measurement values applied to a model (cimgraph.updaters.measurement_updater).

The rules these tests pin: each measurementType reaches the field CIMHub's getters read
and its state variable. A node voltage is reached through Terminal.TopologicalNode (a node
is no PowerSystemResource), and a machine's power goes to the machine and its terminal's
SvPowerFlow. Each owner keeps one balanced state variable. A stream that does not fit the
model changes nothing, and one that does is recorded in model.incrementals.
"""
import json
from types import SimpleNamespace

import cimprofiles.cim18.cim18v17 as cim
import pytest

from cimgraph.core import get_cim_profile
from cimgraph.models import BusBranchModel
from cimgraph.updaters.incremental_builder import new_differences
from cimgraph.updaters.measurement_json import (
    read_measurement_stream,
    write_measurement_stream,
)
from cimgraph.updaters.measurement_updater import apply_measurements

TIME = '2026-11-24T10:00:00Z'


@pytest.fixture
def grid(monkeypatch):
    """A busbar's node, a machine on another node, a line, a load, a tap changer and a
    breaker, each with its measurements."""
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cim18v17')
    get_cim_profile.cache_clear()
    network = BusBranchModel(connection=None, container=cim.Feeder(mRID='fdr'), distributed=False)
    get_cim_profile.cache_clear()

    bus_node, machine_node = cim.TopologicalNode(mRID='TN1'), cim.TopologicalNode(mRID='TN2')
    busbar = cim.BusbarSection(mRID='BB1')
    busbar_terminal = cim.Terminal(mRID='BB1_T1', ConductingEquipment=busbar, TopologicalNode=bus_node)
    machine = cim.SynchronousMachine(mRID='GEN1', p=cim.ActivePower(0, 'MW'), q=cim.ReactivePower(0, 'MVAr'))
    machine_terminal = cim.Terminal(mRID='GEN1_T1', ConductingEquipment=machine, TopologicalNode=machine_node)
    line = cim.ACLineSegment(mRID='LINE1')
    line_terminal = cim.Terminal(mRID='LINE1_T1', ConductingEquipment=line, TopologicalNode=bus_node)
    load = cim.EnergyConsumer(mRID='LOAD1', p=cim.ActivePower(1, 'MW'), q=cim.ReactivePower(0, 'MVAr'))
    tap = cim.RatioTapChanger(mRID='RTC1', step=0.0)
    breaker = cim.Breaker(mRID='BR1', open=False)
    battery = cim.BatteryUnit(mRID='BAT1', ratedE=cim.RealEnergy(2400, 'MWh'))

    def analog(mrid, measurement_type, unit_multiplier, unit_symbol, **links):
        return cim.Analog(mRID=mrid, measurementType=measurement_type, unitMultiplier=unit_multiplier,
                          unitSymbol=unit_symbol, **links)

    at_bus = {'PowerSystemResource': busbar, 'Terminal': busbar_terminal}
    at_machine = {'PowerSystemResource': machine, 'Terminal': machine_terminal}
    at_line = {'PowerSystemResource': line, 'Terminal': line_terminal}
    objects = SimpleNamespace(
        network=network, bus_node=bus_node, machine_node=machine_node, busbar=busbar,
        machine=machine, machine_terminal=machine_terminal, line_terminal=line_terminal,
        load=load, tap=tap, breaker=breaker, battery=battery,
        voltage=analog('TN1_V', 'PhaseVoltage', cim.UnitMultiplier.k, cim.UnitSymbol.V, **at_bus),
        angle=analog('TN1_A', 'Angle', cim.UnitMultiplier.none, cim.UnitSymbol.deg, **at_bus),
        machine_p=analog('GEN1_P', 'ThreePhaseActivePower', cim.UnitMultiplier.M, cim.UnitSymbol.W, **at_machine),
        machine_q=analog('GEN1_Q', 'ThreePhaseReactivePower', cim.UnitMultiplier.M, cim.UnitSymbol.VAr,
                         **at_machine),
        line_p=analog('LINE1_P', 'ThreePhaseActivePower', cim.UnitMultiplier.M, cim.UnitSymbol.W, **at_line),
        line_q=analog('LINE1_Q', 'ThreePhaseReactivePower', cim.UnitMultiplier.M, cim.UnitSymbol.VAr, **at_line),
        load_p=analog('LOAD1_P', 'ThreePhaseActivePower', cim.UnitMultiplier.k, cim.UnitSymbol.W,
                      PowerSystemResource=load),
        tap_position=analog('RTC1_TAP', 'TapPosition', None, cim.UnitSymbol.none, PowerSystemResource=tap),
        state_of_charge=analog('BAT1_SOC', 'StateOfCharge', None, cim.UnitSymbol.none, PowerSystemResource=battery),
        switch_position=cim.Discrete(mRID='BR1_POS', measurementType='SwitchPosition', PowerSystemResource=breaker),
    )
    for obj in (*vars(objects).values(), busbar_terminal, line):
        if obj is not network:
            network.add_to_graph(obj)
    return objects


def _readings(*measured, time=TIME):
    """The readings of a written and read stream of (measurement, value) pairs."""
    values = []
    for measurement, value in measured:
        if isinstance(measurement, cim.Analog):
            values.append(cim.AnalogValue(Analog=measurement, value=value))
        else:
            values.append(cim.DiscreteValue(Discrete=measurement, value=value))
    return read_measurement_stream(json.loads(json.dumps(write_measurement_stream(values, timestamp=time))))


def _balanced(owner, state_class):
    """The owner's one balanced state variable, as get_node_voltage
    (cimhub_core.getters.voltage) requires of a node's SvVoltage."""
    states = getattr(owner, state_class)
    states = states if isinstance(states, list) else [states]
    balanced = [state for state in states if getattr(state, 'phase', None) is None]
    assert len(balanced) == 1
    return balanced[0]


def test_a_machines_power_goes_to_the_machine_and_its_terminal_not_its_node(grid):
    changed = apply_measurements(grid.network, _readings((grid.machine_p, 50), (grid.machine_q, -10)))
    flow = _balanced(grid.machine_terminal, 'SvPowerFlow')
    assert grid.machine.p.to('MW') == pytest.approx(50)
    assert grid.machine.q.to('MVAr') == pytest.approx(-10)
    assert (flow.p.to('MW'), flow.q.to('MVAr')) == (pytest.approx(50), pytest.approx(-10))
    assert grid.machine_node.SvVoltage == []
    assert changed == [grid.machine, flow]
    # Written through model.modify and create: the compiled stream is also a difference
    forward = grid.network.incrementals['forwardDifferences']
    assert {'p', 'q'} <= set(forward[cim.SynchronousMachine][grid.machine.uri()])
    assert {'p', 'q', 'Terminal'} <= set(forward[cim.SvPowerFlow][flow.uri()])


def test_a_node_voltage_reaches_the_node_through_its_terminal(grid):
    readings = _readings((grid.voltage, 115.2), (grid.angle, -3.5))
    (state,) = apply_measurements(grid.network, readings)
    assert _balanced(grid.bus_node, 'SvVoltage') is state
    assert state.TopologicalNode is grid.bus_node
    assert state.v.to('kV') == pytest.approx(115.2)
    assert state.angle.to('deg') == pytest.approx(-3.5)

    # Applied again, the voltage modifies the node's SvVoltage rather than adding one
    apply_measurements(grid.network, _readings((grid.voltage, 116.0), time='2026-11-24T10:00:01Z'))
    assert _balanced(grid.bus_node, 'SvVoltage') is state
    assert state.v.to('kV') == pytest.approx(116.0)


def test_a_line_flow_has_only_its_terminals_sv_power_flow(grid):
    (flow,) = apply_measurements(grid.network, _readings((grid.line_p, -80), (grid.line_q, 12)))
    assert flow is _balanced(grid.line_terminal, 'SvPowerFlow')
    assert flow.Terminal is grid.line_terminal
    assert (flow.p.to('MW'), flow.q.to('MVAr')) == (pytest.approx(-80), pytest.approx(12))


def test_load_tap_and_switch_values_go_to_the_equipment_and_its_state(grid):
    apply_measurements(grid.network, _readings((grid.load_p, 2500), (grid.tap_position, 5),
                                               (grid.switch_position, 1)))
    assert grid.load.p.to('MW') == pytest.approx(2.5)
    assert grid.load.SvStatus == []  # no measurement says whether it is in service
    assert grid.tap.step == 5.0
    assert grid.tap.SvTapStep.position == 5.0
    assert grid.breaker.open is True
    switch_state = _balanced(grid.breaker, 'SvSwitch')
    assert switch_state.open is True

    apply_measurements(grid.network, _readings((grid.switch_position, 0)))
    assert grid.breaker.open is False
    assert _balanced(grid.breaker, 'SvSwitch') is switch_state
    assert switch_state.open is False


def test_a_state_of_charge_is_a_fraction_of_the_rated_energy(grid):
    (battery,) = apply_measurements(grid.network, _readings((grid.state_of_charge, 0.5)))
    assert battery is grid.battery
    assert battery.storedE.to('MWh') == pytest.approx(1200)


def test_the_latest_value_of_a_measurement_is_applied(grid):
    values = [cim.AnalogValue(Analog=grid.machine_p, value=value, timeStamp=time)
              for value, time in ((40, '2026-11-24T10:00:02Z'), (30, '2026-11-24T10:00:01Z'))]
    apply_measurements(grid.network, read_measurement_stream(write_measurement_stream(values)))
    assert grid.machine.p.to('MW') == pytest.approx(40)


def test_a_measurement_is_found_by_its_identifier_not_its_mrid(grid):
    identified = cim.Analog(identifier='6f0b4c1e-2d3a-4b5c-8d9e-0a1b2c3d4e5f', mRID='GEN1 P (SCADA)',
                            measurementType='ThreePhaseActivePower', unitMultiplier=cim.UnitMultiplier.M,
                            unitSymbol=cim.UnitSymbol.W, PowerSystemResource=grid.machine)
    grid.network.add_to_graph(identified)
    readings = _readings((identified, 20))
    assert list(readings) == ['6f0b4c1e-2d3a-4b5c-8d9e-0a1b2c3d4e5f']
    apply_measurements(grid.network, readings)
    assert grid.machine.p.to('MW') == pytest.approx(20)


def _unknown(grid):
    readings = _readings((grid.machine_p, 50), (grid.voltage, 115.2))
    readings['00000000-0000-4000-8000-000000000000'] = readings.pop(grid.voltage.uri())
    return readings


def _other_unit(grid):
    readings = _readings((grid.machine_p, 50))
    reading = readings[grid.machine_p.uri()]
    reading['unitMultiplier'] = reading['unitMultiplier'].replace('UnitMultiplier.M', 'UnitMultiplier.k')
    return readings


def _two_for_one_attribute(grid):
    other = cim.Analog(mRID='GEN1_P2', measurementType='ThreePhaseActivePower', unitMultiplier=cim.UnitMultiplier.M,
                       unitSymbol=cim.UnitSymbol.W, PowerSystemResource=grid.machine)
    grid.network.add_to_graph(other)
    return _readings((grid.machine_p, 50), (other, 51))


def _phase_loads(grid):
    phase = cim.EnergyConsumerPhase(EnergyConsumer=grid.load, p=cim.ActivePower(1, 'MW'))
    grid.load.EnergyConsumerPhase.append(phase)
    grid.network.add_to_graph(phase)
    return _readings((grid.machine_p, 50), (grid.load_p, 2500))


def _unbalanced(grid):
    grid.line_p.phases = cim.PhaseCode.A
    return _readings((grid.machine_p, 50), (grid.line_p, 1))


def _no_rated_energy(grid):
    grid.battery.ratedE = None
    return _readings((grid.machine_p, 50), (grid.state_of_charge, 0.5))


def _swapped_type(grid, measurement, measurement_type):
    measurement.measurementType = measurement_type
    return _readings((grid.machine_p, 50), (measurement, 1))


@pytest.mark.parametrize('readings, error', [
    (_unknown, '00000000-0000-4000-8000-000000000000 is not in the model'),
    (lambda grid: _readings((grid.machine_p, 50), (grid.angle, -3.5)), 'no v to create one'),
    (lambda grid: _readings((grid.machine_p, 50), (grid.switch_position, 2)), r'is not 1 \(open\) or 0'),
    (_other_unit, 'unitMultiplier is .* in the stream but .* in the model'),
    (_unbalanced, 'measures phases A'),
    (lambda grid: _swapped_type(grid, grid.tap_position, 'LineCurrent'), "'LineCurrent' has no target"),
    (lambda grid: _swapped_type(grid, grid.load_p, 'PhaseVoltage'), 'needs a Terminal with a TopologicalNode'),
    (lambda grid: _swapped_type(grid, grid.switch_position, 'ThreePhaseActivePower'), 'those are Analogs'),
    (lambda grid: _swapped_type(grid, grid.tap_position, 'SwitchPosition'), 'those are Discretes'),
    (lambda grid: _swapped_type(grid, grid.load_p, 'TapPosition'), 'measures EnergyConsumer .* needs a TapChanger'),
    (lambda grid: _swapped_type(grid, grid.tap_position, 'ThreePhaseActivePower'),
     'or a Terminal for its SvPowerFlow'),
    (lambda grid: _swapped_type(grid, grid.machine_q, 'PhaseVoltage'), 'is in MVAr, which is not a unit'),
    (lambda grid: _readings((grid.machine_p, 50), (grid.state_of_charge, 50)), 'is not a fraction from 0 to 1'),
    (_no_rated_energy, 'ratedE is None'),
    (lambda grid: _swapped_type(grid, grid.load_p, 'StateOfCharge'), 'needs a BatteryUnit'),
    (_two_for_one_attribute, 'and another measurement both set p of SynchronousMachine'),
    (_phase_loads, 'EnergyConsumerPhase with p or q'),
])
def test_a_stream_that_does_not_fit_raises_and_changes_nothing(grid, readings, error):
    readings = readings(grid)
    with pytest.raises(ValueError, match=error):
        apply_measurements(grid.network, readings)
    # GEN1_P comes first in each stream: nothing of it may be applied either
    assert grid.machine.p.to('MW') == 0
    assert grid.machine_terminal.SvPowerFlow == []
    assert grid.bus_node.SvVoltage == []
    assert grid.network.incrementals == new_differences()
