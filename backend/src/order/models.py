from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from src.database import Base

class Order(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    gas_volume: Mapped[float]
    created_at: Mapped[Date]
    cost: Mapped[float]

    status_id: Mapped[int] = mapped_column(ForeignKey("orderstatus.id"))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
