import string

digits = string.digits + string.ascii_uppercase

def int_to_base(n, b):
    if b == 1:
        return
        
    if n == 0:
        return digits[0]
    
    result = []
    while n:
        result.append(digits[int(n % b)])
        n //= b
    return ''.join(result)[::-1]

print(int_to_base(int(input()), int(input())))