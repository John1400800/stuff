class ArifmErrors(Exception):
    pass

class NotIsDigit(ArifmErrors):
    pass

class NotIsInteger(NotIsDigit):
    pass

class IsZero(ArifmErrors):
    pass


def is_digit(n):
    if n.isdigit():
        return True
    raise NotIsDigit('Это не число')
    


def not_is_zero(n):
    if int(n) == 0:
        raise IsZero('На ноль делить нельзя!')
    else:
        return True


def run(a, b):
    if is_digit(a) and is_digit(b) and not_is_zero(b):
        return int(a) / int(b)


a = input('Введите целое число a: ')
b = input('Введите целое число b: ')

print(run(a, b))