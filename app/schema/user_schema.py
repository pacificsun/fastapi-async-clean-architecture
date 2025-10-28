from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr

from app.schema.base_schema import BaseSchema


# _____ Base shared fields for User _____ #
class BaseUser(BaseModel):
    username: str
    email: EmailStr


# _____ Schemas for creation and update _____ #
class UserCreate(BaseUser):
    password: str


class UserUpdate(BaseUser):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# _____ Read/Response Schema _____ #
class UserRead(BaseSchema, BaseUser):
    posts: List["PostRead"] = []
    comments: List["CommentRead"] = []
    likes: List["LikeRead"] = []


# Resolve forward references
from app.schema.post_schema import PostRead
from app.schema.comment_schema import CommentRead
from app.schema.like_schema import LikeRead
