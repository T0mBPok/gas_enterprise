from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.deposit.dao import DepositDAO


class DepositLogic(DepositDAO):

    @classmethod
    @with_session
    async def update_deposit(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        deposit_exists = await session.scalar(stmt)

        if not deposit_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Месторождение не найдено"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_depost_by_id(cls, id: int):
        deposit = await cls.get_one_by_id(id, "region", "status")
        if not deposit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Месторождение не найдено"
            )
        return deposit
    
    @classmethod
    async def get_all_deposits(cls, **filter_by):
        classifiers = ["region", "status"]
        return await cls.get_all(*classifiers, **filter_by)