s = '1'+'5'*25
while True:
    if '15' in s:
        s = s.replace('15', '5551', 1)
    elif '1' in s:
        s = s.replace('1', '5', 1)
    else:
        break

print(s.count('5'))
