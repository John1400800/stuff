cnt = 0
with open(r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Рудин.txt") as file:
    for w in file.read().split():
        if (w.startswith('Человек') and
            not ''.join(w[7:8]).isalpha()):
            cnt += 1
print(cnt)
