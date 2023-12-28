def foo(n: int):
    n_s = str(n)
    return int(''.join(sorted(
        [str(int(n_s[i])+int(n_s[i+1]))
            for i in range(0, 3, 2)],
        key=int, reverse=True)))


for i in range(1000, 10000):
    if foo(i) == 1311:
        print(i)
        break
