def f(a: int, x: int) -> bool:
    return (not(x%a==0)) <= ((x%24==0) <= (not(96%x==0)))

for a in range(1000, 0, -1):
    if all(f(a, x) for x in range(1, 100000)):
        print(a)
        break
