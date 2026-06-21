# cim-graph 0.5 — Profile identity as a single source of truth

**Status:** proposal / plan only (no code yet)
**Target release:** 0.5 (breaking change; current `main` is 0.4.3a12)
**Author of record:** to be filled by maintainer

---

## 1. The problem

cim-graph resolves "which CIM profile am I using" from the `CIMG_CIM_PROFILE`
environment variable, via `cimgraph/core/env_vars.py::get_cim_profile()`:

```python
cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)
```

That returns **one importable module**, e.g.
`cimgraph.data_profile.cim18gmdm.connectivity`. Its `ACLineSegment` is a
specific dataclass object.

Runtime profile merging (`data_profile/merge.py::merge_profiles`) was added so a
split export (connectivity + electrical + asset + …) can be read into one graph
without a hand-maintained `canonical.py` mega-profile. The merged profile is
passed to a connection via `cim_override=`, and the connection correctly stores
it (`databases/__init__.py:76-80`: `self.cim = cim_override`,
`self.cim_profile = 'merged'`).

> **Note on `cim_override`.** That kwarg was introduced in the same 0.4.3a11
> commit as `merge.py`, purely to prove the merge concept. Nothing in the
> codebase or any consumer repo passes it except two cim-graph tests
> (`test_merge_profiles.py:194`, `test_blazegraph_seto.py:109`). 0.5 **removes
> it entirely** (§"Retiring `cim_override`") and replaces it with the env-var
> comma-spec, which is the supported, zero-plumbing way to select a merge.

**But the model re-derives the profile independently of the connection it was
handed.** `FeederModel.__post_init__` (and `NodeBreakerModel`,
`BusBranchModel`) do:

```python
cim_profile, cim_module = get_cim_profile()   # reads the env var
self.cim = cim_module
```

This produces two distinct failures.

### Failure 1 — silent class-identity mismatch

The graph is **built through `connection.cim`** (the merged module), so every
object in `network.graph` is an instance of `merged.ACLineSegment`. But
`network.cim` was set from the env var to `connectivity.ACLineSegment`. These
are different class objects. They duck-type identically, so nothing raises — but
every identity-based operation silently misbehaves:

- `isinstance(self.container, self.cim.Feeder)` — `feeder_model.py:128`,
  `sparql_endpoint.py:259`, `distributed_area.py:33/46`, `gridappsd.py:115`,
  `neo4j.py:216`. Compares against the wrong `Feeder` class → wrong branch taken.
- `graph[self.cim.Terminal]`, `graph[self.cim.ConnectivityNode]` —
  `mysql.py:85-90` and the universal `graph[type, dict[UUID, object]]` keying.
  The graph dict is **keyed by class object**; a non-identical `Terminal` class
  is a key miss → "no terminals found" when there are thousands.
- Downstream `network.graph[network.cim.ACLineSegment]` lookups in consumer
  repos return empty.

The notebook `EPRI-GMDM-II/test_model/9500node_merge_metadata.ipynb` papers over
this with a manual `network.cim = merged` after construction. That only works
because the author knew the failure existed. It is not a fix; it is a landmine.

### Failure 2 — the env var cannot name a merged profile

`get_cim_profile()` resolves a **single module path** via `import_module`. A
runtime-merged profile has no module path, so the env var is structurally
incapable of naming it. Consequences:

- The merge path *requires* passing `cim_override` to a connection. There is no
  zero-plumbing way (the original point of the env var) to select a merge.
- If `canonical.py` is deleted — and it genuinely duplicates the sub-profile
  parts — there is no longer any single-module profile that spans all the GMDM
  parts to point the env var at. The env var becomes unsatisfiable for that
  family.

### Why the env var existed (the ergonomics we must not lose)

The env var let a deeply-nested leaf helper resolve the profile with **no
plumbing** — no connection or model threaded down through every call. Example
(`CIM-Builder/cimbuilder/object_builder/base/new_base_voltage.py:27`):

