full_res = []
for n in range(1000, 10000):
    n = str(n)
    res = []
    for i in range(3):
        res.append(str(int(n[i])+int(n[i+1])))
    res = sorted(res, key=int)[1:]
    if ''.join(res) == '511':
        full_res.append(n)
print(min(full_res), max(full_res))