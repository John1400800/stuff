def r(n):
    #n>0
    bn = bin(n)[2:]
    if n%2:
        bn = '11' + bn + '11'
    else:
        bn = '1' + bn + '0'
    return int(bn, 2)

lst = []
for n in range(1, 10000):
    if (res:=r(n))>225: lst.append(r(n))

print(min(lst))