```python
def new_base_voltage(network: GraphModel, base_voltage, name=None):
    cim_profile, cim_module = get_cim_profile()   # no connection in scope
    cim = cim_module
    ...
```

Any redesign has to preserve that ergonomics, or it is a regression for the
~40 leaf helpers across CIM-Builder / CIMHub.

---

## 2. The design: layered profile-identity contract

One profile object — the one the graph is built from — is the single source of
class identity. Every layer either *chooses* it or *reads* it; no layer
re-derives it.

```
┌─ Connection ──────────────────────────────────────────────────────────┐
│  Chooses the profile — from ONE source after 0.5:                       │
│    self.cim = get_cim_profile()   (env var; comma-spec → merged module) │
│  The cim_override kwarg is removed (§"Retiring cim_override"). The merge │
│  arrives via the comma-spec, resolved+cached in get_cim_profile().      │
└─────────────────────────────────────────────────────────────────────────┘
              │ self.cim  (the authoritative class set)
              ▼
┌─ GraphModel / FeederModel / NodeBreakerModel / BusBranchModel ─────────┐
│  Carries the profile. Sourced FROM the connection:                      │
│    self.cim = self.connection.cim   (when a connection exists)          │
│    else fall back to get_cim_profile()  (no-connection construction)    │
│  DistributedArea ALREADY does this (distributed_area.py:15-16).         │
│  The three top-level models must be made consistent with it.            │
└─────────────────────────────────────────────────────────────────────────┘
              │ network.cim  (same object — graph keys & isinstance now match)
              ▼
┌─ Leaf helpers (CIM-Builder builders, CIMHub get_utils, etc.) ──────────┐
│  Read the profile off the model they already receive:                   │
│    cim = network.cim          ← NOT get_cim_profile()                    │
│  Already proven: CIMHub get_substation.py:11 does exactly this, with     │
│  the old get_cim_profile() line commented out right above it.           │
└─────────────────────────────────────────────────────────────────────────┘
```

The env var is the **single profile source** consumed inside the connection
constructor, plus the no-model construction fallback for models. It is never a
second, independent source a model or leaf re-derives from. With `cim_override`
gone, `get_cim_profile()` is the *only* way a merged module enters the system —
which makes the §3 cache-identity guarantee load-bearing, not optional.

### The env var gains the ability to name a merge

To keep zero-plumbing selection *and* let `canonical.py` go away, extend the
**syntax** the env var accepts (decided: comma-separated module list):

```bash
CIMG_CIM_PROFILE="cimgraph.data_profile.cim18gmdm.connectivity,\
cimgraph.data_profile.cim18gmdm.electrical,\
cimgraph.data_profile.cim18gmdm.asset"
```

```python
# get_cim_profile(), conceptually:
parts = [p.strip() for p in cim_profile.split(',') if p.strip()]
if len(parts) == 1:
    cim = import_module(_qualify(parts[0]))      # UNCHANGED — 0.4 behavior
else:
    mods = [import_module(_qualify(p)) for p in parts]
    cim = merge_profiles(*mods)                  # NEW — built once, see §3
```

- **One part → today's behavior verbatim.** Fully backward compatible; every
  existing repo keeps working untouched.
- **Two+ parts → a merged module**, selectable with no connection in scope.
- `merge_profiles` is *not* currently re-exported from
  `data_profile/__init__.py`; `env_vars.py` would import it directly from
  `cimgraph.data_profile.merge`. (Watch for import cycles — `env_vars` is low in
  the stack; import lazily inside the function.)

---

## 3. The cache-identity hazard (must be solved with the syntax, not after)

`get_cim_profile()` is `@cache`d on its (empty) args, and **`cache_clear()` is
called in every connection `__init__`**: `xml_parser.py:25`, `graphdb.py:26`,
`neo4j.py:35`, `databases/__init__.py:70`, `gridappsd.py:27`,
`json_ld_parser.py:21`, plus `incremental_builder.py:92`.

