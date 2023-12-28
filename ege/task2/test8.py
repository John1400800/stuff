def int_to_base(n: int, base=10 )-> str:
    new_n = []
    while n:
        new_n.insert(0, str(n%base))
        n //= base
    return ''.join(new_n)

def bin_to_int(dig: str)-> int:
    res = 0
    mx_idx = pow_ = len(dig) - 1
    idx = 0
    while idx <= mx_idx:
        res += 2**pow_ * 1 if dig[idx] == '1' else 0
        idx += 1
        pow_ -= 1
    return res

##print(bin_to_int(bin(1532)[2:]))
        
def r(n: int):
    res = int_to_base(n - n % 8 + n % 2, 2)
    for _ in range(2):
        res += str(res.count('1')%2)
    return bin_to_int(res)


n = 1
while True:
    if (res := r(n)) > 90:
        print(res)
        break
    n+= 1
