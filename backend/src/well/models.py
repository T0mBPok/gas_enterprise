from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from src.Model3d.models import Model3D
from src.prodMetrics.models import ProdMetrics
from src.classifiers.models import WellStatus

class Well(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str]
    depth: Mapped[float]

    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprises.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("wellstatuses.id"))

    enterprise: Mapped["Enterprise"] = relationship("Enterprise", back_populates="wells")
    models = relationship("Model3D", back_populates="well")
    metrics = relationship("ProdMetrics", back_populates="well")
    status: Mapped["WellStatus"] = relationship("WellStatus")
