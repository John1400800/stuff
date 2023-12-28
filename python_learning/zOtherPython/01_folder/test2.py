def new_base_num(num, base=10):
    if any((num <= 0, base <= 1)):
        raise SomeError

    digits = []
    while num:
        digits += [num % base]
        num //= base
    return digits[::-1]


def r(n: int) -> int:
    n = new_base_num(n, 2)
    dct = {0: "01", 1: "10"}
    n = ''.join([str(dct[i]) for i in n])
    return int(n, 2)


mx = 0
for n in range(1, 10000):
    res = r(n)
    if all((res < 256, res % 2, res > mx)):
        mx = res
print(mx)
