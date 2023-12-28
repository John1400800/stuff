s = 'деньги'
s_lst = list(s)
link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Отцы и дети.txt"
txt = open(link, 'r').read().lower().split()

cnt = 0
for w in txt:
    if (s in w) or [c for c in w if c.isalpha()]==s_lst:
        cnt += 1

print(cnt)
