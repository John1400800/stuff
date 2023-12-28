def decorator(func):
    def inner(n: int):
        f = func()
        for i in range(2, n + 1):
            num = f()
        return num
    return inner


@decorator
def fib():
    x0 = 0
    x1 = 1

    def next_num() -> int:
        nonlocal x0, x1
        x0, x1 = x1, x0 + x1
        return x1
    return next_num


print(fib(20))
