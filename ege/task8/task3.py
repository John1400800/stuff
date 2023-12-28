from itertools import permutations

def valid(w):
    if w[0] != 'Й' and 'АЕ' not in w:
        return True
    return False

cnt = 0
for w in permutations('МАТВЕЙ', r=6):
    if valid(''.join(w)):
        cnt += 1

print(cnt)
