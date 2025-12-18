from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.prodMetrics.dao import ProdMetricsDAO


class ProdMetricsLogic(ProdMetricsDAO):

    @classmethod
    @with_session
    async def update_metric(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        exists_metric = await session.scalar(stmt)
        if not exists_metric:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Показатель не найден"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_metric_by_id(cls, id: int):
        metric = await cls.get_one_with_well(id)
        if not metric:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Показатель не найден"
            )
        return metric

    @classmethod
    async def get_all_metrics(cls, **filter_by):
        return await cls.get_all_with_well(**filter_by)