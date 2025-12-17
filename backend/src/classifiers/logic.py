from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from .dao import ClassifierDAO


class ClassifierLogic(ClassifierDAO):

    @classmethod
    @with_session
    async def create(cls, session, **values):
        stmt = select(exists().where(cls.model.code == values["code"]))
        exists_code = await session.scalar(stmt)

        if exists_code:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Код уже существует"
            )

        return await cls.add(**values)

    @classmethod
    @with_session
    async def update_classifier(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.Id == id))
        exists_obj = await session.scalar(stmt)

        if not exists_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Запись не найдена"
            )

        return await cls.update(id=id, **values)
