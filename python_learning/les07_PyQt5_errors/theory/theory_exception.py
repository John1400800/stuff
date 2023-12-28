# Если нужен доступ к исключению как к объекту, пригодится такая конструкция:

class MyError(ValueError):
    pass

try:
    a = int(input("Введите целое число: "))
    print(a + 10)
except MyError as er:
    print("Неверное число")
    print(er)
    print(dir(er))
