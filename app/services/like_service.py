from app.services.base_service import BaseService
from app.repositories.like_repository import LikeRepository

from app.model.like_model import LikeModel
from sqlalchemy.ext.asyncio import AsyncSession

class LikeService(BaseService[LikeModel]):
    """Service layer for Like Business Logic."""
    def __init__(self):
        super().__init__(LikeRepository())

    # Additional business logic specific to likes can be added here
    # Example: count likes for a specific post
    async def count_likes_for_post(self, session: AsyncSession, post_id: str) -> int:
        return await self.repository.count_likes_by_post_id(session, post_id)
    
     # Example: prevent duplicate like from same user on same target
    async def add_like(self, session, user_id: str, post_id=None, comment_id=None):
        existing_likes = await self.repository.get_all(session)
        if any(
            l for l in existing_likes
            if l.author_id == user_id and (l.post_id == post_id or l.comment_id == comment_id)
        ):
            return None  # already liked
        return await self.repository.create(session, {
            "author_id": user_id,
            "post_id": post_id,
            "comment_id": comment_id
        })