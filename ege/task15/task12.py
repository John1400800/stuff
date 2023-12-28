# неравенства
def f(x, y, a):
    return (x<a) and (y<a) and (x*y>1200)

for a in range(10000):
    if all(f(x, y, a)==0
           for x in range(1, 1000)
               for y in range(1, 1000)):
        print(a)
        break
        
