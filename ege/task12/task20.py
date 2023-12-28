from string import digits

def is_prime(n):
    for mul in range(2, n):
        if n % mul == 0:
            return False
    return True

n = 1
while True:
    s = '>'+'1'*23+'2'*n+'3'*25
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '1>', 1)
        if '>2' in s:
            s = s.replace('>2', '>3', 1)
        if '>3' in s:
            s = s.replace('>3', '>11', 1)
    if is_prime(sum([int(symb) for symb in s if symb in digits])):
        print(n)
        break
    else:
        n += 1

