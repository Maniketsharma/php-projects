import time
from functools import lru_cache
@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print("now running in some work")
    some_work(3)
    print("dene...")
    input()
    some_work(3)
    print("called again...")
    some_work(3)
    print("called again...")