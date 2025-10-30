from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

from app.schema.base_schema import BaseSchemaInfo


# _____ Base shared fields for User _____ #
class BaseUser(BaseModel):
    email: EmailStr
    username: str



# _____ Schemas for creation and update _____ #
class UserCreate(BaseUser):
    password: str


class UserUpdate(BaseUser):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# _____ Read/Response Schema _____ #
class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    updated_at: datetime
    created_at: datetime
    

    model_config = ConfigDict(from_attributes=True)





class UserActivity(BaseSchemaInfo, BaseUser):
    posts: List["PostRead"] = []
    comments: List["CommentRead"] = []
    likes: List["LikeRead"] = []


# Resolve forward references
from app.schema.post_schema import PostRead
from app.schema.comment_schema import CommentRead
from app.schema.like_schema import LikeRead

UserRead.model_rebuild()