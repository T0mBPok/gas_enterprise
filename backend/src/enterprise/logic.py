from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.enterprise.dao import EnterpriseDAO


class EnterpriseLogic(EnterpriseDAO):

    @classmethod
    @with_session
    async def update_enterprise(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        enterprise_exists = await session.scalar(stmt)

        if not enterprise_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Предприятие не найдено"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_enterprise_by_id(cls, id: int):
        enterprise = await cls.get_one_with_deposit(id)
        if not enterprise:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Предприятие не найдено"
            )
        return enterprise

    @classmethod
    async def get_all_enterprises(cls, **filter_by):
        return await cls.get_all_with_deposit(**filter_by)