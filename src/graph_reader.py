class GraphReader:
    def __init__(self, driver):
        self.driver = driver

    def find_materials_for_kpi(self, kpi_name: str) -> list[dict]:
        records, _, _ = self.driver.execute_query(
            """
            MATCH
                (m:Material)-[r:HAS_PROPERTY]->(p:Property)-[:AFFECTS]->(k:KPI {name: $kpi_name})
            RETURN
                m.name AS material,
                p.name AS property,
                k.name AS kpi,
                r.value AS value,
                r.unit AS unit
            """,
            kpi_name=kpi_name,
        )

        result = []

        for record in records:
            data = record.data()
            data["evidence_path"] = (
                f"{data['material']} -> {data['property']} -> {data['kpi']}"
            )
            result.append(data)

        return result
