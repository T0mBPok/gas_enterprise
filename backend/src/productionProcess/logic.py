from sqlalchemy import select, exists
from fastapi import HTTPException, status
from src.database import with_session
from src.productionProcess.dao import ProductionProcessDAO
from src.services.email import send_email
from src.user.logic import UserLogic


class ProductionProcessLogic(ProductionProcessDAO):

    @classmethod
    @with_session
    async def update_process(cls, session, id: int, **values):
        if not values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нет полей для обновления"
            )

        stmt = select(cls.model).where(cls.model.id == id)
        process = await session.scalar(stmt)

        if not process:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Процесс не найден"
            )

        # 1️⃣ обновляем процесс
        updated = await cls.update(id=id, **values)

        # 2️⃣ получаем email всех пользователей
        emails = await UserLogic.get_all_emails()

        # 3️⃣ отправляем уведомление
        if emails:
            send_email(
                to=emails,
                subject="Обновление производственного процесса",
                body=(
                    f"Производственный процесс был обновлён.\n\n"
                    f"ID процесса: {id}\n"
                    f"Изменённые поля: {', '.join(values.keys())}"
                )
            )

        return updated

    @classmethod
    async def get_process_by_id(cls, id: int):
        process = await cls.get_one_with_relations(id)
        if not process:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Процесс не найден"
            )
        return process

    @classmethod
    async def get_all_processes(cls, **filter_by):
        return await cls.get_all_with_relations(**filter_by)