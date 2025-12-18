from fastapi import APIRouter, Depends, Path
from src.order.logic import OrderLogic
from src.order.rb import RBOrder
from src.order.schemas import GetOrder, AddOrder, UpdateOrder

router = APIRouter(prefix="/order", tags=["Заказы"])


@router.get("/", response_model=list[GetOrder])
async def get_orders(filters: RBOrder = Depends()):
    return await OrderLogic.get_all_orders(**filters.to_dict())


@router.get("/{id}", response_model=GetOrder)
async def get_order_by_id(id: int = Path(..., gt=0)):
    return await OrderLogic.get_order_by_id(id=id)


@router.post("/", response_model=AddOrder)
async def add_order(form: AddOrder = Depends()):
    return await OrderLogic.add(**form.model_dump())


@router.delete("/{id}")
async def delete_order(id: int = Path(..., gt=0)):
    await OrderLogic.delete(id=id)
    return {"message": f"Заказ с id={id} удален"}


@router.put("/{id}", response_model=UpdateOrder)
async def update_order(order: UpdateOrder, id: int = Path(..., gt=0)):
    values = order.model_dump(exclude_unset=True)
    await OrderLogic.update_order(id=id, **values)
    return values