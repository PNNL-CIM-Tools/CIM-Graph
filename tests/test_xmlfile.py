import json
import os
import tempfile
import unittest
from uuid import NAMESPACE_URL, UUID, uuid4, uuid5
from xml.etree import ElementTree

import cimprofiles.cim17.cimhub_2023 as cim
from cimprofiles.jsonld import profile_jsonld

from cimgraph.core import get_model_authority, get_model_name, set_model_scope
from cimgraph.databases import JSONLDFile, XMLFile
from cimgraph.databases.fileparsers.metadata import is_header_element
from cimgraph.models import FeederModel
from cimgraph.utils import write_json_ld, write_xml

PNNL = 'https://www.pnnl.gov'


def _part_xml(authority, line_id):
    """A part file with a model header and one line whose rdf:ID is not a UUID."""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#"
    xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<md:FullModel rdf:about="urn:uuid:{uuid4()}">
  <md:Model.description>feeder_1</md:Model.description>
  <md:Model.modelingAuthoritySet>{authority}</md:Model.modelingAuthoritySet>
</md:FullModel>
<cim:ACLineSegment rdf:ID="{line_id}">
  <cim:IdentifiedObject.name>{line_id}</cim:IdentifiedObject.name>
</cim:ACLineSegment>
</rdf:RDF>
'''


def _dataset_part_xml(authority, line_id, extra_type=''):
    """A part file with a dcat:Dataset header (ENTSO-E layout), its md:Model.modelingAuthoritySet
    unless authority is None, and one line whose rdf:ID is not a UUID."""
    authority_set = '' if authority is None else (
        f'\n  <md:Model.modelingAuthoritySet>{authority}</md:Model.modelingAuthoritySet>')
    return f'''<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/CIM100#"
    xmlns:dcat="http://www.w3.org/ns/dcat#" xmlns:dct="http://purl.org/dc/terms/"
    xmlns:md="http://iec.ch/TC57/61970-552/ModelDescription/1#"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<dcat:Dataset rdf:about="urn:uuid:{uuid4()}">{extra_type}
  <dct:title>{line_id}.xml</dct:title>
  <dcat:isVersionOf rdf:resource="https://gridkitchen.example/parts/x/{line_id}"/>{authority_set}
</dcat:Dataset>
<cim:ACLineSegment rdf:ID="{line_id}">
  <cim:IdentifiedObject.name>{line_id}</cim:IdentifiedObject.name>
