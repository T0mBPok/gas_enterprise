from fastapi import APIRouter, Depends, Path
from src.prodMetrics.logic import ProdMetricsLogic
from src.prodMetrics.rb import RBProdMetrics
from src.prodMetrics.schemas import GetProdMetrics, AddProdMetrics, UpdateProdMetrics
from src.user.dependencies import get_current_user

router = APIRouter(prefix="/metrics", tags=["Показатели скважин"])


@router.get("/", summary="Получить список показателей", response_model=list[GetProdMetrics])
async def get_metrics(filters: RBProdMetrics = Depends(), user: str = Depends(get_current_user)):
    return await ProdMetricsLogic.get_all_metrics(**filters.to_dict())


@router.get("/{id}", summary="Получить показатель по id", response_model=GetProdMetrics)
async def get_metric_by_id(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await ProdMetricsLogic.get_metric_by_id(id=id)


@router.post("/", summary="Добавить показатель", response_model=AddProdMetrics)
async def add_metric(form_data: AddProdMetrics = Depends(), user: str = Depends(get_current_user)):
    return await ProdMetricsLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить показатель")
async def delete_metric(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    await ProdMetricsLogic.delete(id=id)
    return {"message": f"Показатель с id={id} удален"}


@router.put("/{id}", summary="Обновить показатель", response_model=UpdateProdMetrics)
async def update_metric(metric: UpdateProdMetrics, id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    values = metric.model_dump(exclude_unset=True)
    await ProdMetricsLogic.update_metric(id=id, **values)
    return values