RU = 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю'
ENG = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
COMB = []


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


for r in ENG + RU:
    for i in range(len(r) - 2):
        COMB.append(r[i:i + 3])


def check_password(password: str):
    if not len(password) > 8:
        raise LengthError
    if not (any([s.islower() for s in password]) and
            any([s.isupper() for s in password])):
        raise LetterError
    if not any([s.isdigit() for s in password]):
        raise DigitError
    for el in COMB:
        if el in password:
            raise SequenceError
    return 'ok'


while True:
    try:
        inp = input()
        if inp == 'Ctrl+Break':
            raise KeyboardInterrupt
        print(check_password(inp))
        break
    except (LengthError, LetterError, DigitError, SequenceError) as err:
        print(err.__class__.__name__)
    except KeyboardInterrupt:
        print('Bye-Bye')
        break
