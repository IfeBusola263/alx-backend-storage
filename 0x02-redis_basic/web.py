#!/usr/bin/env python3
'''
This module hosues a function that makes
a get request to a url
'''

import requests
import redis
import time
from functools import wraps


def cache_page(expiration_time=10):
    '''
    Decorator to inspected the url.
    and record the counts
    '''
    def decorator(func):
        '''
        A decorator to wrap the function.
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
            The function wrapper
            Carrying out the count.
            '''
            url = args[0]  # Assuming the URL is the first argument
            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
            # Key for tracking access count
            count_key = f"count:{url}"

            # Key for caching the result
            cache_key = f"cache:{url}"

            # Check if the result is already cached
            cached_result = redis_client.get(cache_key)
            if cached_result:
                # Increment access count
                redis_client.incr(count_key)
                redis_client.save()
                return cached_result.decode('utf-8')

            # If not cached, fetch the page
            result = func(*args, **kwargs)

            # Cache the result with expiration time
            redis_client.setex(cache_key, expiration_time, result)

            # Increment access count
            redis_client.incr(count_key)
            redis_client.save()

            return result

        return wrapper
    return decorator


@cache_page()
def get_page(url: str) -> str:
    '''
    This function makes a get request and check number of times
    the url is called
    '''
    response = requests.get(url)
    return response.text
