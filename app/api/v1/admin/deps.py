from fastapi.requests import Request

from app.core.database.session import SessionDep
from app.core.exceptions.http_exceptions import UnauthorizedException
from app.core.security.jwt import verify_token
from app.repositories.admin.crud import AdminCrudRepository


async def auth_middleware(request: Request, session: SessionDep):
    exclude_path = ['/api/v1/admin/auth/login']

    if not request.url.path in exclude_path:
        bearer_token = request.headers.get("Authorization")

        if not bearer_token:
            raise UnauthorizedException(detail=False)

        token = bearer_token.split(" ")[1]

        if not token:
            raise UnauthorizedException(detail=False)

        data = await verify_token(token=token, session=session)

        if not data:
            raise UnauthorizedException(detail=False)

        repo_admin = AdminCrudRepository(session)

        admin = repo_admin.find_by_one(email=data['email'])

        if not admin:
            raise UnauthorizedException(detail=False)
