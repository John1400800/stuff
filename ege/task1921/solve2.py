def moves(s):
    a, b = s
    return (a+1, b), (a*3, b), (a, b+1), (a, b*3)


def f(s, n, w):
    if sum(s) >= 68:
        return n%2 == w%2
    if n == w:
        return 0
    h = []
    for m in moves(s):
        h.append(f(m, n+1, w))
    
    # if (n+1)%2 == w%2:
    #     return any(h)
    # return all(h)
    return any(h)


for s in range(1, 61+1):
    m = 2
    if f((6, s), 0, m):
        print(s)
        break
