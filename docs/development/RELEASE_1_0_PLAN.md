# cim-graph 1.0 — security and stability fix plan

**Status:** plan. Every item below was re-verified against `profile_writer` @ 548492a plus the
uncommitted identity/header work, on 2026-10-17.
**Source:** release audit (security, core/models, adapters/parsers, packaging), 2026-10-17.
**Goal:** move from 0.5.0a12 to 1.0.0 with no known data-loss or injection bugs, a tested offline
suite in CI, and a frozen public API.

---

## 0. Already done (uncommitted on `profile_writer`)

| Change | Files |
|---|---|
| Identity equality: `==`/`hash` by `identifier`; generated classes use `@dataclass(eq=False)`; CIMUnits keep value equality | `data_profile/identity.py`, `merge.py`, `build_merged_profiles.py`, `CIMTool_plugin/cimantic-graphs.xsl`, all generated profiles |
| `diff_attributes(a, b)`: one-level attribute comparison | `core/attribute_utils.py` |
| `add_object_to_graph` raises on identifier collision instead of silently dropping | `databases/__init__.py`, `models/graph_model.py` |
| Class name always part of the UUID seed (mRID/URI seeds left it out) | `data_profile/identity.py` |
| Default `CIMG_MODEL_AUTHORITY = 'CIManticGraphs'` (was `user@hostname`) | `core/env_vars.py`, `README.md` |
| XML reader reads `md:FullModel` / `cim:ModelAuthority`, sets the model scope per part file, and keeps header elements out of the graph | `fileparsers/metadata.py`, `fileparsers/xml_parser.py`, `core/env_vars.py::set_model_scope` |
| Tests | `tests/test_equality.py`, `tests/test_uuid.py`, `tests/test_xmlfile.py` |

Breaking changes for the CHANGELOG:
- Seeded UUIDs from non-UUID mRIDs/URIs change (the class is now in the seed).
- The default authority changed.
- Objects compare by identifier.
- `add_to_graph` can raise.

---

## Ground rules

- **One workstream = one branch/PR.** File ownership is listed per workstream so parallel agents
  don't collide. `databases/__init__.py` is shared by WS2, WS3 and WS4. Land WS3's lazy-import
  change first, then rebase the other two on it.
- **Every fix ships with an offline test.** Use the XML/RDFlib backends, or canned
  SPARQL-binding / Neo4j-record fixtures for the server adapters.
- Follow AGENTS.md: fail fast, no bare `except:`, no fallbacks.
- Don't touch `utils/write_xml.py` or `databases/mysql/` without checking with whoever owns them.

## Order

```
WS3a (pytest config + CI)  ──►  everything else (CI now gates PRs)
WS3b (lazy imports/extras) ──►  WS2, WS4 (they edit databases/__init__.py)
WS1 (security)                 independent, start immediately
WS2 (data-loss bugs)           after WS3b
WS4 (adapter consistency)      after WS2 (it reuses WS2's identifier helper)
WS5 (API freeze + docs)        last; needs WS1–WS4 merged
→ 1.0.0rc1 → soak → 1.0.0
```

---

## WS1 — Security (start now)

Owns: `queries/`, `core/serialization.py` escaping, `fileparsers/metadata.py`, `utils/mermaid.py`,
`models/incremental_builder.py` (validation parts), `shacl/shacl_exporter.py`, `.github/workflows/`,
`docker-compose.yml`, `core/env_vars.py` (credentials).

**Status (2026-11-08, uncommitted on `cimprofiles-0.6`): done in the repo. Regression tests are
in `tests/test_security.py` (45 tests).**

