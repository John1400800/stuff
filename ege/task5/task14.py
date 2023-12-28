def r(n):
    # n > 0
    bn = bin(n)[2:]
    if (sm:=bn.count('1'))%3==0:
        bn += bn[:2]
    else:
        bn = bin((sm%3)*3)[2:] + bn

    return int(bn, 2)

##print(r(14))
for n in range(100000, 1, -1):
    if r(n)<=60:
        print(n)
        break