If the merge is rebuilt on every cache miss, then constructing two connections
for the same merged env var yields **two different merged modules** →
`connA.cim.ACLineSegment is not connB.cim.ACLineSegment` → Failure 1 returns,
now *across connections* instead of across model/connection. Accumulating a
split read across multiple `XMLFile`s (the canonical multi-file use case) is
exactly this scenario.

**Requirement:** a given comma-spec string must always resolve to the **same
merged module object** for the life of the process, surviving the `cache_clear()`
churn. Options to evaluate (pick during implementation):

1. **Module-level memo keyed by the normalized spec string**, independent of the
   `@cache` that `cache_clear()` wipes. `merge_profiles` results are cached in a
   plain `dict[str, ModuleType]`; `cache_clear()` only resets the cheap env-var
   read, not the expensive merged build. Cheapest, keeps identity stable
   **within cim-graph** — but see the hard requirement below: a private memo is
   *not sufficient* for `import`-based consumers.
2. **Install the merged module in `sys.modules`** under its canonical name, so
   `importlib.import_module(name)` *and* a plain `import …name as cim` statement
   in any consumer both round-trip to the same object. Heavier and it occupies an
   import name — but for the target state (§3a) this is **mandatory, not
   optional**: it is the only mechanism that serves consumers who reach the
   profile via `import`, not via `network.cim`.
3. **Audit and reduce the `cache_clear()` calls.** They exist so a test that
   re-sets the env var mid-process is honored. Reconsider whether every
   connection needs to clear; possibly clear only when the env var actually
   changed. Larger blast radius; defer.

This section is a *gate*: the comma-merge syntax is not done until same-spec →
same-object identity is guaranteed.

### 3a. The target state forces option 2: `cimhub_2026` *becomes* a merge

The decided end goal is that **`cimhub_2026` stops being a 953 KB generated
`.py` file and becomes a runtime merge** of its sub-profiles — that is the whole
reason this cross-repo plan exists. The single-file profile is what makes the
Pylance ">1000 dataclasses" explosion and the canonical-maintenance burden
unavoidable; a merge dissolves both. **But it raises the identity bar.**

Today, every CIMTool-generated converter resolves the profile by *importing it
by name*:

```python
import cimgraph.data_profile.cimhub_2026 as cim   # in dozens of converter files
@registry.register(cim.ACLineSegment)             # registry key = this object
... network.graph.get(cim.ACLineSegment) ...      # graph key must == this object
```

(Live example: `CIMHub_2_0/cimhub_opendss/.../exporter/lines/ac_line_segment.py`
and `.../exporter/cim_to_dss.py`. The registry is a raw `dict[type, callable]`
keyed on the class object — `cimhub_core/.../registry.py` — no `__name__`
fallback, no MRO walk. Identity is the only key.)

This works **only because `cimhub_2026.py` is a real file**: the first `import`
caches one module object in `sys.modules`, and every later `import` — in the
converter, in `EXPORT_ORDER`, in whatever built the graph — returns that same
object. The single file *is* the identity guarantee, by accident of being
importable.

The moment `cimhub_2026` is a runtime merge, **a private memo (option 1) cannot
serve those `import` statements.** A converter that does
`import cimgraph.data_profile.cimhub_2026 as cim` at its own module-load time
goes through `sys.modules`, not through `get_cim_profile()`'s dict — so it would
capture *no* module (ImportError) or the *old* generated file, never the merge.

**Therefore, for the target state, the canonical merge must be installed in
`sys.modules['cimgraph.data_profile.cimhub_2026']` before any converter imports
it**, so that:

```
import …cimhub_2026 as cim   (converter, at registration)   ┐
EXPORT_ORDER[(cim.ACLineSegment, …)]                         ├─ all the SAME
network.graph.get(cim.ACLineSegment)  (built via the merge)  ├─ ACLineSegment
network.cim.ACLineSegment             (model carries it)     ┘  object
```

The `get_cim_profile()` memo (option 1) and the `sys.modules` entry (option 2)
must point at the **same** object — option 1 for cim-graph's own
`network.cim` flow, option 2 for the import-based consumer flow. They are not
alternatives; the target state needs both, with option 2 as the canonical home
and the memo as a same-object alias.

