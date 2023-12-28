OPERATORS = []
OPERATORS.extend(range(910, 920))  # Коды МТС — 910..919
OPERATORS.extend(range(980, 990))  # Коды МТС — 980..989
OPERATORS.extend(range(920, 940))  # Коды МегаФона — 920..939
OPERATORS.extend(range(902, 907))  # Коды Билайна — 902..906
OPERATORS.extend(range(960, 970))  # Коды Билайна — 960..969


class NumError(Exception):
    pass


class IncorrectSymbol(NumError):
    pass


class InvalidStaples(NumError):
    pass


class InvalidDash(NumError):
    pass


class IncorectStart(NumError):
    pass


class ErrorLen(NumError):
    pass


class NoneOperator(NumError):
    pass


def staples(s: str):
    """Проверяет правельность постановки скобок"""

    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt == -1 or cnt == 2:
            raise InvalidStaples('неправильные скобки')
    if cnt == 0:
        return True
    raise InvalidStaples('неправильные скобки')


def dash(s: str):
    """Проверяет правильность постановки тире"""

    if '--' in s:
        raise InvalidDash('неправильные тире')
    elif s[0] == '-' or s[-1] == '-':
        raise InvalidDash('неправильные тире')
    return True


def in_base(s: str):
    """Проверяет допустимость символов"""

    base = '+-()0123456789'
    if all([symb in base for symb in s]):
        return True
    raise IncorrectSymbol('неправильные символы')


def start_with(s: str):
    """Провкряет что номер правильно начинается"""
    if s[0] == '+':
        if s.startswith('+7'):
            return True
        elif s[:4] == '+359' or s[:3] == '+55' or s[:2] == '+1':
            return False
        else:
            raise IncorectStart('нету такого кода страны')
    else:
        raise IncorrectSymbol('Неправильное начало')


def operator_code(s: str):
    """Проверяет существование оператора"""
    code = s[2:5]
    if int(code) in OPERATORS:
        return True
    raise NoneOperator('оператор не существует')


def create_num(s: str):
    """Создаёт номер в числовом вид,\n
    Переделывает начало номера из вида 8... в +7... """

    base = '+0123456789'
    s = ''.join([el for el in s if el in base])
    if s[0] == '8':
        s = '+7' + s[1:]
    return s


def foo(s: str):
    s = ''.join(s.split())  # Уберает пробельные символы

    try:
        in_base(s)
        staples(s)
        dash(s)

        start_with(create_num(s))
        if len(create_num(s)) != 12:
            raise ErrorLen('неверное количество цифр')

        if start_with(create_num(s)):
            operator_code(create_num(s))

    except (InvalidStaples, InvalidDash,
            IncorrectSymbol):
        return 'неверный формат'
    except IncorectStart:
        return 'не определяется код страны'
    except ErrorLen:
        return 'неверное количество цифр'
    except NoneOperator:
        return 'не определяется оператор сотовой связи'
    else:
        return create_num(s)


a = input()
print(foo(a))

# print(foo(' 864357))4  92	8  2'))
# print(foo('8  114356 30'))
# print(foo('+79700830356'))
# print(foo('8(916)    12 4 32-6 7'))
