from neo4j import GraphDatabase
from src.ingestion_service import IngestionService
from src.graph_loader import GraphLoader
from src.models import Material, KPI, Property
from src.parsers.json_parser import load_material_facts
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Connected to Neo4j")

    loader = GraphLoader(driver=driver)
    service = IngestionService(graph_loader=loader)
    facts = load_material_facts("data/extracted/material_facts.json")

    for fact in facts:
        service.ingest_material_fact(
            material=fact.material,
            prop=fact.prop,
            kpi=fact.kpi,
            value=fact.value,
            unit=fact.unit,
        )

    print("Material fact ingested")
