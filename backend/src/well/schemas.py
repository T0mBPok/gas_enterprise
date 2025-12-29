from fastapi import Form
from pydantic import BaseModel, Field
from datetime import date
from src.classifiers.schemas import ClassifierRead
from src.enterprise.schemas import GetEnterprise
from datetime import datetime


class GetWell(BaseModel):
    id: int
    number: str
    depth: float
    enterprise_id: int
    status_id: int
    enterprise: GetEnterprise
    status: ClassifierRead
    created_at: datetime


class AddWell(BaseModel):
    number: str = Field(..., min_length=1)
    depth: float
    enterprise_id: int
    status_id: int


class UpdateWell(BaseModel):
    number: str | None = None
    depth: float | None = None
    enterprise_id: int | None = None
    status_id: int | None = None