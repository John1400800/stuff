from itertools import product

def valid(w):
    if len(set(w)) != 3:
        return False
    for i in range(len(w)-1):
        if w[i]==w[i+1]:
            return True
    return False


cnt = 0
for w in product('01234567', repeat=4):
    if w[0]!='0' and valid(w):
        cnt += 1

print(cnt)
