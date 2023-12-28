from functools import reduce

def r(n):
    lst = [int(d) for d in str(n)]
    pd = reduce(lambda a, b: a*b, lst)
    sm = sum(lst)
    res = ''.join(sorted((str(pd), str(sm)), key=int)[::-1])
    return int(res)


for n in range(999, 99, -1):
    if r(n) == 24019:
        print(n); break
