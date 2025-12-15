from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class Customer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    phone_num: Mapped[str]
    contact_info: Mapped[str]
