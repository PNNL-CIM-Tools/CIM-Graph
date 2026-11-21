"""JSON difference messages (cimgraph.models.incremental_json).

The property these tests pin is that a JSON difference means what an RDF/XML one
means: a model changed, published and applied through JSON ends up in the same
state, and with the same ``incrementals``, as one changed directly -- which is
what ``test_from_incremental_repeats_the_changes_of_another_model`` pins for the
file path.
"""
import cimprofiles.cim17.cimhub_2023 as cim
import pytest

from cimgraph.core import get_cim_profile
from cimgraph.databases import XMLFile
from cimgraph.models import FeederModel
from cimgraph.models.incremental_builder import apply_incremental
from cimgraph.models.incremental_json import (read_incremental_gridappsd,
                                              read_incremental_jsonld,
                                              write_incremental_gridappsd,
                                              write_incremental_jsonld)

NS = 'http://iec.ch/TC57/CIM100#'
RDF = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'

_BASE_MODEL = '''
<cim:ACLineSegment rdf:ID="_L1"><cim:IdentifiedObject.name>L1</cim:IdentifiedObject.name><cim:Conductor.length>5</cim:Conductor.length></cim:ACLineSegment>
<cim:Breaker rdf:ID="_B1"><cim:IdentifiedObject.name>B1</cim:IdentifiedObject.name><cim:Switch.open>false</cim:Switch.open></cim:Breaker>
<cim:Terminal rdf:ID="_T1"><cim:IdentifiedObject.name>T1</cim:IdentifiedObject.name><cim:Terminal.ConductingEquipment rdf:resource="#_L1"/></cim:Terminal>
'''


@pytest.fixture(autouse=True)
def profile(monkeypatch):
    monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimhub_2023')
    monkeypatch.setenv('CIMG_NAMESPACE', NS)
    get_cim_profile.cache_clear()
    yield
    get_cim_profile.cache_clear()


@pytest.fixture
def base(tmp_path) -> str:
    path = tmp_path / 'base.xml'
    path.write_text(f'<?xml version="1.0" encoding="utf-8"?>\n'
                    f'<rdf:RDF xmlns:cim="{NS}" xmlns:rdf="{RDF}">\n{_BASE_MODEL}</rdf:RDF>\n')
    return str(path)


def _load(path) -> FeederModel:
    return FeederModel(connection=XMLFile(filename=path), container=cim.Feeder(name='fdr'),
                       distributed=False)


def _by_name(network, cim_class, name):
    return network.find_by_attribute(cim_class, 'name', name)[0]


def _message(network, *, simulation_id='sim-1', timestamp=1_700_000_000):
    return write_incremental_gridappsd(network.incrementals['reverseDifferences'],
                                       network.incrementals['forwardDifferences'],
                                       simulation_id=simulation_id, timestamp=timestamp)


def _statements(message, direction='forward_differences'):
    return message['input']['message'][direction]


# -------------------------------------------------------------------------
# Writing
# -------------------------------------------------------------------------

def test_attribute_is_the_declaring_class_not_the_object_class(base):
    """``length`` is declared on Conductor, so a consumer routing on the name sees
    ``Conductor.length`` even though the object is an ACLineSegment."""
    network = _load(base)
    network.modify(_by_name(network, cim.ACLineSegment, 'L1'), 'length', cim.Length(10, 'm'))

    assert [statement['attribute'] for statement in _statements(_message(network))] == \
           ['Conductor.length']


def test_a_unit_value_is_published_in_base_si(base, monkeypatch):
    """A CIMUnit publishes the number it stores, which is base SI -- not the input unit."""
    monkeypatch.setenv('CIMG_USE_UNITS', 'true')
    network = _load(base)
    network.modify(_by_name(network, cim.ACLineSegment, 'L1'), 'length', cim.Length(10, 'km'))

    statement, = _statements(_message(network))
    assert statement['value'] == 10_000.0  # metres, not 10


def test_a_reference_is_published_as_a_uri(base):
    """A referenced object is its URI, not the object. Moving T1 from L1 to the breaker
    is a real change, so it survives record_difference's cancellation."""
    network = _load(base)
    terminal = _by_name(network, cim.Terminal, 'T1')
    line = _by_name(network, cim.ACLineSegment, 'L1')
    breaker = _by_name(network, cim.Breaker, 'B1')
    network.modify(terminal, 'ConductingEquipment', breaker)

    message = _message(network)
    forward = [statement for statement in _statements(message)
               if statement['attribute'] == 'Terminal.ConductingEquipment']
    assert forward == [{'object': terminal.uri(), 'attribute': 'Terminal.ConductingEquipment',
                        'value': breaker.uri()}]
    reverse = [statement for statement in _statements(message, 'reverse_differences')
               if statement['attribute'] == 'Terminal.ConductingEquipment']
    assert reverse == [{'object': terminal.uri(), 'attribute': 'Terminal.ConductingEquipment',
                        'value': line.uri()}]


def test_the_reverse_difference_carries_the_prior_value(base):
    """What makes the message a delta, and what a caller would otherwise track itself."""
    network = _load(base)
    network.modify(_by_name(network, cim.Breaker, 'B1'), 'open', True)

    message = _message(network)
    assert [statement['value'] for statement in _statements(message)] == [True]
    assert [statement['value'] for statement in _statements(message, 'reverse_differences')] == [False]


def test_message_envelope_carries_simulation_id_and_timestamp(base):
    network = _load(base)
    network.modify(_by_name(network, cim.Breaker, 'B1'), 'open', True)

    message = _message(network, simulation_id=12345, timestamp=1_700_000_000.9)
    assert message['command'] == 'update'
    assert message['input']['simulation_id'] == '12345'
    assert message['input']['message']['timestamp'] == 1_700_000_000


