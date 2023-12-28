s = '1'*91

while '2222' in s or '1111' in s:
    if '2222' in s:
        s = s.replace('2222', '11', 1)
    else:
        s = s.replace('1111', '22', 1)

print(s)
