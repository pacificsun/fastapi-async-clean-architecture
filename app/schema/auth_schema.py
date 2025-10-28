from datetime import datetime

from pydantic import BaseModel, EmailStr

from app.schema.user_schema import UserRead

class SignIn(BaseModel):
    email: EmailStr
    password: str

class SignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class TokenPayLoad(BaseModel):
    id: str
    email: EmailStr
    exp: datetime

class SignInResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_at: datetime
    user: UserRead


