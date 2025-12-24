from fastapi import APIRouter, Depends, Path, Response
from fastapi.responses import JSONResponse
from src.user.schemas import SUserCreate, SUserCreateValidate, SUserAuth, SUser, SUserUpdate
from src.user.logic import UserLogic
from src.user.dependencies import get_current_user
from pydantic import ValidationError


router = APIRouter(prefix='/user', tags=['Пользователь'])

@router.post('/create/', response_model=SUser)
async def create_user(user_data: SUserCreateValidate, user: str = Depends(get_current_user)) -> dict:
    new_user = await UserLogic.create(user_data, user)
    return new_user

@router.get('/me/', response_model=SUser)
async def get_user(user: str = Depends(get_current_user)):
    return user

@router.get('/list/', response_model = list[SUser])
async def get_user_list(user: str = Depends(get_current_user)):
    return await UserLogic.get_user_list(user)

@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth) -> dict:
    access_token = await UserLogic.auth(user_data)
    response = JSONResponse(content={
        'ok': True,
        'access_token': access_token,
        'message': "Авторизация успешна!"   
    })
    response.set_cookie(key='access_user_token', value=access_token, httponly=True, secure=True, samesite='None', max_age=3600)
    return response

@router.get("/check/")
async def check_user(user: str = Depends(get_current_user)):
    return {"ok": True, "user": {"id": user.id, "username": user.username, "email": user.email}}

@router.post("/logout/")
async def logout_user(response: Response):
    response = JSONResponse(content={"message": "Пользователь успешно вышел из системы!"})
    response.delete_cookie(
        key="access_user_token",
        path="/",
        secure=True,
        samesite="None"
    )
    return response

@router.post("/{id}", summary="Удалить пользователя")
async def delete_user(id: int = Path(..., gt=0), user: str = Depends(get_current_user)):
    return await UserLogic.delete_user(id, user)

@router.put("/{id}", summary="Обновить пользователя")
async def update_user(update_data: SUserUpdate, user: str = Depends(get_current_user), id: int = Path(..., gt=0)):
    return await UserLogic.update_user(id, user, **update_data.model_dump(exclude_unset=True))