from string import digits, ascii_lowercase


def int_to_b(n, b, alpha=digits+ascii_lowercase):
    res = ''
    while n>0:
        res = alpha[n%b]+res
        n //= b
    return res

f = 7**80+49**15-49
print(int_to_b(f, 7).count('6'))
