from src.user.dao import UserDAO
from src.exceptions import UserAlreadyExistsException, PasswordMismatchException, IncorrectEmailOrPasswordException, ForbiddenException
from src.user.auth import get_pass_hashed, authenticate_user, create_token


class UserLogic(UserDAO):
    @classmethod
    async def create(cls, user_data, user) -> dict:
        if not user.role == 'admin':
            raise ForbiddenException
        
        user_exists = await cls.get_one_or_none(email=user_data.email)
        if user_exists:
            raise UserAlreadyExistsException
        
        password = get_pass_hashed(user_data.password)
        
        new_user = await UserDAO.add(
            email = user_data.email,
            username = user_data.username,
            password = password
        )
        return new_user

    async def auth(user_data) -> dict:
        check = await authenticate_user(**user_data.model_dump())
        if check is None:
            raise IncorrectEmailOrPasswordException
        return create_token({'sub': str(check.id)})
    
    @classmethod
    async def get_user_list(cls, user: str):
        if not user.role == 'admin':
            raise ForbiddenException    
        return await cls.get_except_current(current_id=int(user.id))
    
    @classmethod
    async def delete_user(cls, user_id, user):
        if not user.role == 'admin':
            raise ForbiddenException
        return await cls.delete(id=user_id)
    
    @classmethod
    async def update_user(cls, user_id, user, **update_data):
        if not user.role == 'admin':
            raise ForbiddenException
        if 'password' in update_data.keys():
            update_data["password"] = get_pass_hashed(update_data["password"])
        return await cls.update(id=user_id, **update_data)