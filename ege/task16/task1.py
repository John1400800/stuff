import functools

@functools.lru_cache
def F(n):
    if n > 5:
        if n % 2 == 0:
            return F(n-2) + 3*F(n//2) + n
        return F(n-1) + F(n-2) + F(n-3)
    return 2*n

print(F(99) + F(100))