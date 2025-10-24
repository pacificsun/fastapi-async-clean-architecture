from typing import AsyncGenerator

from app.core.config import settings
from app.core.database import Database, Base

# Initialize Database with URL from settings
db = Database(settings.DB_URL)

# Dependency to create async sessions
async def get_session() -> AsyncGenerator:
    """
    FastAPI dependency that yields an AsyncSession for each request.
    Usage: `session: AsyncSession = Depends(get_session)`
    """
    async with db.session() as session:
        yield session
