from fastapi import APIRouter

from app.api.v1.endpoints.post import router as post_router
from app.api.v1.endpoints.comment import router as comment_router
from app.api.v1.endpoints.like import router as like_router
from app.api.v1.endpoints.user import router as user_router
from app.api.v1.endpoints.auth import router as auth_router

routers = APIRouter()
router_list = [post_router, comment_router, like_router, user_router, auth_router]

for route in router_list:
    route.tags = route.tags.append("v1") 
    routers.include_router(route)