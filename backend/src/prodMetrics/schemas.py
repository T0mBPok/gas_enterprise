from pydantic import BaseModel
from src.well.schemas import GetWell


class GetProdMetrics(BaseModel):
    id: int
    gas_volume: float
    pressure: float
    temperature: float
    well: GetWell


class AddProdMetrics(BaseModel):
    gas_volume: float
    pressure: float
    temperature: float
    well_id: int


class UpdateProdMetrics(BaseModel):
    gas_volume: float | None = None
    pressure: float | None = None
    temperature: float | None = None
    well_id: int | None = None