from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.dependencies import get_session
from app.services.post_service import PostService
from app.schema.post_schema import PostCreate, PostRead

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=list[PostRead])
@inject
async def list_posts(
    service: PostService = Depends(Provide[Container.post_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    return await service.get_all(session)

@router.get("/{post_id}", response_model=PostRead)
@inject
async def get_post(
    post_id: str,
    service: PostService = Depends(Provide[Container.post_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    post = await service.get_post_with_comments(session, post_id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.post("/", response_model= PostRead, status_code = status.HTTP_201_CREATED)
@inject
async def create_post(post_in: PostCreate, service: PostService = Depends(Provide[Container.post_service]), session: AsyncSession = Depends(get_session)):
    service.repository.session = session
    post = await service.create(session, post_in)
    return post







