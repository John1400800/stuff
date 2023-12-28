s = '1'+'2'*70
while True:
    if '12' in s:
        s = s.replace('12', '221', 1)
    elif '1' in s:
        s = s.replace('1', '2', 1)
    else:
        break

print(s.count('2'))
