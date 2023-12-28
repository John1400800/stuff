from itertools import product


alpha = '01234'
even  = '024'

def valid(w):
    cnt_e = 0
    for d in w:
        if d in even: cnt_e += 1
    return cnt_e <= 3

cnt = 0
for w in product(alpha, repeat=5):
    if w[0]!='0' and valid(w): cnt += 1

print(cnt)
