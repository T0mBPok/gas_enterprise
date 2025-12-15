from sqlalchemy.orm import Mapped
from .database import Base, int_pk


class Region(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]


class EnterpriseStatus(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class EnterpriseType(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class DepositStatus(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class WellStatus(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class ProcessType(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class ProcessStatus(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]

class Transport(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class DeliveryStatus(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class OrderStatus(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class Position(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]


class Qualification(Base):
    Id: Mapped[int_pk]
    code: Mapped[str]
    name: Mapped[str]
    description: Mapped[str | None]