</cim:ACLineSegment>
</rdf:RDF>
'''


class TestXMLFile(unittest.TestCase):

    def setUp(self):
        # Backup environment variables
        self.original_env = {
            'CIMG_CIM_PROFILE': os.getenv('CIMG_CIM_PROFILE'),
            'CIMG_URL': os.getenv('CIMG_URL'),
            'CIMG_DATABASE': os.getenv('CIMG_DATABASE'),
            'CIMG_HOST': os.getenv('CIMG_HOST'),
            'CIMG_PORT': os.getenv('CIMG_PORT'),
            'CIMG_USERNAME': os.getenv('CIMG_USERNAME'),
            'CIMG_PASSWORD': os.getenv('CIMG_PASSWORD'),
            'CIMG_NAMESPACE': os.getenv('CIMG_NAMESPACE'),
            'CIMG_IEC61970_552': os.getenv('CIMG_IEC61970_552'),
            'CIMG_USE_UNITS': os.getenv('CIMG_USE_UNITS'),
            'CIMG_MODEL_AUTHORITY': os.getenv('CIMG_MODEL_AUTHORITY'),
            'CIMG_MODEL_NAME': os.getenv('CIMG_MODEL_NAME'),
        }

        # Set environment variables for testing
        os.environ['CIMG_CIM_PROFILE'] = 'cimhub_2023'
        os.environ['CIMG_URL'] = 'http://localhost:8889/bigdata/namespace/kb/sparql'
        os.environ['CIMG_NAMESPACE'] = 'http://iec.ch/TC57/CIM100#'
        os.environ['CIMG_IEC61970_552'] = '552-NEW'
        os.environ['CIMG_USE_UNITS'] = 'false'

        self.feeder_mrid = '49AD8E07-3BF9-A4E2-CB8F-C3722F837B62'

    def tearDown(self):
        # Restore environment variables
        for key, value in self.original_env.items():
            if value is not None:
                os.environ[key] = value
            else:
                os.environ.pop(key, None)

    def test_xml_connection_with_env_vars(self):

        connection = XMLFile(filename='tests/test_models/ieee13.xml')
        self.assertIsInstance(connection, XMLFile, 'Connection should be an instance of XMLFile')
        self.assertEqual(connection.cim_profile, 'cimhub_2023', 'CIM profile mismatch')
        self.assertEqual(connection.namespace, 'http://iec.ch/TC57/CIM100#', 'Namespace mismatch')
        self.assertEqual(connection.iec61970_552, '552-NEW', 'IEC61970_552 mismatch')


    def test_get_feeder_model(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        initial_keys = len(network.graph.keys())
        self.assertEqual(initial_keys, 48)

    def test_get_all_line_data(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertEqual(len(line.Terminals),2)
        # check value of line 645646
        self.assertEqual(line.name, '645646')
        self.assertEqual(line.length, 91.44)

        # check phase C
        for phase in line.ACLineSegmentPhases:
            if phase.phase.value == 'C':
               break
        self.assertEqual(phase.name, '645646_C')
        self.assertEqual(phase.ACLineSegment, line)

    def test_units_disabled_raw_float(self):
        os.environ['CIMG_USE_UNITS'] = 'false'
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertIs(type(line.length), float)
        self.assertEqual(line.length, 91.44)

    def test_units_enabled_si_fallback(self):
        os.environ['CIMG_USE_UNITS'] = 'true'
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line = network.graph[cim.ACLineSegment][UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')]
        self.assertIsInstance(line.length, cim.Length)
        self.assertEqual(float(line.length), 91.44)
        self.assertAlmostEqual(line.length.to('km'), 0.09144)

    def test_upload_round_trip_via_write_xml(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)
        line_uuid = UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')
        line = network.graph[cim.ACLineSegment][line_uuid]
        original_name = line.name
        original_length = line.length

        tmp = tempfile.NamedTemporaryFile(suffix='.xml', delete=False)
        tmp.close()
        tmp_path = tmp.name
        try:
            network.connection.filename = tmp_path
            network.upload()

            database2 = XMLFile(filename=tmp_path)
            feeder2 = cim.Feeder(mRID=self.feeder_mrid)
            network2 = FeederModel(connection=database2, container=feeder2, distributed=False)
            line2 = network2.graph[cim.ACLineSegment][line_uuid]

            self.assertEqual(line2.name, original_name)
            self.assertEqual(line2.length, original_length)
        finally:
            os.unlink(tmp_path)

    def test_writers_include_model_header(self):
        self._use_model_scope(PNNL, 'ieee13')
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        feeder = cim.Feeder(mRID=self.feeder_mrid)
        network = FeederModel(connection=database, container=feeder, distributed=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            xml_path = os.path.join(tmp_dir, 'out.xml')
            json_path = os.path.join(tmp_dir, 'out.jsonld')
            write_xml(network, xml_path)
            write_json_ld(network, json_path)

            with open(xml_path, encoding='utf-8') as f:
                xml_text = f.read()
            self.assertIn('<md:FullModel rdf:about="urn:uuid:', xml_text)
            self.assertIn(f'<md:Model.modelingAuthoritySet>{PNNL}</md:Model.modelingAuthoritySet>', xml_text)
            self.assertIn('<md:Model.description>ieee13</md:Model.description>', xml_text)
            self.assertIn('<cim:ModelAuthority rdf:about="urn:uuid:', xml_text)

            with open(json_path, encoding='utf-8') as f:
                document = json.load(f)
            published = profile_jsonld('cimhub_2023')   # versioned URLs: .../cimhub_2023/<X.Y>/...
            self.assertEqual(document['@context'], published['context'])
            # ENTSO-E layout: the top-level map is the dcat:Dataset, @graph its named graph
            self.assertEqual(document['@type'], ['dcat:Dataset', 'http://www.w3.org/2004/03/trix/rdfg-1/Graph'])
            self.assertEqual(document['md:Model.modelingAuthoritySet'], PNNL)
            self.assertEqual(document['dct:title'], 'ieee13')
            self.assertRegex(document['dct:issued'], r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$')
            self.assertEqual(document['dct:conformsTo'], published['conventions']['si'])
            self.assertEqual(document['dcat:distribution'],
                             {'@type': 'dcat:Distribution', 'dct:conformsTo': published['conventions']['si']})
            self.assertNotIn('dcat:isVersionOf', document)   # the model series is the caller's
            types = [node['@type'] for node in document['@graph']]
            self.assertNotIn('dcat:Dataset', types)
            self.assertNotIn('cim:ModelAuthority', types)     # no profile defines it

    def _ieee13(self):
        return FeederModel(connection=XMLFile(filename='tests/test_models/ieee13.xml'),
                           container=cim.Feeder(mRID=self.feeder_mrid), distributed=False)

    def test_json_ld_header_from_the_caller(self):
        """A publisher sets the identity, series, title and its own terms; identical exports are identical."""
        self._use_model_scope('pnnl', 'ieee13')    # any text: the authority is a literal
        network = self._ieee13()
        header = {'@id': 'urn:uuid:5a0c3a4e-0000-5000-8000-000000000001',
                  'dct:identifier': '5a0c3a4e-0000-5000-8000-000000000001',
                  'dct:issued': '2026-11-01T00:00:00Z',
                  'dcat:isVersionOf': 'https://gridkitchen.example/models/ieee13',
                  'dct:title': 'ieee13', 'dct:description': 'IEEE 13 node test feeder',
                  'gk:feederCount': 1,
                  'dqv:hasQualityMeasurement': [{'@type': 'dqv:QualityMeasurement', 'dqv:value': 'source'}]}
        extension = {'gk': 'https://gridkitchen.example/ns#', 'dqv': 'http://www.w3.org/ns/dqv#'}
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = [os.path.join(tmp_dir, f'{n}.jsonld') for n in (1, 2)]
            for path in paths:
                write_json_ld(network, path, header=header, contexts=[extension])
            with open(paths[0], encoding='utf-8') as first, open(paths[1], encoding='utf-8') as second:
                text = first.read()
                self.assertEqual(text, second.read())
            document = json.loads(text)

            self.assertEqual(document['@context'], [profile_jsonld('cimhub_2023')['context'], extension])
            for key, value in header.items():
                self.assertEqual(document[key], value)
            self.assertEqual(document['md:Model.modelingAuthoritySet'], 'pnnl')

            self._use_model_scope('https://someone.else', 'utility')
            reread = JSONLDFile(filename=paths[0])
            reread.create_new_graph(container=None)
        (read_header,) = reread.model_headers
        self.assertEqual((read_header.authority, read_header.description), ('pnnl', 'ieee13'))
        self.assertEqual(read_header.full_model_uuid, '5a0c3a4e-0000-5000-8000-000000000001')
        self.assertEqual((get_model_authority(), get_model_name()), ('pnnl', 'utility'))

    def test_json_ld_header_checks(self):
        self._use_model_scope(PNNL, 'ieee13')
        network = self._ieee13()
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = os.path.join(tmp_dir, 'out.jsonld')
            with self.assertRaisesRegex(ValueError, r"prefixes \['gk'\] are not defined"):
                write_json_ld(network, path, header={'gk:feederCount': 1})
            with self.assertRaisesRegex(ValueError, r"prefixes \['dqv'\] are not defined"):
                write_json_ld(network, path, header={'dct:x': [{'@type': 'dqv:QualityMeasurement'}]})
            with self.assertRaisesRegex(ValueError, 'must not set dcat:distribution'):
                write_json_ld(network, path, header={'dcat:distribution': {'@type': 'dcat:Distribution'}})
            with self.assertRaisesRegex(ValueError, "'ieee13' is not an absolute IRI"):
                write_json_ld(network, path, header={'dcat:isVersionOf': 'ieee13'})
            with self.assertRaisesRegex(ValueError, 'is not a UTC date-time'):
                write_json_ld(network, path, header={'dct:issued': '2026-11-01'})

    def test_json_ld_reader_restores_model_header(self):
        self._use_model_scope(PNNL, 'ieee13')
        network = self._ieee13()

        with tempfile.TemporaryDirectory() as tmp_dir:
            json_path = os.path.join(tmp_dir, 'out.jsonld')
            # A series IRI is not the authority, and a description is not the model name
            write_json_ld(network, json_path, header={'dcat:isVersionOf': 'https://example.org/series',
                                                      'dct:description': 'a generated description'})

            self._use_model_scope('https://someone.else', 'utility')
            reread = JSONLDFile(filename=json_path)
            reread.create_new_graph(container=None)

        header = reread.model_headers[0]
        self.assertEqual(header.authority, PNNL)
        self.assertEqual(header.description, 'ieee13')
        self.assertEqual(header.authority_uuid, str(uuid5(NAMESPACE_URL, PNNL)))
        self.assertIsNotNone(header.full_model_uuid)
        self.assertEqual((get_model_authority(), get_model_name()), (PNNL, 'utility'))

    def test_xml_dataset_header_from_the_caller(self):
        """write_xml(header=...) writes the ENTSO-E dcat:Dataset block in place of md:FullModel;
        identical exports are identical, and the reader restores the model scope from it."""
        self._use_model_scope(PNNL, 'ieee13')
        network = self._ieee13()
        header = {'@id': 'urn:uuid:5a0c3a4e-0000-5000-8000-000000000001',
                  'dct:identifier': '5a0c3a4e-0000-5000-8000-000000000001',
                  'dct:issued': '2026-11-01T00:00:00Z', 'dct:title': 'ieee13 <test>',
                  'dcat:isVersionOf': {'@id': 'https://gridkitchen.example/models/ieee13'},
                  'dct:license': {'@id': 'https://spdx.org/licenses/BSD-3-Clause.html'},
                  'gk:feederCount': 1}
        extension = {'gk': 'https://gridkitchen.example/ns#'}
        si = profile_jsonld('cimhub_2023')['conventions']['si']
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = [os.path.join(tmp_dir, f'{n}.xml') for n in (1, 2)]
            for path in paths:
                write_xml(network, path, header=header, contexts=[extension])
            with open(paths[0], encoding='utf-8') as first, open(paths[1], encoding='utf-8') as second:
                text = first.read()
                self.assertEqual(text, second.read())

            self.assertIn('<dcat:Dataset rdf:about="urn:uuid:5a0c3a4e-0000-5000-8000-000000000001">', text)
            self.assertIn('<dcat:isVersionOf rdf:resource="https://gridkitchen.example/models/ieee13"/>', text)
            self.assertIn('<dct:title>ieee13 &lt;test&gt;</dct:title>', text)
            self.assertIn('<dct:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">'
                          '2026-11-01T00:00:00Z</dct:issued>', text)
            self.assertIn(f'<dct:conformsTo rdf:resource="{si[0]}"/>', text)   # CIM XML numbers are SI
            self.assertIn('<gk:feederCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1<', text)
            self.assertIn('xmlns:gk="https://gridkitchen.example/ns#"', text)
            self.assertNotIn('md:FullModel', text)
            self.assertNotIn('cim:ModelAuthority', text)
            self.assertNotIn('rdfg-1/Graph', text)       # not a named graph in RDF/XML

            self._use_model_scope('https://someone.else', 'utility')
            reread = XMLFile(filename=paths[0])
            reread.create_new_graph(container=None)
        (read_header,) = reread.model_headers
        self.assertEqual((read_header.authority, read_header.description), (PNNL, 'ieee13 <test>'))
        self.assertEqual(read_header.full_model_uuid, '5a0c3a4e-0000-5000-8000-000000000001')
        self.assertEqual(read_header.created, '2026-11-01T00:00:00Z')
        self.assertEqual((get_model_authority(), get_model_name()), (PNNL, 'utility'))
        self.assertNotIn('Dataset', {cim_class.__name__ for cim_class in reread.graph})
        self.assertEqual(sum(map(len, reread.graph.values())), sum(map(len, network.graph.values())))

    def test_xml_dataset_header_checks(self):
        self._use_model_scope(PNNL, 'ieee13')
        network = self._ieee13()
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = os.path.join(tmp_dir, 'out.xml')
            with self.assertRaisesRegex(ValueError, 'needs write_model_header=True'):
                write_xml(network, path, write_model_header=False, header={})
            with self.assertRaisesRegex(ValueError, r"prefixes \['gk'\] are not defined"):
                write_xml(network, path, header={'gk:feederCount': 1})
            with self.assertRaisesRegex(ValueError, 'must be a compact IRI'):
                write_xml(network, path, header={'https://example.org/ns#count': 1})

    def test_dataset_header_output_depends_only_on_graph_and_header(self):
        """With @id, dct:identifier and dct:issued set, writing again, at another time and in
        another model scope, gives the same bytes, in XML and JSON-LD."""
        self._use_model_scope(PNNL, 'ieee13')
        network = self._ieee13()
        header = {'@id': 'urn:uuid:5a0c3a4e-0000-5000-8000-000000000001',
                  'dct:identifier': '5a0c3a4e-0000-5000-8000-000000000001',
                  'dct:issued': '2026-11-01T00:00:00Z', 'dct:title': 'reference',
                  'dct:description': {'@value': 'Reference data', '@language': 'en'},
                  'adms:versionNotes': {'@value': 'First release.', '@language': 'en'},
                  'dcat:startDate': '2026-11-24T00:00:00Z',
                  'adms:status': {'@id': 'http://purl.org/adms/status/Completed'},
                  'prov:wasAttributedTo': {'@id': 'https://www.pnnl.gov/'},
                  'md:Model.modelingAuthoritySet': {'@id': 'https://example.org/authority/utility'}}
        extension = {'adms': 'http://www.w3.org/ns/adms#', 'prov': 'http://www.w3.org/ns/prov#'}
        with tempfile.TemporaryDirectory() as tmp_dir:
            texts = {}
            for scope in ((PNNL, 'ieee13'), ('https://someone.else', 'other')):
                self._use_model_scope(*scope)
                for suffix, write in (('xml', write_xml), ('jsonld', write_json_ld)):
                    path = os.path.join(tmp_dir, f'{scope[1]}.{suffix}')
                    write(network, path, header=header, contexts=[extension])
                    with open(path, 'rb') as f:
                        texts.setdefault(suffix, []).append(f.read())
        for suffix, (first, second) in texts.items():
            self.assertEqual(first, second, suffix)

        xml_text = texts['xml'][0].decode()
        self.assertIn('<dct:description xml:lang="en">Reference data</dct:description>', xml_text)
        self.assertIn('<adms:versionNotes xml:lang="en">First release.</adms:versionNotes>', xml_text)
        self.assertIn('<dcat:startDate rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTimeStamp">'
                      '2026-11-24T00:00:00Z</dcat:startDate>', xml_text)
        self.assertIn('<adms:status rdf:resource="http://purl.org/adms/status/Completed"/>', xml_text)
        self.assertIn('<prov:wasAttributedTo rdf:resource="https://www.pnnl.gov/"/>', xml_text)
        self.assertIn('<md:Model.modelingAuthoritySet rdf:resource="https://example.org/authority/utility"/>',
                      xml_text)
        self.assertIn('xmlns:adms="http://www.w3.org/ns/adms#"', xml_text)
        self.assertIn('xmlns:prov="http://www.w3.org/ns/prov#"', xml_text)

    def test_parts_with_dataset_headers_load_together(self):
        """Parts whose dcat:Dataset headers carry one authority load as one model; a header
        that is also a gad:GridAssembly is still a header. Their dct:titles are file names, not
        the model name: UUIDs seed with the authority and the model name set beforehand."""
        grid_assembly = '\n  <rdf:type rdf:resource="http://gridappsd.org/CIM/extension#GridAssembly"/>'
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = []
            for line_id, extra_type in (('LINE_A', ''), ('LINE_B', grid_assembly)):
                path = os.path.join(tmp_dir, f'{line_id}.xml')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(_dataset_part_xml('utility_a', line_id, extra_type))
                paths.append(path)
            self._use_model_scope('utility_a', 'utility')
            database = XMLFile(filename=paths)
            graph = database.create_new_graph(container=None)
            grid_assembly_header = ElementTree.parse(paths[1]).getroot()[0]
        self.assertTrue(is_header_element(grid_assembly_header, cim))

        self.assertEqual([header.authority for header in database.model_headers], ['utility_a', 'utility_a'])
        self.assertEqual({cim_class.__name__ for cim_class in graph}, {'ACLineSegment'})
        lines = {line.name: line.identifier for line in graph[cim.ACLineSegment].values()}
        set_model_scope('utility_a', 'utility')
        self.assertEqual(lines, {line_id: cim.ACLineSegment(identifier=line_id).identifier
                                 for line_id in ('LINE_A', 'LINE_B')})

    def test_json_ld_parts_with_dataset_headers_load_together(self):
        """As test_parts_with_dataset_headers_load_together, for JSON-LD."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = []
            for line_id, types in (('LINE_A', ['dcat:Dataset']), ('LINE_B', ['dcat:Dataset', 'gad:GridAssembly'])):
                document = {'@context': {'cim': 'http://iec.ch/TC57/CIM100#', 'dcat': 'http://www.w3.org/ns/dcat#',
                                         'dct': 'http://purl.org/dc/terms/', 'gad': 'http://gridappsd.org/CIM/extension#',
                                         'md': 'http://iec.ch/TC57/61970-552/ModelDescription/1#'},
                            '@id': f'urn:uuid:{uuid4()}', '@type': types, 'dct:title': f'{line_id}.jsonld',
                            'dcat:isVersionOf': {'@id': f'https://gridkitchen.example/parts/x/{line_id}'},
                            'md:Model.modelingAuthoritySet': 'utility_a',
                            '@graph': [{'@id': line_id, '@type': 'cim:ACLineSegment',
                                        'cim:IdentifiedObject.name': line_id}]}
                path = os.path.join(tmp_dir, f'{line_id}.jsonld')
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(document, f)
                paths.append(path)
            self._use_model_scope('utility_a', 'utility')
            database = JSONLDFile(filename=paths)
            graph = database.create_new_graph(container=None)
        self.assertTrue(database._is_header(['gad:GridAssembly', 'dcat:Dataset']))

        self.assertEqual([header.authority for header in database.model_headers], ['utility_a', 'utility_a'])
        self.assertEqual({cim_class.__name__ for cim_class in graph}, {'ACLineSegment'})
        lines = {line.name: line.identifier for line in graph[cim.ACLineSegment].values()}
        set_model_scope('utility_a', 'utility')
        self.assertEqual(lines, {line_id: cim.ACLineSegment(identifier=line_id).identifier
                                 for line_id in ('LINE_A', 'LINE_B')})

    def test_a_model_series_is_not_the_model_authority(self):
        """A dcat:Dataset header without md:Model.modelingAuthoritySet leaves the scope as it is,
        unless CIMG_AUTHORITY_FROM_IS_VERSION_OF opts in to its dcat:isVersionOf."""
        series = 'https://gridkitchen.example/parts/x/LINE_A'
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = os.path.join(tmp_dir, 'part.xml')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(_dataset_part_xml(None, 'LINE_A'))
            self._use_model_scope('utility_a', 'feeder_1')
            with self.assertLogs('cimgraph.databases.fileparsers.metadata', 'WARNING') as logs:
                database = XMLFile(filename=path)
                database.create_new_graph(container=None)
            self.assertIsNone(database.model_headers[0].authority)
            self.assertEqual((get_model_authority(), get_model_name()), ('utility_a', 'feeder_1'))
            self.assertIn(f'from dcat:isVersionOf {series!r}', logs.output[0])

            os.environ['CIMG_AUTHORITY_FROM_IS_VERSION_OF'] = 'true'
            self.addCleanup(os.environ.pop, 'CIMG_AUTHORITY_FROM_IS_VERSION_OF')
            database = XMLFile(filename=path)
            database.create_new_graph(container=None)
        self.assertEqual(database.model_headers[0].authority, series)
        self.assertEqual(get_model_authority(), series)

    def _use_model_scope(self, authority, model_name):
        set_model_scope(authority, model_name)
        self.addCleanup(get_model_name.cache_clear)
        self.addCleanup(get_model_authority.cache_clear)

    def test_reader_restores_model_header(self):
        self._use_model_scope('pnnl', 'ieee13')
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        network = FeederModel(connection=database, container=cim.Feeder(mRID=self.feeder_mrid),
                              distributed=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            xml_path = os.path.join(tmp_dir, 'out.xml')
            write_xml(network, xml_path)

            self._use_model_scope('someone_else', '')
            reread = XMLFile(filename=xml_path)
            reread.create_new_graph(container=None)

        header = reread.model_headers[0]
        self.assertEqual(header.authority, 'pnnl')
        self.assertEqual(header.description, 'ieee13')
        self.assertEqual(header.authority_uuid, str(uuid5(NAMESPACE_URL, 'pnnl')))
        self.assertIsNotNone(header.full_model_uuid)
        self.assertEqual((get_model_authority(), get_model_name()), ('pnnl', 'ieee13'))
        class_names = {cim_class.__name__ for cim_class in reread.graph}
        self.assertNotIn('FullModel', class_names)
        self.assertNotIn('ModelAuthority', class_names)

    def test_headerless_file_keeps_model_scope(self):
        self._use_model_scope('pnnl', 'ieee13')
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        database.create_new_graph(container=None)
        self.assertIsNone(database.model_headers[0].authority)
        self.assertEqual((get_model_authority(), get_model_name()), ('pnnl', 'ieee13'))

    def test_each_part_seeds_with_its_own_authority(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = []
            for authority, line_id in (('utility_a', 'LINE_A'), ('utility_b', 'LINE_B')):
                path = os.path.join(tmp_dir, f'{authority}.xml')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(_part_xml(authority, line_id))
                paths.append(path)
            database = XMLFile(filename=paths)
            self.addCleanup(get_model_name.cache_clear)
            self.addCleanup(get_model_authority.cache_clear)
            graph = database.create_new_graph(container=None)

        lines = {line.name: line.identifier for line in graph[cim.ACLineSegment].values()}
        for authority, line_id in (('utility_a', 'LINE_A'), ('utility_b', 'LINE_B')):
            set_model_scope(authority, 'feeder_1')
            self.assertEqual(lines[line_id], cim.ACLineSegment(identifier=line_id).identifier)

    def test_get_object_matches_the_identifier_exactly(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')   # rdf:about="urn:uuid:<UPPER>"
        feeder = database.get_object(self.feeder_mrid)
        self.assertIsInstance(feeder, cim.Feeder)
        for form in (self.feeder_mrid.lower(), f'_{self.feeder_mrid.lower()}',
                     f'#_{self.feeder_mrid}', f'urn:uuid:{self.feeder_mrid.lower()}'):
            self.assertIs(database.get_object(form), feeder, form)
        # A part of an identifier is not the identifier
        self.assertIsNone(database.get_object(self.feeder_mrid[:8]))
        self.assertIsNone(database.get_object('0'))

    def test_get_object_returns_the_graph_object(self):
        network = self._ieee13()
        line_uuid = UUID('0bbd0ea3-f665-465b-86fd-fc8b8466ad53')
        self.assertIs(network.get_object(str(line_uuid)), network.graph[cim.ACLineSegment][line_uuid])

    def test_get_object_searches_every_part(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            paths = []
            for authority, line_id in (('utility_a', 'LINE_A'), ('utility_b', 'LINE_B')):
                path = os.path.join(tmp_dir, f'{authority}.xml')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(_part_xml(authority, line_id))
                paths.append(path)
            database = XMLFile(filename=paths)
            self.addCleanup(get_model_name.cache_clear)
            self.addCleanup(get_model_authority.cache_clear)
            line = database.get_object('_LINE_B')
            self.assertIsNone(database.get_object('LINE'))
            graph = database.create_new_graph(container=None)

        # The identifier create_new_graph gives the line, seeded with its part's authority
        set_model_scope('utility_b', 'feeder_1')
        self.assertEqual(line.identifier, cim.ACLineSegment(identifier='LINE_B').identifier)
        self.assertIs(graph[cim.ACLineSegment][line.identifier], line)

    def test_get_object_skips_elements_without_an_id(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = os.path.join(tmp_dir, 'part.xml')
            with open(path, 'w', encoding='utf-8') as f:
                # after the line, where a stale rdf:ID would make it match 'LINE_A'
                f.write(_part_xml('utility_a', 'LINE_A').replace(
                    '</rdf:RDF>', '<cim:NotInTheProfile/>\n</rdf:RDF>'))
            database = XMLFile(filename=path)
            self.addCleanup(get_model_name.cache_clear)
            self.addCleanup(get_model_authority.cache_clear)
            self.assertIsInstance(database.get_object('LINE_A'), cim.ACLineSegment)
            self.assertIsNone(database.get_object('LINE_B'))

    def test_get_from_triple_without_the_predicate_is_empty(self):
        network = self._ieee13()
        self.assertEqual(network.connection.get_from_triple(network.container, 'Feeder.FeederArea'), [])
        self.assertEqual(network.connection.get_from_triple(network.container, 'IdentifiedObject.name'),
                         ['ieee13nodeckt'])

    def test_distributed_feeder_needs_a_feeder_area(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        with self.assertRaisesRegex(ValueError, r'No FeederArea defined .* method from the'):
            FeederModel(connection=database, container=cim.Feeder(mRID=self.feeder_mrid), distributed=True)

    def test_create_distributed_graph_is_not_supported(self):
        database = XMLFile(filename='tests/test_models/ieee13.xml')
        with self.assertRaisesRegex(NotImplementedError, 'RDFlibConnection'):
            database.create_distributed_graph(area=cim.FeederArea(mRID=str(uuid4())), graph={})

    def test_container_is_the_graph_object(self):
        for connection in (XMLFile(filename='tests/test_models/ieee13.xml'),
                           JSONLDFile(filename='tests/test_models/ieee13.jsonld')):
            feeder = cim.Feeder(mRID=self.feeder_mrid)
            network = FeederModel(connection=connection, container=feeder, distributed=False)
            self.assertIs(network.graph[cim.Feeder][feeder.identifier], feeder, type(connection).__name__)
            self.assertEqual(len(network.graph[cim.Feeder]), 1)
            self.assertEqual(feeder.name, 'ieee13nodeckt')


if __name__ == '__main__':
    unittest.main()
