from pydantic import BaseModel, Field
from src.classifiers.schemas import ClassifierRead
from src.deposit.schemas import GetDeposit
from datetime import datetime


class GetEnterprise(BaseModel):
    id: int
    name: str
    contacts: str | None
    status: ClassifierRead
    type: ClassifierRead
    deposit: GetDeposit
    country: ClassifierRead
    city: ClassifierRead
    street: ClassifierRead
    house: ClassifierRead
    created_at: datetime


class AddEnterprise(BaseModel):
    name: str = Field(..., min_length=2)
    contacts: str | None = None
    status_id: int
    type_id: int
    deposit_id: int
    country_id: int
    city_id: int
    street_id: int
    house_id: int

class UpdateEnterprise(BaseModel):
    name: str | None = Field(None, min_length=2)
    contacts: str | None = None
    status_id: int | None = None
    type_id: int | None = None
    deposit_id: int | None = None
    country_id: int | None = None
    city_id: int | None = None
    street_id: int | None = None
    house_id: int | None = None