from string import punctuation

search = 'заря' # <-- слово кот. надо найти
lst_search = list(search)

cnt = 0
with open(r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Отцы и дети.txt", 'r') as file:
    for line in file:
        for w in line.split():
            w = w.lower()
            if (search in w and
                [s for s in w.lower()
                 if s not in punctuation] == lst_search):
                cnt += 1

print(cnt)
