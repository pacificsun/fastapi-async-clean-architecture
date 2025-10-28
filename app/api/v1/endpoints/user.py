from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import Container
from app.core.dependencies import get_session
from app.services.user_service import UserService
from app.schema.user_schema import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
@inject
async def list_users(
    service: UserService = Depends(Provide[Container.user_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    return await service.get_all(session)

@router.get("/{user_id}", response_model=UserRead)
@inject
async def get_user(
    user_id: str,
    service: UserService = Depends(Provide[Container.user_service]),
    session: AsyncSession = Depends(get_session),
):
    service.repository.session = session
    user = await service.get_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model= UserCreate)
@inject
async def create_user(
    user_in: UserCreate,
    service: UserService = Depends(Provide[Container.user_service]),
    session: AsyncSession = Depends(get_session)
):
    service.repository.session = session
    user = await service.create(session, user_in)
    return user
