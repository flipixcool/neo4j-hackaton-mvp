from neo4j import GraphDatabase
from src.ingestion_service import IngestionService
from src.graph_loader import GraphLoader
from src.models import Material, KPI, Property
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

    material = Material(material_id="mat_3", name="Titanium Alloy")
    prop = Property(property_id="prop_strength", name="Strength")
    kpi = KPI(kpi_id="kpi_durability", name="Durability")

    service.ingest_material_fact(material, prop, kpi, value=0.91, unit="score")
    print("Material fact ingested")
