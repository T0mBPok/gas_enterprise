from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date
from src.database import Base

class ProdMetrics(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date]
    gas_volume: Mapped[float]
    pressure: Mapped[float]
    temperature: Mapped[float]

    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    well = relationship("Well", back_populates="metrics")