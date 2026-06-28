# LRU Cache Decorator Example
import functools
import time

@functools.lru_cache(maxsize=128)
def expensive_operation(n):
    time.sleep(1) # Simulating an expensive operation
    return n * n

if __name__ == "__main__":
    print("First call (takes 1 sec):", expensive_operation(10))
    print("Second call (instant):", expensive_operation(10))
    print("Third call (takes 1 sec):", expensive_operation(20))
    print("Cache Info:", expensive_operation.cache_info())
