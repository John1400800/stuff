# делимость простая програма
def f(x: int, a: int) -> bool:
    return ((x%a==0) and (x%36!=0)) <= (x%12!=0)

for a in range(1, 10000):
    if all([f(x, a) for x in range(1, 1000000)]):
        print(a)
        break
    
