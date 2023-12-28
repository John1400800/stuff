def foo(n: int) -> int:
    res = bin(n)[2:]
    for _ in range(2):
        summ = 0
        for i in res:
            summ += int(i)
        res += str(summ % 2)
    return int(res, 2)

for i in range(10000):
    if (res := foo(i)) > 43 :
        print(res)
        break