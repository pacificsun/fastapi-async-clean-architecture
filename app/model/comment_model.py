from __future__ import annotations
from typing import List, Optional

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base_model import BaseModel


class CommentModel(BaseModel):
    __tablename__ = "comments"

    post_id: Mapped[str] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    author_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Backref to parent Post
    post: Mapped["PostModel"] = relationship("PostModel", back_populates="comments")

    # Likes on this comment
    likes: Mapped[List["LikeModel"]] = relationship(
        "LikeModel",
        back_populates="comment",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<CommentModel(post_id={self.post_id}, content={self.content[:20]!r})>"
