for n in range(100, 1000):
    sort = ''.join(sorted(str(n), key=int))
    a, b = sort[:2], sort[:0:-1]
    if a == '00':
        continue
    if a[0] == '0':
        a = a[::-1]
    if int(b) - int(a) == 40:
        print(n)