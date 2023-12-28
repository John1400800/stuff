from string import digits, ascii_lowercase


def int_to_b(n: int, base=10,
             alpha=digits+ascii_lowercase
             ) -> str:
    res = ''
    while n > 0:
        res = alpha[n%base]+res
        n //= base
    return res

# task1
##for x in digits:
##   n = int(f'28{x}2', 18)+int(f'93{x}5', 12)
##   if not n%133:
##       print(n//133)

# task2
##f = 9**8 + 3**5 - 2
##print(int_to_b(f, 3).count('2'))
