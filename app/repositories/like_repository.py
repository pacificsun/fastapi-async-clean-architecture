from app.model.like_model import LikeModel
from app.repositories.base_repository import BaseRepository
from sqlalchemy import select, func
class LikeRepository(BaseRepository[LikeModel]):
    """Repository for Like model."""

    def __init__(self):
        super().__init__(LikeModel)

    async def count_likes_by_post_id(self, session, post_id: str) -> int:
        """Count likes for a specific post."""
        stmt = select(func.count(LikeModel.id)).where(LikeModel.post_id == post_id)
        result = await session.execute(stmt)
        return result.scalar_one() or 0