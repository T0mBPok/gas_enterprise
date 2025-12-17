from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base
from src.enterprise.models import Enterprise
from src.classifiers.models import DepositStatus, Region

class Deposit(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("depositstatuses.id"))

    status: Mapped["DepositStatus"] = relationship("DepositStatus")
    region: Mapped["Region"] = relationship("Region")
    enterprise = relationship("Enterprise", back_populates="deposit")
