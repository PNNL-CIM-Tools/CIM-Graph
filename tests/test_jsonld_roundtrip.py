"""JSON-LD in the CGMES draft style (#225): resolvable @context, QUDT unit vocabularies
named by dct:conformsTo, string references, and round trips through write_json_ld."""
import json
import math
import urllib.error
import urllib.request

import pytest
from cimprofiles.jsonld import profile_jsonld
from cimprofiles.units import CIMUnit

from cimgraph.core import get_cim_profile, get_model_authority
from cimgraph.core.attribute_utils import diff_attributes
from cimgraph.databases import JSONLDFile, XMLFile
from cimgraph.models import FeederModel, NodeBreakerModel
from cimgraph.utils import write_json_ld

CGMES_FILE = 'tests/test_models/cgmes_style_eq.jsonld'
IEEE13 = 'tests/test_models/ieee13.xml'
FEEDER_MRID = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'
CONTEXT_OLD = 'https://raw.githack.com/Sveino/Inst4CIM-KG/develop/rdf-improved/cim-context-old.jsonld'
EQ_VOCABULARY = 'http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0'
NORDIC44_EQ = ('https://raw.githubusercontent.com/statnett/Nordic44/main/instances/Grid/jsonld/'
               'Nordic44-HV_EQ.jsonld')
# ieee13.xml links one OperationalLimitSet to several terminals and nodes, but the profile
# allows one, so a written file keeps one link and the other ends' lists lose it (an
# XML -> XML round trip differs in exactly these attributes too)
AMBIGUOUS = {('OperationalLimitSet', 'Terminal'), ('OperationalLimitSet', 'ConnectivityNode'),
             ('Terminal', 'OperationalLimitSet'), ('ConnectivityNode', 'OperationalLimitSet')}


@pytest.fixture
def profile(monkeypatch):
    """Select a CIM profile for one test."""
    def use(name):
        monkeypatch.setenv('CIMG_CIM_PROFILE', name)
        monkeypatch.setenv('CIMG_USE_UNITS', 'true')
        get_cim_profile.cache_clear()
        return get_cim_profile()[1]
    yield use
    get_cim_profile.cache_clear()


def _read(path) -> NodeBreakerModel:
    return NodeBreakerModel(container=None, connection=JSONLDFile(str(path)), distributed=False)


def _only(network, cim_class):
    (obj,) = network.graph[cim_class].values()
    return obj


def _same(value, other) -> bool:
    """Equal values; unit values equal to float precision (unit conversion rounds)."""
    if isinstance(value, CIMUnit) and isinstance(other, CIMUnit):
        return math.isclose(float(value), float(other), rel_tol=1e-12, abs_tol=1e-15)
    return False


def _differences(network, expected) -> list[str]:
    differences = []
    for cim_class, objects in expected.graph.items():
        for identifier, expected_obj in objects.items():
            obj = network.graph.get(cim_class, {}).get(identifier)
            if obj is None:
                differences.append(f'{cim_class.__name__} {identifier} missing')
                continue
            for attribute, (value, expected_value) in diff_attributes(obj, expected_obj).items():
                if (cim_class.__name__, attribute) in AMBIGUOUS or _same(value, expected_value):
                    continue
                differences.append(f'{cim_class.__name__}.{attribute}: {value!r} != {expected_value!r}')
    return differences


def test_cgmes_style_file_reads_in_vocabulary_units(profile):
    cim = profile('cgmes_3_0_0')
    network = _read(CGMES_FILE)

    assert _only(network, cim.BaseVoltage).nominalVoltage.to('kV') == 420
    line = _only(network, cim.ACLineSegment)
    assert line.length.to('km') == 12.5
    assert line.r.to('ohm') == 3.1752
    assert line.BaseVoltage is _only(network, cim.BaseVoltage)
    assert line.normallyInService is True
    assert sorted(terminal.sequenceNumber for terminal in line.Terminals) == [1, 2]
    assert all(terminal.ConductingEquipment is line for terminal in line.Terminals)

    machine = _only(network, cim.SynchronousMachine)
    assert machine.ratedS.to('MVA') == 680
    assert machine.minQ.to('MVAr') == -500
    assert machine.type is cim.SynchronousMachineKind.generator
    assert machine.GeneratingUnit.maxOperatingP.to('MW') == 1050

    limit_type = _only(network, cim.OperationalLimitType)
    assert limit_type.direction is cim.OperationalLimitDirectionKind.high
    assert limit_type.kind is cim.LimitKind.tatl

    (header,) = network.connection.model_headers
    assert header.authority == 'https://github.com/PNNL-CIM-Tools/CIM-Graph/tests'
    assert header.full_model_uuid == '7b1e0c2a-1d3f-4b6e-9a51-000000000001'
    assert get_model_authority() == header.authority     # the file's scope, as for CIM XML


