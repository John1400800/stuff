with open(r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Тарас Бульба.txt", 'r') as file:
    s = 'сын'
    cnt = 0
    for w in file.read().split():
        if (w==s or
            (w.startswith(s) and
              (not(w[len(s)].isalpha())))):
            cnt += 1

    print(cnt)
