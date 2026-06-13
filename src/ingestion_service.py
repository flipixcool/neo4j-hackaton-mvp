from src.graph_loader import GraphLoader
from src.models import Material, KPI, Property


class IngestionService:
    def __init__(self, graph_loader: GraphLoader):
        self.graph_loader = graph_loader

    def ingest_material_fact(
        self,
        material: Material,
        prop: Property,
        kpi: KPI,
        value: float | None = None,
        unit: str | None = None,
    ) -> None:
        self.graph_loader.load_material(material)
        self.graph_loader.load_property(prop)
        self.graph_loader.load_kpi(kpi)

        self.graph_loader.link_material_property(
            material=material,
            prop=prop,
            value=value,
            unit=unit,
        )

        self.graph_loader.link_property_kpi(
            prop=prop,
            kpi=kpi,
        )
