from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all ORM models."""
    pass

class Database:
    """ PostgreSQL Async Database connection and session management."""
    def __init__(self, db_url: str):
        self._engine = create_async_engine(db_url, echo=False, future=True) # what echo and future do ?
        self._session_factory = async_sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )

    async def create_database(self):
        """Create database tables based on ORM models."""
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        """Provide a transactional scope around a series of operations."""
        sesssion:  AsyncSession = self._session_factory()
        try:
            yield sesssion
            await sesssion.commit()
        except Exception:
            await sesssion.rollback()
            raise
        finally:
            await sesssion.close()