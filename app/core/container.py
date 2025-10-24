from dependency_injector import containers, providers

from app.repositories.post_repository import PostRepository
from app.repositories.comment_repository import CommentRepository
from app.repositories.like_repository import LikeRepository

from app.services.post_service import PostService
from app.services.comment_service import CommentService
from app.services.like_service import LikeService

from app.core.database import Database
from app.core.config import settings


class Container(containers.DeclarativeContainer):
    """Dependency Injection container for services and repositories."""

    wiring_config = containers.WiringConfiguration(packages=["app.api.v1.endpoints"])

    # Database instance
    db = providers.Singleton(Database, db_url=settings.DB_URL)

    # Repositories (per-request)
    post_repository = providers.Factory(PostRepository)
    comment_repository = providers.Factory(CommentRepository)
    like_repository = providers.Factory(LikeRepository)

    # Services (per-request)
    post_service = providers.Factory(PostService, repository=post_repository)
    comment_service = providers.Factory(CommentService, repository=comment_repository)
    like_service = providers.Factory(LikeService, repository=like_repository)
