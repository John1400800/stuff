link = r"C:\Users\bubik\Downloads\9.csv"
lines = open(link).readlines()


def valid(line):
    setline = set(line)
    for n in setline:
        nr = setline-{n}
        if line.count(n)==3 and len(nr)==4:
            if sum(nr)/len(nr)<=n:
                return True
    return False
    
cnt = 0
for line in lines:
    line = sorted(map(int, line.replace('"', '').split(',')))
    if valid(line):
        cnt += 1

print(cnt)
