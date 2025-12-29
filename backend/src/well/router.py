from fastapi import APIRouter, Depends, Path
from src.well.logic import WellLogic
from src.well.rb import RBWell
from src.well.schemas import GetWell, AddWell, UpdateWell

router = APIRouter(prefix="/well", tags=["Скважины"])


@router.get("/", summary="Получить список скважин", response_model=list[GetWell])
async def get_wells(filters: RBWell = Depends()):
    return await WellLogic.get_all_wells(**filters.to_dict())


@router.get("/{id}", summary="Получить скважину по id", response_model=GetWell)
async def get_well_by_id(id: int = Path(..., gt=0)):
    return await WellLogic.get_well_by_id(id=id)


@router.post("/", summary="Добавить скважину", response_model=AddWell)
async def add_well(form_data: AddWell):
    return await WellLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить скважину")
async def delete_well(id: int = Path(..., gt=0)):
    await WellLogic.delete(id=id)
    return {"message": f"Скважина с id={id} удалена"}


@router.put("/{id}", summary="Обновить скважину", response_model=UpdateWell)
async def update_well(well: UpdateWell, id: int = Path(..., gt=0)):
    values = well.model_dump(exclude_unset=True)
    await WellLogic.update_well(id=id, **values)
    return values