| Item | Outcome |
|---|---|
| 1.1 | New `core/validation.py`: `validate_identifier` / `validate_attribute`, called in the SPARQL and Cypher builders that interpolate raw strings. Removed the `container.mRID` bare-except fallbacks. Object-derived identifiers are always UUID text, so they were already safe. **Cypher `$param` binding is deferred to WS3b:** reads go through `execute_read`, and `execute_with_params` uses `execute_write`. |
| 1.2 | `validate_incremental` / `modify_from_incremental` rewritten around `_graph_object`, `_difference_object` and `_converted_value`. No per-URI state can leak between objects. Attributes are checked against the class and its MRO, values are converted, and `modify` raises on unvalidated input. Also fixed 2.5, 2.6's `NAMESPACES` mutation and env-profile validation, and the 2-tuple unpack bug in `validate_attr_datatype`'s list branch. Later replaced by `apply_incremental` (see Diff models in WS2), which keeps these checks and also rejects the whole file instead of dropping parts of it. |
| 1.3 | `resolve_part_paths` raises `ValueError` when an `accessURL` leaves the metadata directory. Checked before `exists()`, so files outside it can't be probed either. |
| 1.4 | `eval()` removed from `utils/mermaid.py`. Path steps are parsed by regex; only dataclass fields, `[int]` and `__subclasses__()[int]` are allowed. |
| 1.5 | String references must be valid IRI text (`validate_iri_text`). `rdf:resource` values are XML-escaped, and SPARQL literals escape `\n`/`\r`. |
| 1.6 | All six parser enum lookups go through `ConnectionInterface.profile_enum`, which only returns members of `Enum` classes in the profile's `__all__`. |
| 1.7 | `get_username` / `get_password` raise when unset (no `system`/`manager`). GridAPPS-D passes credentials to `GridAPPSD(...)` instead of `os.environ`. The compose file binds to localhost, requires Neo4j auth, and turns APOC file import/export off. |
| 1.8 | **Resolved by removal:** `cimgraph/shacl/` (the exporter and catalog processor) and `GraphModel.export_with_shacl*` were deleted, at the maintainer's decision (the ABAC experiment is retired). Also closes 2.11. |
| 1.9 | `RDFlibConnection` requires a local file and parses it as RDF/XML. Also closes 2.7 for rdflib (no more "not found → empty graph"). |
| 1.10 | Trusted Publishing via `uv publish --trusted-publishing always`, in a separate `publish` job with `environment: pypi` and `id-token: write`. Top-level `contents: read`; all actions pinned to commit SHAs; tj-actions replaced by `git diff`. **Maintainer action is required on PyPI and GitHub** (see below). |
| 1.11 | Lock upgraded: urllib3 2.8.0, certifi, virtualenv 21.15.6, filelock, tornado. `pip-audit` is clean on Python ≥3.11. On 3.10, tornado 6.5.10 and filelock 4.1.0 have no fixed release; both come only through the `dev` extra. |
| 1.12 | Verified: every value is parameterized, and table and column names come from `information_schema` or profile metadata checked against the schema. Hardening suggestion for the MySQL owner: reject names containing `"` or `'` in `build_schema`. |

Maintainer actions for 1.10, before the next release run:
1. On PyPI (`cim-graph` → Publishing), add a GitHub trusted publisher for each of
   `release.yml`, `dev-pre-release.yml` and `dispatch-pypi.yml`, with environment `pypi`.
2. In GitHub repo settings, create the `pypi` environment (optionally with required reviewers).
3. Delete the `PYPI_TOKEN` repository secret and revoke the token on PyPI.

### 1.1 Query injection (High)
- **Where:**
  - `queries/sparql/get_object.py:32` and `get_triple.py:31` (`VALUES ?identifier {"%s"}' % mRID`)
  - `queries/sparql/get_all_nodes.py` (`get_all_nodes_from_list`, container fallback)
  - `queries/cypher/get_object.py:25` (`n.uri = "{split+mRID}"`)
  - `queries/cypher/get_triple.py:26,30`: the `` `{attribute}` `` backtick labels break out on a backtick.
- **Entry points carrying untrusted strings:**
  - `GraphModel.get_object(mRID)`
  - `SPARQLEndpointConnection.build_graph_from_list` (GridAPPS-D topology messages)
  - `incremental_builder` reading difference files
- **Fix:**
  - Add `validate_identifier(value: str) -> str` (new, in `core/`). It accepts a UUID with an
    optional leading `_`, or a strict legacy pattern `^[A-Za-z0-9_.-]+$`, and raises
    `ValueError` otherwise. Call it in every query builder that interpolates an mRID.
  - Predicates and attributes: require `attribute in cim_class.__dataclass_fields__` (the
    `Class.attr` form) before building the query.
  - Cypher: pass mRIDs as parameters (`$uri`) via the existing `execute_with_params`.
    Labels can't be parameterized, so validate them.
- **Test:** an mRID like `x"} } UNION { ?a ?b ?c } #` raises `ValueError` before any query is
  built, for both the SPARQL and Cypher builders.

### 1.2 Incremental builder trusts message contents (Medium; also a data-integrity bug)
- **Where:** `models/incremental_builder.py`.
  - The forward loop has no `continue` after an invalid UUID.
  - `found` and `obj` are never reset per URI, so differences for an unknown mRID get applied to
    the previous object.
  - `modify_from_incremental` calls `setattr(obj, attr, new_value)` (line 212) with an
    unchecked attribute and value.
  - Validation reads `getattr` before checking the attribute exists.
