from fastapi import APIRouter, Depends, Path
from src.deposit.logic import DepositLogic
from src.deposit.schemas import GetDeposit, AddDeposit, UpdateDeposit
from src.deposit.rb import RBDeposit

router = APIRouter(prefix="/deposit", tags=["Месторождения"])


@router.get("/", summary="Получить список месторождений", response_model=list[GetDeposit])
async def get_deposits(filters: RBDeposit = Depends()):
    return await DepositLogic.get_all_deposits(**filters.to_dict())


@router.get("/{id}", summary="Получить месторождение по id", response_model=GetDeposit)
async def get_deposit_by_id(id: int = Path(..., gt=0)):
    return await DepositLogic.get_depost_by_id(id=id)


@router.post("/", summary="Добавить месторождение", response_model=AddDeposit)
async def add_deposit(form_data: AddDeposit = Depends()):
    return await DepositLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить месторождение")
async def delete_deposit(id: int = Path(..., gt=0)):
    await DepositLogic.delete(id=id)
    return {"message": f"Месторождение с id={id} удалено"}


@router.put("/{id}", summary="Обновить месторождение", response_model=UpdateDeposit)
async def update_deposit(deposit: UpdateDeposit, id: int = Path(..., gt=0)):
    values = deposit.model_dump(exclude_unset=True)
    await DepositLogic.update_deposit(id=id, **values)
    return values
