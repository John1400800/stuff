def is_progression1(w):
##    d = w[1]-w[0]
##    for i in range(1, len(w)):
##        if w[i] != w[0] + d*i:
##            return False
##    return True
    d = set([w[i+1]-w[i]
             for i in range(len(w)-1)])
    return len(d)==1

print(is_progression1([1, 2, 3, 2]))

with open(r'C:\Users\bubik\Desktop\инфа доп. файлы (data)\9\9 варианты 1, 2, 3, 4.csv', 'r') as file:
    cnt = 0
    for l in file:
        l = sorted(map(int, l.rstrip().split(';')))
        if (l[3]**2 > l[0]*l[1]*l[2] or is_progression1(l)):
            cnt += 1

    print(cnt)


