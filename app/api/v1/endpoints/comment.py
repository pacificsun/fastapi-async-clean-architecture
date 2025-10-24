from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.dependencies import get_session
from app.services.comment_service import CommentService
from app.schema.comment_schema import CommentCreate, CommentRead

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("/post/{post_id}", response_model=list[CommentRead])
@inject
async def get_comments_by_post(
    post_id: str,
    service: CommentService = Depends(Provide[Container.comment_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    return await service.get_comments_by_post_id(session, post_id)


@router.post("/", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
@inject
async def create_comment(
    comment_in: CommentCreate,
    service: CommentService = Depends(Provide[Container.comment_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    return await service.create(session, comment_in)
