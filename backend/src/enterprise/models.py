from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database import Base

class Enterprise(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str | None]
    contacts: Mapped[str | None]

    status_id: Mapped[int] = mapped_column(ForeignKey("enterprisestatus.id"))
    type_id: Mapped[int] = mapped_column(ForeignKey("enterprisetype.id"))
    deposit_id: Mapped[int] = mapped_column(ForeignKey("deposit.id"))

    deposit = relationship("Deposit", back_populates="enterprises")
    wells = relationship("Well", back_populates="enterprise")
    employees = relationship("Employee", back_populates="enterprise")
    deliveries = relationship("Delivery", back_populates="enterprise")
