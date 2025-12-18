from fastapi import APIRouter, Depends, Path
from src.productionProcess.logic import ProductionProcessLogic
from src.productionProcess.rb import RBProductionProcess
from src.productionProcess.schemas import GetProductionProcess, AddProductionProcess, UpdateProductionProcess


router = APIRouter(prefix="/process", tags=["Производственные процессы"])

@router.get("/", summary="Получить список процессов", response_model=list[GetProductionProcess])
async def get_processes(filters: RBProductionProcess = Depends()):
    return await ProductionProcessLogic.get_all_processes(**filters.to_dict())


@router.get("/{id}", summary="Получить процесс по id", response_model=GetProductionProcess)
async def get_process_by_id(id: int = Path(..., gt=0)):
    return await ProductionProcessLogic.get_process_by_id(id=id)


@router.post("/", summary="Добавить процесс", response_model=AddProductionProcess)
async def add_process(form_data: AddProductionProcess = Depends()):
    return await ProductionProcessLogic.add(**form_data.model_dump())


@router.delete("/{id}", summary="Удалить процесс")
async def delete_process(id: int = Path(..., gt=0)):
    await ProductionProcessLogic.delete(id=id)
    return {"message": f"Процесс с id={id} удален"}


@router.put("/{id}", summary="Обновить процесс", response_model=UpdateProductionProcess)
async def update_process(process: UpdateProductionProcess, id: int = Path(..., gt=0)):
    values = process.model_dump(exclude_unset=True)
    await ProductionProcessLogic.update_process(id=id, **values)
    return values