- **Fix:**
  - Reset `obj = None` per URI.
  - Raise (or skip with an error) on unknown mRIDs.
  - Require `attr in obj.__dataclass_fields__`.
  - Run `validate_attr_datatype`, and fix its return so it is checked (see 2.4).
- **Test:** a difference file with an unknown URI followed by a known one leaves the known
  object untouched by the unknown one's differences. An unknown attribute raises.

### 1.3 Path traversal in 557 metadata (Medium)
- **Where:** `fileparsers/metadata.py::resolve_part_paths` (`(base / relative).resolve()` at
  line 177, no containment check).
- **Fix:** `if not part_path.is_relative_to(base.resolve()): raise ValueError(...)`.
- **Test:** an `accessURL="../../etc/passwd"` raises.

### 1.4 `eval()` on caller strings (Medium)
- **Where:** `utils/mermaid.py` has five `eval(...)` calls (`add_object_path_mermaid`,
  `get_mermaid_path`).
- **Fix:**
  - Parse `name[index]` path segments with a regex, then use `getattr` plus `int(index)`.
  - Resolve class names with `getattr(sys.modules[cls.__module__], name)`.
- **Test:** existing `tests/test_mermaid.py` passes, and a path containing
  `__class__.__init__.__globals__` raises.

### 1.5 Serializer escaping (Low)
- **Where:** `core/serialization.py`.
  - Bare string references go unescaped into `rdf:resource="..."` and SPARQL `<...>`.
  - `_sparql_literal` escapes `\` and `"` but not `\n` or `\r`.
- **Fix:**
  - XML-escape attribute values.
  - Reject IRIs containing `<>"{}|^\`` or whitespace.
  - Escape newlines in SPARQL literals.
- Coordinate with the write_xml owner.

### 1.6 Enum lookup by unchecked name (Low)
- **Where:**
  - `fileparsers/xml_parser.py` enum branch (`getattr(self.cim, enum_class)(value)` under
    `except: pass`)
  - `fileparsers/json_ld_parser.py`
  - `databases/sparql_endpoint.py` enum detection
- **Fix:** require `name in self.cim.__all__ and issubclass(cls, Enum)`. Shares the helper with
  4.2.

### 1.7 Credentials (Medium)
- `core/env_vars.py:20-21`: default `system`/`manager` is used with only a warning. Raise when
  a connector that needs credentials has none set.
- `databases/gridappsd/gridappsd.py:44-49`: `connect()` writes the user and password into
  `os.environ`. Pass them to the `GridAPPSD(...)` constructor instead.
- `docker-compose.yml`:
  - Neo4j runs with `NEO4J_AUTH=none`, APOC file import/export on, and ports on `0.0.0.0`.
  - Bind to `127.0.0.1`, require auth, and turn APOC export off.
  - Label the file dev-only.

### 1.8 SHACL export filter fails open (Medium)
It's an access-control filter, so failures must deny.
- **Where:** `shacl/shacl_exporter.py`:
  - An exception in a condition returns `True`.
  - An unknown condition type, a malformed path, or a missing attribute means "allowed".
  - A failed conditional parse turns the class into an unfiltered root.
  - A failed property-type lookup goes into `allowed_attributes`.
  - Stub objects leak identifiers.
- **Fix:** every failure path either denies or raises.
- **Test:** a malformed shape exports nothing for that class.

### 1.9 rdflib parse (Low)
- **Where:** `databases/rdflib/rdflib.py` calls `Graph.parse(filename)` with a guessed format.
  A `.jsonld` file or a URL can fetch remote contexts.
- **Fix:** pass `format=` explicitly and require a local path.

### 1.10 CI supply chain (Medium)
- Switch `release.yml`, `dev-pre-release.yml` and `dispatch-pypi.yml` to PyPI Trusted
  Publishing: `pypa/gh-action-pypi-publish`, with `id-token: write` on the publish job only and
  a GitHub `environment: pypi`. Then revoke `PYPI_TOKEN`.
- `dispatch-pypi.yml:14` exposes the token in workflow-level `env`; remove it.
- Add `permissions: contents: read` at the top of every workflow, and widen per job only where
  needed.
- Pin third-party actions to commit SHAs: `tj-actions/changed-files`,
  `ncipollo/release-action`, `astral-sh/setup-uv`. Consider replacing tj-actions with
  `git diff --name-only`.

### 1.11 Dependency CVEs
`uv lock --upgrade-package urllib3 --upgrade-package tornado --upgrade-package virtualenv`.
Only urllib3 (≥2.8) matters at runtime.

### 1.12 MySQL SQL building
bandit B608 no longer fires on `databases/mysql/` at HEAD. Confirm with the MySQL owner that
every table and column name is checked against `schema.py` and every value is parameterized.

