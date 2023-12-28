def f(x, a, b):
    return (((a <= x <= b) <= (x**2 <= 64)) and
            (x**2 <= 25) <= (a <= x <= b))

minimal = 1000
for a in range(-100, 100):
    for b in range(a, 100):
        for x in range(-100, 100):
            if not f(x, a, b):
                break
        else:
            minimal = min(minimal, abs(b-a))
print(minimal)