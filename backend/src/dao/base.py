from src.database import with_session
from sqlalchemy import exists, select, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status


class BaseDAO:
    model = None
    
    default_relations = []

    @classmethod
    @with_session
    async def get(cls, session, **filter_by):
        data = await session.execute(select(cls.model).filter_by(**filter_by))
        return data.scalars().all()
    
    @classmethod
    @with_session
    async def get_except_current(cls, session, current_id: int):
        data = await session.execute(select(cls.model).filter(cls.model.id!=current_id))
        return data.scalars().all()
    
    @classmethod
    @with_session
    async def get_one_or_none_by_id(cls, session, id: int):
        data = await session.execute(select(cls.model).filter_by(id=id))
        return data.scalar_one_or_none()
    
    @classmethod
    @with_session
    async def get_one_or_none(cls, session, **filter_by):
        data = await session.execute(select(cls.model).filter_by(**filter_by))
        return data.scalar_one_or_none()
            
    @classmethod
    @with_session
    async def add(cls, session, **values):
        new_obj = cls.model(**values)
        session.add(new_obj)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return new_obj
            
    @classmethod
    @with_session
    async def delete(cls, session, id: int):
        check = await session.execute(delete(cls.model).where(cls.model.id == id))
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return check.rowcount
    
    @classmethod
    @with_session
    async def update(cls, session, id:int, **values):
        result = await session.execute(update(cls.model).where(cls.model.id == id).values(**values))
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return result.rowcount
    
    @classmethod
    def _with_related(cls, query, *relations):
        for rel in relations:
            if isinstance(rel, str):
                attr = getattr(cls.model, rel)
            else:
                attr = rel
            query = query.options(selectinload(attr))
            
        # for rel in getattr(cls, "default_relations", []):
        #     query = query.options(selectinload(getattr(cls.model, rel)))
            
        return query


    @classmethod
    @with_session
    async def get_all(cls, *relations, session=None, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        query = cls._with_related(query, *relations)

        result = await session.scalars(query)
        return result.all()

    @classmethod
    @with_session
    async def get_one_by_id(cls, id: int, *relations, session=None):
        query = select(cls.model).where(cls.model.id == id)
        query = cls._with_related(query, *relations)

        result = await session.scalars(query)
        return result.one_or_none()
    
    @classmethod
    @with_session
    async def get_one(cls, session, *relations, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        query = cls._with_related(query, *relations)
        result = await session.scalars(query)
        return result.one_or_none()