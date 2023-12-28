from itertools import product


'''
Леся составляет слова, содержащие
ровно три буквы М, из букв Ч, О, А, Н, И, М, Е.
Слово может иметь длину от 4 до 6 букв.
Сколько слов может составить Леся?
'''
alpha = 'чоаниме'
def valid(w):
    return ''.join(w).count('м')==3

cnt = 0
for n in range(4, 7):
    for w in product(alpha, repeat=n):
        if valid(w): cnt += 1

print(cnt)
