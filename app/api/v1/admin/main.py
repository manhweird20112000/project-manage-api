from fastapi import APIRouter
from app.api.v1.admin.auth import  controller as amin_auth_router

api_router = APIRouter()

api_router.include_router(amin_auth_router.router, prefix='/auth')