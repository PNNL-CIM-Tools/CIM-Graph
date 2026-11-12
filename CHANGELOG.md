# Changelog

## 0.6.0 (unreleased)

### JSON-LD in the CGMES draft style, with QUDT units (#225)

Requires `cim-profiles>=0.2`, which ships the contexts and unit vocabularies
(`cimprofiles.jsonld`) and an offline cache of them.

- `write_json_ld` writes the profile's published `@context` URL (e.g.
  `https://pnnl-cim-tools.github.io/CIM-Profiles/cimhub_2023/0.2.0/context.jsonld`, versioned by
  the stable cim-profiles release as CGMES versions its IRIs; `cgmes_3_0_0` uses the Inst4CIM CGMES
  context) instead of an inline prefix map. A runtime-merged profile gets an
  inline context built from its classes.
- **Breaking:** references are written as `"urn:uuid:..."` strings, not `{"@id": ...}` objects
  (the context types them `@id`), and the header is a `dcat:Dataset` instead of `md:FullModel`
  and `cim:ModelAuthority` (which no profile defines), in the ENTSO-E metadata layout: the
  top-level map is the dataset (typed `dcat:Dataset` and `rdfg:Graph`, as Nordic44 and KGraphPy
  expect) and `@graph` its named graph. It carries `dct:identifier`, `dct:issued` (UTC, ending
  with `Z`), the model authority as `md:Model.modelingAuthoritySet` and the model name as
  `dct:title`.
- `write_json_ld(..., header={...}, contexts=[...])`: a publisher adds header properties or
  replaces ours (e.g. a stable `@id`/`dct:identifier` and `dct:issued`, so identical exports are
  identical files; `dcat:isVersionOf`, the model series IRI; extension terms and blank nodes).
  `contexts` are written after the profile's context and define the header's other prefixes; an
  undefined header prefix fails.
- Numbers are written in the units of a units convention, named in the header's
  `dct:conformsTo` and in that of its `dcat:distribution` (the Dataset's own survives tools
  such as KGraphPy that drop the distribution). `write_json_ld(..., convention='distribution')` writes kW/kVAr/kVA, line
  constants per km (ohm/km, uS/km) and wire sizes in mm. The default is the profile's default convention (base SI; MW/kV/km for
  `cgmes_3_0_0`). A number kept in its own unit is written exactly, as in CIM XML; a converted
  one to 15 significant digits.
- `JSONLDFile` reads these files and Nordic44-style ones (the header a node in `@graph`): a URL
  `@context`, `"urn:uuid:..."` string references, and numbers in the units of the vocabularies
  the header's distribution names, or, for CGMES files, the cached vocabularies among the
  Dataset's own `dct:conformsTo` (other IRIs there are profiles, not units). A file naming none
  is read with the profile's default convention. Files loaded together must agree on units. Each
  file's header is read into `JSONLDFile.model_headers`, and its authority
  (`md:Model.modelingAuthoritySet`, else `dcat:isVersionOf` as CGMES files carry it) and
  `dct:title` set the model scope, as `md:FullModel` does for `XMLFile`.
- The cimprofiles contexts type the header as the Inst4CIM CGMES context does
  (`dct:conformsTo`, `dcat:isVersionOf` as IRIs; `dct:issued` as `xsd:dateTime`), matching
  what DCAT tools such as statnett's KGraphPy expect.
- Contexts and vocabularies that are not in the cimprofiles cache are fetched only with
  `CIMG_ALLOW_REMOTE_CONTEXT=true`; otherwise reading the file fails and names the URL.
