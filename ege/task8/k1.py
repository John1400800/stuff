from itertools import product


EVEN =  '1', '3', '5', '7', '9'
ODD  =  0, 2, 4, 6, 8

def valid(w):
    idxs = tuple(i for i in range(len(w)) if w[i] == '4')
    if len(idxs) != 2:
        return False
    for idx in idxs:
        for step in (-1, 1):
            if ((0 <= (n_idx:=(idx+step)) < len(w)) and
                (w[n_idx] in EVEN)):
                return False
    return True

cnt = 0
for w in product('01234567', repeat=5):
    if w[0] != '0' and valid(w):
        cnt += 1

print(cnt)

