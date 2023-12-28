def r(n):
    #n>0
    bn = bin(n)[2:]
    for _ in range(2):
        if bn.count('1')%2==0:
            bn = bn + '00'
            bn = '11' + bn[2:]
        else:
            bn = bn + '11'
            bn = '10' + bn[2:]
    return int(bn, 2)

r_lst = []
for n in range(1, 100):
    r_lst.append(r(n))

print(max(r_lst))
