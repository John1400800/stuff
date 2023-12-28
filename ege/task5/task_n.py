def F(a, b) -> int:
    a, b = map(str, (a, b))

    res = ''
    r1 = int(a[0]) + int(b[0])
    r2 = int(a[1]) + int(b[1])
    res = str(r1) + str(r2)
    if r2 < r1:
        res = res[::-1]
    res += str(int(a[2]) + int(b[2]))
    return int(res)

g = (141819, 171418, 141802, 171814)
for a in range(100, 1000):
    for b in range(100, 1000):
        r = F(a, b)
        if r in g:
            print(r)
        