---

## WS2 — Data loss and correctness bugs

Owns: `databases/graphdb/`, `databases/sparql_endpoint.py`, `databases/fileparsers/` (except
the header code), `models/` (except the incremental validation in WS1), `shacl/shacl_catalog_processor.py`,
`data_profile/build_merged_profiles.py`, `utils/write_csv.py`.

**Status (2026-11-08, uncommitted on `cimprofiles-0.6`): done. Regression tests are in
`tests/test_correctness.py` (15 tests) and CIM-Profiles `tests/test_identity_str.py`.**

| Item | Outcome |
|---|---|
| 2.1 | `_update_raw` returns `updater.query()`. |
| 2.2 | `SPARQLEndpointConnection.run_batch_queries` runs the batch queries on up to `MAX_PARALLEL_QUERIES` threads (`BATCH_SIZE` and the limit are in `databases/__init__.py`). Results are parsed in order on the calling thread. `_execute_raw_query` must be thread-safe: Blazegraph and GraphDB make one SPARQLWrapper per call. `get_all_attributes` shares the same path. Neo4j's runner awaits instead of calling `asyncio.run`, behind a semaphore. RDFlib (in-process) and GridAPPS-D (one STOMP client) stay sequential. |
| #159 | `ConnectionInterface.create_reference` is used by every adapter's `expand_graph=False` branch. It links an object already in the graph, else stores `read_identifier` text, which the shared serializer writes as a reference. The SPARQL and RDFlib `get_all_attributes_sparql` now return the edges query, because the old queries never bound `?edge`/`?edge_class` (and RDFlib's never selected `?identifier`). |
| #160 | `ConnectionInterface.enum_from_iri` replaces the four enum copies (this is 4.2): the namespace must be the enum's declared `__namespace__` or `CIMG_NAMESPACE`. The edge queries take the class after `#`, not after the cim namespace. RDFlib takes the attribute's local name, and skips only `rdf:type` (it skipped every attribute containing "type"). |
| #155 | `clean_inverse_reference` replaces an association list instead of removing from it in place, so `for point in location.PositionPoints: network.delete(point)` deletes every point (it deleted every other one, leaving the rest orphaned). `delete` raises for a non-object or an object not in the graph instead of doing nothing. `utils.create_object` calls the new `databases.create_graph_object`, shared with `ConnectionInterface.create_object`; it keyed non-UUID IDs by their text. |
| Diff models | `create`/`modify`/`delete` record straight into `GraphModel.incrementals` with `incremental_builder.record_change`/`record_created`/`record_deleted`, all through `record_difference`: the reverse keeps each attribute's value before its first change, the forward its current value, a change back cancels, and creation/deletion is `rdf:type` None ↔ class (a typed element), so create-then-delete leaves nothing. Only serialized ends are recorded; `sync_inverse_references` records the other objects' ends. Every `incremental_file` (create, modify, delete, from_incremental) writes the full set, as `write_all_incrementals` does. Lists write only added/removed items. `read_incremental_xml` reads typed elements, `rdf:resource` and repeated properties. `from_incremental` is `apply_incremental(model, message)`: it checks everything first (raises, nothing changed), then creates, modifies and deletes through the model, so the result and `incrementals` match the model that wrote the file (round-trip test). `validate_incremental`/`modify_from_incremental` are removed; `profile_enum`/`enum_from_iri` are module functions in `databases` (the connection methods delegate) so models without a connection read enumerations. |
| 2.3 | Both `UnaddressableEquipment` loops fixed. |
| 2.4 | `validate_attr_datatype` returns `(valid, datatypes, value)` and accepts objects of a subclass. `convert_datatype` no longer turns a CIMUnit into a bare float. `modify` raises `TypeError`, sets the converted value, and allows `None` for `Optional` fields. |
| 2.6 | Remaining parts: `modify_incremental` records `None`/objects through `_difference_value`, `incremantal_row` uses `all(... is None)`, and `write_incremental` uses `with open`. |
| 2.7 | XML and JSON-LD: the bare excepts are gone, so missing or malformed files raise (rdflib was fixed in 1.9). Tests that used a missing file as an empty model now pass `connection=None`. |
| 2.8 | New `databases.reference_key(uri)`: the UUID in any serialization, else `normalize_identifier` text. The XML and JSON-LD `object_index` and every reference lookup use it. This is the start of 4.1. |
| 2.9 | An enumeration needs `prefix:Enum.member` or a full IRI (including the old `#:` form in `ieee13.jsonld`) **and** an attribute whose datatype is that enum; anything else is a literal. `{"@value","@type"}` goes to `create_value` with the expanded datatype IRI. `_lookup_class` and `class_index` were replaced by `object_index`, which also fixes references to non-UUID `@id`s. |
| 2.10 | `JSONLDFile` reads a list of files into `self.items`. `self.data` is gone. |
| 2.11 | Closed by 1.8. |
| 2.12 | Closed: the tool now lives in CIM-Profiles (`python -m cimprofiles.build_merged_profiles`), which declares pyyaml and reads its config next to the module. |
| 2.13 | `utils/write_csv.py` and its export removed. |
| 2.14 | Fixed in CIM-Profiles `identity.py`: `_json_value` builds the dump and it is serialized once. |
| 2.15 | `incrementals` and `_class_iter` (was `__class_iter__`; now `init=False, repr=False`, as are `_mrid_index` and `_mrid_count`) have real defaults on `GraphModel` (subclass re-initialization removed). `first`/`next` return `None` when there is nothing more (after which `next` starts over, and it skips deleted objects), `find_by_attribute` compares whole values (units in base SI), and `from_incremental` raises for non-`.xml`. |
| 2.16 | New `incremental_builder.sync_inverse_references`, used by `create`, `modify` and `delete`. It moves a single-valued end off its previous object and skips ends missing from the profile. `clean_inverse_reference` lost its blanket `except`, and `get_attr_inverse` lost its bare `except`. |

