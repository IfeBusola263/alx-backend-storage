#!/usr/bin/env python3
import requests
import redis
import time
from functools import wraps

def cache_page(expiration_time=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]  # Assuming the URL is the first argument

            # Key for tracking access count
            count_key = f"count:{url}"

            # Key for caching the result
            cache_key = f"cache:{url}"

            # Check if the result is already cached
            cached_result = redis_client.get(cache_key)
            if cached_result:
                # Increment access count
                redis_client.incr(count_key)
                return cached_result.decode('utf-8')

            # If not cached, fetch the page
            result = func(*args, **kwargs)

            # Cache the result with expiration time
            redis_client.setex(cache_key, expiration_time, result)

            # Increment access count
            redis_client.incr(count_key)

            return result

        return wrapper
    return decorator

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@cache_page()
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