> **Sequencing hazard — does not apply here.** `cimhub_2026` is already a
> package (`cimhub_2026/__init__.py`), so `import cimgraph.data_profile.cimhub_2026`
> already runs `__init__.py` on first import. Replacing the re-export in that
> file with a `merge_profiles(...)` call means the merge is built at the moment
> the package is first imported — no converter can capture a stale flat module
> ahead of it, because no flat module is in play. The `cimantic-graphs-init.xsl`
> already generates this package layout; the only XSL change needed is in the
> body of the generated `__init__.py`.

---

## 4. Blast-radius assessment (verified against the three consumer repos)

Searched `CIM-Builder`, `CIM-Loader`, and all ~20 `CIMHub_2_0/cimhub_*`
packages for: `CIMG_CIM_PROFILE`, `get_cim_profile`, `cim_override`,
`connection.cim`, model instantiation, `.cim =` assignment, and model
subclassing.

**Key finding: `cim_override` appears in NONE of the three repos.** Every
consumer selects its profile via `CIMG_CIM_PROFILE` and lets it flow through.
So the "connection wins" change only has teeth in the *new* merged path that no
downstream code uses yet — the non-merged path is behavior-identical because
`connection.cim` already equals `get_cim_profile()` when no override is given.

| Repo | How it selects the profile | Effect of "connection wins" | Effect of comma-merge env var |
|------|----------------------------|-----------------------------|-------------------------------|
| **CIM-Builder** | Sets `CIMG_CIM_PROFILE`; leaf builders call `get_cim_profile()` directly; models built with **no override** | None — `connection.cim` == env-var module | None until it opts into a comma-spec |
| **CIM-Loader** | Connection classes set `self.cim` from `get_cim_profile()` in `__init__`; models built with that connection | None — model reads the same module the connection set | None until opt-in |
| **CIMHub_2_0** | `os.environ.setdefault("CIMG_CIM_PROFILE", ...)` per package; `FeederModel/NodeBreakerModel(connection=XMLFile(""), container=None)` everywhere | None — `XMLFile("")` sets `connection.cim` from env var; model reads it. **`cimhub_core`/`cimhub_powersimulator` already do `cim = network.cim`** — change makes them *more* robust | None until opt-in |

No model subclassing exists in any repo (all `(...Model)` grep hits are
docstrings/type comments). No repo will break on the non-breaking core (§6
Phase 1).

---

## 5. Leaf-helper migration pattern

The fix for leaf helpers is **not** to thread a connection through every call —
they already receive a `network: GraphModel`. The migration is one line:

```python
# BEFORE (re-derives from env var; wrong class identity under a merge)
cim_profile, cim_module = get_cim_profile()
cim = cim_module

# AFTER (reads the profile off the model that owns the graph)
cim = network.cim
```

Precedent already in the tree:
`CIMHub_2_0/cimhub_core/src/cimhub_core/get_utils/get_substation.py:11` does
`cim = network.cim` with the `get_cim_profile()` line commented out above it.

Helpers that genuinely have **no** model/connection in scope (pure
constructors) keep using `get_cim_profile()` — now merge-capable via the comma
syntax — so they are still served with zero plumbing.

The runtime swap is only half the leaf story; the edit-time typing model that
goes with it (per-method single-profile annotations) is **§5a**, and
`line_builder.py` is the worked example for both.

---

## 5a. Static typing for merged profiles (the leaf-builder model)

The runtime fix (`cim = network.cim`) leaves an edit-time question: a merged
module **does not exist as a file**, so Pylance can only see `network.cim` as
`ModuleType`/`Any` — no completions, no field checking. The first intended
merge consumer, `CIM-Builder/.../line/line_builder.py`, is a hand-written sketch
exploring how to solve this. Its `cim: EQ = get_cim_profile()` lines are *not*
runtime code to fix — they are probing the typing contract. The recommended
model formalizes what that sketch is reaching for.

