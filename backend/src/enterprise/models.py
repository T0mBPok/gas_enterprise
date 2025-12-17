from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database import Base
from src.well.models import Well
from src.user.models import User
from src.delivery.models import Delivery
from src.classifiers.models import Country, City, Street, House, EnterpriseStatus, EnterpriseType

class Enterprise(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    contacts: Mapped[str | None]

    status_id: Mapped[int] = mapped_column(ForeignKey("enterprisestatuses.id"))
    type_id: Mapped[int] = mapped_column(ForeignKey("enterprisetypes.id"))
    deposit_id: Mapped[int] = mapped_column(ForeignKey("deposits.id"))

    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    street_id: Mapped[int] = mapped_column(ForeignKey("streets.id"))
    house_id: Mapped[int] = mapped_column(ForeignKey("houses.id"))

    status: Mapped["EnterpriseStatus"] = relationship("EnterpriseStatus")
    type: Mapped["EnterpriseType"] = relationship("EnterpriseType")
    deposit: Mapped["Deposit"] = relationship("Deposit", back_populates="enterprise")

    country: Mapped["Country"] = relationship("Country")
    city: Mapped["City"] = relationship("City")
    street: Mapped["Street"] = relationship("Street")
    house: Mapped["House"] = relationship("House")

    employees: Mapped[list[User]] = relationship("User", back_populates="enterprise")
    wells: Mapped[list[Well]] = relationship("Well", back_populates="enterprise")
    deliveries: Mapped[list[Delivery]] = relationship("Delivery", back_populates="enterprise")
