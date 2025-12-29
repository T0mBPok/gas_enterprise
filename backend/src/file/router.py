import os
import shutil
from uuid import uuid4
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from src.user.dependencies import get_current_user
from src.file.logic import FileLogic

router = APIRouter(prefix='/files', tags=['Файлы'])
UPLOAD_DIR = 'media'

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    user: str = Depends(get_current_user)
):
    if user.role != "admin":
        raise HTTPException(403)
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    allowed = {
        "text/csv",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/pdf",
        "image/png",
        "image/jpeg",
    }

    if file.content_type not in allowed:
        raise HTTPException(400, "Unsupported file type")

    path = f"media/{uuid4()}_{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return await FileLogic.add(
        filename=path,
        original_name=file.filename,
        uploaded_by=user.id,
    )
    
@router.get("/download/{id}")
async def download_file(
    id: int,
    user: str = Depends(get_current_user)
):
    file = await FileLogic.get_one_or_none_by_id(id=id)

    return FileResponse(
        path=file.filename,
        filename=file.original_name
    )

    
@router.get("/")
async def get_files(
    user: str = Depends(get_current_user)
):
    return await FileLogic.get_all()
