def f(a, x):
    return ( x&51==0 ) or ( (x&41==0)<=(x&a==0) )

for a in range(1000, 0, -1):
    if all(f(a, x) for x in range(100000)):
        print(a)
        break
