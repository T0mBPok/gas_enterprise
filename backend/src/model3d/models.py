from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database import Base

class Model3D(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str]
    format: Mapped[str]

    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"), unique=False)
    well = relationship("Well", back_populates="models")