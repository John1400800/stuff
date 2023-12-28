def f(x, y, a):
    return (3*x+y<a)or(x<y)or(16<=x)

for a in range(1, 10000):
    if all(f(x, y, a)==1
           for x in range(0, 1000)
           for y in range(0, 1000)):
        print(a)
        break
