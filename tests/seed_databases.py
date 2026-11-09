"""Load the integration-test model into the docker-compose.yml databases, replacing what they
hold, with each database's own RDF loader (not cimgraph, whose adapters are what the tests check).

    docker compose up -d --wait
    uv run python tests/seed_databases.py [blazegraph] [graphdb] [neo4j]

With no arguments every database is seeded. Needs the neo4j extra for Neo4j.
"""
import sys
from pathlib import Path

import requests

MODEL = Path(__file__).parent / 'test_models' / 'ieee13.xml'
RDF_XML = {'Content-Type': 'application/rdf+xml'}

BLAZEGRAPH_URL = 'http://localhost:8889/bigdata/namespace/kb/sparql'
GRAPHDB_URL = 'http://localhost:7200'
GRAPHDB_REPOSITORY = 'powergrid_models'
NEO4J_URL = 'neo4j://localhost:7687'
NEO4J_AUTH = ('neo4j', 'test1234')

# No inference ("empty" ruleset): queries see only the types and properties in the file
GRAPHDB_CONFIG = f'''
@prefix rep: <http://www.openrdf.org/config/repository#> .
@prefix sr: <http://www.openrdf.org/config/repository/sail#> .
@prefix sail: <http://www.openrdf.org/config/sail#> .
@prefix graphdb: <http://www.ontotext.com/config/graphdb#> .
[] a rep:Repository ;
    rep:repositoryID "{GRAPHDB_REPOSITORY}" ;
    rep:repositoryImpl [
        rep:repositoryType "graphdb:SailRepository" ;
        sr:sailImpl [ sail:sailType "graphdb:Sail" ; graphdb:ruleset "empty" ]
    ] .
'''


def seed_blazegraph(rdf_xml: bytes) -> None:
    requests.post(BLAZEGRAPH_URL, data={'update': 'DROP ALL'}, timeout=60).raise_for_status()
    requests.post(BLAZEGRAPH_URL, data=rdf_xml, headers=RDF_XML, timeout=300).raise_for_status()


def seed_graphdb(rdf_xml: bytes) -> None:
    repositories = f'{GRAPHDB_URL}/rest/repositories'
    existing = requests.get(repositories, timeout=60)
    existing.raise_for_status()
    if any(repository['id'] == GRAPHDB_REPOSITORY for repository in existing.json()):
        requests.delete(f'{repositories}/{GRAPHDB_REPOSITORY}', timeout=60).raise_for_status()
    requests.post(repositories, files={'config': ('config.ttl', GRAPHDB_CONFIG)},
                  timeout=60).raise_for_status()
    requests.post(f'{GRAPHDB_URL}/repositories/{GRAPHDB_REPOSITORY}/statements',
                  data=rdf_xml, headers=RDF_XML, timeout=300).raise_for_status()


def seed_neo4j(rdf_xml: bytes) -> None:
    from neo4j import GraphDatabase
    with GraphDatabase.driver(NEO4J_URL, auth=NEO4J_AUTH) as driver:
        # Deleting every node also deletes the n10s configuration node
        driver.execute_query('MATCH (n) DETACH DELETE n')
        driver.execute_query('CREATE CONSTRAINT n10s_unique_uri IF NOT EXISTS '
                             'FOR (r:Resource) REQUIRE r.uri IS UNIQUE')
        # Class and property names without namespace prefixes, as the Cypher queries expect
        driver.execute_query("CALL n10s.graphconfig.init({handleVocabUris: 'IGNORE'})")
        records, _, _ = driver.execute_query(
            "CALL n10s.rdf.import.inline($rdf, 'RDF/XML')", rdf=rdf_xml.decode('utf-8'))
        if records[0]['terminationStatus'] != 'OK':
            raise RuntimeError(f'n10s import failed: {records[0]["extraInfo"]}')


SEEDERS = {'blazegraph': seed_blazegraph, 'graphdb': seed_graphdb, 'neo4j': seed_neo4j}


def main(services: list[str]) -> None:
    unknown = set(services) - set(SEEDERS)
    if unknown:
        raise SystemExit(f'unknown service(s) {sorted(unknown)}; choose from {sorted(SEEDERS)}')
    rdf_xml = MODEL.read_bytes()
    for service in services or SEEDERS:
        SEEDERS[service](rdf_xml)
        print(f'{service}: loaded {MODEL.name}')


if __name__ == '__main__':
    main(sys.argv[1:])
