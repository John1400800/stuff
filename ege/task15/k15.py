def f(x, y, a):
    return (x<a) and (y<a) and (x*y>601)

for a in range(1000, -1, -1):
    if all(not(f(x, y, a))
           for x in range(1, 1000)
               for y in range(1, 1000)):
        print(a)
        break
