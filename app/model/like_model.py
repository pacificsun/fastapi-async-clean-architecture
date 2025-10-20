from __future__ import annotations
from typing import Optional

from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base_model import BaseModel


class LikeModel(BaseModel):
    __tablename__ = "likes"

    user_id: Mapped[str] = mapped_column(String(50), nullable=False)

    # A like belongs to either a post OR a comment. Both foreign keys allowed, but only one should be non-null.
    post_id: Mapped[Optional[str]] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=True)
    comment_id: Mapped[Optional[str]] = mapped_column(ForeignKey("comments.id", ondelete="CASCADE"), nullable=True)

    # Relationships back to post/comment
    post: Mapped[Optional["PostModel"]] = relationship("PostModel", back_populates="likes")
    comment: Mapped[Optional["CommentModel"]] = relationship("CommentModel", back_populates="likes")

    # Optional DB-level constraint to enforce: at least one of post_id/comment_id is non-null.
    __table_args__ = (
        CheckConstraint(
            "(post_id IS NOT NULL) OR (comment_id IS NOT NULL)",
            name="like_must_have_post_or_comment"
        ),
    )

    def __repr__(self) -> str:
        return f"<LikeModel(user_id={self.user_id}, post_id={self.post_id}, comment_id={self.comment_id})>"
