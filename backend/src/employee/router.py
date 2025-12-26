from fastapi import APIRouter, Depends, Path
from src.user.dependencies import get_current_user
from src.employee.logic import EmployeeLogic
from src.employee.rb import RBEmployee
from src.employee.schemas import GetEmployee, AddEmployee, UpdateEmployee


router = APIRouter(prefix="/employee", tags=["Сотрудники"])

@router.get("/", summary="Получить список сотрудников", response_model=list[GetEmployee])
async def get_employees(filters: RBEmployee = Depends(), user: str = Depends(get_current_user)):
    return await EmployeeLogic.get_all_employees(**filters.to_dict())


@router.get("/{id}", summary="Получить сотрудника по id", response_model=GetEmployee)
async def get_employee_by_id(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await EmployeeLogic.get_employee_by_id(id=id)


@router.post("/", summary="Добавить сотрудника", response_model=AddEmployee)
async def add_employee(form_data: AddEmployee = Depends(), user: str = Depends(get_current_user)):
    return await EmployeeLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить сотрудника")
async def delete_employee(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    await EmployeeLogic.delete(id=id)
    return {"message": f"Сотрудник с id={id} удален"}


@router.put("/{id}", summary="Обновить сотрудника", response_model=UpdateEmployee)
async def update_employee(employee: UpdateEmployee, id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    values = employee.model_dump(exclude_unset=True)
    await EmployeeLogic.update_employee(id=id, **values)
    return values