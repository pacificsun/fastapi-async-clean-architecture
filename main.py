# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routes import routers as v1_routers
from app.core.config import settings
from app.core.container import Container
from app.core.database import Database
from app.util.class_object import singleton


@singleton
class AppCreator:
    def __init__(self):
        # Initialize container and database first
        self.container = Container()
        self.db: Database = self.container.db()

        # Define FastAPI lifespan context
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            # Startup actions
            await self.db.create_database()
            self.container.wire(modules=["app.api.v1.routes"])
            yield
            # Shutdown actions
            await self.db._engine.dispose()

        # Initialize FastAPI app
        self.app = FastAPI(
            title=settings.PROJECT_NAME,
            version="0.0.1",
            openapi_url=f"{settings.API_PREFIX}/openapi.json",
            lifespan=lifespan,  # ✅ Replaces @on_event startup/shutdown
        )

        # Configure CORS
        if settings.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # Include API routers
        self.app.include_router(v1_routers, prefix=settings.API_V1_STR)

        # Root endpoint
        @self.app.get("/", tags=["Root"])
        async def root():
            return {"status": "ok", "message": "Service is working"}


# -----------------------------
# Global app, db, container
# -----------------------------
app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
