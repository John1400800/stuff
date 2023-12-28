data = []
for s in open("C:\\Users\\bubik\\van_python\\ege\\task18\\18-0.csv"):
    row = list(map(int, s.split(';')))
    data.append(row)

N = len(data)
M = len(data[0])

work = [[0]*M for i in range(N)]

work[0][0] = data[0][0]

for row in range(1, N):
    work[row][0] = work[row-1][0] + data[row][0]

for col in range(1, M):
    work[0][col] = work[0][col-1] + data[0][col]

for row in range(1, N):
    for col in range(1, M):
        work[row][col] = data[row][col] + max((work[row-1][col], work[row][col-1]))

print(work[N-1][M-1])