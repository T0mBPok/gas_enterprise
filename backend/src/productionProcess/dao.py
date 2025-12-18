from src.dao.base import BaseDAO
from src.productionProcess.models import ProductionProcess
from src.enterprise.dao import EnterpriseDAO
from src.well.dao import WellDAO


class ProductionProcessDAO(BaseDAO):
    model = ProductionProcess

    @classmethod
    async def get_one_with_relations(cls, id: int):
        process = await cls.get_one_by_id(id, "type", "status",)
        
        if process.enterprise_id:
            enterprise = await EnterpriseDAO.get_one_with_deposit(process.enterprise_id)
            process.enterprise = enterprise

        if process.well_id:
            well = await WellDAO.get_one_with_enterprise(process.well_id)
            process.well = well

        return process

    @classmethod
    async def get_all_with_relations(cls, **filter_by):
        processes = await cls.get_all("type", "status", **filter_by)

        for p in processes:
            if p.enterprise_id:
                p.enterprise = await EnterpriseDAO.get_one_with_deposit(p.enterprise_id)

            if p.well_id:
                p.well = await WellDAO.get_one_with_enterprise(p.well_id)

        return processes