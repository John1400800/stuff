def r(n):
    #n>0
    bn = bin(n)[2:]
    if n%2==0:
        bn = '10' + bn
    else:
        bn =  '1' + bn + '01'
    return int(bn, 2)

lst = []
for n in range(1, 8+1):
    lst += [r(n)]

print(max(lst))
