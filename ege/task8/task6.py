from itertools import product


alpha = sorted('грант')
n = 1
for w in product(alpha, repeat=6):
    if ''.join(w)=='гранат':
        print(n)
        break
    n += 1
