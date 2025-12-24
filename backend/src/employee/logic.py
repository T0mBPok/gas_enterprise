from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.employee.dao import EmployeeDAO


class EmployeeLogic(EmployeeDAO):

    @classmethod
    @with_session
    async def update_employee(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(exists().where(cls.model.id == id))
        exists_emp = await session.scalar(stmt)

        if not exists_emp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Сотрудник не найден"
            )

        return await cls.update(id=id, **values)

    @classmethod
    async def get_employee_by_id(cls, id: int):
        emp = await cls.get_one_with_relations(id)
        if not emp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Сотрудник не найден"
            )
        return emp

    @classmethod
    async def get_all_employees(cls, **filter_by):
        return await cls.get_all_with_relations(**filter_by)