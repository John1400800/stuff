def R(n):
    r = bin(n)[2:]
    for _ in range(2):
        r += str(r.count('1') % 2)
    return int(r, 2)



for n in range(100000):
    if R(n) > 77:
        print(n)
        break