from fastapi import APIRouter, Depends, Path
from src.delivery.logic import DeliveryLogic
from src.delivery.schemas import GetDelivery, AddDelivery, UpdateDelivery
from src.delivery.rb import RBDelivery

router = APIRouter(prefix="/delivery", tags=["Доставки"])


@router.get("/", summary="Получить список доставок", response_model=list[GetDelivery])
async def get_deliveries(filters: RBDelivery = Depends()):
    return await DeliveryLogic.get_all_deliveries(**filters.to_dict())


@router.get("/{id}", summary="Получить доставку по id", response_model=GetDelivery)
async def get_delivery_by_id(id: int = Path(..., gt=0)):
    return await DeliveryLogic.get_delivery_by_id(id=id)


@router.post("/", summary="Добавить доставку", response_model=AddDelivery)
async def add_delivery(form_data: AddDelivery = Depends()):
    return await DeliveryLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить доставку")
async def delete_delivery(id: int = Path(..., gt=0)):
    await DeliveryLogic.delete(id=id)
    return {"message": f"Доставка с id={id} удалена"}


@router.put("/{id}", summary="Обновить доставку", response_model=UpdateDelivery)
async def update_delivery(delivery: UpdateDelivery, id: int = Path(..., gt=0)):
    values = delivery.model_dump(exclude_unset=True)
    await DeliveryLogic.update_delivery(id=id, **values)
    return values