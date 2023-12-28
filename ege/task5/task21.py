def r(n):
    #n>0
    bn = bin(n)[2:]
    if n%2==0:
        bn = '1' + bn + '00'
    else:
        bn = bn + bin(bn.count('1'))[2:]
    return int(bn, 2)

lst = []
for n in range(1, 10000):
    if (res:=r(n))>190:
        lst.append((n, res))

print(min(lst, key=lambda tpl: tpl[1])[0])
