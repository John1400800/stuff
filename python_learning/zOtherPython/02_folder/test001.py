class NumberError(Exception):
    pass


class CompositionError(NumberError):
    pass


class FirstSymbolsError(NumberError):
    pass


class BracketsError(NumberError):
    pass


class DashError(NumberError):
    pass


class Number:
    def __init__(self, number: str) -> None:
        self.number = ''.join(number.split())

    def check_consist_of(self):
        ss = '+-()1234567890'
        if any([i not in ss for i in self.number]):
            raise CompositionError(
                'Номер модет состоять из символов +-()1234567890')
        elif len(self.number.replace('+7', '')) != 10:
            raise CompositionError('Длина номера 11 или 10')

    def check_start_symbols(self):
        if not any([self.number.startswith(i) for i in ('+7', '8')]):
            raise FirstSymbolsError(
                'Номер может начинаться символоми +7, или 8'
            )

    def check_brackets(self):
        error_text = '''Допускается наличие в любом месте\n
            одной пары скобок (обязательно пары), например: 8 (905) 3434 341.'''
        brackets = 0
        for s in self.number:
            if s == '(':
                brackets += 1
            elif s == ')':
                brackets -= 1
            if brackets < 0 or brackets > 1:
                raise BracketsError(error_text)
        if brackets != 0:
            raise BracketsError(error_text)

    def check_dashes(self):
        error_text = '''Допускается наличие любого количества знаков -,\n
            только не подряд (--), не в начале и не в конце.\n
            Например, +7 905-34-34-341.'''
        for st in ('+-', '-'):
            if self.number.startswith(st):
                raise DashError(error_text)
        if self.number.endswith('-'):
            raise DashError(error_text)
        if '--' in self.number:
            raise DashError(error_text)

    def convert(self):
        number = self.number.replace('-', '')
        number = number.replace('(', '')
        number = number.replace(')', '')
        if number.startswith('8'):
            number = '+7' + number[1:]
        return number

    def pprint(self):
        print(self.convert())

    def validate_number(self):
        try:
            self.check_start_symbols()
            self.check_brackets()
            self.check_dashes()
            self.number = self.convert()
            self.check_consist_of()
        except (CompositionError, FirstSymbolsError, BracketsError, DashError):
            print('error')
        else:
            self.pprint()


if __name__ == '__main__':
    num = Number('+7495123456')
    num.validate_number()
