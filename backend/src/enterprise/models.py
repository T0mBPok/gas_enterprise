from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database import Base
from src.well.models import Well
from src.user.models import User
from src.delivery.models import Delivery

class Enterprise(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str | None]
    contacts: Mapped[str | None]

    status_id: Mapped[int] = mapped_column(ForeignKey("enterprisestatuses.id"))
    type_id: Mapped[int] = mapped_column(ForeignKey("enterprisetypes.id"))
    deposit_id: Mapped[int] = mapped_column(ForeignKey("deposits.id"))
    employees: Mapped[list[User]] = relationship("User", back_populates='enterprise')

    deposit = relationship("Deposit", back_populates="enterprise")
    wells = relationship("Well", back_populates="enterprise")
    deliveries = relationship("Delivery", back_populates="enterprise")
