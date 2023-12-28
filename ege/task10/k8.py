from string import ascii_letters

cnt = 0
s = 'брат'
link = r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Отцы и дети.txt"
text = open(link).read()

for i in set(text):
    if not i.isalpha():
        text = text.replace(i, ' ')

for w in text.split():
    if w.lower()==s:
        cnt += 1

print(cnt)
