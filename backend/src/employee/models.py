from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base, int_pk
from src.enterprise.models import Enterprise
from src.classifiers.models import Position, Qualification


class Employee(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    hire_date: Mapped[date]

    position_id: Mapped[int] = mapped_column(ForeignKey("positions.id"))
    qualification_id: Mapped[int] = mapped_column(ForeignKey("qualifications.id"))
    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprises.id"))

    position: Mapped["Position"] = relationship("Position")
    qualification: Mapped["Qualification"] = relationship("Qualification")
    enterprise: Mapped["Enterprise"] = relationship("Enterprise", back_populates='employees')