import itertools
def F(x, y, z, w): return int((x or y) and (not(y ==
z)) and (not w))


print('x y z w F')
for v in itertools.product((0, 1), repeat=4):
    if (f := F(*v)):
        print(*v, f)

