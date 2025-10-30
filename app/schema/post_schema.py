from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from app.schema.base_schema import BaseSchemaInfo

# _____ Base shared fields for Post _____ #
class BasePost(BaseModel):
    title: str
    content: str
    author_id: Optional[str] = None

# _____ Schema for creating and updating a Post _____ #
class PostCreate(BasePost):
    pass    

class PostUpdate(BasePost):
    title: Optional[str] = None
    content: Optional[str] = None

# _____ Response/Read Schema for Post _____ #
class PostRead(BaseSchemaInfo, BasePost):
    comments: List["CommentRead"] = None
    likes: List["LikeRead"] = None

# for forward references to resolve CommentRead and LikeRead
from app.schema.comment_schema import CommentRead
from app.schema.like_schema import LikeRead

