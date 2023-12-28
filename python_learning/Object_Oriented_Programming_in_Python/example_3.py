# Object Oriented Programming in Python
# Наследование классов и super()

class SomePet:
    SOUND = "I dont't know what I say"
    TYPE_OF_ANIMAL = 'SomePet'

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        return (f'I am {self.TYPE_OF_ANIMAL}: "{self.name}"'
                + f' and I am {self.age} years old')

    def speak(self):
        return self.SOUND


class Dog(SomePet):
    SOUND = 'Bark'
    TYPE_OF_ANIMAL = 'Dog'


class Cat(SomePet):
    SOUND = 'Meow'
    TYPE_OF_ANIMAL = 'Cat'

    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.color = color

    def show(self) -> str:
        return super().show() + f' and I am {self.color}'


if __name__ == '__main__':
    some_pet = SomePet('Olli', 3)
    some_dog = Dog('Bill', 5)
    some_cat = Cat('Tim', 3, 'Broun')
    print(some_pet.speak())
    print(some_pet.show())
    print(some_dog.speak())
    print(some_dog.show())
    print(some_cat.speak())
    print(some_cat.show())
