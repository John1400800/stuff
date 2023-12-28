from string import digits, ascii_lowercase


def int_to_b(n, base=10,
             alpha=digits+ascii_lowercase) -> str:
    res = ''
    while n>0:
        res = alpha[n%base]+res
        n //= base
    return res

f = 4**700+4**100-16**100-64
print(int_to_b(f, 4).count('3'))
