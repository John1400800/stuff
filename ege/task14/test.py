from string import digits, ascii_lowercase


def int_to_b(n, base=10, digits_ = digits+ascii_lowercase):
    res = ''
    while n>0:
        res = digits_[n%base]+res
        n //= base
    return res

