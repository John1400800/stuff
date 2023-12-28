def r(n):
    #n>0
    n = n - format(n, 'b').count('0')
    bn = format(n, 'b') 
    bn = bn[-3:] + bn
    return int(bn, 2)

mn = 10000000
for n in range(1, 10000):
    if (res:=r(n))>224 and res<mn:
        mn = res

print(mn)
