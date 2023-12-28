
# Работа с файлами
file = open(r'C:\Users\bubik\van_python\les8_PyQt5_working_with_files\theory\somefile.txt', encoding='utf-8')

for row in file:
    for letter in row:
        print(letter)

file.seek(0)

lst = file.readlines()
print(lst)