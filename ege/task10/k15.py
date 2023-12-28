link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Мертвые души.txt"
s = 'кучер'
f = False
file = open(link, 'r')
cnt = 0
for w in file.read().split():
    if not f:
        w = w.lower()
    if w==s or w.startswith(s) and not(w[len(s)].isalpha()):
        cnt += 1

print(cnt)
