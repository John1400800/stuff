import itertools


def F(x, y, z, w):
    return int(((x and y) or (y and z)) == ((x <= w) and (w <= z)))

print('X Y Z W F')
for tup in itertools.product((0, 1), repeat=4):
    (f := F(*tup)) and print(*tup, f)
