from string import punctuation


with open(r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Рудин.txt", 'r') as file:
    cnt = 0
    for w in file.read().split():
        if (w == 'Человек' or
            (w.startswith('Человек') and (not w[7].isalpha()))):
            cnt += 1
            

    print(cnt)
