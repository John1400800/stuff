def r(n):
    r = bin(n)[2:]+str(n%2)
    if r.count('1')%3==0:
        r = '11'+r[2:]
    else:
        r = '10'+r[2:]
    return int(r, 2)

n = 1
while r(n) < 26:
    n += 1
else:
    print(n)
