import itertools


def F(x, y, z):
    return int((x or (not y) or (not z)) and ((not x) or y))

print('X Y Z F')
for tup in itertools.product((0, 1), repeat=3):
    print(*tup, F(*tup))
