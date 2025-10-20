from app.model.like_model import LikeModel
from app.repositories.base_repository import BaseRepository

class LikeRepository(BaseRepository[LikeModel]):
    """Repository for Like model."""

    def __init__(self):
        super().__init__(LikeModel)
