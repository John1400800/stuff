from datetime import datetime
from random import shuffle


def decorator_timeit(func):
    def inner(arg):
        start = datetime.now()
        res = func(arg)
        print(datetime.now() - start)
        return res

    return inner


# Best
def average_number1():
    summ = 0
    cnt = 0

    def inner(n: int):
        nonlocal summ, cnt
        summ += n
        cnt += 1
        return summ / cnt

    return inner


def average_number2():
    lst = []

    def inner(n: int):
        nonlocal lst
        lst.append(n)
        return sum(lst) / len(lst)

    return inner


lst = list(range(1, 1000001))
shuffle(lst)
# print(lst)

a1 = average_number1()
for i in lst:
    a1(i)
decorator_timeit(a1)(1)

print()
# Тупой тест работает так долго из-за .append
a2 = average_number2()
for i in lst:
    a2(i)
decorator_timeit(a2)(1)
