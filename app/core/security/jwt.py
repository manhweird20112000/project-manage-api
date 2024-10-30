
from datetime import datetime, UTC, timedelta
from typing import Any

import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app import TokenBlackList
from app.core.secret.config import settings
from app.repositories.token_blacklist.crud import TokenBlacklistCrudRepository

ALGORITHM = 'HS256'

async def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC).replace(tzinfo=None) + expires_delta
    else:
        expire = datetime.now(UTC).replace(tzinfo=None) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def create_refresh_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(UTC).replace(tzinfo=None) + expires_delta
    else:
        expire = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_token(token: str, session: AsyncSession):
    options = {
        'verify_signature': True,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': True,
        'verify_aud': False
    }
    repo_token_blacklist = TokenBlacklistCrudRepository(session)
    exist = repo_token_blacklist.find_by_one(token=token)

    if exist:
        return None
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM], options=options)




async def blacklist_token(token: str, session: AsyncSession) -> None:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    expires_at = datetime.fromtimestamp(payload.get("exp"))
    repo_token_blacklist = TokenBlacklistCrudRepository(session)
    data = TokenBlackList(
        token=token,
        expires_at=expires_at,
    )
    repo_token_blacklist.store(data)