| # | Bug | Where | Fix | Test |
|---|---|---|---|---|
| 2.1 | GraphDB `upload()`/`update()` never sends the update: `_update_raw` builds `updater` and then calls `self.connection_obj.query()` | `graphdb/graphdb.py:55` | `return updater.query()` | Unit test with a mocked SPARQLWrapper asserting the `/statements` endpoint is hit |
| 2.2 | `get_all_edges` thread race: batches share one stateful SPARQLWrapper (`setQuery` then `query`), and threads write unlocked to shared graph dicts | `sparql_endpoint.py:465` | Run sequentially (simplest), or give each worker its own SPARQLWrapper and merge results on the main thread | Fake `_execute_raw_query` that records queries: every batch is run exactly once |
| 2.3 | `DistributedArea` loops over `AddressableEquipment` twice, so unaddressable equipment is lost | `models/distributed_area.py` (4 occurrences) | The second loop of each pair uses `UnaddressableEquipment` | Topology-message fixture (`tests/topo_message.json`) |
| 2.4 | `GraphModel.modify` never validates: `validate_attr_datatype` returns a 3-tuple, which is always truthy | `models/graph_model.py:310`, `core/attribute_utils.py:63` | `valid, _, value = validate_attr_datatype(...)`; fix the `-> bool` annotation | `modify(line, 'length', 'not-a-number')` raises |
| 2.5 | **Done in WS1 (1.2).** `.strip('urn:uuid:')` strips characters, not the prefix, so UUIDs ending in those characters get truncated | `models/incremental_builder.py:71` | `removeprefix('urn:uuid:')` | A UUID ending in `d` survives |
| 2.6 | Incremental builder: mutates global `NAMESPACES['dm']`; validates against the env profile instead of `connection.cim`; `old_value.uri()` on `None`; `set()` of unhashable values; `open()` without a context manager | `models/incremental_builder.py` | Local namespace copy, `connection.cim`, None guard, list instead of set, `with open` | Round-trip `tests/test_models` incremental fixture |
| 2.7 | File parsers treat every failure as "not found" and return an empty graph | `xml_parser.py:65`, `json_ld_parser.py` connect, `rdflib.py` load | Remove the bare except and let `FileNotFoundError` / `ParseError` / `EntitiesForbidden` raise | Malformed file raises; missing file raises |
| 2.8 | XML `rdf:about="#_<uuid>"` fails: `parse_nodes` doesn't strip `#` but `parse_edges` does | `xml_parser.py::parse_nodes` | Normalize through one helper (4.1) | 552-OLD fixture with `rdf:ID` + `rdf:about="#_..."` loads |
| 2.9 | JSON-LD drops any string containing both `:` and `.` (names, timestamps) as a failed enum; typed literals (`{"@value","@type"}`) are dropped | `json_ld_parser.py:253` and the reference branch | Enums only when the value matches `<Enum>.<member>` and the enum is in the profile (1.6); handle `@value`/`@type` and units | `"Line 1: 12.47kV"` and an ISO timestamp round-trip |
| 2.10 | `JSONLDFile` annotated `str \| list[str]` but raises on a list | `json_ld_parser.py:18,31` | Support lists like `XMLFile` | Two-file load |
| 2.11 | **Closed: `cimgraph/shacl/` removed in WS1 (1.8).** `format='xml'` calls `_create_xml_catalog`, which doesn't exist | `shacl/shacl_catalog_processor.py:170` | Implement it or remove the option | |
| 2.12 | `build_merged_profiles.py` broke when it moved into the package: `_REPO_ROOT` resolves to `cimgraph/`; imports undeclared `yaml`; mutates `sys.path` | `data_profile/build_merged_profiles.py:35-38` | Fix paths, make it a dev-only tool or declare pyyaml, drop the `sys.path` hack; also `merge.py:29` still points at `scripts/` | Run the CLI |
| 2.13 | `write_csv` is broken (wrong kwarg, `.values()` on a str, writes to cwd, `os.remove` under a bare except) | `utils/write_csv.py` | Remove it before 1.0 (nobody can be using it) | |
| 2.14 | `Identity.__str__` builds JSON by string replace, so a `"` in a name breaks `pprint` and dumps | `data_profile/identity.py` `__str__` | Build a dict and `json.dumps` it | Name containing `"[` |
| 2.15 | `GraphModel` small bugs: `from_incremental` UnboundLocalError for non-`.xml` files; `find_by_attribute` substring match (`'L1'` matches `'L10'`); `next()` StopIteration; `first()` returns `[]`; `__class_iter__` defaultdict with no factory; `DistributedArea`/SHACL-filtered models lack `incrementals['forwardDifferences']` | `models/graph_model.py`, `distributed_area.py` | Fix individually; the API shape is decided in WS5 | One test each |
| 2.16 | `create()`/`modify()` don't keep inverse associations in sync; `delete()` cleanup sits under a bare except | `models/graph_model.py` | Use `get_attr_inverse` to update both ends | Create a Terminal with `ConductingEquipment=line` and check `line.Terminals` |

