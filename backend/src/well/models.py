from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class Well(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str]
    creation_date: Mapped[Date]
    depth: Mapped[float]

    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprise.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("wellstatus.id"))

    enterprise = relationship("Enterprise", back_populates="wells")
    models = relationship("Model3D", back_populates="well")
    metrics = relationship("ProdMetrics", back_populates="well")