def test_cgmes_round_trip_keeps_cgmes_units(profile, tmp_path):
    profile('cgmes_3_0_0')
    network = _read(CGMES_FILE)
    path = tmp_path / 'eq.jsonld'
    write_json_ld(network, str(path))

    document = json.loads(path.read_text())    # the top-level map is the dcat:Dataset header
    assert document['@context'] == CONTEXT_OLD
    assert document['@type'] == ['dcat:Dataset', 'http://www.w3.org/2004/03/trix/rdfg-1/Graph']
    assert EQ_VOCABULARY in document['dct:conformsTo']
    assert document['dcat:distribution']['dct:conformsTo'] == document['dct:conformsTo']
    nodes = {node['@id']: node for node in document['@graph']}
    line = nodes['urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000020']
    assert line['cim:Conductor.length'] == '12.5'          # km, as in the source file
    assert line['cim:ConductingEquipment.BaseVoltage'] == 'urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000010'
    assert nodes['urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000010']['cim:BaseVoltage.nominalVoltage'] == '420'

    assert _differences(_read(path), network) == []


@pytest.mark.parametrize('convention, load_p', [('si', 'W'), ('distribution', 'kW')])
def test_distribution_round_trip_through_each_convention(profile, tmp_path, convention, load_p):
    cim = profile('cimhub_2023')
    xml_network = FeederModel(connection=XMLFile(filename=IEEE13),
                              container=cim.Feeder(mRID=FEEDER_MRID), distributed=False)
    path = tmp_path / f'ieee13-{convention}.jsonld'
    write_json_ld(xml_network, str(path), convention=convention)

    document = json.loads(path.read_text())
    assert document['dct:conformsTo'] == profile_jsonld('cimhub_2023')['conventions'][convention]
    load = next(iter(xml_network.graph[cim.EnergyConsumer].values()))
    written = next(node for node in document['@graph'] if node['@id'] == f'urn:uuid:{load.uri()}')
    assert float(written['cim:EnergyConsumer.p']) == pytest.approx(load.p.to(load_p))

    network = _read(path)
    assert sum(len(objects) for objects in network.graph.values()) > 400
    assert _differences(network, xml_network) == []


@pytest.mark.parametrize('name, convention, power_unit, length_unit', [
    ('cim18v17_distribution', 'distribution', 'kW', 'm'),
    ('cim18v17_transmission', 'transmission', 'MW', 'km'),
])
def test_cim18v17_flavor_round_trip(profile, tmp_path, name, convention, power_unit, length_unit):
    """Each cim18v17 flavor writes its own convention's units and reads them back."""
    cim = profile(name)
    network = NodeBreakerModel(container=None, connection=None, distributed=False)
    base_voltage = cim.BaseVoltage(mRID='bv', nominalVoltage=cim.Voltage(12.47, 'kV'))
    impedance = cim.PerLengthSequenceImpedance(mRID='z', r=cim.ResistancePerLength(0.0002153),
                                               bch=cim.SusceptancePerLength(3.2e-9))
    line = cim.ACLineSegment(mRID='line', BaseVoltage=base_voltage, length=cim.Length(1609, 'm'),
                             r=cim.Resistance(0.3, 'ohm'), PerLengthImpedance=impedance)
    load = cim.EnergyConsumer(mRID='load', BaseVoltage=base_voltage, p=cim.ActivePower(1.5, 'MW'))
    base_voltage.ConductingEquipment = [line, load]  # the reader links both ends
    impedance.ACLineSegments = [line]
    for obj in (base_voltage, impedance, line, load):
        network.add_to_graph(obj)
    path = tmp_path / f'{name}.jsonld'
    write_json_ld(network, str(path), convention=convention)

    nodes = {node['@id']: node for node in json.loads(path.read_text())['@graph']}
    written_load = nodes[f'urn:uuid:{load.uri()}']
    written_line = nodes[f'urn:uuid:{line.uri()}']
    assert float(written_load['cim:EnergyConsumer.p']) == pytest.approx(load.p.to(power_unit))
    assert float(written_line['cim:Conductor.length']) == pytest.approx(line.length.to(length_unit))
    written_impedance = nodes[f'urn:uuid:{impedance.uri()}']   # line constants per km in both
    assert written_impedance['cim:PerLengthSequenceImpedance.r'] == '0.2153'
    assert written_impedance['cim:PerLengthSequenceImpedance.bch'] == '3.2'
    assert _differences(_read(path), network) == []


