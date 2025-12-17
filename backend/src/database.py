from typing import Annotated
from src.config import get_db_url
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import mapped_column, DeclarativeBase, declared_attr

DATABASE_URL = get_db_url()
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit = False)
def with_session(func):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            return await func(*args, session=session, **kwargs)
    return wrapper

#Аннотации
int_pk = Annotated[int, mapped_column(primary_key=True)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]

class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        name = cls.__name__.lower()

        # y → ies
        if name.endswith("y") and not name.endswith(("ay", "ey", "iy", "oy", "uy")):
            return f"{name[:-1]}ies"

        # f → ves
        if name.endswith("fe"):
            return f"{name[:-2]}ves"
        if name.endswith("f"):
            return f"{name[:-1]}ves"

        # o → oes
        if name.endswith("o"):
            return f"{name}es"

        # s, x, z, ch, sh → es
        if name.endswith(("s", "x", "z", "ch", "sh")):
            return f"{name}es"

        # по умолчанию добавляем s
        return f"{name}s"
