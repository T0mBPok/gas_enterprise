from __future__ import annotations
from pydantic import BaseModel
from src.classifiers.schemas import ClassifierRead
from src.customer.schemas import GetCustomer
from datetime import datetime


class GetOrder(BaseModel):
    id: int
    gas_volume: float
    cost: float
    status: ClassifierRead
    customer: GetCustomer
    created_at: datetime


class AddOrder(BaseModel):
    gas_volume: float
    cost: float
    status_id: int
    customer_id: int


class UpdateOrder(BaseModel):
    gas_volume: float | None = None
    cost: float | None = None
    status_id: int | None = None
    customer_id: int | None = None
