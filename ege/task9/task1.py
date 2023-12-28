def valid(line: list[int]) -> bool:
    if len(set(line)) < len(line):
        return False
    line.sort()
    if 3*(line[0]+line[-1]) > 2*sum(line[1:4]):
        return False
    return True


with open('09_1.txt', 'r') as file:
    cnt = 0
    for line in file:
        if line.strip() != '':
            line = [int(el)
                    for el in line.replace('', '').lstrip().split()]
            if valid(line): cnt += 1
    print(cnt)
