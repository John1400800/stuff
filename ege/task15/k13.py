def f(x, y, a):
    return (x>=a) or (y>=a) or (x*y<=200)

for a in range(10000, 0, -1):
    if (all(f(x, y, a)
           for x in range(1, 1001)
               for y in range(1, 1001))):
        print(a)
        break
