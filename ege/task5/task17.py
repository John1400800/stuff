def r(n):
    #n>0
    bn = bin(n)[2:]
    if n%3==0:
        bn += bn[:2]
    else:
        bn += bin(n%3)[2:]
    return int(bn, 2)

lst = []
for n in range(1, 10000):
    if (res:=r(n)) < 105:
        lst.append((n, res))

mx = max(lst, key=lambda tpl: tpl[1])[1]
print(min([tpl[0] for tpl in lst if tpl[1]==mx]))
        
        
