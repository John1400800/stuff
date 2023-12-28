data = {}
for row in [s.split(',') for s in open(r"path_to_file.csv")]:
    data[int(row[0])] = [
        int(row[1]),
        [int(i) for i in row[2].split(';')]
    ]

data = dict(
    sorted(data.items(), key=lambda x: x[1][1][-1]))

res = {}
for idb, [time, ida] in data.items():
    if set(ida) == {0}:
        res[idb] = time
        continue
    res[idb] = time + max(map(lambda x: max(data[x][0], res[x]), ida))

print(max(res.values()))