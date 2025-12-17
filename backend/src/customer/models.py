from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from src.classifiers.models import Country, City, Street, House

class Customer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone_num: Mapped[str]
    contact_info: Mapped[str | None] = None
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'))
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    street_id: Mapped[int] = mapped_column(ForeignKey('streets.id'))
    house_id: Mapped[int] = mapped_column(ForeignKey('houses.id'))
    
    country: Mapped["Country"] = relationship("Country")
    city: Mapped["City"] = relationship("City")
    street: Mapped['Street'] = relationship("Street")
    house: Mapped['House'] = relationship("House")