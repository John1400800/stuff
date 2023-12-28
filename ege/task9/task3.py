from statistics import mean
#6925

link = r"C:\Users\bubik\Downloads\9_6925.txt"
lines = open(link, 'r').read().replace('', '').split('\n')

def valid(line):
    lst_even, lst_odd = [], []
    for n in line:
        if n%2:
            lst_odd.append(n)
        else:
            lst_even.append(n)
    mean_even = sum(lst_even)/len(lst_even) if lst_even else 0
    mean_odd = sum(lst_odd)/len(lst_odd) if lst_odd else 0
    return (len(set(line))==5) != (abs(mean_even-mean_odd)>50)
    

cnt = 0
for line in lines:
    line = sorted(map(int, line.split()))
    if valid(line): cnt += 1

print(cnt)