### Runtime vs. edit-time are deliberately split

| | What `cim` is | Why |
|---|---|---|
| **Runtime** | `network.cim` — the merged module. One `ACLineSegment` object carries **every** profile's fields. | Class identity correctness (the 0.5 thesis). |
| **Edit time** | annotated as a **single** sub-profile per method (`cim: CN`, `cim: EQ`, …) via `TYPE_CHECKING` imports. | Scopes each builder method's **write access** to one profile's fields. |

So the annotation is a **profile-scoping contract, not a typing hack.** A
per-method single-profile annotation is *narrower than the runtime truth on
purpose*: it tells Pylance "in this method you may only touch this profile's
fields."

```python
if TYPE_CHECKING:
    import cimgraph.data_profile.cim18gmdm.connectivity as CN
    import cimgraph.data_profile.cim18gmdm.electrical   as EQ

class LineBuilder(ObjectBuilder):
    network: GraphModel
    container: "CN.EquipmentContainer"

    def add_connectivity(self, name, node1, node2) -> "CN.ACLineSegment":
        cim: CN = self.network.cim          # runtime: merged module
        line = cim.ACLineSegment(name=name) # edit time: only CN fields offered
        ...                                 # `line.r = ...` here would (correctly) flag —
                                            #  r is an electrical field, wrong method

    def add_electrical(self, line: "EQ.ACLineSegment", r, x, bch, ...):
        cim: EQ = self.network.cim          # same object, electrical slice
        line.r = cim.Resistance(r, r_unit or 'ohm')
```

### Why scoping by profile is the right boundary

- **Guardrail:** `line.r` inside `add_connectivity` is a category error — `r` is
  an electrical field. The narrowed `cim: CN` makes Pylance reject it, so the
  partition is enforced at edit time, not discovered at runtime.
- **No file on disk:** no `.pyi`, no `generate_type_stubs` output, no canonical
  import. The `TYPE_CHECKING` imports of the real sub-profile modules are the
  only machinery; they are erased at runtime.
- **It maps 1:1 to the planned UI (Phase 42 goal).** A GUI ribbon "Add Line" →
  a wizard with **one page per profile** (Connectivity → Electrical →
  Short-circuit), user fills or clicks Next. Each wizard page is backed by one
  `add_<profile>` method, and that method's `cim: <PROFILE>` annotation is
  exactly the set of fields the page renders. The type narrowing and the UI step
  structure are the same boundary.

### The one wrinkle to name (so it isn't mistaken for a type bug)

