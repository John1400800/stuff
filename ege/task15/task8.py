A = range(70, 91)
B = range(40, 61)

def F(x, N):
    return (((not(x in A)) <= (x in B)) and ((not(x in range(N + 1))) <= (x in A)))

cnt = 0
for N in range(1, 10000):
    if cnt > 30:
        break
    cnt = 0
    for x in range(-1000, 1000):
        if F(x, N):
            cnt += 1
        if cnt > 30:
            print(N)
            break