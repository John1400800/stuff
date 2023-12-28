from itertools import product


cnt = 0
for w in product('0123', repeat=3):
    if w[0]!='0' and ord(w[0])>=ord(w[1])>=ord(w[2]):
        cnt += 1

print(cnt)
