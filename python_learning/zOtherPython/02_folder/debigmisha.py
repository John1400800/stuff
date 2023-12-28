class NumberError(Exception):
    pass


class NumberCompositionError(NumberError):
    pass


class NumberFirstSymbolsError(NumberError):
    pass


class NumberBracketsError(NumberError):
    pass


class NumberDashError(NumberError):
    pass


class NumberLenghtError(NumberError):
    pass


class Number:
    def __init__(self, number: str) -> None:
        self.number = ''.join(number.split())

    def check_number(self):
        ss = '+-()1234567890'
        if any([i not in ss for i in self.number]):
            raise NumberCompositionError(
                'Номер может состоять из символов +-()1234567890')

        if not any([self.number.startswith(i) for i in ('+7', '8')]):
            raise NumberFirstSymbolsError(
                'Номер может начинаться символоми +7, или 8'
            )

        error_text = '''Допускается наличие в любом месте\nодной
        пары скобок (обязательно пары), например: 8 (905) 3434 341.'''
        brackets = 0
        for s in self.number:
            if s == '(':
                brackets += 1
            elif s == ')':
                brackets -= 1
            if brackets < 0 or brackets > 1:
                raise NumberBracketsError(error_text)
        if brackets != 0:
            raise NumberBracketsError(error_text)

        error_text = '''Допускается наличие любого количества знаков -,\n
            только не подряд (--), не в начале и не в конце.\n
            Например, +7 905-34-34-341.'''
        for st in ('+-', '-'):
            if self.number.startswith(st):
                raise NumberDashError(error_text)
        if self.number.endswith('-'):
            raise NumberDashError(error_text)
        if '--' in self.number:
            raise NumberDashError(error_text)

    def convert(self):
        number = self.number.replace('-', '')
        number = number.replace('(', '').replace(')', '')
        if number.startswith('8'):
            number = '+7' + number[1:]
        if len(number.replace('+7', '')) != 10:
            raise NumberLenghtError('Длина номера 11 или 12')
        return number

    def validate_number(self):
        try:
            self.check_number()
            print(self.convert())
        except (
                NumberCompositionError,
                NumberFirstSymbolsError,
                NumberBracketsError,
                NumberDashError,
                NumberLenghError,
        ):
            print('error')


if __name__ == '__main__':
    num = Number('+7(902)123-4567')
    num.validate_number()