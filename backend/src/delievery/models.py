from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey
from src.database import Base

class Delivery(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    delivery_date: Mapped[Date]
    volume: Mapped[float | None]

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    transport_id: Mapped[int] = mapped_column(ForeignKey("transport.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("deliverystatus.id"))
    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprise.id"))

    enterprise = relationship("Enterprise", back_populates="deliveries")
