# Менеджер контекста
def foo(op: str):
    if op == '+':
        return lambda a, b: a + b
    elif op == '-':
        return lambda a, b: a - b
    elif op == '*':
        return lambda a, b: a * b
    elif op == '/':
        return lambda a, b: a / b if b != 0 else 'На ноль делить нельзя'
    else:
        return lambda a, b: 'Ошибка'


with open(r'les8_PyQt5_working_with_files\theory\somefile.txt',
          mode='w', encoding='utf-8') as file:

    num1 = input()
    file.write(f'{num1} ')

    operator = input()
    file.write(f'{operator} ')

    num2 = input()
    file.write(f'{num2} = ')

    if all([el.isdigit() for el in (num1, num2)]):
        res = str(foo(operator)(int(num1), int(num2)))
    else:
        res = 'Ошибка'

    file.write(f'{res}')
