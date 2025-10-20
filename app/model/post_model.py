from __future__ import annotations
from typing import List, Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base_model import BaseModel


class PostModel(BaseModel):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    # Relationships use forward references (string names). SQLAlchemy will resolve them later.
    comments: Mapped[List["CommentModel"]] = relationship(
        "CommentModel",
        back_populates="post",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    likes: Mapped[List["LikeModel"]] = relationship(
        "LikeModel",
        back_populates="post",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<PostModel(title={self.title!r})>"
