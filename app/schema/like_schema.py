from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from app.schema.base_schema import BaseSchema

class LikeBase(BaseModel):
    user_id: str 
    post_id: Optional[UUID] = None
    comment_id: Optional[UUID] = None

class LikeCreate(LikeBase):
    pass

class LikeRead(BaseSchema, LikeBase):
    pass

