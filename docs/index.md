# CIMantic Graphs Library Documentation

CIMantic Graphs is an open-source library for creating, parsing, and editing CIM power system models using in-memory knowledge graphs to reduce the burden and learning curve associated with using the Common Information Model.

![CIM Graph Structure](./04_graph_models/images/4_1_property_graph.svg)

## Key Features

* **Single API method** to obtain data for any CIM class. No more custom database queries.
* **Single API method** to obtain data for EMS node-breaker transmission models, bus-branch planning models, and distribution feeder models.
* **Single API method** for both centralized and distributed architectures.
* **Multiple database support** with no changes to upper-level graph data or API calls. Only need to change host/port specified in ConnectionParameters data object.
* **Create CIM models from scratch** with full object-oriented interface.
* **Open-source data engineering tool** for management of CIM models.
* **Knowledge graph approach** based on semantic understanding of CIM.
* **Object-oriented data structure** with enforcement of CIM Schema.
* **Data profiles** generated directly from Enterprise Architect UML.
* **Custom profile support** using CIMTool.
* **Direct creation/editing/parsing** of CIM XML, JSON-LD.
* **API support** for centralized/distributed transmission + distribution models.

## Installation

To install CIMantic Graphs, clone the github repository or use pip install:

```bash
pip install cim-graph
```

## Quick Start

```python
import cimgraph.data_profile.cim17v40 as cim
from cimgraph.databases.blazegraph import BlazegraphConnection
from cimgraph.models import FeederModel

# Connect to database
database = BlazegraphConnection()

# Create a feeder model
feeder = database.get_object(mRID="49AD8E07-3BF9-A4E2-CB8F-C3722F837B62")
network = FeederModel(connection=database, container=feeder, distributed=False)

# Query for all line data
network.get_all_edges(cim.ACLineSegment)

# Access graph data
for line in network.graph[cim.ACLineSegment].values():
    print(f"Line: {line.name}, Length: {line.length}")
```

## Documentation Sections

### Overview
Get started with CIMantic Graphs, learn about installation, project structure, and how to contribute.

### CIM Profiles
Learn how to work with different CIM profiles, build custom profiles, and use CIM objects.

### Databases
Connect to various databases including Blazegraph, Neo4j, GraphDB, MySQL, and GridAPPS-D. Also learn how to parse XML and JSON-LD files.

### Graph Models
Understand the different graph model types: FeederModel for distribution, NodeBreakerModel for transmission, and BusBranchModel for planning studies.

### Utils & Shortcuts
Discover utility functions for file writing, bulk data queries, and automatic mermaid diagram generation.

## Support & Contributing

- **GitHub Repository**: [PNNL-CIM-Tools/CIM-Graph](https://github.com/PNNL-CIM-Tools/CIM-Graph)
- **PyPI Package**: [cim-graph](https://pypi.org/project/cim-graph/)
- **Issue Tracker**: [GitHub Issues](https://github.com/PNNL-CIM-Tools/CIM-Graph/issues)

## License

This project is maintained by Pacific Northwest National Laboratory and is available under the terms specified in the repository license.

![CIM Graph Logo](./images/CIM_Graph_Logo.png)
