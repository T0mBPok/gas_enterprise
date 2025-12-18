from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.order.dao import OrderDAO


class OrderLogic(OrderDAO):

    @classmethod
    @with_session
    async def update_order(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        exists_result = await session.scalar(stmt)

        if not exists_result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Заказ не найден"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_order_by_id(cls, id: int):
        order = await cls.get_one_with_relations(id)
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Заказ не найден"
            )
        return order

    @classmethod
    async def get_all_orders(cls, **filter_by):
        return await cls.get_all_with_relations(**filter_by)