---

## WS3 — Packaging, imports, CI

Owns: `pyproject.toml`, `uv.lock`, `.github/workflows/` (CI parts; coordinate with 1.10),
`.pre-commit-config.yaml`, `tests/conftest.py`, `cimgraph/databases/__init__.py` (import block only),
`cimgraph/utils/__init__.py`, `databases/neo4j/neo4j.py` (async parts).

**Status (2026-11-08, uncommitted on `cimprofiles-0.6`): 3a done; 3b done except Neo4j; 3c
partly done.**

| Item | Outcome |
|---|---|
| 3a pytest | `[tool.pytest.ini_options]`: `testpaths`, `integration(service)` marker. `tests/conftest.py` skips a marked test when nothing listens on the service's port (`SERVICES`). Only tests that connect are marked: the query-building and env-var tests in the service files run offline (173 offline tests). `test_mysql.py` uses the marker instead of its own check. |
| 3a CI | `.github/workflows/ci.yml`: tests on 3.10–3.14 (`uv sync --locked --all-extras`), a `--resolution lowest-direct` job, and ruff `E9,F63,F7,F82` only (the full lint is WS5). It runs on pull requests and is called (`workflow_call`) by `release.yml`, `dev-pre-release.yml` and `dispatch-pypi.yml`, whose build needs it. CIM-Profiles is checked out next to CIM-Graph at `CIM_PROFILES_REF` (`rc2`) for `[tool.uv.sources]`; drop that with the sources block. All three Python environments verified locally (3.13, 3.14, lowest-direct). |
| 3a strays | `tests/timing.py` and `tests/uuid_test.ipynb` removed. |
| 3b | Lazy adapter imports and per-driver extras were already done (CHANGELOG). The `dev` extra is now a `[dependency-groups]` group. The unused cimhub_2023 imports in `feeder_model.py` and `neo4j.py` are gone. **Open: Neo4j sync driver** (drop `nest_asyncio`, whose event-loop-policy calls warn on 3.14 and break on 3.16). Needs a live Neo4j or the 4.8 canned-response tests to verify. |
| 3c | PEP 639 `license = "BSD-3-Clause"` + `license-files`, `hatchling>=1.27`, a real `description`, 3.13/3.14 classifiers, `requires-python = ">=3.10"`. The wheel already leaves out the profile markdown (profiles are in cimprofiles; 341 kB, 96 files). Pre-commit gained `check-added-large-files` and the CI ruff check. **Open for the maintainer:** the `1.0.0rc1` bump and `5 - Production/Stable` (at the rc), and moving `ieee9500bal.xml` (38 MB) to LFS or a download, which rewrites history or changes the test fixture. |

### 3a. Test gate (do first)
- `pyproject.toml`: add
  `[tool.pytest.ini_options] testpaths = ["tests"]` and
  `markers = ["integration: needs a live database"]`.
