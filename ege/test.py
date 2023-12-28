def f(s: str) -> str:
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s.count('1'), s.count('2'), s.count('3')


for x in range(100):
    for y in range(100):
        for z in range(100):
            if ((x + 2*y + 3*z == 61) and
                    (x + y + 3*z == 50) and
                    (y + z == 18)):
                print(sum((x, y, z))+2)

print(f('0' + 18*'1' + 11*'2' + 7*'3' + '0'))
