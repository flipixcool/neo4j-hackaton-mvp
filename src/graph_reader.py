class GraphReader:
    def __init__(self, driver):
        self.driver = driver

    def find_materials_for_kpi(self, kpi_name: str) -> list[dict]:
        records, _, _ = self.driver.execute_query(
            """
            MATCH
                (m:Material)-[:HAS_PROPERTY]->(p:Property)-[:AFFECTS]->(k:KPI {name: $kpi_name})
            RETURN
                m.name AS material,
                p.name AS property,
                k.name AS kpi
            """,
            kpi_name=kpi_name,
        )

        return [record.data() for record in records]