from itertools import product

vow = ('О', 'И', 'А')
cons = ('П', 'Л', 'Н')

def valid(w) -> bool:
    for i in range(len(w)-1):
        if ((w[i] in vow and w[i+1] in vow) or
            (w[i] in cons and w[i+1] in cons)):
            return False
    return True
        

cnt = 0
for w in product('ПОЛИНА', repeat=4):
    if valid(w):
        cnt += 1

print(cnt)
