import os

from dotenv import load_dotenv
from fastapi import FastAPI
from neo4j import GraphDatabase

from src.graph_reader import GraphReader

load_dotenv()

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))

driver = GraphDatabase.driver(URI, auth=AUTH)
reader = GraphReader(driver)

app = FastAPI(title="Graph Hackathon API")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/materials-for-kpi")
def get_materials_for_kpi(name: str) -> list[dict]:
    return reader.find_materials_for_kpi(name)
