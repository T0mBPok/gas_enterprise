from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date
from src.database import Base
from src.classifiers.models import DeliveryStatus, Transport
from src.order.models import Order

class Delivery(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    delivery_date: Mapped[date]
    volume: Mapped[float | None]

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    transport_id: Mapped[int] = mapped_column(ForeignKey("transports.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("deliverystatuses.id"))
    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprises.id"))

    enterprise: Mapped["Enterprise"] = relationship("Enterprise", back_populates="deliveries")
    order: Mapped["Order"] = relationship("Order", back_populates="deliveries")
    status: Mapped["DeliveryStatus"] = relationship("DeliveryStatus")
    transport: Mapped["Transport"] = relationship("Transport")