from datetime import datetime
# Декораторы


def timeit(func):
    def wrapper(arg):
        start = datetime.now()
        res = func(arg)
        print(datetime.now() - start)
        return res
    return wrapper


# @timeit
def one(n) -> list:
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append(i)
    return lst


# @timeit
def two(n) -> list:
    return [i for i in range(n) if i % 2 == 0]


# print(len(one(100000)))
print(len(timeit(one)(100000)))
