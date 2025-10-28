from app.services.base_service import BaseService
from app.repositories.user_repository import UserRepository
from app.model.user_model import UserModel

from sqlalchemy.ext.asyncio import AsyncSession

class UserService(BaseService[UserModel]):
    """Service layer for User Business Logic."""
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    async def get_by_email(self, session:AsyncSession, email: str) -> UserModel | None:
        return await self.user_repository.get_by_email(session, email)

