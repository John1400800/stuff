from string import ascii_lowercase, digits
from itertools import product

def int_to_base(n, base=10, digits_=digits+ascii_lowercase):
    res = []
    while n>0:
        res.insert(0, digits_[n%base])
        n //= base
    return res

def valid(w):
    f = []
    # каждая следущая цифра должна быть меньшей предидущей
    for idx in range(len(w)-1):
        f += [ord(w[idx]) > ord(w[idx+1])]
    return all(f)


##cnt = 0
##for n in range(2400, 342, -1):
##    if valid(int_to_base(n, 7)):
##        cnt += 1

##cnt = 0
##for w in product('0123456', repeat=4):
##    if valid(w): cnt += 1

##alpha = '0123456'
##cnt = 0
##for d1 in alpha:
##    for d2 in alpha:
##        for d3 in alpha:
##            for d4 in alpha:
##                if valid(d1+d2+d3+d4):
##                    cnt += 1
##
##print(cnt)