def test_units_survive_a_tool_that_drops_the_distribution(profile, tmp_path):
    """KGraphPy's header validation removes dcat:distribution; the Dataset's conformsTo remains."""
    cim = profile('cimhub_2023')
    xml_network = FeederModel(connection=XMLFile(filename=IEEE13),
                              container=cim.Feeder(mRID=FEEDER_MRID), distributed=False)
    path = tmp_path / 'ieee13-distribution.jsonld'
    write_json_ld(xml_network, str(path), convention='distribution')
    document = json.loads(path.read_text())
    del document['dcat:distribution']
    path.write_text(json.dumps(document))
    assert _differences(_read(path), xml_network) == []


def test_files_with_different_units_fail_together(profile, tmp_path):
    profile('cgmes_3_0_0')
    si_file = tmp_path / 'si.jsonld'
    document = json.loads(open(CGMES_FILE).read())
    document['@graph'][0]['dct:conformsTo'] = profile_jsonld('cimhub_2023')['conventions']['si']
    si_file.write_text(json.dumps(document))
    with pytest.raises(ValueError, match='must use the same units'):
        JSONLDFile([CGMES_FILE, str(si_file)])


def test_unknown_units_vocabulary_fails_offline(profile, tmp_path, monkeypatch):
    """A distribution's conformsTo names the units of the numbers: guessing would be 1000x off."""
    profile('cgmes_3_0_0')
    monkeypatch.delenv('CIMG_ALLOW_REMOTE_CONTEXT', raising=False)
    document = json.loads(open(CGMES_FILE).read())
    document['@graph'][0]['dcat:distribution'] = {'@type': 'dcat:Distribution',
                                                  'dct:conformsTo': 'https://example.org/my-units.jsonld'}
    path = tmp_path / 'unknown.jsonld'
    path.write_text(json.dumps(document))
    with pytest.raises(LookupError, match='my-units.jsonld'):
        JSONLDFile(str(path))


def test_unknown_dataset_profile_is_not_a_units_vocabulary(profile, tmp_path, monkeypatch):
    """A Dataset's own conformsTo may name profiles the data was validated against."""
    profile('cgmes_3_0_0')
    monkeypatch.delenv('CIMG_ALLOW_REMOTE_CONTEXT', raising=False)
    document = json.loads(open(CGMES_FILE).read())
    document['@graph'][0]['dct:conformsTo'] = [EQ_VOCABULARY, 'urn:iso:std:iec:61970-552:2016']
    path = tmp_path / 'profiles.jsonld'
    path.write_text(json.dumps(document))
    assert JSONLDFile(str(path)).units['BaseVoltage.nominalVoltage'] == 'kV'