- `tests/conftest.py`: per-service reachability checks (Blazegraph, GraphDB, Neo4j, GridAPPS-D,
  MySQL) that skip `integration` tests, following the `test_mysql.py::mysql_is_running` pattern.
  Mark `test_blazegraph_seto`, `test_graphdb`, `test_neo4j`, `test_gridappsd_*` and
  `test_get_all_edges`.
- New `.github/workflows/ci.yml`:
  - Triggers: PRs, plus pushes to `develop` and `main`.
  - Jobs:
    - `uv sync`
    - `pytest -m "not integration"` on Python 3.10–3.14
    - `ruff check`
    - a `--resolution lowest-direct` job
  - Make release/publish depend on it.
- Remove stray files: `tests/timing.py`, `tests/uuid_test.ipynb`.

### 3b. Optional backends
- `databases/__init__.py:316-323` imports every adapter at import time; `neo4j.py:20` runs
  `nest_asyncio.apply()` process-wide.
  - Replace the imports with a module `__getattr__` that imports the adapter on first access.
    A missing extra raises an `ImportError` naming the extra.
- `pyproject.toml`:
  - Core dependencies: `defusedxml`, `rdflib`, `oxrdflib` (needed for the Oxigraph store),
    `pint`.
  - Extras:
    - `[sparql]` = SPARQLWrapper
    - `[neo4j]`
    - `[mysql]`
    - `[gridappsd]`
    - `[all]`
  - Remove `mermaid-python` (unused).
  - Declare `requests`, or import it lazily in `mermaid.download_mermaid`.
  - Move dev tools to `[dependency-groups]`.
- Neo4j: switch to the sync `GraphDatabase` driver.
  - Drop `nest_asyncio` and the nested `asyncio.run` calls in `edge_query_runner`.
  - Make `get_all_attributes` run the attribute query only, not the full edge query.
  - Fix `disconnect()` before `connect()`.
- `feeder_model.py:6` and `neo4j.py:13` import whole profiles they don't use; remove those
  imports.
- Test: in a fresh venv with only the core install, `import cimgraph.databases;
  from cimgraph.databases import XMLFile` works. `Neo4jConnection` raises an error naming
  `pip install cim-graph[neo4j]`.

### 3c. Release mechanics
- `release.yml` only strips the prerelease suffix, so 0.5.0a12 would become 0.5.0. Bump by hand
  to `1.0.0rc1` on `develop`.
- Classifiers:
  - `5 - Production/Stable`
  - add 3.13 and 3.14
  - `requires-python = ">=3.10"`
- Use the PEP 639 license string and a real `description`.
- Leave `*.rdfs-t2b.md` (~8 MB) out of the wheel; keep them in the sdist.
- Move `tests/test_models/ieee9500bal.xml` (38 MB) to Git LFS or a download fixture. Add the
  `check-added-large-files` and ruff hooks to pre-commit.

---

## WS4 — Adapter interface consistency

Owns: `databases/*` adapters, `queries/*` (after WS1 lands its validation).

- **4.1 One `normalize_identifier(uri) -> UUID | str`** replaces about 8 variants
  (`strip('_').lower()`, `split(':')[-1]`, `strip('#')`, …) in `databases/__init__.py`,
  `sparql_endpoint.py`, `neo4j.py`, `rdflib.py`, `xml_parser.py` and `json_ld_parser.py`.
  Also drop JSON-LD `_lookup_class`'s five case/underscore fallbacks.
- **4.2 Done with #160 (see WS2).** One enum-detection routine replaces the four copies (`sparql_endpoint.py`,
  `rdflib.py`, `neo4j.py`, `gridappsd.py`). The current `split('.')[1]` raises `IndexError` on
  some literals, and Blazegraph hard-codes the GMDM namespace. Shares the gating from 1.6.
- **4.3 GridAPPS-D subclasses `SPARQLEndpointConnection`.** About 250 duplicated lines have
  drifted:
  - `expand_graph=True` in `get_all_attributes`
  - a silent `use_units = False`
  - `upload` through `query_data`

  After the change it implements only `_execute_raw_query` and `_parse_result_field`.
- **4.4 Same semantics across backends.**

  | Method | Rule |
  |---|---|
  | `create_new_graph` | adds the container |
  | `get_object` | exact match; `None` if missing |
  | `get_all_edges` / `get_all_attributes` on file backends | raise `NotImplementedError` instead of `pass` |
  | `create_distributed_graph` | returns a graph or raises |
  | `get_from_triple` | not a stub returning `[]` |

  Add `update`, `get_edges_query` and `build_graph_from_list` to the base class or stop calling
  them.
