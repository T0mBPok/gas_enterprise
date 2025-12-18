from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database import Base
from src.classifiers.models import OrderStatus
from src.customer.models import Customer

class Order(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    gas_volume: Mapped[float]
    cost: Mapped[float]

    status_id: Mapped[int] = mapped_column(ForeignKey("orderstatuses.id"))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    deliveries: Mapped[list["Delivery"]] = relationship("Delivery", back_populates='order')
    
    status: Mapped["OrderStatus"] = relationship("OrderStatus")
    customer: Mapped["Customer"] = relationship("Customer")