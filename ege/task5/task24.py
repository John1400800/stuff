def r(n):
    #n>0
    bn = bin(n)[2:]
    if bn.count('1')%2==0:
        bn = bn + '0'
        bn = '1' + bn[2:]
    else:
        bn = bn + '1'
        bn = '11' + bn[2:]
    return int(bn, 2)

lst = []
for n in range(1, 10000):
    if (res:=r(n))>25:
        lst.append((n, res))

print(min(lst, key=lambda tpl: tpl[1])[0])
        
    
