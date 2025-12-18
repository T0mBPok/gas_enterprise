from pydantic import BaseModel
from datetime import date
from src.enterprise.schemas import GetEnterprise
from src.well.schemas import GetWell
from src.classifiers.schemas import ClassifierRead


class GetProductionProcess(BaseModel):
    id: int
    name: str
    date_start: date | None
    date_end: date | None
    notes: str | None
    enterprise: GetEnterprise
    well: GetWell | None
    status: ClassifierRead
    type: ClassifierRead


class AddProductionProcess(BaseModel):
    name: str
    date_start: date | None
    date_end: date | None
    notes: str | None = None
    enterprise_id: int
    well_id: int | None
    type_id: int
    status_id: int


class UpdateProductionProcess(BaseModel):
    name: str | None = None
    date_start: date | None = None
    date_end: date | None = None
    notes: str | None = None
    enterprise_id: int | None = None
    well_id: int | None = None
    type_id: int | None = None
    status_id: int | None = None