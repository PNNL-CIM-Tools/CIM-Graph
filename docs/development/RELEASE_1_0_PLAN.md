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

| # | Bug | Where | Fix | Test |
|---|---|---|---|---|
| 2.1 | GraphDB `upload()`/`update()` never sends the update: `_update_raw` builds `updater` and then calls `self.connection_obj.query()` | `graphdb/graphdb.py:55` | `return updater.query()` | Unit test with a mocked SPARQLWrapper asserting the `/statements` endpoint is hit |
| 2.2 | `get_all_edges` thread race: batches share one stateful SPARQLWrapper (`setQuery` then `query`), and threads write unlocked to shared graph dicts | `sparql_endpoint.py:465` | Run sequentially (simplest), or give each worker its own SPARQLWrapper and merge results on the main thread | Fake `_execute_raw_query` that records queries: every batch is run exactly once |
| 2.3 | `DistributedArea` loops over `AddressableEquipment` twice, so unaddressable equipment is lost | `models/distributed_area.py` (4 occurrences) | The second loop of each pair uses `UnaddressableEquipment` | Topology-message fixture (`tests/topo_message.json`) |
| 2.4 | `GraphModel.modify` never validates: `validate_attr_datatype` returns a 3-tuple, which is always truthy | `models/graph_model.py:310`, `core/attribute_utils.py:63` | `valid, _, value = validate_attr_datatype(...)`; fix the `-> bool` annotation | `modify(line, 'length', 'not-a-number')` raises |
| 2.5 | `.strip('urn:uuid:')` strips characters, not the prefix, so UUIDs ending in those characters get truncated | `models/incremental_builder.py:71` | `removeprefix('urn:uuid:')` | A UUID ending in `d` survives |
| 2.6 | Incremental builder: mutates global `NAMESPACES['dm']`; validates against the env profile instead of `connection.cim`; `old_value.uri()` on `None`; `set()` of unhashable values; `open()` without a context manager | `models/incremental_builder.py` | Local namespace copy, `connection.cim`, None guard, list instead of set, `with open` | Round-trip `tests/test_models` incremental fixture |
| 2.7 | File parsers treat every failure as "not found" and return an empty graph | `xml_parser.py:65`, `json_ld_parser.py` connect, `rdflib.py` load | Remove the bare except and let `FileNotFoundError` / `ParseError` / `EntitiesForbidden` raise | Malformed file raises; missing file raises |
| 2.8 | XML `rdf:about="#_<uuid>"` fails: `parse_nodes` doesn't strip `#` but `parse_edges` does | `xml_parser.py::parse_nodes` | Normalize through one helper (4.1) | 552-OLD fixture with `rdf:ID` + `rdf:about="#_..."` loads |
| 2.9 | JSON-LD drops any string containing both `:` and `.` (names, timestamps) as a failed enum; typed literals (`{"@value","@type"}`) are dropped | `json_ld_parser.py:253` and the reference branch | Enums only when the value matches `<Enum>.<member>` and the enum is in the profile (1.6); handle `@value`/`@type` and units | `"Line 1: 12.47kV"` and an ISO timestamp round-trip |
| 2.10 | `JSONLDFile` annotated `str \| list[str]` but raises on a list | `json_ld_parser.py:18,31` | Support lists like `XMLFile` | Two-file load |
| 2.11 | `format='xml'` calls `_create_xml_catalog`, which doesn't exist | `shacl/shacl_catalog_processor.py:170` | Implement it or remove the option | |
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
- **4.2 One enum-detection routine** replaces the four copies (`sparql_endpoint.py`,
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

  See `PROFILE_IDENTITY_0_5_PLAN.md`.
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
  - `utils.create_object` (duplicates `ConnectionInterface.create_object`)
  - no-op `distributed=True` on BusBranch/NodeBreaker (raise instead)
  - `NodeBreakerModel.aggregate_lower_areas`
- **Rename before freezing:**
  - `__dumps__` → `dumps`
  - `__class_iter__` → private
  - drop the stateful `first()`/`next()` in favour of `iter_by_class`/`list_by_class`
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
