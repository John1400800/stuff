def DEL(m, n):
    return m % n == 0

def F(x, A):
    return (not DEL(x, A)) <= (DEL(x, 6) <= (not DEL(x, 9)))

for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not F(x, A):
            ok = False
            break
    if ok:
        print(A)