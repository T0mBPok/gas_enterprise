from sqlalchemy import ForeignKey
from src.database import Base, int_pk
from sqlalchemy.orm import Mapped, mapped_column

class File(Base):
    id: Mapped[int_pk]
    filename: Mapped[str]
    original_name: Mapped[str]

    uploaded_by: Mapped[int] = mapped_column(ForeignKey("users.id"))