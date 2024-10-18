from fastapi import APIRouter

from app import User
from app.core.database.session import SessionDep
from app.repositories.user.crud import UserCRUDRepository

router = APIRouter()

@router.get('/auth')
def view_auth(session: SessionDep):
    repo = UserCRUDRepository(session)

    # user = User(
    #     name='Dinh Manh',
    #     password='12345678',
    #     email='dmanh20112000@gmail.com'
    # )
    # repo.store(user)
    user = repo.get_by_id(1)
    # user.id = 1
    # repo.update(user)
    return { 'data': user }