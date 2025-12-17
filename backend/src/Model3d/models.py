from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey
from datetime import date
from src.database import Base

class Model3D(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str]
    format: Mapped[str]
    created_at: Mapped[date]

    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    well = relationship("Well", back_populates="models")