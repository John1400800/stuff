def r(n):
    bn = bin(n)[2:]
    if n%5==0:
        bn = bn[:3] + bn
    else:
        bn += bin((n%3)*5)[2:]
    return int(bn, 2)

lst_res = []
for n in range(0, 100000):
    if (res:=r(n))>39000:
        lst_res += [res]

print(min(lst_res))


