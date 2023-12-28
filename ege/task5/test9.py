def int_to_base(n: int, base=10):
    digit = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digit) or base <= 1 or n <= 0: return 
    res = ''
    while n > 0:
        res = digit[(n % base)] + res
        n //= base
    return res

def bin_to_int(b: str):
    if not(set(b) <= {'1', '0'}): return
    res = 0
    pow_ = len_ = len(b) - 1
    i = 0
    while i <= len_:
        res += 2**pow_ * 1 if b[i] == '1' else 0
        i += 1
        pow_ -= 1
    return res

def r(n: int):
    res = int_to_base(n, 2)
    res = res[:-1] + res[1]*2
    return bin_to_int(res)


n = 2
while r(n) <= 92:
    n += 1
else:
    print(n)
