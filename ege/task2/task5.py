import itertools


def F(x, y, z):
    return int((x or y) <= (y == z))

print('X Y Z')

for tup in itertools.product((0, 1), repeat=3):
    not (f := F(*tup)) and print(*tup, f)
