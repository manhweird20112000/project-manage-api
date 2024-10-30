from app.core.cache.session import get_redis


async def set_key(key: str, value: str):
    redis = await get_redis()
    return redis.set(key, value)

async def get_key(key: str):
    redis = await get_redis()
    return redis.get(key)

async def remove_key(key: str):
    redis = await get_redis()
    redis.delete(key)