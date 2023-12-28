from string import ascii_lowercase, digits

def int_to_base(n: int, base: int,
                digit=digits+ascii_lowercase) -> list:
    res = []
    while n > 0:
        res.insert(0, digit[n%base])
        n //= base
    return res

print(int_to_base(249, 4, 'ЛНОС'))
