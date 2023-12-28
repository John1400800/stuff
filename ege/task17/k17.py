link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\17\17var17.txt"
lst = [int(n.strip()) for n in open(link, 'r')]
res = []

for i in range(len(lst)-1):
    n1, n2 = lst[i], lst[i+1]
    if all(n<450 for n in (n1, n2)):
        res.append(n1**3+n2**3)

print(len(res), max(res))
        
    
