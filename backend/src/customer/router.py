from fastapi import APIRouter, Depends, Path
from backend.src.user.dependencies import get_current_user
from src.customer.logic import CustomerLogic
from src.customer.rb import RBCustomer
from src.customer.schemas import GetCustomer, AddCustomer, UpdateCustomer

router = APIRouter(prefix="/customer", tags=["Клиенты"])


@router.get("/", summary="Получить список клиентов", response_model=list[GetCustomer])
async def get_customers(filters: RBCustomer = Depends(), user: str = Depends(get_current_user)):
    return await CustomerLogic.get_all_customers(**filters.to_dict())


@router.get("/{id}", summary="Получить клиента по id", response_model=GetCustomer)
async def get_customer_by_id(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await CustomerLogic.get_customer_by_id(id=id)


@router.post("/", summary="Добавить клиента", response_model=AddCustomer)
async def add_customer(form_data: AddCustomer = Depends(), user: str = Depends(get_current_user)):
    return await CustomerLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить клиента")
async def delete_customer(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    await CustomerLogic.delete(id=id)
    return {"message": f"Клиент с id={id} удален"}


@router.put("/{id}", summary="Обновить клиента", response_model=UpdateCustomer)
async def update_customer(customer: UpdateCustomer, id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    values = customer.model_dump(exclude_unset=True)
    await CustomerLogic.update_customer(id=id, **values)
    return values
