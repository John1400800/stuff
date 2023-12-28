def r(n):
    res = bin(n-(n%4))[2:]
    for _ in range(2):
        res += str(res.count('1')%2)
    return int(res, 2)

mx = 0
for n in range(1, 10000):
    if r(n) < 64: mx = n

print(mx)