`cim: CN` is narrower than the runtime module (which has all profiles' fields).
That is correct for **writes**. If a method ever needs to **read** a field that
belongs to another profile on the same object, Pylance will flag it — that flag
is the signal to move the read into the method scoped to that profile, not to
widen the annotation. The constraint is healthy; document it rather than
defeating it.

### Alternatives considered (and why not)

- **`.pyi` via `generate_type_stubs`** — most accurate (reflects the actual
  merged class), but reintroduces a generated file on disk and offers *all*
  fields everywhere, losing the per-method scoping that is the point.
- **Union annotation `cim: CN | EQ | AST`** — no disk file, but unions *all*
  fields into every method, again losing the write-scoping guardrail.
- **`Any` at the leaf** — no completions, no guardrail.

The per-method single-profile annotation is the only option that gives
completions *and* enforces the profile partition *and* needs no stub file.

---

## 5c. Static typing for merged profiles (the exporter/converter model)

§5a covers the **write** side (builders): annotate `cim` *narrow* — one
sub-profile per method — to scope what each method may populate. The **read**
side (exporters, converters) is the mirror image and needs the opposite
treatment.

A converter reads many profiles' fields off **one** object in **one** function.
Live example — `cimhub_opendss/.../exporter/lines/ac_line_segment.py`,
`convert_ac_line_segment(segment: cim.ACLineSegment, …)`:

- `segment.Terminals[0].ConnectivityNode.name` — **connectivity**
- `segment.r`, `segment.x`, `segment.bch` (as `cim.Resistance` / `cim.Susceptance`) — **electrical**
- `segment.ACLineSegmentPhases[i].WireInfo` (`cim.ConcentricNeutralCableInfo`, …) — **asset**
- `segment.EarthResistivity.rho` — **location/asset**

There is no per-method profile partition to enforce here — reading across
profiles is the converter's *job*. So the annotation must be the **full merged
profile**, the wide pole:

| | §5a builder (write) | §5c converter (read) |
|---|---|---|
| Annotation | per-method single sub-profile (`cim: CN`) | the whole merged profile (`import …cimhub_2026 as cim`) |
| Intent | *narrow* — scope writes to one profile | *widen* — read every profile's fields at once |
| Cross-profile access | flagged (a guardrail) | required (the point) |

This is exactly why **the merge must be importable by name** (§3a). The
converter already writes `import cimgraph.data_profile.cimhub_2026 as cim` and
annotates `segment: cim.ACLineSegment`. For those annotations to type-check
*today*, `cimhub_2026.py` exists as a file Pylance can read. Once it becomes a
merge, the file is gone and `cim.ACLineSegment` is unresolvable to the type
checker — **this is the case `generate_type_stubs` was built for**:

- emit `cimhub_2026.pyi` (the full merged class surface) next to a thin runtime
  shim that installs the `sys.modules` merge (§3a);
- Pylance reads the `.pyi` → converter signatures resolve, wide reads complete;
- CPython imports the shim → gets the live merged object, identity intact.

So the `.pyi` answers a **typing** need on the wide/read pole, while §3a answers
the **identity** need on the runtime side. They are independent: the `.pyi`
without the `sys.modules` install gives green type-checks over a registry that
silently exports nothing; the `sys.modules` install without the `.pyi` gives a
correct runtime with red squiggles over every converter. The target state needs
**both**, and `generate_type_stubs` already produces the `.pyi` half.

> Contrast with §5a deliberately: a `.pyi` is **wrong** for the builder (it
> surfaces all fields everywhere, destroying the write-scoping), but **right**
> for the converter (which legitimately needs all fields). Same merge, opposite
> typing treatment, because writes are scoped and reads are not.

### A silent-failure guard the converter needs regardless

`cim_to_dss.py` dispatches `network.graph.get(cim_class, {})` wrapped in
`try/except (AttributeError, TypeError): return []`. A dict `.get()` raises
neither, so a **wrong-identity key** (the exact Failure-1 symptom: graph built
from object A, `EXPORT_ORDER` keyed on object B) yields an empty `.values()` and
exports **zero** rows with no error. Under "Fail Fast," when a class is in
`EXPORT_ORDER` *and* has a registered converter but is absent as a `network.graph`
key, that is a profile-identity mismatch and should warn loudly — it would have
turned the 9500 merge's silent no-op into an immediate diagnostic. (Consumer-repo
fix, noted here because it is the same root cause this plan addresses.)

---

## 5b. Retiring `cim_override`

`cim_override` was added in 0.4.3a11 alongside `merge.py` as proof-of-concept
plumbing — a way to hand a runtime-built merged module to a connection before
the env var could name one. The audit confirms it never graduated to real API:

- **No consumer repo passes it.** CIM-Builder, CIM-Loader, and all ~20
  `CIMHub_2_0/cimhub_*` packages: zero occurrences.
- **Only two callers exist**, both cim-graph tests: `test_merge_profiles.py:194`
  and `test_blazegraph_seto.py:109`. (Plus docstring examples in `merge.py`.)
- Where it's *implemented*, it's mostly **duplicated** — the same
  `if cim_override is not None: self.cim = cim_override else: get_cim_profile()`
  branch is copy-pasted into `xml_parser.py`, `neo4j.py`, `gridappsd.py`,
  `mysql.py`, and `json_ld_parser.py` instead of delegating to the base
  `ConnectionInterface.__init__` (`databases/__init__.py:67`). The forwarding
  classes (`sparql_endpoint`, `graphdb`, `rdflib`, `blazegraph`) already just
  call `super()`.

