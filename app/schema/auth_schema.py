from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict

from app.schema.user_schema import BaseUser

class SignIn(BaseModel):
    email: EmailStr
    password: str

class SignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class TokenPayload(BaseModel):
    id: str
    email: EmailStr
    exp: datetime

class SignInResponse(BaseUser):
    access_token: str
    token_type: str = "bearer"
    expires_at: datetime

    model_config = ConfigDict(from_attributes=True)
 


