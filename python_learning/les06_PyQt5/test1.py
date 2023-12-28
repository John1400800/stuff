from random import choice

symb = '0'

res = '0'
cash_num = ''
num = '0'
operator = ''


def number(num):
    global res

    if num == '0' and res != '0':
        res += '0'
    elif num != '0':
        if '.' not in res and num == '.':
            res += num
        elif num != '.':
            if res != '0':
                res += num
            else:
                res = num


def kalkulate(inp):
    global res, cash_num, num, operator
    if inp in '0123456789.':
        number(inp)
    else:
        if inp == '+':
            cash_num = float(res)
            operator = '+'
            return lambda: (
                int(n) if '.0' == str(n := (cash_num + num))[-2:] else n)
        elif inp == '-':
            cash_num = float(res)
            operator = '-'
            return lambda: float(cash_num - num)
        elif inp == '*':
            cash_num = float(res)
            operator = '+'
            return lambda: float(cash_num * num)
        elif inp == '':
            cash_num = float(res)
            operator = '+'
            return lambda: float(cash_num  num)
        elif inp == '=':
            num = float(res)
            res = kalkulate(operator)()


while True:
    print(f'Дисплэй: {res}')
    if symb in '+-*':
        res = '0'
    #  symb = choice(list('0123456789.+-*='))
    symb = input()
    #  print(f'Ввод: {symb}', end='\n')
    kalkulate(symb)
