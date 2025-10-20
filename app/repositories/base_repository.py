from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.model.base_model import BaseModel
from uuid import UUID

T = TypeVar("T", bound=BaseModel)

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def get_by_id(self, session: AsyncSession, id: UUID) -> Optional[T]:
        stmt = select(self.model).where(self.model.id == id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self, session: AsyncSession) -> List[T]:
        stmt = select(self.model)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def create(self, session: AsyncSession, obj_in: dict) -> T:
        db_obj = self.model(**obj_in)
        session.add(obj_in)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(self, session:AsyncSession, id: UUID, obj_in: dict) -> Optional[T]:
        stmt = (update(self.model).where(self.model,id == id).values(**obj_in).returning(self.model))
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one_or_none() 

    async def delete(self, session: AsyncSession, id: UUID) -> bool:
        stmt = delete(self.model).where(self.model.id == id)
        await session.execute(stmt)
        await session.commit()
        return True