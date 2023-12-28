def tr(a, b, c):
    a, b, c = sorted((a, b, c))
    return a+b > c

def f(a, x):
    return not((tr(x, 11, 18)==(not(max(x, 5)>15))) and tr(x, a, 5))

for a in range(1000, 0, -1):
    if all(f(a, x) for x in range(1, 10000)):
        print(a)
        break
