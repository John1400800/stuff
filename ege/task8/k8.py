from itertools import product


def valid(w):
    return all((w.count('а')<=2,
                w.count('в')==2,
                w.count('и')==0))


alpha = 'авикл'
n = 1
for w in product(alpha, repeat=6):
    if valid(w):
        print(n)
        break
    n += 1
