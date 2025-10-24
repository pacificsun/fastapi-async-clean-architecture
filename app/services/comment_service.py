from app.services.base_service import BaseService
from app.repositories.comment_repository import CommentRepository

from app.model.comment_model import CommentModel
from sqlalchemy.ext.asyncio import AsyncSession

class CommentService(BaseService[CommentModel]):
    """Service layer for Comment Business Logic."""
    def __init__(self):
        super().__init__(CommentRepository())

    # Additional business logic specific to comments can be added here
    # Example: count likes per comment
    async def count_likes(self, session, comment_id):
        comment = await self.repository.get_by_id(session, comment_id)
        if comment and comment.likes:
            return len(comment.likes)
        return 0