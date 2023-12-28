# Object Oriented Programming in Python
# @classmethod класс методы, метод всего класса а не единного обьекта этого класса

class Person:
    _number_of_people = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Person.add_people()

    @classmethod
    def num_of_people(cls) -> int:
        return cls._number_of_people

    @classmethod
    def add_people(cls) -> None:
        cls._number_of_people += 1


person1 = Person('Tim')
person2 = Person('Jill')
person3 = Person('Bill')
print(Person.num_of_people())
