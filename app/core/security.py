import bcrypt
from datetime import datetime, timedelta, timezone
from typing import Tuple
from jose import jwt

from app.core.config import settings



def get_password_hash(password: str) -> str:
    # Placeholder for password hashing logic
    return  bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_access_token(data: dict, expires_delta: timedelta = None) -> Tuple[str, datetime]:
    to_encode = data.copy()
    expire = datetime.now(timezone.ut) + (expires_delta or timedelta(hours=1))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return token, expire
    