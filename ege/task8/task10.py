from itertools import product


alpha = 'инфа'
cnt = 0
for w in product(alpha, repeat=6):
    if ''.join(w).count('ф')==2:
        cnt += 1

print(cnt)