The comma-spec env var subsumes its only real use (selecting a merge), **and**
restores zero-plumbing selection (which `cim_override` never gave a leaf helper).
So 0.5 removes the kwarg from all nine connection classes:

```python
# ConnectionInterface.__init__ after removal — one source, no branch
def __init__(self):
    get_cim_profile.cache_clear()
    self.cim_profile, self.cim = get_cim_profile()   # comma-spec → merged
    ...
```

**Test migration (no capability lost).** Both proof tests already set
`CIMG_CIM_PROFILE` separately from building the merge; they collapse to the
comma-spec and drop the kwarg:

```python
# test_merge_profiles.py — BEFORE
monkeypatch.setenv('CIMG_CIM_PROFILE', 'cimgraph.data_profile.cim18gmdm.connectivity')
merged = merge_profiles(connectivity, electrical)
file = XMLFile(filename=str(_ROUND_TRIP_MODEL), cim_override=merged)

# AFTER
monkeypatch.setenv('CIMG_CIM_PROFILE',
    'cimgraph.data_profile.cim18gmdm.connectivity,'
    'cimgraph.data_profile.cim18gmdm.electrical')
file = XMLFile(filename=str(_ROUND_TRIP_MODEL))
# get the merged module the resolver built, to assert against the graph key:
_, merged = get_cim_profile()
```

The two niche capabilities `cim_override` technically allowed —
profiles **built programmatically** (not nameable as a string) and **two
profiles in one process** — have no current users and are explicitly out of
scope for 0.5. If a real need appears later, the resolver (not a per-connection
kwarg) is where it should live.

---

## 6. Phased rollout

### Phase 1 — non-breaking core (can land before 0.5, on 0.4.x)
Backward-compatible; no consumer repo changes required.

1. **Models prefer `connection.cim`.** In `FeederModel`, `NodeBreakerModel`,
   `BusBranchModel` `__post_init__`: set `self.cim = self.connection.cim` when a
   connection exists, else `get_cim_profile()`. Mirror `DistributedArea`.
   Resolves the abandoned TODO at `node_breaker_model.py:47`.
2. **`get_cim_profile()` comma-merge syntax** with the §3 same-spec→same-object
   guarantee. One-part path byte-for-byte unchanged.
3. **`cimantic-graphs-init.xsl` — emit merge-based `__init__.py`.** Change the
   generated `__init__.py` body from a flat re-export to a `merge_profiles(...)`
   call that installs itself into `sys.modules` under its canonical name (§3a).
   Every profile that adopts the new XSL output automatically becomes import-safe
   for `import …<profile> as cim` consumers (registries, `EXPORT_ORDER`, graph
   keys all resolve to the same merged object). The `cimhub_2026` package already
   has the right directory structure (`__init__.py` + sub-profile packages
   following the `cim18gmdm` pattern); no directory layout change is needed,
   only the XSL template body.
4. **Tests:** (a) model built from a comma-spec connection has
   `network.cim is connection.cim`; (b) `isinstance` / `graph[cim.X]` keying
   works end-to-end under a merge — no manual `network.cim = merged`; (c)
   comma-spec env var with one part == today; with N parts == `merge_profiles`;
   (d) two connections from the same comma-spec share the merged object identity;
   (e) `import cimgraph.data_profile.cimhub_2026 as cim` after the XSL change
   returns the merged module and `cim.ACLineSegment is network.cim.ACLineSegment`.
5. **Update `9500node_merge_metadata.ipynb`:** delete the `network.cim = merged`
   workaround; select the merge via the env-var comma-spec.

Note: removing `cim_override` (§5b) is the one **breaking** item that can't ride
on 0.4.x — it changes nine constructor signatures. If Phase 1 lands on 0.4.x,
keep `cim_override` working there (it's harmless once models prefer
`connection.cim`) and remove it at the 0.5 cut. If everything goes on a 0.5
branch, remove it in Phase 1.

