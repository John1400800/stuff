from math import sqrt
link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\17\17var05.txt"
file = open(link, 'r')
lst = [int(el) for el in file.read().split()]
res = []

try:
    for i in range(len(lst)-1):
        n1, n2 = lst[i], lst[i+1]
        if any(n>0 and sqrt(n)%1==0 for n in (n1, n2)):
            res.append(n1+n2)
except:
    print(n1, n2)

print(len(res), max(res))

        
