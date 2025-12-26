from fastapi import APIRouter, Depends, Path
from src.model3d.schemas import GetModel3D, ModelParams, default_model_params
from src.model3d.logic import Model3DLogic
from src.user.router import get_current_user

router = APIRouter(prefix="/models", tags=['3D Модели'])

@router.post("/generate/{well_id}")
async def generate(well_id: int, params: ModelParams = default_model_params, user: str = Depends(get_current_user)):
    return await Model3DLogic.generate_and_save(well_id, params)

@router.get("/view/{model_id}", summary="Просмотр PNG 3D модели")
async def view_model(model_id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await Model3DLogic.view_model(model_id)

@router.get("/download/{model_id}", summary="Скачать модель")
async def download(model_id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await Model3DLogic.download_model(model_id)

@router.get("/", summary="Получить список всех 3D моделей", response_model=list[GetModel3D])
async def get_all_models(user: str = Depends(get_current_user)):
    return await Model3DLogic.get_all_models()

@router.get("/{model_id}", summary="Получить 3D модель по id", response_model=GetModel3D)
async def get_model_by_id(model_id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await Model3DLogic.get_model_by_id(model_id)

@router.delete("/{model_id}", summary="Удалить 3D модель")
async def delete_model(model_id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await Model3DLogic.delete_model(model_id)