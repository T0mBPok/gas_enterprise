from pydantic import BaseModel, Field
from datetime import date
from src.classifiers.schemas import ClassifierRead
# from src.order.schemas import OrderRead


class GetDelivery(BaseModel):
    id: int
    delivery_date: date
    volume: float | None
    # order: OrderRead
    transport: ClassifierRead
    status: ClassifierRead
    enterprise_id: int
    created_at: str


class AddDelivery(BaseModel):
    delivery_date: date
    volume: float | None = None
    order_id: int
    transport_id: int
    status_id: int
    enterprise_id: int

    @classmethod
    def as_form(
        cls,
        delivery_date: date,
        volume: float | None,
        order_id: int,
        transport_id: int,
        status_id: int,
        enterprise_id: int
    ):
        return cls(
            delivery_date=delivery_date,
            volume=volume,
            order_id=order_id,
            transport_id=transport_id,
            status_id=status_id,
            enterprise_id=enterprise_id
        )


class UpdateDelivery(BaseModel):
    delivery_date: date | None = None
    volume: float | None = None
    order_id: int | None = None
    transport_id: int | None = None
    status_id: int | None = None
    enterprise_id: int | None = None