### Phase 2 — leaf-helper migration (consumer repos, coordinated)
Per repo, swap `get_cim_profile()` → `network.cim` in helpers that receive a
model. Mechanical; covered by each repo's own tests. Order: CIMHub_2_0 (most
helpers, partly migrated) → CIM-Builder → CIM-Loader.

### Phase 3 — `canonical.py` deprecation (0.5, breaking)
1. Inventory every `CIMG_CIM_PROFILE=...canonical` / `import ...canonical`
   across all repos (grep + the XSL builders that emit it).
2. Provide the comma-spec (or a tiny re-export shim module, the §"merge syntax"
   option B) as the replacement for each canonical user.
3. Deprecation warning in `canonical.py` for one minor, then remove in 0.5.
4. Update the CIMTool builder docs / `9500node_exports.ipynb` to show the
   merge workflow instead of the canonical + chained-`FeederModel` trick.

### Phase 4 — 0.5 cut
- Drop the deprecated `canonical.py`.
- **Remove `cim_override`** from all nine connection classes (§5b); migrate the
  two proof tests to the comma-spec.
- Document the layered contract (§2) as the supported model.
- Changelog: the breaking changes below.

---

## 7. 0.5 breaking-change callouts

- **`cim_override` removed** from all connection constructors. The only callers
  were two cim-graph tests (migrated to the comma-spec); no consumer repo used
  it. Selecting a merge is now done via `CIMG_CIM_PROFILE` (comma-spec).
- **`canonical.py` removed.** Anyone naming it in `CIMG_CIM_PROFILE` or importing
  it directly must switch to a comma-spec or a re-export shim. (Phase 3 provides
  the migration + a deprecation cycle first.)
- **`model.cim` now follows the connection, not the env var.** Code that built a
  model with a connection whose profile differed from `CIMG_CIM_PROFILE` and
  *relied on the model showing the env-var profile* will change behavior. No such
  case found in the three audited repos; flagged for completeness.
- **`CIMG_CIM_PROFILE` accepts a comma-separated list.** A profile module path
  containing a literal comma would now be mis-split — not a realistic module
  name, but documented.

---

## 8. Open questions for maintainer review

1. §3 cache strategy: option 1 (spec-keyed memo) serves `network.cim`, but §3a
   establishes that the **target state requires option 2** (`sys.modules`
   install) to serve `import …cimhub_2026 as cim` consumers. Confirm both, with
   option 2 canonical and option 1 as a same-object alias.
1a. **§3a sequencing/replaceability — resolved, low risk.** `cimhub_2026` is
   *already a package* (`cimhub_2026/__init__.py` + `cimhub_2026/cimhub_2026.py`),
   generated by `CIMTool_plugin/cimantic-graphs-init.xsl`. The `__init__.py`
   currently re-exports everything from `cimhub_2026.py`; changing it to call
   `merge_profiles(...)` instead is the entire implementation of §3a. No
   sequencing hazard exists — `import cimgraph.data_profile.cimhub_2026 as cim`
   already runs `__init__.py` on first import; there is no flat `.py` file that
   can be cached in `sys.modules` ahead of the merge. `cim18gmdm` already
   demonstrates the sub-profile package layout (`connectivity/`, `electrical/`,
   `asset/`, …) that `cimhub_2026` will adopt. The XSL change is confined to
   `cimantic-graphs-init.xsl`: emit `merge_profiles(...)` instead of the
   flat re-export.
2. Phase 3: comma-spec vs. a hand-written re-export shim module as the
   `canonical.py` replacement — or offer both?
3. Should `merge_profiles` be re-exported from `data_profile/__init__.py` for
   ergonomics, given `env_vars.py` will import it (mind cycles)?
4. Version/branch: land Phase 1 on a `0.4.x` alpha, or gate everything behind a
   `0.5` branch from the start? (Decides when `cim_override` is removed — see
   Phase 1 note.)
5. Confirm the two niche `cim_override` capabilities (programmatically-built
   profile; two profiles in one process) can stay out of scope for 0.5, with the
   resolver as the future home if needed (§5b).
