"""What changes a GraphModel after it is built.

``cimgraph.models`` holds GraphModel and its subclasses; the modules here record,
read, write and apply changes to one:

- ``incremental_builder``: differences (create, modify, delete) and the RDF/XML
  difference model
- ``incremental_json``: differences as GridAPPS-D JSON messages
- ``measurement_json``: measurement values (``Analog`` / ``Discrete``) as a JSON stream
"""
