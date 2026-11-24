"""Measurement values applied to a model, as ``apply_incremental`` applies a difference.

:func:`apply_measurements` writes each measurement's latest value into the CIM fields that
hold a model's state: the fields CIMHub's exporters read, and the state variable (Sv)
object of the measured node, terminal, tap changer or switch. It writes through
``model.modify`` and ``model.create``, so ``model.incrementals`` records the change: a
measurement stream applied to a model also gives a difference message, and the two are
views of one change.

**Identifiers.** The readings (from ``read_measurement_stream``) are keyed by the payload's
``mRID``. That is CIM4NoUtility's name for the key, but its value is the measurement's
``identifier`` (its ``uri()``, as ``write_measurement_stream`` writes it), and the
measurement is looked up by identifier. A measurement whose ``mRID`` differs from its
identifier is found by its identifier, never by its ``mRID``. The references in a reading
(``PowerSystemResources``, ``ACDCTerminal``) are identifiers too.

**Targets.** By the model's ``measurementType`` of the measurement:

======================== ======== ================================= ================================
measurementType          class    equipment (read by cimhub_core)   state variable
======================== ======== ================================= ================================
PhaseVoltage             Analog   none                              SvVoltage.v of
                                                                    Terminal.TopologicalNode
                                                                    (get_node_voltage)
Angle                    Analog   none                              SvVoltage.angle, as PhaseVoltage
ThreePhaseActivePower    Analog   p of a RotatingMachine,           SvPowerFlow.p of the Terminal
                                  PowerElectronicsConnection or
                                  EnergyConsumer (get_der_output,
                                  get_phase_loads)
ThreePhaseReactivePower  Analog   q, as ThreePhaseActivePower       SvPowerFlow.q of the Terminal
TapPosition              Analog   TapChanger.step (get_tap_steps)   SvTapStep.position
SwitchPosition           Discrete Switch.open (get_switch_state)    SvSwitch.open
StateOfCharge            Analog   BatteryUnit.storedE, derived      none
                                  (get_battery_unit)
======================== ======== ================================= ================================

The equipment fields come first, because CIMHub's exporters read a machine's or load's power
from its own ``p`` and ``q``, a tap from ``step`` and a switch from ``open``. Node voltage has
no equipment field: they read it from the SvVoltage. The other state variables hold the same
value for the readers that take a model's state from them.

- **Node voltage.** A TopologicalNode is not a PowerSystemResource, so a node voltage
  measurement names its node through its Terminal (that of a BusbarSection at the node),
  never through its PowerSystemResource. The value is written to ``v`` as measured, and the
  getters read ``v`` as the line-to-line magnitude.
- **Power.** It is in CIM's sign, positive into the equipment, as the equipment's ``p`` and
  ``q`` and SvPowerFlow are. A measurement on other equipment (a line or transformer
  terminal) has only its SvPowerFlow, so it needs a Terminal. A machine's or load's
  measurement without one has only the equipment field. Equipment whose phases
  (EnergyConsumerPhase, PowerElectronicsConnectionPhase) hold p or q is refused, because a
  new total would contradict them.
- **SwitchPosition.** It is whether the switch is open: 1 (true) is open and 0 (false) is
  closed, as the stream's producers write a switch's open flag. Other values raise.
- **StateOfCharge.** It is a fraction from 0 to 1, and ``storedE`` is that fraction of the
  battery's ``ratedE``. This is the one derived value here, and the relation is an
  assumption: the source (PSM) states a state of charge, not a stored energy. A battery
  without a positive ``ratedE`` raises, rather than getting a storedE from no rating.
- **Balanced only.** A measurement's ``phases`` must be None, ABC or ABCN. Its state variable
  is the owner's one balanced object (``phase`` None), which is created when the owner has
  none. A node's SvVoltage is created only with its ``v``, which get_node_voltage requires,
  so an ``Angle`` alone cannot create one.

**Units.** An Analog value is in its measurement's unitMultiplier and unitSymbol ('kV').
It is converted by the target attribute's CIMUnit class. A TapPosition is a position and
has no unit.

**Values.** A measurement's latest value, by timeStamp, is applied. The earlier values in
the message are superseded.

SvStatus and SvInjection are not written: no measurementType gives a piece of equipment's
in-service status or a node's injection.
"""

