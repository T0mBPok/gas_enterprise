from src.dao.base import BaseDAO
from src.prodMetrics.models import ProdMetrics
from src.well.dao import WellDAO


class ProdMetricsDAO(BaseDAO):
    model = ProdMetrics

    @classmethod
    async def get_one_with_well(cls, id: int):
        metric = await cls.get_one_by_id(id)
        if metric and metric.well_id:
            well = await WellDAO.get_one_with_enterprise(metric.well_id)
            metric.well = well
        return metric

    @classmethod
    async def get_all_with_well(cls, **filter_by):
        metrics = await cls.get_all(**filter_by)
        for m in metrics:
            if m.well_id:
                well = await WellDAO.get_one_with_enterprise(m.well_id)
                m.well = well
        return metrics