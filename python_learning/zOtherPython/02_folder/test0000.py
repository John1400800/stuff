while True:
    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
    except ValueError:
        print('введите целые a и b')
        continue
        

    try:
        res = a / b
        if a % b == 0:
            res = int(res)
        print(res)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    else:
        break

