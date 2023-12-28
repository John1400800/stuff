link = r"C:\Users\bubik\Downloads\9_8497.txt"
lines = open(link, 'r').read().replace('', '').split('\n')


def valid(l:list):
    return len(set(l))==5 and (l[0]+l[4])*3 >= sum(l[1:4])*2

cnt = 0
for line in lines:
    line = sorted(int(n) for n in line.split())
    if valid(line):
        cnt += 1

print(cnt)
