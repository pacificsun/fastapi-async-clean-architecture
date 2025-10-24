from sqlalchemy.ext.asyncio import AsyncSession
from app.services.base_service import BaseService
from app.repositories.post_repository import PostRepository
from app.model.post_model import PostModel

class PostService(BaseService[PostModel]):
    """Service layer for Post Business Logic."""
    def __init__(self):
        super().__init__(PostRepository())

    # get posts with comments
    async def get_post_with_comments(self, session: AsyncSession, post_id: str):
        post = await self.repository.get_by_id(session, post_id)
        if not post:
            return None
        await session.refresh(post, ["comments"]) # load comments relationship but how ?
        return post
        