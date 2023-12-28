res_set = set()
for n in range(500, 5001):
    res_set.add(n - int(bin(n)[3:], 2))
print(len(res_set))