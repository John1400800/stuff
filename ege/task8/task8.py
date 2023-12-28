from itertools import permutations


alpha = 'кусать'
cnt = 0
for w in permutations(alpha, r=5):
    if w[0] == 'ь':
        continue
    if 'сук' not in ''.join(w):
        cnt += 1

print(cnt)
