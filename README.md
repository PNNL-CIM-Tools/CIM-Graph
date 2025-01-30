# CIMantic Graphs Library

![GitHub Tag](https://img.shields.io/github/v/tag/PNNL-CIM-Tools/CIM-Graph)
![GitHub Release Date](https://img.shields.io/github/release-date-pre/PNNL-CIM-Tools/CIM-Graph)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/PNNL-CIM-Tools/CIM-Graph/dev-pre-release.yml)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/PNNL-CIM-Tools/CIM-Graph)


![PyPI - Version](https://img.shields.io/pypi/v/cim-graph)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cim-graph?label=pypi%20downloads)
![PyPI - Format](https://img.shields.io/pypi/format/cim-graph)


![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/PNNL-CIM-Tools/CIM-Graph)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/PNNL-CIM-Tools/CIM-Graph)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/PNNL-CIM-Tools/CIM-Graph)

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/PNNL-CIM-Tools/CIM-Graph/total?label=git%20downloads)
![GitHub License](https://img.shields.io/github/license/PNNL-CIM-Tools/CIM-Graph)
![https://doi.org/10.11578/dc.20240507.3](https://img.shields.io/badge/doi-10.11578/dc.20240507.3-blue)


CIMantic Graphs is an open-source library for for creating, parsing, and editing CIM power system models using in-memory knowledge graphs to reduce the burden and learning curve associated with using the Common Information Model.

Key features:

* Single API method to obtain data for any CIM class. No more custom database queries.
* Single API method to obtain data for EMS node-breaker transmission models, bus-branch planning models, and distribution feeder models.
* Singe API method for both centralized and distributed architectures.
* Support for multiple databases and query languages with no changes to upper-level graph data or API calls. Only need to change host/port specified in ConnectionParameters data object.
* Ability to create CIM models "from scratch".
* Open-source data engineering tool for management of CIM models.
* Knowledge graph approach based on semantic understanding of CIM.
* Object-oriented data structure with enforcement of CIM Schema.
* Data profiles generated directly from Enterprise Architect UML.
* Support for custom profiles using CIMTool or Schema Composer.
* Support for direct creation / editing / parsing of CIM XML, JSON-LD.
* API support for centralized/distributed transmission + distribution models.

![summary-image](https://raw.githubusercontent.com/PNNL-CIM-Tools/CIM-Graph/develop/cim_graph_structure.png)

## Requirements

CIM-Graph requires a python version >=3.8 and <4. No testing has been done with other versions.

Support is currently offered for opening XML, JSON-LD, and CSV files

Support is currently offered for GridAPPS-D, Blazegraph, Neo4J, GraphDB, and json-formatted MySQL databases. More databases will be added in the future.

## Installation

```bash
pip install cim-graph
```

## Specifying the CIM Profile

The CIM-Graph library supports multiple CIM profiles, which can be exported using CIMtool or Enterprise Architect Schema Composer as a .xsd data profile. The data profiles are ingested using the xsdata python library and saved in the cimgraph/data_profile directory.

When importing the library, the CIM profile must be specified using the gridappsd-python constructor or directly as

```python
import cimgraph.data_profile.rc4_2021 as cim
```

or by using `importlib`:

```python
import importlib
cim_profile = 'rc4_2021'
cim = importlib.import_module('cimgraph.data_profile.' + cim_profile)
```

## Specifying the Connection Parameters

The CIM-Graph library supports multiple databases. The ConnectionParameters specify how to read the CIM model:

__Required arguments:__

* `cim_profile`: This specifies the specific version of CIM to be used, based on the available python data profiles loaded into the library

__Optional arguments:__

* `namespace`: CIM namespace, default is `"http://iec.ch/TC57/CIM100#"`
* `iec61970-301`: Serialization version. Versions 7(default) and below use `rdf:ID=`. Version 8 uses `rdf:about=urn:uuid:`
* `url`: URL at which the database can be reached via TCP/IP or other connection
* `host`: Database host address
* `port`: Database host port
* `database`: Database name
* `username`: Database username
* `password`: Database password
* `filename`: Filename for importing CIM models from an XML file

Note that not all parameters are required. Each database connection uses a subset of these arguments depending on the requirements of the database connection driver.

## Graph Model Classes

### Model Initialization

The CIM-Graph library creates object instances populated with the attributes of `mRID` for all nodes, terminals, and conducting equipment in the centralized netork or each distributed area. All other attributes are `None` or `[]` by default until queried for using `.get_all_edges(cim.ClassName)`.

### Transmission Node-Breaker Models

```python
from cimgraph.models import NodeBreakerModel

geo_region_id = "_EE4C60AE-550D-4599-92F4-022DF3118B3C" #Maple 10 bus
geo_region = cim.GeographicalRegion(mRID = geo_region_id)
network = NodeBreakerModel(connection=database, container=geo_region, distributed=True)
```

### Transmission Bus-Branch Models

```python
from cimgraph.models import BusBranchModel

model_mrid = "1783D2A8-1204-4781-A0B4-7A73A2FA6038" #IEEE 118 Bus"
container = cim.ConnectivityNodeContainer(mRID = model_mrid)
network = BusBranchModel(connection=database, container=container, distributed=False)
```

### Distribution Feeder Models

```python
from cimgraph.models import FeederModel

feeder_mrid = "49AD8E07-3BF9-A4E2-CB8F-C3722F837B62"
feeder = cim.Feeder(mRID = feeder_mrid)
network = FeederModel(connection=database, container=feeder, distributed=False)
```

### Centralized vs Distributed Models

If the `distributed` flag is set to `False`, then all equipment are contained within a single knowledge graph. If set to `True`, a `DistributedArea` graph model is created for each topological area inside the power system model.

```python
network = FeederModel(connection=rdf, container=feeder, distributed=True)
for switch_area in network.distributed_areas:
    switch_area.get_all_edges(cim.ACLineSegement)

    for secondary_area in switch_area.distributed_areas:
         secondary_area.get_all_edges(cim.ACLineSegement)
```

### Usage with GridAPPS-D Context Manager

If an application is built using the GridAPPS-D Context Manager and Field Interface in gridappsd-python, initialization of the `FeederModel` and `DistributedArea` graphs is performed automatically.

Internally, the GridAPPS-D Context Manager initializes distributed areas as `dist_network =  FeederModel(connection=gapps, container=feeder, distributed=True, topology_message=topo_msg)`.

## Core Library Methods

### .get_all_edges(cim.ClassName)

The CIM power system model can then be parsed by invoking the `.get_all_edges(cim.ClassName)` method. The method populates all available attributes of the given class and creates default instances of all associated class object instances that are one association away in the CIM UML. Associated default instances are only populated with `mRID` attribute. The `.get_all_edges` method must be invoked in sequential order following the inheritance hierarchy in the CIM UML, starting with the particular equiment class (e.g. ACLineSegment) and then each child class inheriting from the previous class.

### .graph[cim.ClassName]

The Python object instances can be accessed using the `graph` dictionary of each distributed area class instance. The typed catalog is organized by the class type and then mRID of each object. The attributes of each class can be accessed directly or through any associated class. These two calls are equivalent:

```python
bus_name = network.graph[cim.ConnectivityNode][node_mrid].name
```

```python
bus_name = network.graph[cim.ACLineSegment][line_mrid].Terminals[0].ConnectivityNode.name
```

Note that all classes and attributes are case sensitive and follow the CIM UML conventions for each class.

### pprint

Printing of individual CIM objects using default `print()` is now supported. Individual objects can be pretty-printed using the

```python
line = cim.ACLineSegment(name = 'new_line', r=0.002, x=0.050, b=0.003)
line.pprint()
```

All instances of all given CIM class within the network graph can be printed `.pprint(cim.ClassName)` method:

```python
network.pprint(cim.ACLineSegment)
```

Additional examples of usage are available on ReadTheDocs.

## Attribution and Disclaimer

This software was created under a project sponsored by the U.S. Department of Energy’s Office of Electricity, an agency of the United States Government.  Neither the United States Government nor the United States Department of Energy, nor Battelle, nor any of their employees, nor any jurisdiction or organization that has cooperated in the development of these materials, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product, software, or process disclosed, or represents that its use would not infringe privately owned rights.

Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.

PACIFIC NORTHWEST NATIONAL LABORATORY
operated by
BATTELLE
for the
UNITED STATES DEPARTMENT OF ENERGY
under Contract DE-AC05-76RL01830
