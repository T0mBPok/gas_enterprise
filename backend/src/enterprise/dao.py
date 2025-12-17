from src.deposit.dao import DepositDAO
from src.dao.base import BaseDAO
from src.enterprise.models import Enterprise


class EnterpriseDAO(BaseDAO):
    model = Enterprise
    
    @classmethod
    async def get_one_with_deposit(cls, id: int):
        enterprise = await cls.get_one_by_id(
            id, "status", "type", "country", "city", "street", "house"
        )
        if enterprise and enterprise.deposit_id:
            deposit = await DepositDAO.get_one_by_id(enterprise.deposit_id, "region", "status")
            enterprise.deposit = deposit
        return enterprise

    @classmethod
    async def get_all_with_deposit(cls, **filter_by):
        enterprises = await cls.get_all(
            "status", "type", "country", "city", "street", "house", **filter_by
        )
        for ent in enterprises:
            if ent.deposit_id:
                deposit = await DepositDAO.get_one_by_id(ent.deposit_id, "region", "status")
                ent.deposit = deposit
        return enterprises