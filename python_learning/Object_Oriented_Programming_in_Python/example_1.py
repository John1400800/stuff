# Object Oriented Programming in Python
# Создание класса

class Dog(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def set_age(self, new_age: int) -> None:
        self.age = new_age


# d1 = Dog('Tom', 2)
# print(d1.get_name(), d1.get_age())
# d1.set_age(12)
# print(d1.get_age())
