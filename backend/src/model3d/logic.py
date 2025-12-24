import os
from fastapi import HTTPException, status
from fastapi.responses import FileResponse
from src.model3d.dao import Model3DDAO
from src.services.generate_3d_mesh import save_3d_model_stl

class Model3DLogic(Model3DDAO):
    @classmethod
    async def generate_and_save(cls, well_id: int, params: str):
        path = save_3d_model_stl(params.model_dump())
        return await cls.add(file_path=path, format="stl", well_id=well_id)
    
    @classmethod
    async def view_model(cls, model_id: int):
        # Проверяем существование записи
        model = await cls.get_one_or_none_by_id(id=model_id)
        if not model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Модель не найдена"
            )

        file_path = model.file_path

        # Проверяем существование файла
        if not os.path.exists(file_path):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Файл модели отсутствует на сервере"
            )

        # Возвращаем PNG файл
        return FileResponse(
            file_path,
            media_type="image/png",
            filename=os.path.basename(file_path),
            headers={"Content-Disposition": "inline"}
        )
        
    @classmethod
    async def download_model(cls, model_id: int):
        model = await cls.get_one_or_none(id=model_id)
        if not model:
            raise HTTPException(status_code=404, detail="Model not found")

        return FileResponse(
            path=model.file_path,
            media_type="application/octet-stream",
            filename=os.path.basename(model.file_path)
        )
        
    @classmethod
    async def get_all_models(cls):
        return await cls.get()
    
    @classmethod
    async def get_model_by_id(cls, model_id: int):
        model = await cls.get_one_or_none_by_id(model_id)
        if not model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"3D модель с id={model_id} не найдена"
            )
        return model

    @classmethod
    async def delete_model(cls, model_id: int):
        model = await cls.get_one_or_none_by_id(model_id)
        if not model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"3D модель с id={model_id} не найдена"
            )

        # удаляем файл с диска
        file_path = model.file_path
        if os.path.exists(file_path):
            os.remove(file_path)

        # удаляем запись из БД
        await cls.delete(model_id)
        return {"message": f"3D модель с id={model_id} удалена"}