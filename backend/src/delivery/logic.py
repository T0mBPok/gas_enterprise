from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.delivery.dao import DeliveryDAO


class DeliveryLogic(DeliveryDAO):
    @classmethod
    @with_session
    async def update_delivery(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        delivery_exists = await session.scalar(stmt)

        if not delivery_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Доставка не найдена"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_delivery_by_id(cls, id: int):
        delivery = await cls.get_one_with_relations(id)
        if not delivery:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Доставка не найдена"
            )
        return delivery

    @classmethod
    async def get_all_deliveries(cls, **filter_by):
        return await cls.get_all_with_relations(**filter_by)