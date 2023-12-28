import itertools


def F(x, y, z, w):
    return int(((x and (not y)) or (w <= z)) == (z == x))

print('X Y Z W F')
for v in itertools.product((0, 1), repeat=4):
    if f := F(*v):
        print(*v, f)