- The CIM XML writer no longer adds an invalid `rdf:datatype="…UnitSymbol.*"` to unit values
  (#224). CIM XML values are plain base SI numbers.
- The readers read plain numbers for unit-only types (e.g. cim18v17 `Optional[ApparentPower]`),
  which were previously kept as strings.

### Profiles moved to `cimprofiles`

The CIM profiles and the object model they are built on (`Identity`, `CIMUnit`, profile merging)
now ship as the separate [`cimprofiles`](https://github.com/PNNL-CIM-Tools/CIM-Profiles) package,
released on its own cycle. cim-graph depends on it, so nothing extra needs installing.

- New imports: `import cimprofiles.cim18.cimhub_2026 as cim`, `from cimprofiles.identity import Identity`.
- Profiles are grouped by CIM version: `cimprofiles.cim16.cim16v33`, `cimprofiles.cim17.cim17v40`,
  `cimprofiles.cim17.cimhub_2023`, `cimprofiles.cim18.cimhub_2026`, ... The GridAPPS-D
  `rc4_2021` profile is `cimprofiles.cim17.gridappsd_rc4_2021`.
- **The old `cimgraph.data_profile.*` imports still work, with a `DeprecationWarning`:**
  - `cimgraph.data_profile.identity`, `.units` and `.merge` are aliases of the `cimprofiles`
    modules (the same module objects), and stay for all of 1.x.
  - The profile packages (`cimgraph.data_profile.cim17v40` etc.) re-export `cimprofiles` and are
    removed in 1.0.
- `CIMG_CIM_PROFILE`:
  - A short name (`cimhub_2026`, `cim18gmdm.connectivity`) resolves through
    `cimprofiles.PROFILE_PACKAGES`, so `cimhub_2026` is `cimprofiles.cim18.cimhub_2026`. An
    unknown name raises a `ValueError` listing the known ones.
  - The old `cimgraph.data_profile.<name>` paths resolve the same way, with a
    `DeprecationWarning`. Every spelling gives the same module and the same merged classes.
- `get_model_authority`, `get_model_name` and `get_validation_log_level` are defined in
  `cimprofiles.env_vars`; `cimgraph.core` re-exports them.
- The profile build tools moved with the profiles: `python -m cimprofiles.build_merged_profiles`
  and `python -m cimprofiles.dedupe_profile_fields`.

### Database drivers are optional extras (breaking install change)

`pip install cim-graph` no longer installs any database driver. XML and JSON-LD files and
`SPARQLEndpointConnection` work without them. Install the extra for each connection you use:

| Extra | For |
|---|---|
| `sparql` | `BlazegraphConnection`, `GraphDBConnection` |
| `neo4j` | `Neo4jConnection` |
| `mysql` | `MySQLConnection` |
| `gridappsd` | `GridappsdConnection` |
| `rdflib` | `RDFlibConnection` |
| `all` | everything |

Using a connection without its driver raises an `ImportError` naming the extra to install.
`requests` and the unused `mermaid-python` are no longer dependencies.

The `dev` extra is now a `dev` dependency group, which is not published with the package.
`uv sync` installs it; `uv sync --all-extras` adds every driver. Python 3.13 and 3.14 are
supported, and `requires-python` no longer has an upper bound.

### Tests and CI

- Tests that need a live database are marked `@pytest.mark.integration('<service>')`. They are
  skipped when nothing listens on the service's port (`tests/conftest.py`), and
  `pytest -m "not integration"` runs only the rest.
- New `.github/workflows/ci.yml` runs on pull requests and gates the release workflows:
  - the offline tests on Python 3.10–3.14;
  - the offline tests with the lowest declared version of every direct dependency;
  - a ruff check for syntax errors and undefined names.
- Pre-commit also rejects new files over 500 kB and runs the same ruff check.
- `docker-compose.yml` now runs Blazegraph, GraphDB 10 and Neo4j 5.26 with no stored data, and
  `tests/seed_databases.py` loads `tests/test_models/ieee13.xml` into each with the database's
  own RDF loader. CI runs the integration tests against them. `tests/test_backends_match_xml.py`
  checks that every object each database adapter reads matches what `XMLFile` reads.

### Database adapters

- Removed unused query modules: `cimgraph.queries.ontotext` (`get_all_edges_ontotext`, which was
  malformed and, once fixed, no faster than the standard query on IEEE 9500;
  `get_all_nodes_ontotext`), `cimgraph.queries.rdflib.get_all_nodes_sparql` (never called:
  `RDFlibConnection` uses the `queries.sparql` node query), and the empty
  `cimgraph.queries.jsonld_sql`.
- `Neo4jConnection` no longer needs `nest-asyncio`, and importing it no longer patches asyncio
  for the whole process (which breaks on Python 3.16). It keeps the async driver and its
  batched `get_all_edges`. Its coroutines now run on the connection's own event loop in a
  background thread, so the synchronous methods also work where a loop is already running
  (Jupyter). `async_execute` and the other coroutines must be awaited only on that loop.
  `disconnect()` stops the loop and is safe to call when not connected.
- `Neo4jConnection.create_new_graph` adds the container to the graph, as the other connections do.
- Every connection reads all `CIMG_*` connection settings (URL, host, port, user, password,
  database) as they are when it is created. `BlazegraphConnection` kept the URL of the first
  connection, and `GridappsdConnection` the database of the previous one.

### Identifiers (breaking)

All of these change UUIDs or comparisons that existing code may rely on:

- **Seeded UUIDs are now version 5 (name-based, RFC 9562 §5.5)**, reproducible in any language.
  An object created from a non-UUID identifier, mRID or name gets
  `uuid5(uuid5(NAMESPACE_URL, authority), '<model>+<ClassName>+<mRID>+<name>+<seed>')`.
  They were previously random-generator output labeled version 4. Objects created with no
  identifying input still get a random `uuid4()`. See the cimprofiles README for the full rules.
  - The namespace is derived from the model authority URI, and is the same UUID written for the
    `cim:ModelAuthority` header object.
  - Components are separated by `+`, with `%` and `+` escaped inside them. Before, name and mRID
    were concatenated, so name `650` + mRID `LINE` collided with name `65` + mRID `0LINE`.
  - `Identity.identifier` is a UUID (CIM 18), so it is never a seed itself: a non-UUID
    `rdf:ID`/`rdf:about` stands in for the mRID when none is given (it used to be appended
    twice). The mRID is normalized, so `rdf:ID="_LINE1"`, `rdf:about="#_LINE1"` and
    `mRID="LINE1"` give the same UUID.
  - Read from a file, the `rdf:ID`/`rdf:about` is the UUID and the name is not used. One that is
    not a UUID is replaced, with a warning, by the UUID seeded from it, so reading the file again
    gives the same UUIDs, and is kept as the mRID. Built objects are seeded from their mRID and
    name, so renaming an object (bus 300 to bus 301) makes it a new object with a new UUID.
  - Readers key the graph by that identifier (`cimprofiles.identity.read_identifier`) also for
    non-UUID IDs. They used the raw string, so `graph[cls][obj.identifier]` missed such objects.
  - An empty mRID or blank name no longer seeds with the class alone, which gave every such
    object of a class the same UUID; those objects now get random UUIDs.
  - A UUID is recognized in every serialization (`urn:uuid:…`, `#_…`, `_…`); `#_<uuid>`
    previously became a seeded UUID. A UUID mRID is used when the identifier is not a UUID.
  - Names are whitespace-trimmed before seeding.
- The class name is always part of the UUID seed. Before, mRID and URI seeds left it out.
- The default model authority is the URI `https://github.com/PNNL-CIM-Tools/CIM-Graph` (was
  `user@hostname`), so seeded UUIDs are the same on every machine. Set `CIMG_MODEL_AUTHORITY` to
  your organization's URI.
- **Identifier formatting is set by the serialization style, not tracked per object.**
  `CIMG_IEC61970_552` gains a third style, `CGMES`:

  | Style | rdf:ID / rdf:about | References | mRID (when it is the UUID) |
  |---|---|---|---|
  | `552-NEW` | `rdf:about="urn:uuid:<uuid>"` | `urn:uuid:<uuid>` | `<uuid>` |
  | `552-LEGACY` | `rdf:ID="_<uuid>"` | `#_<uuid>` | `_<uuid>` |
  | `CGMES` | `rdf:ID="_<uuid>"` | `#_<uuid>` | `<uuid>` |

  A non-UUID mRID is written as-is. The same rule builds the IRIs in SPARQL and Cypher queries
  and the MySQL `mRID` keys. Fixes: 552-NEW no longer writes `urn:uuid:_…` for objects read from
  legacy files, `cim:Identity.identifier` never carries an underscore, and legacy/CGMES file
  headers (`md:FullModel`, `cim:ModelAuthority`) get valid `rdf:ID`s.
- **`Identity.uri()` returns the bare UUID** (no underscore), uppercase if it was read uppercase
  (CIMHub and GridAPPS-D data), so round trips and database queries keep matching. Generated
  UUIDs are lowercase. The per-object `__uuid__` (`UUID_Meta`) is gone, saving about 420 bytes
  per object (29 MB on the 9500-node model). `__json_ld__` stays cached for `repr()`.
- Objects compare and hash by `identifier` only (CIM #7540). Use
  `cimgraph.core.attribute_utils.diff_attributes` to compare attribute values.
- `add_object_to_graph` raises when two different objects share an identifier, instead of
  silently dropping one.

### Data-loss and correctness fixes

Breaking:

- `set_default_bases` takes `base_frequency` from the graph's `BaseFrequency.frequency`, as
  it already took `base_power` from `BasePower`. A 50 Hz model used to get 60 Hz. Several
  BaseFrequency objects that disagree, or one that disagrees with an explicit
  `base_frequency`, raise `ValueError`.
- `XMLFile` and `JSONLDFile` raise when a file is missing (`FileNotFoundError`) or malformed
  (`ParseError`, `json.JSONDecodeError`). They used to log a warning and return an empty or
  partial graph. For an empty in-memory model, pass `connection=None` to the model.
- `GraphModel.modify` validates the value against the attribute's datatype and raises
  `TypeError` (the check never ran before). Text is converted (`'12.5'` to `12.5`), an object
  fits an association to any of its base classes, and `None` clears an optional attribute.
- `GraphModel.create`, `modify` and `delete` keep both ends of an association in sync:
  `create(cim.Terminal, ConductingEquipment=line)` adds the terminal to `line.Terminals`.
- `GraphModel.find_by_attribute` matches whole values (`'L1'` no longer finds `'L10'`). Use
  `find_by_condition` for partial matches.
- `GraphModel.first` returns `None` for a class with no objects (was `[]`), and `next` returns
  `None` after the last object (it raised `StopIteration`); the call after that starts over.
  `next` skips objects deleted since `first`.
- `GraphModel.delete` raises `TypeError` for anything but a CIM object (e.g. the class
  `cim.PositionPoint`) and `ValueError` for an object that is not in the graph. It used to do
  nothing. (#155)
- `GraphModel`'s internal state (`_class_iter`, `_mrid_index`, `_mrid_count`, formerly
  `__class_iter__`, `__mrid_index__`, `__mrid_count__`) is no longer a constructor argument or
  part of its repr.
- `GraphModel.from_incremental` raises `ValueError` for a file that is not `.xml`.
- CIM difference models. `GraphModel.incrementals` holds every `create`, `modify` and `delete`
  since the model was loaded, and every difference file written is that full set:
  `incremental_file` of `create`, `modify`, `delete` (new) and `from_incremental` (new) writes
  the same file as `write_all_incrementals`. (It wrote only the changed object's entry.)
  - `delete` records the deletion (it recorded nothing). A deleted object is a typed element
    (`<cim:Terminal rdf:about=...>`) in the reverse differences, with its values from before
    any change; references to it from other objects are recorded as removed.
  - A created object is a typed element in the forward differences, so its class is known
    (it was an `rdf:Description`). An object created and then deleted leaves no difference.
  - A value changed back to its original leaves no difference, and the reverse difference
    keeps the value from before the first change.
  - An association is recorded on the end that is serialized: `modify(line, 'Terminals', [t])`
    records `Terminal.ConductingEquipment` on `t`. A list writes only the added items forward
    and the removed items reverse.
  - The file declares the namespaces of its classes' profiles, also extension namespaces,
    and the `DifferenceModel` has an `rdf:about`. `NAMESPACES` in `incremental_builder` is
    now only `rdf` and `dm`; its `cim` entry was read once at import.
- `GraphModel.from_incremental` applies a difference file: it creates, modifies and deletes
  objects through `create`, `modify` and `delete`, so the inverse associations and
  `incrementals` are as if the changes had been made on the model. Applying the file another
  model wrote gives the same objects and the same `incrementals`. Every difference is checked
  first: an unknown class, object, attribute or referenced object, or a value that does not fit
  its attribute, raises `ValueError` and the model is not changed. (It dropped such differences
  with an error and applied the rest, and could not create or delete objects.) A reverse value
  that differs from the current value is a warning. Enumerations and unit values are read.
- `read_incremental_xml` reads references and enumerations (`rdf:resource`; they were
  `None`), repeated properties as lists, and the class of typed elements.
- Removed from `cimgraph.models.incremental_builder`: `validate_incremental` and
  `modify_from_incremental` (use `apply_incremental(model, message)` or
  `GraphModel.from_incremental`), `new_obj_incremental`, `del_obj_difference`,
  `modify_incremental`, `add_to_incremental`, `incremantal_row` and `REVERSE_NS`.
  `sync_inverse_references`, `clean_inverse_reference` and `add_inverse_reference` take the
  `differences` to record into.
- `cimgraph.utils.write_csv` is removed. It could not run.
- `cimgraph.utils.download_mermaid` is removed. Rendering through mermaid.ink never worked
  reliably; render the text from `get_mermaid` with any Mermaid tool instead.

Fixes:

- `GraphDBConnection.update` and `upload` send the update to the `/statements` endpoint. They
  re-ran the last query instead.
- `get_all_edges` and `get_all_attributes` on SPARQL endpoints (Blazegraph, GraphDB) run up to
  `MAX_PARALLEL_QUERIES` (8) batch queries at once, and parse the results on the calling thread.
  Before, threads shared one SPARQLWrapper and the graph, so batches could be skipped or run
  twice. Each query now gets its own SPARQLWrapper. Neo4j batches now really overlap, with the
  same limit; before, each batch called `asyncio.run`, so they ran one after another.
- `get_all_attributes` sets associations to the referenced object when it is already in the
  graph, else to its identifier text. Writers serialize that text as a reference
  (`rdf:resource`, `@id`). Before, the value was the raw query text, which replaced object links
  and could pass through int/float conversion (an association to a `PositionPoint` contains
  "int"). GridAPPS-D `get_all_attributes` no longer adds objects to the graph. RDFlib
  `get_all_attributes`, whose query never returned `?identifier`, works. (#159)
- Enumerations in extension namespaces (`gad`, `eu`, ...) are read by every database adapter
  (SPARQL, RDFlib, Neo4j, GridAPPS-D). One routine, `ConnectionInterface.enum_from_iri`, accepts
  an enumeration IRI in the namespace its enumeration declares, or in `CIMG_NAMESPACE`. Edge
  queries take the class name after `#`, so references to extension classes (`gad:BatteryInfo`)
  are no longer dropped. Blazegraph's hard-coded GMDM namespace list and the
  `SPARQLEndpointConnection._get_namespaces` hook are removed. (#160)
- `GraphModel.delete` no longer makes a loop over an association skip objects:
  `for point in location.PositionPoints: network.delete(point)` deleted only every other point,
  and left the rest in the graph without a Location. The association list is now replaced, not
  changed in place. `cimgraph.utils.create_object` keys the graph by the object's identifier,
  as the readers do; for a non-UUID ID it used the ID text, so `delete` could not find the
  object. (#155)
- `DistributedArea.build_from_topo_message` reads `UnaddressableEquipment`. It read
  `AddressableEquipment` twice, so unaddressable equipment was lost.
- The XML reader resolves references written in any identifier style. A reference to an
  `rdf:about="#_<uuid>"` object was dropped.
- JSON-LD reading:
  - Names and timestamps that contain `:` and `.` are kept. They were dropped as failed
    enumerations. A value is an enumeration only if the attribute's datatype is that enumeration.
  - Typed literals (`{"@value": "2.5", "@type": "cim:Length.km"}`) are read, with units.
  - References to non-UUID `@id`s resolve.
  - `JSONLDFile(filename=[...])` reads a list of files into one graph, like `XMLFile`.
- Incrementals:
  - Recording a change from `None` to an object no longer raises.
  - Unit and list values can be written.
- Every `GraphModel`, including `DistributedArea`, starts with empty `forwardDifferences` and
  `reverseDifferences`.
- `Identity.__str__` (cimprofiles) builds its JSON in one step, so a name containing `"` or `[`
  no longer breaks `pprint` and dumps.

## 0.5.0 (v0.5.0a2 – v0.5.0a12, 2026-06-21 – 2026-08-26)

### Breaking changes
- Removed the `cim_override` argument from connection constructors (`XMLFile`, `Neo4jConnection`,
  `GraphDBConnection`, `GridappsdConnection`, `MySQLJSONConnection`, `SPARQLEndpointConnection`,
  `ConnectionInterface`). Select a profile with `CIMG_CIM_PROFILE` instead, including a
  comma-separated list for a merged profile. (a2)
- Replaced the integer `CIMG_IEC61970_301` setting with `CIMG_IEC61970_552` (`'552-NEW'` or
  `'552-LEGACY'`). Connections expose `iec61970_552` instead of `iec61970_301`, and
  `get_iec61970_552()` replaces `get_iec61970_301()`. The old variable still works with a
  `DeprecationWarning`. (a2)
- Removed the `EVSE1` and `MassPerLength` exports from `cimhub_2026`. (a2)

### Added
- `cimgraph.data_profile.cgmes_3_0_0`, a CGMES 3.0.0 profile package with sub-profiles for core
  equipment, equipment boundary, operation, short circuit, SSH, SV, topology, geographical
  location and diagram. (a2)
- Runtime profile merging: a comma-separated `CIMG_CIM_PROFILE` builds one module containing the
  union of the listed profiles' classes and fields. Merged modules are cached per spec string. (a2)
- `merge_releases.yaml` and `scripts/build_merged_profiles.py` generate committed, pre-merged
  profile modules such as `cim18gmdm` and `cgmes_3_0_0`. (a2)
- `XMLFile(metadata=...)` reads an IEC 61970-552 metadata graph, resolves the `dcat:Distribution`
  part files, and loads them into one graph. (a2)
- `XMLFile` accepts a list of filenames and parses each part into one graph. (a2)
- `GraphModel.cim` field, so a model carries its CIM profile module. (a5)
- Per-unit (`pu`), currency (`USD`) and `Ohm` CIM units. (a11)
- `Neo4jConnection.upload()`, which serializes the graph to RDF/XML and loads it with the n10s
  `rdf.import.inline` procedure, and `Neo4jConnection.execute_with_params()` for parameterized
  Cypher. (a11)

### Changed
- CIM profile modules regenerated from CIMTool 2.3 (`cimhub_2023`, `cimhub_2026`, `cim16v33`,
  `cim17v40`, `cim18gmdm`). (a2)
- README rewritten around `CIMG_CIM_PROFILE`, merged profiles, `.cimx` metadata loading and a full
  environment-variable table. (a2)
- `GraphModel.upload()` on an `XMLFile` connection writes the model to XML. (a2)
- `BusBranchModel` uses the connection's CIM profile, and initialization keeps objects the caller
  has already built. (a2)
- `gridappsd-python` requirement raised to `>=2026.2.1`. (a11)

### Fixed
- `create_object` no longer raises `KeyError` when the graph has no entry for the class yet. (a5)
- `get_object` normalizes string identifiers to UUIDs so they match stored keys. (a2)
- The incremental writer's enumeration branch was unreachable. It now emits enum references. (a2)
- `Identity` serialization handles stray instance attributes and expands `CIMUnit` values. (a2)
- Inverse-reference lookup only considers `Association` fields. (a2)
- Merging profiles with conflicting base classes fails with a clear error. Non-default field
  ordering no longer breaks the merged dataclasses. (a3)
- Pint's "Redefining" warnings are suppressed while the CIM unit definitions load. (a3)
- Mermaid diagram output reworked (wrapping, enum and role handling, unit display). (a2, a7)
- GraphDB upload posts to the `/statements` endpoint. (a12)

## 0.4.3 (v0.4.3a0 – v0.4.3a12, 2025-10-23 – 2026-04-01)

### Breaking changes
- Removed the `cimgraph.data_profile.ufls`, `cimgraph.data_profile.cimhub_ufls` and
  `cimgraph.data_profile.cim17gad` profiles. (a3)
- `cimgraph.data_profile.cim18gad` is now a single CIM18v15 module; the `cim18gad.line` and
  `cim18gad.pmu` subpackages were removed. (a3)
- `GraphModel.find_by_attribute()` matches when the value is a substring of the attribute
  (`str(value) in str(attr)`) instead of requiring equality. (a11)

### Added
- `cimhub_2026` data profile, including wire info and regulating-control PT-ratio classes. (a12)
- `merge_profiles()` and `generate_type_stubs()` in `cimgraph.data_profile.merge`, which combine
  sub-profile modules (e.g. `cim18gmdm.connectivity` + `cim18gmdm.electrical`) into one runtime
  profile. (a11)
- `JSONLDFile` parser (`cimgraph.databases.fileparsers.json_ld_parser`) for JSON-LD input. (a10)
- `SPARQLEndpointConnection` (`cimgraph.databases.sparql_endpoint`), a shared SPARQL
  implementation that replaces logic duplicated across the Blazegraph, GraphDB and RDFlib
  connections. (a8)
- `cimgraph.core.env_vars` with the `CIMG_*` configuration getters, still re-exported from
  `cimgraph.databases`. (a6)
- `extract_namespaces_from_header()` on the XML parser, which reads RDF namespaces from the file
  header. (a7)
- `write_xml(..., enforce_rdf_direction=False)` option. (a3)
- `cim18gmdm` additions: series compensator R and X, `UsagePoint` and other missing canonical
  classes, and `crsUrn` on location. (a0, a1)
- Asset classes for `cim17v40`. (a5)
- `py.typed` marker so type checkers recognize the package. (a7)
- MkDocs documentation site and notebooks moved into the repo. (a10)

### Changed
- Packaging moved from Poetry to PEP 621 metadata with a Hatchling build backend; development
  uses `uv`. (a10)
- Example notebooks moved from `examples/` into the docs. (a10)
- `cim16v33`, `cim17v40`, `cim18gad` and `cim18gmdm` profiles regenerated with RDFS
  documentation. (a3, a4)
- The XML writer emits `CIMUnit` values with an `rdf:datatype` attribute. (a7)
- `CIMUnit` supports `float()`, `int()` and `.to(unit)`, and accepts `CIMUnit` or pint `Quantity`
  inputs. (a6, a7)
- Updated to the latest `gridappsd-python`. (a7)

### Fixed
- JSON-LD writer output. (a0)
- Neo4j `get_all_attributes`. (a1)
- Unit multiplier handling for CIM units. (a6, a7)
- Duplicate objects created for non-UUID identifiers. (a10)

## 0.4.1 (v0.4.1a0 – v0.4.1a2, 2025-07-09 – 2025-09-09)

### Breaking changes
- `cim18gmdm` is split into subpackages (`asset`, `canonical`, `connectivity`, `diagram`,
  `electrical`, `location`, `marketnode`). The flat `cimgraph.data_profile.cim18gmdm.cim18gmdm`
  module was removed.

### Added
- `cim17gad` canonical profile and `cim18gad` line and PMU profile modules.
- `kgPerm` unit symbol (kg/m) in `UnitSymbol`.

### Fixed
- `BlazegraphConnection` calls `super().__init__()`, so parent attributes such as `log_level`
  are initialized.
- `GridappsdConnection` passes `graph` to `get_all_attributes_sparql`, fixing edge queries.
- `write_xml` and `Identity` serialization write `CIMUnit` attributes as their numeric value.

## 0.4.0 (v0.4.0a2 – v0.4.0a3, 2025-07-03 – 2025-07-09)

### Breaking changes
- Removed `CIM_PROFILE.CIMHUB_UFLS` and `CIM_PROFILE.UFLS`.
- `write_xml` defaults to `write_identifier=True` (was `False`).

### Added
- `CIM_PROFILE.CIM16V33` and `CIM_PROFILE.CIM18GMDM` enum members.

### Changed
- `GraphModel.list_by_class` returns objects sorted by `uri()`.
- `write_xml` writes classes in name order and objects in `list_by_class` order, so output is
  deterministic.
- `cim18gmdm` profile regenerated.
- Errors while cleaning inverse references are logged as warnings instead of raised.

## 0.3.2 (v0.3.1a1 – v0.3.2a4, 2025-03-20 – 2025-07-03)

### Breaking changes
- SPARQL query helpers (e.g. `get_object_sparql`) no longer take a `connection_params` argument.
  Connections are configured from environment variables.

### Added
- Environment-based configuration with `CIMG_*` variables: `CIMG_CIM_PROFILE`, `CIMG_URL`,
  `CIMG_HOST`, `CIMG_PORT`, `CIMG_DATABASE`, `CIMG_USERNAME`, `CIMG_PASSWORD`, `CIMG_NAMESPACE`,
  `CIMG_IEC61970_301`. See `example.env`.
- Units support enabled with `CIMG_USE_UNITS`, built on `CIMUnit`, `UnitSymbol` and
  `UnitMultiplier` in `cimgraph.data_profile.units`. `pint` is now a declared dependency.
- `CIMG_VALIDATION_LOG_LEVEL` and `CIMG_ALLOW_UNDEFINED_ATTRIBUTES` control validation logging and
  handling of undefined attributes.
- CIM 16 v33 (`cimgraph.data_profile.cim16v33`) and CIM 18 GMDM (`cimgraph.data_profile.cim18gmdm`)
  data profiles.
- `Identity.identifier` (a `UUID`), which supersedes `mRID`. The XML parser and `write_xml` read and
  write it.
- `CIMStereotype` enum and `stereotype` decorator in `cimgraph.data_profile.identity`.
- Incremental change tracking on `GraphModel` (`cimgraph.models.incremental_builder`):
  `create(..., incremental_file=...)`, `modify()`, `from_incremental()`,
  `write_all_incrementals()`, with incremental messages written as XML.
- Model query helpers on `GraphModel`: `first()`, `next()`, `list_by_class()`, `iter_by_class()`,
  `find_by_attribute()` and `find_by_condition()`.
- SHACL support in `cimgraph.shacl` (`SHACLExportFilter`, `SHACLCatalogProcessor`), plus
  `GraphModel.export_with_shacl()` and `export_with_shacl_and_serialize()` for XML or JSON-LD output.
- Mermaid class diagrams render unit classes and `CIMStereotype` labels.

### Changed
- `ConnectionParameters` is deprecated in favor of the `CIMG_*` environment variables.
- `GridappsdConnection` reads its configuration from environment variables and sets the
  `GRIDAPPSD_*` variables from them. `gridappsd-python` pinned to `^2025.3.2a1`.
- CIMTool plugin XSL updated to 3.0 (`cimantic-graphs.xsl`); `cimantic-graphs-2.3.xsl` removed.
- `cim17v40` and `cimhub_ufls` profiles regenerated.

### Fixed
- Cached environment-variable lookups are cleared when a Neo4j, GraphDB or GridAPPS-D connection
  is created, so changed `CIMG_*` values take effect.
- XML parser `add_to_graph` handling.
- `get_object` and CIM profile handling in SPARQL upload and Blazegraph.

## 0.2.2 (v0.2.1.a0 – v0.2.2a4, 2025-03-03 – 2025-03-12)

### Breaking changes
- Removed `CIM_PROFILE.CIMEXT_2022`, which had no matching profile module.
- In `cim17v40`, `ServiceRequestKind.turn-off` / `turn-on` renamed to `turn_off` / `turn_on`.
- `BlazegraphConnection.get_object()` parameter renamed from `mrid` to `mRID` to match
  `ConnectionInterface`.

### Added
- `cimgraph.utils.mermaid`: `get_mermaid`, `get_mermaid_path`, `add_mermaid_path` and
  `download_mermaid` (fetches rendered images from mermaid.ink), with docs in `mermaid.md`.
- `CIM_PROFILE` members `CIM17V40`, `CIMHUB_UFLS` and `UFLS`.

### Changed
- All database connectors, `GraphModel` and `get_all_data` look up classes and enums with
  `getattr()` instead of `eval()`, so class names from query results are no longer evaluated as code.
- `mysql-connector-python` raised to `^9.2.0`; `gridappsd-python` changed to `>=2025.3.1a1`.
- Added the `mermaid-python` dependency and removed `rdflib-neo4j`.

### Fixed
- `FeederModel` builds the distributed model only when `topology_message` is non-empty.
- `BlazegraphConnection.get_object()` no longer uses a mutable `{}` default for `graph`.
- Corrected the `WorkTimeScheduleKind` entry in the known-problem classes list.

## 0.1.7a0 (2025-02-05)
- JSON-LD output via `cimgraph.utils.write_json_ld`.
- Profile attributes carry namespace metadata; `IdentifiedObject` gains `DiagramObjects` and
  `TargetingCIMDataObject` associations.
- `DistributedArea.build_from_topo_message` builds distributed models from a GridAPPS-D JSON-LD
  topology message; `DistributedArea` and `FeederModel` reworked.
- `gridappsd-python` raised to `^2025.2.1`.

## 0.1.6a0 (2024-12-11)

### Breaking changes
- Minimum Python raised to 3.10.
- `XMLParser` rewritten and renamed to `XMLFile`.
- `cimgraph` no longer re-exports `ConnectionParameters`, `BusBranchModel`, `FeederModel`,
  `GraphModel` or `NodeBreakerModel`; import them from `cimgraph.databases` / `cimgraph.models`.
- Removed `distributed_hierarchy` and the bundled `.rdfs` profile files.

### Added
- `cim17v40`, `cimhub_ufls` and `ufls` data profiles and the shared `identity` module;
  `rc4_2021` and `cimhub_2023` regenerated.
- `XMLFile.upload()`.
- `get_all_attributes` for the RDFlib backend; `pprint` uses attribute names.
- Experimental pint-based unit classes in `cimgraph.data_profile.units` (`pint` was not yet a
  declared dependency).
- CIMTool XSLT plugin and XSLT-based profile builder (`CIMTool_plugin/`).

### Changed
- Neo4j and Cypher node and edge lookups use UUIDs.

## 0.1.5a0 (2024-02-08)
- Fixed Blazegraph dropping edge objects (new `BlazegraphConnection.add_to_graph`).
- `GridappsdConnection` defaults to `http://localhost:8889/bigdata/namespace/kb/sparql` when no
  `url` is given.
- Fixed a missing object in `DistributedArea`.

## 0.1.4a0 (2024-02-01)
- Fixed `GridappsdConnection`: `params` renamed to `connection_params`, and `disconnect()` now
  calls `self.gapps.disconnect()`.

## 0.1.3a0 (2024-01-25)
- Loosened `gridappsd-python` from `^2023.9.1` to `^2024`.

## 0.1.2a0 (2024-01-22)
- `RDFlibConnection` accepts `filename=None`. An unparseable file logs a warning and starts an
  empty graph.

## 0.1.1a0 (2023-12-27)
- Same code as 0.1.0b0.

## 0.1.0b0 (2023-12-27)

Initial public release.

### Models
- `FeederModel` (distribution feeders), `NodeBreakerModel` (EMS node-breaker) and `BusBranchModel`
  (bus-branch planning), built on a common `GraphModel` with `container`, `connection` and
  `distributed` arguments. Objects are stored in `graph[cim.ClassName][mRID]`.
- `distributed=True` builds `DistributedArea` graphs per topological area (`distributed_areas`),
  optionally from a GridAPPS-D `topology_message`.
- `get_all_edges(cim.ClassName)` expands the graph one association hop at a time;
  `get_edges_query()` returns the query text for debugging.
- `pprint()` and `__dumps__()` print or export a class's instances as JSON (optionally JSON-LD).
- `upload()` writes graph changes back to the connection; `new_mrid()` generates UUIDs.

### Database connections
- `ConnectionParameters` dataclass (`cim_profile`, `url`, `host`, `port`, `database`, `username`,
  `password`, `namespace`, `iec61970_301`, `filename`).
- `GridappsdConnection`, `BlazegraphConnection`, `GraphDBConnection`, `Neo4jConnection`,
  `RDFlibConnection` (Oxigraph store), `MySQLJSONConnection` and `XMLParser` for CIM XML files.
- `ConnectionInterface` base class for custom connectors.
- Query builders for SPARQL (including `upload_triples`), Cypher, GraphDB, MySQL JSON and RDFlib.

### CIM profiles
- `cimgraph.data_profile.rc4_2021` and `cimgraph.data_profile.cimhub_2023`, generated from XSD with
  xsdata and importable as `import cimgraph.data_profile.rc4_2021 as cim`.
- `CIM_PROFILE` enum of profile names.

### Utilities
- `write_xml` (CIM XML) and `write_csv` (one CSV per class, zipped).
- `get_all_data` and per-category loaders (`get_all_line_data`, `get_all_transformer_data`,
  `get_all_load_data`, `get_all_switch_data`, `get_all_bus_data`, `get_all_measurement_data`, ...).

### Packaging
- Published to PyPI as `cim-graph`; requires Python `>=3.8.1,<4.0`.
