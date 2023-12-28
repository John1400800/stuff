def r(n):
    res = bin(n-n%8+n%2)[2:]
    for _ in range(2):
        res += str(res.count('1')%2)
    return int(res, 2)

n = 1
while (res:=r(n))<=90:
    n += 1
else:
    print(res)
