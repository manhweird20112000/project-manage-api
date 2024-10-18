from fastapi import APIRouter

from app import User
from app.core.database.database import SessionDep

router = APIRouter()

@router.get('/auth')
def view_auth(session: SessionDep):
    users = session.query(User).all()
    return { 'data': users }