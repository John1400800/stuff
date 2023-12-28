import functools

@functools.lru_cache
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a*2, b) + f(a + 3, b)

print(f(2, 10) * f(10, 14))