from __future__ import annotations

from datetime import datetime

from cimprofiles.identity import Identity
from cimprofiles.units import CIMUnit
from pint.errors import DimensionalityError

from cimgraph.core.attribute_utils import get_attr_datatype, validate_attr_datatype
from cimgraph.updaters.incremental_builder import _find_object
from cimgraph.updaters.measurement_json import (
    MEASUREMENT_ATTRIBUTES,
    _entry,
    _measurement_unit,
    _plain,
)

__all__ = [
    'apply_measurements',
]

POWER_EQUIPMENT = ('RotatingMachine', 'PowerElectronicsConnection', 'EnergyConsumer')
# measurementType: (measurement class, equipment classes, equipment attribute,
#                   state variable class, its attribute)
TARGETS = {
    'PhaseVoltage': ('Analog', (), None, 'SvVoltage', 'v'),
    'Angle': ('Analog', (), None, 'SvVoltage', 'angle'),
    'ThreePhaseActivePower': ('Analog', POWER_EQUIPMENT, 'p', 'SvPowerFlow', 'p'),
    'ThreePhaseReactivePower': ('Analog', POWER_EQUIPMENT, 'q', 'SvPowerFlow', 'q'),
    'TapPosition': ('Analog', ('TapChanger',), 'step', 'SvTapStep', 'position'),
    'SwitchPosition': ('Discrete', ('Switch',), 'open', 'SvSwitch', 'open'),
    'StateOfCharge': ('Analog', ('BatteryUnit',), 'storedE', None, None),
}
# A state variable class: its reference to its owner. The owner's inverse is named as the class.
STATE_OWNERS = {'SvVoltage': 'TopologicalNode', 'SvPowerFlow': 'Terminal',
                'SvTapStep': 'TapChanger', 'SvSwitch': 'Switch'}
# The attributes a created state variable must have: get_node_voltage requires v
STATE_REQUIRED = {'SvVoltage': ('v',)}
# The PhaseCode names of a balanced measurement (None: no phases given)
BALANCED_PHASES = (None, 'ABC', 'ABCN')
# The power equipment classes with per-phase children that hold p and q
PHASE_CHILDREN = {'EnergyConsumer': 'EnergyConsumerPhase',
                  'PowerElectronicsConnection': 'PowerElectronicsConnectionPhase'}
# SwitchPosition: Switch.open
SWITCH_OPEN = {1: True, 0: False}


def _is_a(obj, class_names: tuple[str, ...]) -> bool:
    """Whether obj is, or specializes, one of the classes."""
    return any(parent.__name__ in class_names for parent in type(obj).__mro__)


def _describe(obj) -> str:
    return f'{type(obj).__name__} {obj.uri()}'


def _measurement(model, objects: dict, identifier: str, reading: dict) -> Identity:
    """The reading's measurement in the model. Every attribute the reading carries must be the model's."""
    measurement = _find_object(model, objects, identifier)
    if not _is_a(measurement, (reading['class'],)):
        raise ValueError(f'The stream lists {identifier} under {reading["class"]}, but it is a '
                         f'{type(measurement).__name__}')
    in_model = {key: _plain(value, key)
                for key, value in _entry(measurement, MEASUREMENT_ATTRIBUTES).items()}
    for key, value in reading.items():
        if key not in ('class', 'values') and in_model.get(key) != value:
            raise ValueError(f'{_describe(measurement)} {key} is {value!r} in the stream but '
                             f'{in_model.get(key)!r} in the model')
    phases = getattr(measurement.phases, 'name', None)
    if phases not in BALANCED_PHASES:
        raise ValueError(f'{_describe(measurement)} measures phases {phases}; only a balanced '
                         f'measurement (phases None, ABC or ABCN) is applied')
    return measurement


def _time(text: str) -> datetime:
    # datetime.fromisoformat reads a 'Z' suffix only from Python 3.11
    return datetime.fromisoformat(text[:-1] + '+00:00' if text.endswith('Z') else text)


def _latest_value(measurement, values: list[dict]) -> object:
    if not values:
        raise ValueError(f'{_describe(measurement)} has no values in the stream')
    return max(values, key=lambda item: _time(item['timeStamp']))['value']


