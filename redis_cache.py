# Redis Caching Helpers

from redis.asyncio import Redis
import json
from typing import Optional

redis_client = Redis(host='localhost', port=6379, db=0)

async def get_cache(key: str) -> Optional[dict]:
    try:
        value = await redis_client.get(key)
        if value:
            return json.loads(value)
        return None
    except Exception as e:
        print(f"Error getting cache: {e}")

def set_cache(key: str, value: dict, ttl: int = 300):
    redis_client.setex(key, ttl, json.dumps(value))