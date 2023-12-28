def r(n):
    return int(''.join(['11' if d=='1' else '00'
                        for d in bin(n)[2:]]), 2)

# натуральное это болше 0 и целое
n = 1
while (res:=r(n))<=32:
    n += 1
else:
    print(res)


    
