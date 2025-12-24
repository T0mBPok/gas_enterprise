from fastapi import APIRouter, Depends, Path
from backend.src.user.dependencies import get_current_user
from src.enterprise.logic import EnterpriseLogic
from src.enterprise.rb import RBEnterprise
from src.enterprise.schemas import GetEnterprise, AddEnterprise, UpdateEnterprise

router = APIRouter(prefix="/enterprise", tags=["Предприятия"])


@router.get("/", summary="Получить список предприятий", response_model=list[GetEnterprise])
async def get_enterprises(filters: RBEnterprise = Depends(), user: str = Depends(get_current_user)):
    return await EnterpriseLogic.get_all_enterprises(**filters.to_dict())


@router.get("/{id}", summary="Получить предприятие по id", response_model=GetEnterprise)
async def get_enterprise_by_id(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await EnterpriseLogic.get_enterprise_by_id(id=id)


@router.post("/", summary="Добавить предприятие", response_model=AddEnterprise)
async def add_enterprise(form_data: AddEnterprise = Depends(), user: str = Depends(get_current_user)):
    return await EnterpriseLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить предприятие")
async def delete_enterprise(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    await EnterpriseLogic.delete(id=id)
    return {"message": f"Предприятие с id={id} удалено"}


@router.put("/{id}", summary="Обновить предприятие", response_model=UpdateEnterprise)
async def update_enterprise(enterprise: UpdateEnterprise, id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    values = enterprise.model_dump(exclude_unset=True)
    await EnterpriseLogic.update_enterprise(id=id, **values)
    return values