from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base

class Deposit(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("depositstatus.id"))

    enterprises = relationship("Enterprise", back_populates="deposit")
