from sqlalchemy import ForeignKey
from src.database import int_pk, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str] = mapped_column(default='user')