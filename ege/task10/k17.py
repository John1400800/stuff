s = 'матушка'
ls = list(s)
link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Мертвые души.txt"
txt = open(link, 'r').read().lower().split()
cnt = 0
for w in txt:
    if s==w or s in w and [c for c in w if c.isalpha()]==ls:
        cnt += 1

print(cnt)
