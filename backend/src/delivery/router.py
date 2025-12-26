from fastapi import APIRouter, Depends, Path
from src.user.dependencies import get_current_user
from src.delivery.logic import DeliveryLogic
from src.delivery.rb import RBDelivery
from src.delivery.schemas import GetDelivery, AddDelivery, UpdateDelivery

router = APIRouter(prefix="/delivery", tags=["Доставки"])


@router.get("/", summary="Получить список доставок", response_model=list[GetDelivery])
async def get_deliveries(filters: RBDelivery = Depends(), user: str = Depends(get_current_user)):
    return await DeliveryLogic.get_all_deliveries(**filters.to_dict())


@router.get("/{id}", summary="Получить доставку по id", response_model=GetDelivery)
async def get_delivery_by_id(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await DeliveryLogic.get_delivery_by_id(id=id)


@router.post("/", summary="Добавить доставку", response_model=AddDelivery)
async def add_delivery(form_data: AddDelivery = Depends(), user: str = Depends(get_current_user)):
    return await DeliveryLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить доставку")
async def delete_delivery(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    await DeliveryLogic.delete(id=id)
    return {"message": f"Доставка с id={id} удалена"}


@router.put("/{id}", summary="Обновить доставку", response_model=UpdateDelivery)
async def update_delivery(delivery: UpdateDelivery, id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    values = delivery.model_dump(exclude_unset=True)
    await DeliveryLogic.update_delivery(id=id, **values)
    return values