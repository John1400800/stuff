import itertools

def F(x, y, z, w):
    return int(((w or y) == x) or ((w <= z) and (y <= w)))

print('X Y Z W')
for tup in itertools.product((0, 1), repeat=4):
    not (f := F(*tup)) and print(*tup, f)
