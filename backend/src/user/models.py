from sqlalchemy import ForeignKey
from src.database import int_pk, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    enterprise_id: Mapped[int | None] = mapped_column(ForeignKey("enterprises.id"))

    enterprise: Mapped["Enterprise"] = relationship("Enterprise",back_populates="employees")