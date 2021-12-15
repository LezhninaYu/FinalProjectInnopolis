from fastapi import APIRouter

from src.api.v1.endpoints.auth import router as auth_router
from src.api.v1.endpoints.post import router as post_router
from src.api.v1.endpoints.user import router as user_router
from src.api.v1.endpoints.migrate import router as migrate_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(post_router)
router.include_router(user_router)
router.include_router(migrate_router)
