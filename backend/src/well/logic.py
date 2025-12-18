from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.well.dao import WellDAO


class WellLogic(WellDAO):

    @classmethod
    @with_session
    async def update_well(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        well_exists = await session.scalar(stmt)

        if not well_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Скважина не найдена"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_well_by_id(cls, id: int):
        well = await cls.get_one_with_enterprise(id)
        if not well:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Скважина не найдена"
            )
        return well

    @classmethod
    async def get_all_wells(cls, **filter_by):
        return await cls.get_all_with_enterprise(**filter_by)