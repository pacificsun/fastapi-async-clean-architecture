from __future__ import annotations
from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base_model import BaseModel

class UserModel(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relationships use forward references (string names). SQLAlchemy will resolve them later.
    posts: Mapped[List["PostModel"]] = relationship(
        "PostModel",
        back_populates="author",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    comments: Mapped[List["CommentModel"]] = relationship(
        "CommentModel",
        back_populates="author",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    likes: Mapped[List["LikeModel"]] = relationship(
        "LikeModel",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<UserModel(username={self.username!r}, email={self.email!r})>"