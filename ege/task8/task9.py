from itertools import permutations


set_w = set()
for w in permutations(alpha):
    if 'оо' not in ''.join(w):
        set_w.add(w)

print(len(set_w))



