from string import digits, ascii_lowercase


def int_to_b(n, b,
             a=digits+ascii_lowercase) -> str:
    r = ''
    while n>0:
        r = a[n%b] + r
        n //= b
    return r

def r(n):
    #n>0
    bt = int_to_b(n, 4)
    bt = str(n%2)+bt+str(n%3)
    return int(bt, 4)

lst = []
for n in range(1, 1000000):
    if (res:=r(n)) < 100:
        lst+=[res]
print(max(lst))