- **4.5 Resource management.** Every adapter gets `close()` plus `__enter__`/`__exit__`, and
  `disconnect()` is safe to call twice. XML/JSON-LD drop the `del` attributes.
- **4.6 SPARQL datatypes.** The edge and attribute queries select `datatype(?value)` and pass
  `datatype_uri` to `create_value`, so units work on every backend and not just XML.
- **4.7 Query layer.**
  - Delete `queries/ontotext/*` (never imported), `queries/rdflib/get_all_nodes.py` (never
    called), the empty `queries/jsonld_sql/` and `databases/piwebapi/`.
  - Hoist the batch size of 100 (hard-coded in 8 places) to one constant.
  - Import config getters from `cimgraph.core`, not `cimgraph.databases`; this fixes the
    circular import.
- **4.8 Canned-response tests for each adapter's parser**, so SPARQL, Neo4j and GridAPPS-D
  parsing get offline coverage.

---

## WS5 — API freeze and documentation (last)

- **Global profile state (Phase 0 decision, still open).** Profile, namespace and 552 format
  are cached env vars, and every connection constructor calls `cache_clear()`. Proposal:
  - `XMLFile(path, cim=module)` (explicit argument, env var as default, resolved once);
  - remove the `cache_clear` calls from constructors;
  - models take the profile from `connection.cim` only.

  See `PROFILE_IDENTITY_0_5_PLAN.md`. The profiles and `Identity` move to the separate
  `cimprofiles` package in 0.6.0; see `CIMPROFILES_0_6_PLAN.md`.
- **UUID policy (remaining).** Name-only seeding contradicts CIM #7540: names are freeform, not
  identification. Decide whether `name=` alone should give `uuid4()`.
- **Public surface.**
  - Add `cimgraph.__version__` (`importlib.metadata.version('cim-graph')`) and `__all__` in
    `cimgraph`, `core`, `databases`, `models`, `utils`.
  - Write a "covered by SemVer" statement.
- **Remove before freezing:**
  - `get_iec61970_301` / `CIMG_IEC61970_301`
  - `get_undefined_handling`
  - `core/model_authority.py` (unused, non-Identity `IdentifiedObject`)
  - the bogus `jsonld = dict['@id':...]` aliases
  - `utils.create_object` (now a thin wrapper of `databases.create_graph_object`)
  - no-op `distributed=True` on BusBranch/NodeBreaker (raise instead)
  - `NodeBreakerModel.aggregate_lower_areas`
- **Rename before freezing:**
  - `__dumps__` → `dumps`
  - ~~`__class_iter__` → private~~ done (`_class_iter`, see 2.15)
  - ~~drop the stateful `first()`/`next()`~~ kept, at the maintainer's decision: `first()` returns the same object every time the same file is read, for sanity checks (fixed in 2.15)
  - `incremantal_row` typo
  - `pprint` returns a string
- **Consolidate `__post_init__`** from Feeder/BusBranch/NodeBreaker into `GraphModel`, with one
  `graph` type.
- **Docs:**
  - Notebooks still use `ConnectionParameters(`, `cimgraph.validators.attribute_utils` and
    `get_iec`; fix them.
  - README: there is no CSV reader; docs are on GitHub Pages, not ReadTheDocs; the
    `ACLineSegement` typo; undefined `cim`/`database` in examples.
  - Remove the leftover Sphinx files.
  - Add `CHANGELOG.md` and a "Migrating from 0.x" page (everything in §0 plus WS2–WS5 removals).
  - Add `SECURITY.md`, `CONTRIBUTING.md` and a deprecation policy.
- **Lint:** about 120 ruff findings are auto-fixable; clear the 30 bare `except:`, the F821
  `'GraphModel'` string annotations in shacl, and the `from incremental_builder import *`.

---

## Verification for the release candidate

1. CI green on 3.10–3.14 with `-m "not integration"`; ruff clean outside `data_profile/`.
2. Integration job (docker-compose services) green for Blazegraph, GraphDB, Neo4j and MySQL.
3. Core-only install imports `cimgraph`, `cimgraph.databases.XMLFile` and `cimgraph.models`.
4. Round trips on real data:
   - IEEE 13/123/9500 XML → write_xml → reread, with `diff_attributes` empty for every object;
   - the GMDM split/stitch in `EPRI-GMDM-II/IEEE9500Node/9500node_exports.ipynb`;
   - a JSON-LD round trip.
5. `pip-audit` clean; `bandit -ll` triaged.
6. `1.0.0rc1` published through Trusted Publishing from a protected environment.
