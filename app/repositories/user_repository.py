from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base_repository import BaseRepository
from app.model.user_model import UserModel
class UserRepository(BaseRepository[UserModel]):
    """Repository for UserModel."""

    def __init__(self):
        super().__init__(UserModel)

    async def get_by_email(self, session:AsyncSession, email:str) -> UserModel | None:
        """find the user by email"""
        stmt = select(self.model).where(self.model.email == email)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()