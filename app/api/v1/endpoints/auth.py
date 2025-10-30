from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from dependency_injector.wiring import inject, Provide

from app.core.container import Container
from app.services.auth_service import AuthService
from app.schema.auth_schema import SignIn, SignInResponse, SignUp
from app.schema.user_schema import UserRead
from app.core.dependencies import get_session

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", response_model=UserRead)
@inject
async def signup(
    data: SignUp, 
    session: AsyncSession = Depends(get_session),
    service: AuthService = Depends(Provide[Container.auth_service])
    ):
        return await service.sign_up(session, data)


@router.post("/signin", response_model=SignInResponse)
@inject
async def signin(
    data:SignIn,
    session: AsyncSession = Depends(get_session),
    service: AuthService = Depends(Provide[Container.auth_service])
):
    return await service.signin(session, data)