import redis

from app.core.secret.config import settings


async def get_redis():
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0
    )
