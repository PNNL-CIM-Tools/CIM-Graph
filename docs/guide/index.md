# User guide

These pages are executed notebooks: each one is a runnable tutorial, and the outputs you see are real. Most of
them run offline against the models in `tests/test_models/`. The database pages need that database running
(Docker setup is on each page). To run a notebook yourself, open it from `docs/` in a checkout; the "edit"
button at the top of a page links to its source.

## Start here

1. [Overview and quick start](../01_overview/1_1_overview.ipynb): the whole library in one notebook.
2. [Installation](../01_overview/1_2_installation.ipynb): `pip install cim-graph` and the database extras.
3. [CIM profiles](../02_cim_profiles/2_1_profiles_overview.ipynb): which CIM classes you get, and how to pick a
   profile with `CIMG_CIM_PROFILE`.

## Find what you need

| You want to | Read |
|---|---|
| create objects and follow associations | [Objects, identity and associations](../02_cim_profiles/2_3_using_objects.ipynb) |
| set and read physical quantities | [Units](../02_cim_profiles/2_5_using_units.ipynb) |
| change a model and record the difference | [Editing a model](../02_cim_profiles/2_4_using_incrementals.ipynb) |
| load a distribution feeder | [Feeder model](../04_graph_models/4_2_feeder_model.ipynb) |
| load a substation or an EMS model | [Node-breaker model](../04_graph_models/4_3_node_breaker.ipynb) |
| load a planning (bus-branch) model | [Bus-branch model](../04_graph_models/4_4_bus_branch.ipynb) |
| split a model into areas | [Distributed areas](../04_graph_models/4_5_distributed_area.ipynb) |
| read a CIM XML or JSON-LD file | [CIM XML files](../03_databases/3_8_xml_file_parser.ipynb), [JSON-LD files](../03_databases/3_9_jsonld_file_parser.ipynb) |
| query a triple store or graph database | [Choosing a connection](../03_databases/3_1_databases_overview.ipynb) |
| configure namespaces, identifiers or credentials | [Environment variables](../03_databases/3_2_env_variables.ipynb) |
| save a model | [Writing files](../05_utils/5_1_file_writers.ipynb) |
| fetch everything in one call | [Loading all data](../05_utils/5_2_get_all_data.ipynb) |
| draw a class or object diagram | [Mermaid diagrams](../05_utils/5_3_mermaid.ipynb) |

## The three ideas

**A profile.** `CIMG_CIM_PROFILE` picks a module of CIM dataclasses from `cim-profiles`. That profile decides
which classes, attributes and enumerations exist; nothing else does.

**A connection.** `XMLFile`, `JSONLDFile`, `BlazegraphConnection` and the rest are interchangeable: each one
fetches CIM objects from its source and creates them as dataclass instances.

**A graph model.** `FeederModel`, `NodeBreakerModel` or `BusBranchModel` holds the objects, starting from a
container. `network.graph[cim.ClassName]` is a dict from UUID to object, and `get_all_edges(cim.ClassName)`
expands it by one association.
