from string import digits, ascii_lowercase


# способ 1
for x in digits+ascii_lowercase:
    n = int(f'2{x}84', 19)+int(f'2b3{x}', 16)
    if n % 88 == 0:
        print(n // 88)
        break

# способ 2
for x in range(0, 16):
    a1 = 2*19**3 + x*19**2 + 8*19 + 4
    a2 = 2*16**3 + 11*16**2 + 3*16 + x
##              >  11  <
##print((digits+ascii_lowercase).find('b'))
    r = a1 + a2
    if not r % 88:
        print(r // 88)
        break


