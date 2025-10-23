"""
Cache utilities using Redis.
Provides caching for analysis results and API responses.
"""

import redis.asyncio as redis
import json
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)


class RedisCache:
    """Redis cache client."""
    
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.client: Optional[redis.Redis] = None
    
    async def connect(self):
        """Connect to Redis."""
        try:
            self.client = await redis.from_url(self.redis_url)
            logger.info("Connected to Redis")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
    
    async def close(self):
        """Close Redis connection."""
        if self.client:
            await self.client.close()
            logger.info("Closed Redis connection")
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        try:
            if not self.client:
                return None
            
            value = await self.client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Error getting from cache: {e}")
            return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600) -> bool:
        """Set value in cache with TTL."""
        try:
            if not self.client:
                return False
            
            await self.client.setex(key, ttl, json.dumps(value))
            return True
        except Exception as e:
            logger.error(f"Error setting cache: {e}")
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache."""
        try:
            if not self.client:
                return False
            
            await self.client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Error deleting from cache: {e}")
            return False
    
    async def clear(self) -> bool:
        """Clear all cache."""
        try:
            if not self.client:
                return False
            
            await self.client.flushdb()
            return True
        except Exception as e:
            logger.error(f"Error clearing cache: {e}")
            return False


# Global cache instance (will be initialized in app startup)
redis_client = RedisCache("redis://localhost:6379")
