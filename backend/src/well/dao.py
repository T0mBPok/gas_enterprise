from src.dao.base import BaseDAO
from src.well.models import Well
from src.enterprise.dao import EnterpriseDAO


class WellDAO(BaseDAO):
    model = Well

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
