from pydantic import BaseModel
from datetime import date
from src.classifiers.schemas import ClassifierRead
from src.enterprise.schemas import GetEnterprise
from src.order.schemas import GetOrder


class GetDelivery(BaseModel):
    id: int
    delivery_date: date
    volume: float | None
    enterprise: GetEnterprise
    order: GetOrder
    status: ClassifierRead
    transport: ClassifierRead


class AddDelivery(BaseModel):
    delivery_date: date
    volume: float | None
    enterprise_id: int
    order_id: int
    transport_id: int
    status_id: int

    @classmethod
    def as_form(
        cls,
        delivery_date: date,
        volume: float | None,
        enterprise_id: int,
        order_id: int,
        transport_id: int,
        status_id: int,
    ):
        return cls(
            delivery_date=delivery_date,
            volume=volume,
            enterprise_id=enterprise_id,
            order_id=order_id,
            transport_id=transport_id,
            status_id=status_id,
        )


class UpdateDelivery(BaseModel):
    delivery_date: date | None = None
    volume: float | None = None
    enterprise_id: int | None = None
    order_id: int | None = None
    transport_id: int | None = None
    status_id: int | None = None