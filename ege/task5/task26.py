def r(n):
    #n>0
    bn = format(n, 'b')
    if bn.count('1')%2==0:
        bn = '1' + bn
        bn = bn[:-2] + '10'
    else:
        bn = bn + '1'
        bn = '10' + bn[2:]
    return int(bn, 2)

# n - min ?
mn = 1000000
for n in range(1, 10000):
    if r(n)>202 and n<mn:
        mn = n

print(mn)
        
