from pydantic import BaseModel


class Material(BaseModel):
    material_id: str
    name: str


class KPI(BaseModel):
    kpi_id: str
    name: str


class Property(BaseModel):
    property_id: str
    name: str
