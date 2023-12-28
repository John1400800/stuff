# Object Oriented Programming in Python
# @staticmethod статик методы, статические методы (ничего не меняют!)

class SomeClass:
    @staticmethod
    def add5(n: int) -> int:
        return n + 5

    @staticmethod
    def add6(n: int) -> int:
        return n + 6

    @staticmethod
    def add_some_x(n: int, x: int) -> int:
        return n + x

    @staticmethod
    def print_run() -> None:
        print('run')


print(SomeClass.add_some_x(1, 7))
SomeClass.print_run()
