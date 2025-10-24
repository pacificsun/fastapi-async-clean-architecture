import os
from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Base
    ENV: str = os.getenv("ENV", "dev")
    API_PREFIX: str = "/api"
    PROJECT_NAME: str = "FastAPI Async Clean Architecture"
    API_V1_STR: str = "/api/v1"

    PROJECT_ROOT: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # Database
    DB_URL: str = os.getenv(
        "DB_URL",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/dev_clean_architecture"
    )

    # Auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Pagination
    PAGE: int = 1
    PAGE_SIZE: int = 20
    ORDERING: str = "-id"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


# Optional Test Settings
class TestSettings(Settings):
    ENV: str = "test"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/test_clean_architecture"


# Initialize
env = os.getenv("ENV", "dev")
settings = TestSettings() if env == "test" else Settings()
