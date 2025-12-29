from fastapi import APIRouter, Depends, HTTPException, Path, Request
from src.order.logic import OrderLogic
from src.order.rb import RBOrder
from src.order.schemas import GetOrder, AddOrder, UpdateOrder
from src.user.dependencies import get_current_user
from src.services.export_orders_pdf import export_orders_pdf
from src.services.export_orders_xlsx import export_orders_xlsx

router = APIRouter(prefix="/order", tags=["Заказы"])


@router.get("/", response_model=list[GetOrder])
async def get_orders(filters: RBOrder = Depends(), user: str = Depends(get_current_user)):
    return await OrderLogic.get_all_orders(**filters.to_dict())

@router.get("/export")
async def export_orders(
    format: str,  # <- отдельно, FastAPI знает, что это query-параметр
    user: str = Depends(get_current_user)
):
    orders = await OrderLogic.get_all_orders()

    if format == "xlsx":
        return export_orders_xlsx(orders)
    elif format == "pdf":
        return export_orders_pdf(orders)
    else:
        raise HTTPException(400, "Unsupported format")

@router.get("/{id}", response_model=GetOrder)
async def get_order_by_id(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await OrderLogic.get_order_by_id(id=id)


@router.post("/", response_model=AddOrder)
async def add_order(form: AddOrder, user: str = Depends(get_current_user)):
    return await OrderLogic.add(**form.model_dump())


@router.delete("/{id}")
async def delete_order(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    await OrderLogic.delete(id=id)
    return {"message": f"Заказ с id={id} удален"}


@router.put("/{id}", response_model=UpdateOrder)
async def update_order(order: UpdateOrder, id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    values = order.model_dump(exclude_unset=True)
    await OrderLogic.update_order(id=id, **values)
    return values