def _equipment(measurement, equipment_classes: tuple[str, ...]) -> Identity | None:
    """The measurement's PowerSystemResource if it is one of the equipment classes, else None."""
    equipment = measurement.PowerSystemResource
    if not _is_a(equipment, equipment_classes):
        return None
    for class_name, children in PHASE_CHILDREN.items():
        if _is_a(equipment, (class_name,)) and any(child.p is not None or child.q is not None
                                                   for child in getattr(equipment, children)):
            raise ValueError(f'{_describe(equipment)} has {children} with p or q, which its '
                             f'three-phase total from {_describe(measurement)} would contradict')
    return equipment


def _state_owner(measurement, state_class: str, equipment: Identity | None) -> Identity | None:
    """The object whose state variable the measurement's value is: the node of its Terminal
    (SvVoltage), its Terminal (SvPowerFlow) or its equipment. None if it has none."""
    if state_class is None:
        return None
    terminal = measurement.Terminal
    if state_class == 'SvVoltage':
        return getattr(terminal, 'TopologicalNode', None)
    if state_class == 'SvPowerFlow':
        return terminal if _is_a(terminal, ('Terminal',)) else None
    return equipment


def _target_value(model, measurement, target_class: type, attribute: str, value: object) -> object:
    """A measured value as the target attribute's datatype."""
    if attribute == 'open':
        if isinstance(value, bool) or value not in SWITCH_OPEN:
            raise ValueError(f'{_describe(measurement)} SwitchPosition {value!r} is not 1 (open) '
                             f'or 0 (closed)')
        return SWITCH_OPEN[value]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f'{_describe(measurement)} value {value!r} is not a number')

    (datatype,) = get_attr_datatype(target_class, attribute)
    unit_class = getattr(model.cim, datatype, None)
    if isinstance(unit_class, type) and issubclass(unit_class, CIMUnit):
        unit = _measurement_unit(measurement)
        try:
            value = unit_class(value, unit)
        except DimensionalityError as error:
            raise ValueError(f'{_describe(measurement)} is in {unit}, which is not a unit of '
                             f'{target_class.__name__}.{attribute} ({datatype})') from error
    valid, _, value = validate_attr_datatype(target_class, attribute, value)
    if not valid:
        raise ValueError(f'{_describe(measurement)} value {value!r} does not fit '
                         f'{target_class.__name__}.{attribute} ({datatype})')
    return value


def _stored_energy(measurement, battery, fraction: object) -> CIMUnit:
    """A StateOfCharge as BatteryUnit.storedE: that fraction of the battery's ratedE (module notes)."""
    if isinstance(fraction, bool) or not isinstance(fraction, (int, float)) or not 0 <= fraction <= 1:
        raise ValueError(f'{_describe(measurement)} StateOfCharge {fraction!r} is not a fraction '
                         f'from 0 to 1')
    rated = battery.ratedE
    if not isinstance(rated, CIMUnit) or rated.to('MWh') <= 0:
        raise ValueError(f'{_describe(battery)} ratedE is {rated!r}; its storedE from '
                         f'{_describe(measurement)} is a fraction of a positive ratedE')
    return type(rated)(fraction * rated.to('MWh'), 'MWh')


def _missing_target(measurement, equipment_classes: tuple[str, ...], state_class: str) -> ValueError:
    measured = measurement.PowerSystemResource
    measured = 'no PowerSystemResource' if measured is None else _describe(measured)
    if state_class == 'SvVoltage':
        needs = 'a Terminal with a TopologicalNode, whose SvVoltage its value is'
    elif state_class == 'SvPowerFlow':
        needs = f'a {" or ".join(equipment_classes)}, or a Terminal for its SvPowerFlow'
    else:
        needs = f'a {" or ".join(equipment_classes)}'
    return ValueError(f'{_describe(measurement)} ({measurement.measurementType}) measures '
                      f'{measured}; it needs {needs}')


def _add_change(changes: dict, key: tuple, value: object, measurement, target: str) -> None:
    if key in changes:
        raise ValueError(f'{_describe(measurement)} and another measurement both set {target}')
    changes[key] = value


