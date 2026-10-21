# Changelog

## 0.6.0a1 (unreleased)

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
| `rdflib` | `RDFlibConnection`, `cimgraph.shacl` |
| `all` | everything |

Using a connection without its driver raises an `ImportError` naming the extra to install.
`requests` (used by `cimgraph.utils.mermaid`) is now a direct dependency. The unused
`mermaid-python` dependency was dropped.

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
