from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.dependencies import get_session
from app.services.like_service import LikeService
from app.schema.like_schema import LikeCreate, LikeRead

router = APIRouter(prefix="/likes", tags=["Likes"])


@router.post("/", response_model=LikeRead, status_code=201)
@inject
async def create_like(
    like_in: LikeCreate,
    service: LikeService = Depends(Provide[Container.like_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    return await service.create(session, like_in)


@router.get("/count/{post_id}", response_model=int)
@inject
async def count_likes(
    post_id: str,
    service: LikeService = Depends(Provide[Container.like_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    return await service.repository.count_likes_by_post_id(session, post_id)