def _balanced_state(owner, state_class: str, attributes: dict[str, object]) -> Identity | None:
    """The owner's one balanced state variable, or None if it has none and the attributes
    create one."""
    states = getattr(owner, state_class)
    states = [] if states is None else states if isinstance(states, list) else [states]
    balanced = [state for state in states if getattr(state, 'phase', None) is None]
    if len(balanced) > 1:
        raise ValueError(f'{_describe(owner)} has {len(balanced)} balanced {state_class}s; it has one')
    missing = [name for name in STATE_REQUIRED.get(state_class, ()) if name not in attributes]
    if not balanced and missing:
        raise ValueError(f'{_describe(owner)} has no {state_class}, and the stream has no '
                         f'{" or ".join(missing)} to create one with')
    return balanced[0] if balanced else None


def apply_measurements(model, readings: dict) -> list[Identity]:
    """
    Apply measurement readings (from read_measurement_stream) to a GraphModel through its
    modify and create. Each measurement's latest value is written to its equipment field
    and its state variable (see the module notes). A state variable is created when its
    owner has none.

    Every reading is checked before any is applied. All of these raise ValueError and leave
    the model unchanged:

    - an unknown measurement identifier;
    - a measurement whose class or attributes in the stream are not the model's;
    - a measurementType with no target, or a measurement that reaches neither its
      equipment nor its state variable's owner;
    - a value that does not fit its target;
    - two measurements that set one attribute.

    Returns the modified and created objects.
    """
    objects = {}  # identifier -> object, for every measurement the readings name
    equipment_values = {}  # (equipment identifier, attribute) -> value
    state_values = {}  # (owner identifier, state class, attribute) -> value
    owners = {}  # identifier -> equipment or state variable owner
    for identifier, reading in readings.items():
        measurement = _measurement(model, objects, identifier, reading)
        if measurement.measurementType not in TARGETS:
            raise ValueError(f'{_describe(measurement)} measurementType {measurement.measurementType!r} '
                             f'has no target; those applied are {sorted(TARGETS)}')
        (class_name, equipment_classes, equipment_attribute,
         state_class, state_attribute) = TARGETS[measurement.measurementType]
        if not _is_a(measurement, (class_name,)):
            raise ValueError(f'{_describe(measurement)} cannot be a {measurement.measurementType}: '
                             f'those are {class_name}s')
        value = _latest_value(measurement, reading['values'])
        equipment = _equipment(measurement, equipment_classes)
        owner = _state_owner(measurement, state_class, equipment)
        if equipment is None and owner is None:
            raise _missing_target(measurement, equipment_classes, state_class)

        if equipment is not None:
            if equipment_attribute == 'storedE':
                converted = _stored_energy(measurement, equipment, value)
            else:
                converted = _target_value(model, measurement, type(equipment), equipment_attribute, value)
            _add_change(equipment_values, (equipment.uri(), equipment_attribute), converted, measurement,
                        f'{equipment_attribute} of {_describe(equipment)}')
            owners[equipment.uri()] = equipment
        if owner is not None:
            converted = _target_value(model, measurement, getattr(model.cim, state_class),
                                      state_attribute, value)
            _add_change(state_values, (owner.uri(), state_class, state_attribute), converted, measurement,
                        f'{state_class}.{state_attribute} of {_describe(owner)}')
            owners[owner.uri()] = owner

    states = {}  # (owner identifier, state class) -> {attribute: value}
    for (owner_uri, state_class, attribute), value in state_values.items():
        states.setdefault((owner_uri, state_class), {})[attribute] = value
    existing = {key: _balanced_state(owners[key[0]], key[1], attributes)
                for key, attributes in states.items()}

    changed = {}  # identifier -> object
    for (uri, attribute), value in equipment_values.items():
        model.modify(owners[uri], attribute, value)
        changed[uri] = owners[uri]
    for (owner_uri, state_class), attributes in states.items():
        state = existing[(owner_uri, state_class)]
        if state is None:
            state = model.create(getattr(model.cim, state_class),
                                 **{STATE_OWNERS[state_class]: owners[owner_uri]}, **attributes)
        else:
            for attribute, value in attributes.items():
                model.modify(state, attribute, value)
        changed[state.uri()] = state
    return list(changed.values())
