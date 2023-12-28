from string import digits, ascii_lowercase


def int_to_b(n: int, base=10,
             alpha=digits+ascii_lowercase) -> str:
    res = ''
    while n > 0:
        res = alpha[n%base] + res
        n //= base
    return res

f = 243**540 - 6*9**530 + 21*3**511 - 3**71 - 200
print(int_to_b(f, 9).count('8'))