def test_reader_takes_units_from_a_top_level_header(profile, tmp_path):
    """The ENTSO-E layout: the header is the top-level map, the objects its @graph."""
    profile('cimhub_2023')
    distribution = profile_jsonld('cimhub_2023')['conventions']['distribution']
    document = {'@context': profile_jsonld('cimhub_2023')['context'],
                '@id': 'urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000099', '@type': 'dcat:Dataset',
                'dcat:distribution': {'@type': 'dcat:Distribution', 'dct:conformsTo': distribution},
                '@graph': [{'@id': 'urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000098',
                            '@type': 'cim:EnergyConsumer', 'cim:EnergyConsumer.p': '1.5'}]}
    path = tmp_path / 'top-level.jsonld'
    path.write_text(json.dumps(document))
    load = _only(_read(path), get_cim_profile()[1].EnergyConsumer)
    assert load.p.to('kW') == 1.5


def _rdf(path):
    """A written file as RDF: the header in the default graph, the objects in the named graph."""
    rdflib = pytest.importorskip('rdflib')
    from cimprofiles.jsonld import load_document
    document = json.loads(path.read_text())
    document['@context'] = load_document(document['@context'])['@context']  # offline copy
    return rdflib.Dataset(default_union=True).parse(data=json.dumps(document), format='json-ld')


def test_written_context_types_values_for_json_ld_processors(profile, tmp_path):
    rdflib = pytest.importorskip('rdflib')
    profile('cgmes_3_0_0')
    path = tmp_path / 'eq.jsonld'
    write_json_ld(_read(CGMES_FILE), str(path))

    graph = _rdf(path)
    cim = rdflib.Namespace('http://iec.ch/TC57/CIM100#')
    line = rdflib.URIRef('urn:uuid:7b1e0c2a-1d3f-4b6e-9a51-000000000020')
    length = graph.value(line, cim['Conductor.length'])
    assert length.datatype == rdflib.XSD.float and length.toPython() == 12.5
    assert isinstance(graph.value(line, cim['ConductingEquipment.BaseVoltage']), rdflib.URIRef)
    dataset = rdflib.URIRef(json.loads(path.read_text())['@id'])
    assert any(g.identifier == dataset for g in graph.graphs())      # the objects' named graph


def test_our_context_types_the_dataset_header(profile, tmp_path):
    """Our generated contexts type the header as the CGMES one does: references are IRIs."""
    rdflib = pytest.importorskip('rdflib')
    cim = profile('cimhub_2023')
    network = FeederModel(connection=XMLFile(filename=IEEE13), container=cim.Feeder(mRID=FEEDER_MRID),
                          distributed=False)
    path = tmp_path / 'ieee13.jsonld'
    write_json_ld(network, str(path), header={'dcat:isVersionOf': 'https://example.org/models/ieee13'})

    graph = _rdf(path)
    dcat = rdflib.Namespace('http://www.w3.org/ns/dcat#')
    (dataset,) = graph.subjects(rdflib.RDF.type, dcat.Dataset)
    distribution = graph.value(dataset, dcat.distribution)
    assert isinstance(graph.value(distribution, rdflib.namespace.DCTERMS.conformsTo), rdflib.URIRef)
    assert graph.value(dataset, dcat.isVersionOf) == rdflib.URIRef('https://example.org/models/ieee13')
    assert graph.value(dataset, rdflib.namespace.DCTERMS.issued).datatype == rdflib.XSD.dateTime


def test_nordic44_equipment(profile, tmp_path):
    """The real Nordic44 EQ file (CC BY-NC-SA 4.0, not vendored): downloaded when online."""
    cim = profile('cgmes_3_0_0')
    path = tmp_path / 'Nordic44-HV_EQ.jsonld'
    try:
        with urllib.request.urlopen(NORDIC44_EQ, timeout=30) as response:
            path.write_bytes(response.read())
    except urllib.error.URLError as error:
        pytest.skip(f'Nordic44 not reachable: {error}')

    network = _read(path)
    assert len(network.graph[cim.Terminal]) == 452
    assert len(network.graph[cim.ACLineSegment]) == 68
    voltages = sorted(bv.nominalVoltage.to('kV') for bv in network.graph[cim.BaseVoltage].values())
    assert 420 in voltages
    written = tmp_path / 'written.jsonld'
    write_json_ld(network, str(written))
    assert _differences(_read(written), network) == []
