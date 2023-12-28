class Someclass:
    __privat_variable = ['Это приватная переменная:', 0]
    some_variable = ['это обычная переменная:', 0]

    def __init__(self) -> None:
        self.var = 0
        self.__privat_var = 0

    def change(self):
        self.some_variable[1] += 1
        self.__privat_variable[1] += 1
        self.var += 1
        self.__privat_var += 1

    def print_all(self):
        all = (self.some_variable,
               self.__privat_variable,
               self.var,
               self.__privat_var)
        
        print(*all, sep='\n')

print('\n\nПеременная a: ')
a = Someclass()
a.change()
a.change()
a.print_all()

print('\nПеременная b: ')
b = Someclass()
b.print_all()

print(a.var)