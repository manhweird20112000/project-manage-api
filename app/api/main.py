from fastapi import APIRouter

from app.api.v1.admin.main import api_router as admin_api_router
api_router = APIRouter()

api_router.include_router(admin_api_router, prefix='/admin', tags=["admin"])