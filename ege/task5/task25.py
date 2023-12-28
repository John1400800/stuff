#100 <= n <= 200
def r(n):
    bn = bin(n)[2:]
    for _ in range(2):
        if len(bn)%2==0:
            bn = bn + '10'
        else:
            bn = '11' + bn
    return int(bn, 2)
    

cnt = 0
for n in range(100, 201):
    if r(n)%2==0:
        cnt += 1

print(cnt)
