link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\17\17var08.txt"
lst = [int(el) for el in open(link, 'r')]
##print(lst)

pairs = []
for i in range(len(lst)-1):
    if lst[i]%5==0 and lst[i+1]%5==0:
        pairs += [lst[i]+lst[i+1]]

print(len(pairs), min(pairs))
