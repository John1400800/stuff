from string import punctuation
PEOPLE = list('Человек')

file = open(r"C:\Users\bubik\Desktop\инфа доп. файлы (data)\10\Рудин.txt", 'r')
try:
    cnt = 0
    for line in file:
        for word in line.split():
            if ('Человек' in word and
                PEOPLE == [let for let in word
                           if let not in punctuation]):
                cnt += 1
    print(cnt)
finally:
    file.close()
