from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.services.base_service import BaseService
from app.core.exceptions import AuthError
from app.services.user_service import UserService
from app.schema.auth_schema import SignUp, SignInResponse, SignIn
from app.core.security import get_password_hash, verify_password, create_access_token
from app.schema.user_schema import UserRead


class AuthService(BaseService):
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    
    async def sign_up(self, session: AsyncSession,  user_info: SignUp ) -> UserRead:
        #Check if user already exists
        existing_user = await self.user_service.get_by_email(session, user_info.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_pw = get_password_hash(user_info.password)
        user_info.password = hashed_pw
        user = await self.user_service.create(session, user_info)
        return user
    
    async def signin(self, session:AsyncSession, data:SignIn) -> SignInResponse:
        user = await self.user_service.get_by_email(session, data.email__eq)
        if not user or not verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        
        token, exp = create_access_token({"sub":str(user.id), "email": user.email})
        return SignInResponse(access_token=token, expires_at=exp, user=user)