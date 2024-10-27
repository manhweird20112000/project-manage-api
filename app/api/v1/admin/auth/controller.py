from fastapi import APIRouter

from app.api.v1.admin.auth.dto.login import LoginDto
from app.api.v1.admin.auth.service import AuthService
from app.core.database.session import SessionDep

router = APIRouter()

@router.post('/login')
async def exec_login(session: SessionDep, dto: LoginDto):
    service = AuthService(session)
    data = await service.login(dto)
    return data

@router.post('/logout')
def exec_logout():
    return {}