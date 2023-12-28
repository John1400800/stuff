from functools import lru_cache

@lru_cache(None)
def f(n):
    if n<=1:
        return 2
    elif n>1 and n%2:
        return 1+f(n-1)*f(n-2)-f(n-1)-f(n-2)
    elif n>1 and (not n%2):
        return 2*f(n-1)

for n in range(1, 13):
    f(n)

print(f(12))
