import functools
import timeit


@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Замеряем время выполнения
print(timeit.timeit(lambda: fib(23), number=1000))
