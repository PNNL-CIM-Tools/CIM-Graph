# TODO

## JSON-LD reader: read the model header
`XMLFile` now reads each part file's `md:FullModel` / `cim:ModelAuthority` header
(`fileparsers/metadata.py::parse_model_header`). Before parsing that part's objects it calls
`core.set_model_scope(authority, model_name)`, and it keeps the header nodes out of the graph.
`JSONLDFile` (`fileparsers/json_ld_parser.py`) still does neither. `write_json_ld` writes
`md:FullModel` and `cim:ModelAuthority` nodes into `@graph`, so a JSON-LD round trip loses the
authority and model name, and the reader logs those header nodes as unknown classes.

- Find the `md:FullModel` / `cim:ModelAuthority` nodes in `@graph`, reading
  `Model.modelingAuthoritySet` (falling back to the ModelAuthority `IdentifiedObject.name`) and
  `Model.description`.
- Call `set_model_scope` before creating objects, and skip header nodes in node/edge parsing.
- Expose them as `JSONLDFile.model_headers` (reuse `ModelHeader`).
- Test: write_json_ld → change scope → reread → scope restored, no header classes in graph
  (mirror `tests/test_xmlfile.py::test_reader_restores_model_header`).

## Writer: namespaces missing from the `namespaces` argument
`write_xml` raises `KeyError: Namespace ... has no prefix` when an attribute's profile
namespace isn't in the caller's `namespaces` dict. For example, the GMDM profiles use
`http://cim.ucaiug.io/CIM101/draft#` and `http://epri.com/gmdm/2025#`. This breaks
`EPRI-GMDM-II/IEEE9500Node/9500node_exports.ipynb`, which maps `gmdm` to the old
`http://epri.com/gmdm#`. Decide on one: update the notebook, or have the writer generate prefixes
for unmapped profile namespaces.
