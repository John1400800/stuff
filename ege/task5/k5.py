def int_to_b(n, b=10):
    lst = []
    while n > 0:
        lst.insert(0, n % b)
        n //= b
    return lst


def reduce(func, obj):
    lst = list(obj)
    a = lst[0]
    for b in lst[1:]:
        a = func(a, b)
    return a


def r(n):
    sum_n = []
    lst_n = [d**2 for d in int_to_b(n)]
    for i in range(len(lst_n)-1):
        sum_n += [lst_n[i]+lst_n[i+1]]

    return int(reduce(lambda a, b: str(a)+str(b),
                      sorted(sum_n)[::-1]))


for n in range(999, 99, -1):
    if r(n) == 9752:
        print(n)
        break
