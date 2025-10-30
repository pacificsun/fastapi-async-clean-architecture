from typing import Generic, TypeVar, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base_repository import BaseRepository

T = TypeVar("T")

class BaseService(Generic[T]):
    """Base Service class with common CRUD operations. """
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    async def get_all(self, session: AsyncSession) -> List[T]:
        return await self.repository.get_all(session)
    
    async def get_by_id(self, session: AsyncSession, id: str) -> Optional[T]:
        return await self.repository.get_by_id(session, id)
    
    async def create(self, session: AsyncSession, obj_in: T) -> T:
        return await self.repository.create(session, obj_in)
    
    async def update(self, session: AsyncSession, id: str, obj_in: dict) -> Optional[T]:
        return await self.repository.update(session, id, obj_in)
    
    async def delete(self, session: AsyncSession, id: str) -> bool:
        return await self.repository.delete(session, id)