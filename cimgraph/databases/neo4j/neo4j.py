from __future__ import annotations

import asyncio
import importlib
import logging
import math
import os

import nest_asyncio
from neo4j.exceptions import DriverError, Neo4jError
from rdflib import Graph, URIRef

import cimgraph.queries.cypher as cypher
from cimgraph.databases import ConnectionInterface, ConnectionParameters, QueryResponse
from neo4j import AsyncGraphDatabase, GraphDatabase

nest_asyncio.apply()

_log = logging.getLogger(__name__)


class Neo4jConnection(ConnectionInterface):

    def __init__(self, connection_parameters: ConnectionParameters):

        self.cim_profile = connection_parameters.cim_profile
        self.cim = importlib.import_module('cimgraph.data_profile.' + self.cim_profile)
        self.connection_params = connection_parameters
        self.namespace = connection_parameters.namespace
        self.url = connection_parameters.url
        self.username = connection_parameters.username
        self.password = connection_parameters.password
        self.database = connection_parameters.database
        self.driver = None

        try:
            self.data_profile = Graph(store='Oxigraph')
            path = os.path.dirname(self.cim.__file__)
            self.data_profile.parse(f'{path}/{self.cim_profile}.rdfs', format='xml')
            self.reverse = URIRef(
                'http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#inverseRoleName')
        except:
            _log.warning('No RDFS schema found, reverting to default logic')
            self.data_profile = None

    def connect(self):
        if not self.driver:
            self.driver = AsyncGraphDatabase.driver(self.url, auth=(self.username, self.password))
            # self.driver.verify_connectivity()

    def disconnect(self):
        self.driver.close()
        self.driver = None

    async def execute(self, query_message: str) -> QueryResponse:
        self.connect()
        # driver = AsyncGraphDatabase.driver(self.url, auth=(self.username, self.password))
        # result = self.read_transaction(driver, query_message)
        # driver.close()
        # try:
        #     records, summary, keys = self.driver.execute_query(query_message, database_=self.database )
        #     return records, summary, keys
        # # Capture any errors along with the query and data for traceability
        # except (DriverError, Neo4jError) as exception:
        #     _log.error("%s raised an error: \n%s", query_message, exception)
        async with self.driver.session(database=self.database) as session:
            result = await session.read_transaction(lambda tx: self.query_tx(tx, query_message))
            # driver.close()
            #     await lambda tx: tx.run(query_message).data()
            # )

        return result

    # async def read_transaction(self, driver, query_message):
    #     async with driver.session(database = self.database) as session:
    #         result = await session.read_transaction(lambda tx: self.query_tx(tx,query_message))
    #     return result

    async def query_tx(self, tx, query_message):
        result = await tx.run(query_message)
        records = await result.data()
        return records

    def create_new_graph(self, container: object) -> dict[type, dict[str, object]]:
        graph = {}
        # Generate cypher message from correct loaders>cypher python script based on class name
        cypher_message = cypher.get_all_nodes_from_container(container, self.namespace)
        # Execute cypher query

        query_output = asyncio.run(self.execute(cypher_message))
        parsed = {}
        for result in query_output:

            # Parse query results
            # node = result['ConnectivityNode']['IdentifiedObject.mRID']
            # terminal = result['Terminal']['IdentifiedObject.mRID']
            # eq_id = result['Equipment']['IdentifiedObject.mRID']
            node = result['ConnectivityNode']
            terminal = result['Terminal']
            eq_id = result['eq_id']
            eq_class = result['eq_class'][1]
            # Add each object to graph
            try:
                graph[self.cim.ConnectivityNode][node]
            except:
                self.create_object(graph, self.cim.ConnectivityNode, node)
            self.create_object(graph, self.cim.Terminal, terminal)
            if eq_class in self.cim.__all__:
                eq_class = eval(f'self.cim.{eq_class}')
                self.create_object(graph, eq_class, eq_id)
            else:
                _log.warning('object class missing from data profile:' + str(eq_class))
                continue
            # Link objects in graph
            graph[eq_class][eq_id].Terminals.append(graph[self.cim.Terminal][terminal])
            graph[self.cim.ConnectivityNode][node].Terminals.append(
                graph[self.cim.Terminal][terminal])
            setattr(graph[self.cim.Terminal][terminal], 'ConnectivityNode',
                    graph[self.cim.ConnectivityNode][node])
            setattr(graph[self.cim.Terminal][terminal], 'ConductingEquipment',
                    graph[eq_class][eq_id])

        return graph

    def create_graph_from_list(self, mrid_list: list[str]) -> dict[type, dict[str, object]]:
        graph = {}
        _log.warning('not supported yet for neo4j')
        return graph

    def get_edges_query(self, graph: dict[type, dict[str, object]], cim_class: type) -> str:

        eq_mrids = list(graph[cim_class].keys())[0:100]
        cypher_message = cypher.get_all_edges_cypher(cim_class, eq_mrids, self.namespace)

        return cypher_message

    def get_all_edges(self, graph: dict[type, dict[str, object]], cim_class: type) -> None:
        mrid_list = list(graph[cim_class].keys())
        num_nodes = len(mrid_list)
        asyncio.run(self.get_all_edges_async(mrid_list, graph, cim_class))

    async def get_all_edges_async(self, mrid_list, graph: dict[type, dict[str, object]],
                                  cim_class: type):
        for f in asyncio.as_completed([
                self.edge_query_parser(mrid_list, index, graph, cim_class)
                for index in range(math.ceil(len(mrid_list) / 100))
        ]):
            await f

    async def edge_query_parser(self, mrid_list: list[str], index: int,
                                graph: dict[type, dict[str, object]], cim_class: type):
        eq_mrids = mrid_list[index * 100:(index + 1) * 100]
        #generate cypher message from correct loaders>cypher python script based on class name
        cypher_message = cypher.get_all_edges_cypher(cim_class, eq_mrids, self.namespace)
        #execute cypher query
        query_output = asyncio.run(self.execute(cypher_message))
        parsed = []
        for result in query_output:
            is_association = False
            is_enumeration = False

            mRID = result['mRID']    #get mRID
            if 'urn:uuid:' in mRID:
                mRID = mRID.split('urn:uuid:')[1]
            elif '#' in mRID:
                mRID = mRID.split('#')[1]

            if mRID not in parsed:
                parsed.append(mRID)
                attr_list = list(result['eq'].keys())
                for attr in attr_list:
                    if attr != 'uri':
                        try:
                            attribute = attr.split('.')[1]
                            value = result['eq'][attr]
                            setattr(graph[cim_class][mRID], attribute, value)
                        except:
                            _log.warning(f'attribute {attribute} not recognized')
            attr = result['attribute']
            attribute = result['attribute'].split('.')    #split edge attribute
            edge_node = result['edge_mrid']    #get edge value
            # edge_node = result['edge_node'] #get edge value
            edge_class = result['edge_class']

            if len(edge_class) == 1:    #check if enumeration
                enum = edge_node.split('#')[1]
                enum_class = enum.split('.')[0]
                enum_value = enum.split('.')[1]
                is_enumeration = True

            else:
                edge_class = edge_class[1]

                if edge_class in self.cim.__all__:
                    is_association = True
                    edge_class = eval(f'self.cim.{edge_class}')
                else:
                    _log.warning(f'unknown class {edge_class}')
                    continue

            if is_association:    # if association to another CIM object

                if 'urn:uuid' in edge_node:
                    edge_mRID = edge_node.split('urn:uuid:')[1]
                elif '#' in edge_node:
                    edge_mRID = edge_node.split('#')[1]
                else:
                    edge_mRID = edge_node

                if attribute[1] in cim_class.__dataclass_fields__:    #check if forward attribute
                    self.create_edge(graph, cim_class, mRID, attribute[1], edge_class, edge_mRID)

                elif self.data_profile is not None:    # use data profile to look up reverse attribute
                    attr_uri = URIRef(f'{self.namespace}{attr}')
                    reverse_uri = self.data_profile.value(object=attr_uri, predicate=self.reverse)
                    try:
                        reverse_attribute = reverse_uri.split('#')[1].split('.')[
                            1]    # split string
                    except:
                        _log.warning(f'{cim_class.__name__} does not have attribute {attr}')

                    self.create_edge(graph, cim_class, mRID, reverse_attribute, edge_class,
                                     edge_mRID)

                else:    # fallback to use basic logic to identify
                    if attribute[
                            0] in cim_class.__dataclass_fields__:    #check if first name is the attribute
                        self.create_edge(graph, cim_class, mRID, attribute[0], edge_class,
                                         edge_mRID)

                    elif attribute[
                            0] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[0] + 's', edge_class,
                                         edge_mRID)

                    elif attribute[
                            1] + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, attribute[1] + 's', edge_class,
                                         edge_mRID)

                    elif edge_class.__name__ in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, edge_class.__name__, edge_class,
                                         edge_mRID)

                    elif edge_class.__name__ + 's' in cim_class.__dataclass_fields__:    #check if attribute spelling is plural
                        self.create_edge(graph, cim_class, mRID, edge_class.__name__ + 's',
                                         edge_class, edge_mRID)

                    else:    #fallback: match class type until a suitable parent edge class is found
                        parsed = False
                        for node_attr in list(cim_class.__dataclass_fields__.keys()):
                            attr_str = cim_class.__dataclass_fields__[node_attr].type
                            edge_parent = attr_str.split('[')[1].split(']')[0]
                            if edge_parent in self.cim.__all__:
                                parent_class = eval(f'self.cim.{edge_parent}')
                                if issubclass(edge_class, parent_class):
                                    self.create_edge(graph, cim_class, mRID, node_attr, edge_class,
                                                     edge_mRID)
                                    parsed = True
                                    break
                        if not parsed:
                            _log.warning(f'unable to find match for {attr} for {mRID}')

            elif is_enumeration:
                if enum_class in self.cim.__all__:    # if enumeration
                    edge_enum = eval(f'self.cim.{enum_class}(enum_value)')
                    setattr(graph[cim_class][mRID], attribute[1], edge_enum)

    def create_object(self, graph, class_type, mRID):

        if class_type not in graph.keys():
            graph[class_type] = {}

        if mRID in graph[class_type].keys():
            obj = graph[class_type][mRID]
        else:
            obj = class_type()
            setattr(obj, 'mRID', mRID)
            graph[class_type][mRID] = obj

        return obj

    def create_edge(self, graph, cim_class, mRID, attribute, edge_class, edge_mRID):
        edge_object = self.create_object(graph, edge_class, edge_mRID)
        attribute_type = cim_class.__dataclass_fields__[attribute].type
        if 'List' in attribute_type:
            obj_list = getattr(graph[cim_class][mRID], attribute)
            obj_list.append(edge_object)
            setattr(graph[cim_class][mRID], attribute, obj_list)
        else:
            setattr(graph[cim_class][mRID], attribute, edge_object)
