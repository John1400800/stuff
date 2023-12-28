def staples(s: str):
    """Проверяет правельность постановки скобок"""

    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt == -1 or cnt == 2:
            return False
    if cnt == 0:
        return True
    return False


def dash(s: str):
    """Проверяет правильность постановки тире"""

    if '--' in s:
        return False
    elif s[0] == '-' or s[-1] == '-':
        return False
    return True


def in_base(s: str):
    """Проверяет допустимость символов"""

    base = '+-()0123456789'
    return all([symb in base for symb in s])


def start_with(s: str):
    """Провкряет что номер правильно начинается"""
    if s[:2] == '+7' or s[0] == '8':
        return True


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

    # Проверяет правильно ли написан номер
    if not all([in_base(s), start_with(s), staples(s), dash(s)]):
        # если номер не соответствует стандартом возвращяет ошибку
        return 'error'

    # Проверяет длину получившегося номера если длина <> 12 то выдаёт ошибку
    if len(create_num(s)) == 12:
        return create_num(s)
    else:
        return 'error'


a = input()
print(foo(a))
