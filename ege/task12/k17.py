def is_prime(n):
    for d in range(2, n):
        if n%d==0:
            return False
    return True

n = 0
while True:
    s = '>'+15*'0'+n*'1'+15*'2'
    while '>0' in s or '>1' in s or '>2' in s:
        s = s.replace('>0', '22>', 1)
        s = s.replace('>1', '2>', 1)
        s = s.replace('>2', '1>', 1)
    s = s.replace('>', '')
    sm = sum(map(int, s))
    if is_prime(sm):
        print(n)
        break
    n += 1
