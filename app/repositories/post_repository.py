from app.model.post_model import PostModel
from app.repositories.base_repository import BaseRepository

class PostRepository(BaseRepository[PostModel]): # what is this line does-> python generics/type hinting, BaseRepo becomes PostModel type ? how it works? PostRepository inherits all CRUD methods from BaseRepository, but specialized for PostModel.
    """Repository for PostModel."""

    def __init__(self):
        super().__init__(PostModel)  # calling the constructor of the parent class BaseRepository with PostModel as the argument. This initializes the PostRepository to work specifically with the PostModel, allowing it to inherit and utilize all the generic CRUD operations defined in BaseRepository for PostModel instances.