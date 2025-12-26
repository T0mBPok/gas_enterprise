from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.dao.base import BaseDAO
from src.well.models import Well
from src.enterprise.dao import EnterpriseDAO
from src.database import with_session


class WellDAO(BaseDAO):
    model = Well
    
    @classmethod
    @with_session
    async def add(cls, session, **data):
        well = Well(**data)
        session.add(well)
        await session.flush()
        await session.commit()

        result = await session.execute(
            select(Well)
            .options(
                selectinload(Well.enterprise),
                selectinload(Well.status),
            )
            .where(Well.id == well.id)
        )
        return result.scalar_one()

    @classmethod
    async def get_one_with_enterprise(cls, id: int):
        well = await cls.get_one_by_id(
            id, "status"
        )
        if well and well.enterprise_id:
            enterprise = await EnterpriseDAO.get_one_with_deposit(well.enterprise_id)
            well.enterprise = enterprise
        return well

    @classmethod
    async def get_all_with_enterprise(cls, **filter_by):
        wells = await cls.get_all(
            "status", **filter_by
        )
        for w in wells:
            if w.enterprise_id:
                enterprise = await EnterpriseDAO.get_one_with_deposit(w.enterprise_id)
                w.enterprise = enterprise
        return wells
