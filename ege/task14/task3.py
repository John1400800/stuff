from string import digits, ascii_lowercase


def int_to_b(n, base=10, digits_ = digits+ascii_lowercase):
    res = ''
    while n>0:
        res = digits_[n%base]+res
        n //= base
    return res

x = 3
while int('121', x)+1 != int('101', 7):
    x += 1
else:
    print(int_to_b(x, 3))

