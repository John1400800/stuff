def foo(n):
    b_n = bin(n)[2:]
    for _ in range(2):
        summ = 0
        for i in b_n:
            summ += int(i)
        b_n += str(summ % 2)
    return int(b_n, 2)

for n in range(0, 10000):
    if foo(n) > 137:
        print(n)
        break