from itertools import product


def valid(w):
    return w.count('1')==1

cnt = 0
for w in product('123456', repeat=5):
    if valid(w): cnt += 1

print(cnt)
