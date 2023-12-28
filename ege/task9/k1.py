from string import punctuation


with open(r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Рудин.txt", 'r') as file:
    cnt = 0
    for line in file:
        for w in line.split():
            if (('Человек' in w) and
                ([sym for sym in w
                  if sym not in punctuation] == list('Человек'))):
                cnt += 1

    print(cnt)
