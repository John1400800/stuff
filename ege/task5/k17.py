def r(n):
    res = ''.join(['01' if d=='0' else '10'
                   for d in bin(n)[2:]])
    return int(res, 2)

n = 1
while (res:=r(n))<=63:
    n+=1
else:
    print(res)
    
