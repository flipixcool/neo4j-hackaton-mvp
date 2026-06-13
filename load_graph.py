from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()


URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Connected to Neo4j")


def load_material(driver, material: dict) -> None:
    driver.execute_query(
        """
        MERGE (m:Material {material_id: $material_id})
        SET m.name = $name
        """,
        material_id=material["material_id"],
        name=material["name"],
    )


material = {
    "material_id": "mat_2",
    "name": "Copper Alloy",
}

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    load_material(driver, material)
    print("Material loaded")
