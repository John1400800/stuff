def r(n):
    #n>0
    bn = bin(n)[2:]
    if n%2:
        bn = bn + bin(bn.count('1'))[2:]
    else:
        bn = '1' + bn + '00'
    return int(bn, 2)

lst = []
for n in range(9, 10000):
   if (res:=r(n)) > 88:
       lst.append((n, res))

print(min(lst, key=lambda tpl: tpl[1]))
