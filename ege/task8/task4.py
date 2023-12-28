from itertools import product


alpha = '012345678'
cnt = 0
for w in product(alpha, repeat=5):
    if w[0] != 0 and (all([ord(w[i]) > ord(w[i+1])
            for i in range(len(w)-1)])):
        cnt += 1
print(cnt)
