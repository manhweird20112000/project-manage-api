from fastapi import APIRouter

router = APIRouter()

@router.get('/auth')
def view_auth():
    return { 'message': 'Hello Auth' }