def r(n):
    #n>0
    bn = format(n, 'b')
    bn = bn + bn[-2:-1]
    bn = bn + bn[1:2]
    return int(bn, 2)

cnt = 0
for n in range(1, 10000):
    if 150 <= r(n) <= 250:
        cnt += 1

print(cnt)