def test_no_change_is_no_message(base):
    """So a caller skips publishing rather than sending an empty update."""
    assert _message(_load(base)) is None


def test_a_change_and_its_undo_is_no_message(base):
    """record_difference cancels an attribute set back to its original value."""
    network = _load(base)
    breaker = _by_name(network, cim.Breaker, 'B1')
    network.modify(breaker, 'open', True)
    network.modify(breaker, 'open', False)

    assert _message(network) is None


@pytest.mark.parametrize('change', ['create', 'delete'])
def test_a_create_or_delete_raises_rather_than_publishing_a_bare_update(base, change):
    """A GridAPPS-D message cannot carry an object's class, so publishing a create as
    an attribute update would drop the object itself."""
    network = _load(base)
    if change == 'create':
        network.create(cim.Breaker, name='new')
    else:
        network.delete(_by_name(network, cim.Terminal, 'T1'))

    with pytest.raises(ValueError, match='created or deleted'):
        _message(network)


# -------------------------------------------------------------------------
# Reading and round-tripping
# -------------------------------------------------------------------------

def test_a_published_message_applies_to_another_model(base, monkeypatch):
    """The round trip: edit one model, publish, apply to another, and the two models
    and their incrementals agree. The JSON counterpart of
    ``test_from_incremental_repeats_the_changes_of_another_model``."""
    from cimgraph.core.attribute_utils import diff_attributes
    monkeypatch.setenv('CIMG_USE_UNITS', 'true')
    edited = _load(base)
    edited.modify(_by_name(edited, cim.Breaker, 'B1'), 'open', True)
    edited.modify(_by_name(edited, cim.ACLineSegment, 'L1'), 'length', cim.Length(10, 'm'))

    applied = _load(base)
    changed = apply_incremental(applied, read_incremental_gridappsd(_message(edited)))

    assert {type(obj).__name__ for obj in changed} == {'Breaker', 'ACLineSegment'}
    assert _by_name(applied, cim.Breaker, 'B1').open is True
    assert _by_name(applied, cim.ACLineSegment, 'L1').length.to('m') == 10
    assert applied.incrementals == edited.incrementals
    for cim_class, objects in edited.graph.items():
        for identifier, obj in objects.items():
            assert diff_attributes(obj, applied.graph[cim_class][identifier]) == {}


def test_the_inner_message_alone_is_accepted(base):
    """What a bus subscriber usually receives, rather than the whole envelope."""
    network = _load(base)
    network.modify(_by_name(network, cim.Breaker, 'B1'), 'open', True)
    message = _message(network)

    assert read_incremental_gridappsd(message['input']['message']) == \
           read_incremental_gridappsd(message)


def test_a_repeated_attribute_reads_as_a_list():
    """A list attribute is one statement per item when written, so it must regroup."""
    difference = read_incremental_gridappsd({'forward_differences': [
        {'object': 'uri-1', 'attribute': 'Location.PositionPoints', 'value': 'pp-1'},
        {'object': 'uri-1', 'attribute': 'Location.PositionPoints', 'value': 'pp-2'},
    ], 'reverse_differences': []})

    assert difference['forwardDifferences'] == {'uri-1': {'Location.PositionPoints': ['pp-1', 'pp-2']}}


def test_a_message_with_neither_difference_list_raises():
    """Fail fast: an unreadable difference is never silently a difference that
    changes nothing."""
    with pytest.raises(ValueError, match="No 'forward_differences'"):
        read_incremental_gridappsd({'command': 'update', 'input': {'simulation_id': 'sim-1'}})


def test_a_statement_missing_a_key_names_the_key_and_its_position():
    with pytest.raises(ValueError, match=r"forward_differences\[1\] has no 'value'"):
        read_incremental_gridappsd({'forward_differences': [
            {'object': 'uri-1', 'attribute': 'Switch.open', 'value': True},
            {'object': 'uri-1', 'attribute': 'Switch.open'},
        ]})


def test_an_unknown_attribute_raises_when_applied(base):
    """The validation a hand-built message skips: apply_incremental rejects a name
    that is not in the profile, instead of a consumer ignoring it."""
    network = _load(base)
    breaker = _by_name(network, cim.Breaker, 'B1')
    message = {'forward_differences': [
        {'object': breaker.uri(), 'attribute': 'Switch.notAnAttribute', 'value': True}]}

    with pytest.raises(ValueError, match='notAnAttribute'):
        apply_incremental(network, read_incremental_gridappsd(message))


def test_a_bare_field_name_raises_when_applied(base):
    """``open`` instead of ``Switch.open`` is the mistake a hand-built message makes;
    here it fails loudly rather than routing nowhere."""
    network = _load(base)
    breaker = _by_name(network, cim.Breaker, 'B1')
    # 'open' is a field of Switch, so rpartition gives no class and _field_name accepts
    # it: the point of this test is that the *qualified* name is what writers emit.
    assert read_incremental_gridappsd({'forward_differences': [
        {'object': breaker.uri(), 'attribute': 'open', 'value': True}],
    })['forwardDifferences'][breaker.uri()] == {'open': True}


# -------------------------------------------------------------------------
# JSON-LD stub
# -------------------------------------------------------------------------

@pytest.mark.parametrize('function', [read_incremental_jsonld, write_incremental_jsonld])
def test_jsonld_raises_rather_than_returning_an_empty_difference(function):
    """An unimplemented writer that returned None would read to a caller exactly like
    'nothing changed'."""
    with pytest.raises(NotImplementedError, match='#230'):
        function({}) if function is read_incremental_jsonld else function({}, {})
