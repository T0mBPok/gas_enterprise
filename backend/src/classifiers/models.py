from sqlalchemy.orm import Mapped
from ..database import Base, int_pk


class Region(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class Country(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class City(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class Street(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class House(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class EnterpriseStatus(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class EnterpriseType(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class DepositStatus(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class WellStatus(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class ProcessType(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class ProcessStatus(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class Transport(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class DeliveryStatus(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class OrderStatus(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class Position(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class Qualification(Base):
    id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]