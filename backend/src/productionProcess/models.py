from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from src.database import Base

class ProductionProcess(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    date_start: Mapped[Date | None]
    date_end: Mapped[Date | None]
    notes: Mapped[str | None]

    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprise.id"))
    well_id: Mapped[int | None] = mapped_column(ForeignKey("well.id"))

    type_id: Mapped[int] = mapped_column(ForeignKey("processtype.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("processstatus.id"))
