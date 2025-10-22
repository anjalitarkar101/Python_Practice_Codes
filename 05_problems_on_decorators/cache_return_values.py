# Write a decorator that caches the return values of a function so that 
# when it is called with the same arguments again, it returns the cached value instead of recomputing it.

import time 

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)        # to execute the original function
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a,b):
    time.sleep(4)  # Simulate a long computation
    return a + b
    
# Example usage
print(long_running_function(2,3))  
print(long_running_function(4,3))