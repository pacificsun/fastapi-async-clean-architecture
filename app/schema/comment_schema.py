from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from app.schema.base_schema import BaseSchema

class CommentBase(BaseModel):
    user_id: Optional[str] = None
    content: str

class CommentCreate(CommentBase):
    post_id: UUID 
    # Where is comment id coming from? It should not be here during creation. no the sqlalchemy model will handle it.

class CommentUpdate(CommentBase):
    content: Optional[str] = None

class CommentRead(BaseSchema, CommentBase):
    post_id: UUID
    likes: Optional[List["LikeRead"]] = None

# for forward references to resolve LikeRead
from app.schema.like_schema import LikeRead
CommentRead.model_rebuild()  # to resolve forward references

