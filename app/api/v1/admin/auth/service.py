import bcrypt
from app.api.v1.admin.auth.dto.login import LoginDto
from app.core.cache.service import set_key, get_key
from app.core.exceptions.http_exceptions import NotFoundException, UnauthorizedException, HttpSuccessException
from app.core.security.jwt import create_access_token, blacklist_token
from app.repositories.admin.crud import AdminCrudRepository


class AuthService:

    def __init__(self, session):
        self.session = session


    async def login(self, dto: LoginDto):

        repo = AdminCrudRepository(self.session)

        admin = repo.find_by_one(email=dto.email)

        if not admin:
            raise NotFoundException(detail=None)

        is_verify = bcrypt.checkpw(dto.password.encode('utf-8'), admin.password.encode('utf-8'))

        if not is_verify:
            raise UnauthorizedException(detail=False)

        data = {
            'email': admin.email,
            'name': admin.name,
            'avatar_url': admin.avatar_url,
        }

        access_token = await create_access_token(data)

        raise HttpSuccessException(
            detail={
                **data,
                'access_token': access_token
            }
        )

    async def logout(self, token: str):
        await blacklist_token(token, self.session)
        raise HttpSuccessException(
            detail=True,
            msg='システムから正常にログアウトしました。'
        )