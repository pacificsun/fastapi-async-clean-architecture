
from app.model.comment_model import CommentModel
from app.repositories.base_repository import BaseRepository

class CommentRepository(BaseRepository[CommentModel]):
    """Repository for Comment model."""

    def __init__(self):
        super().__init__(CommentModel)
