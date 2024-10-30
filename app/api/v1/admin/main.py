from fastapi import APIRouter
from fastapi.params import Depends

from app.api.v1.admin.auth import  controller as amin_auth_router
from app.api.v1.admin.deps import auth_middleware

api_router = APIRouter()

api_router.include_router(
    amin_auth_router.router,
    prefix='/auth',
    dependencies=[Depends(auth_middleware)]
)