def lst_to_int(lst: list[int]) -> int:
    
    res = 0
    z = 0
    for  n in lst[::-1]:
        res += n*10**z
        while n>0:
            n //= 10
            z += 1
    return res


def int_to_base(n: int, base: int=10) -> list[int]:
    remainders = []
    while n > 0:
        int_devis = n // base
        remainders.append(n - base*int_devis)
        n = int_devis
    return remainders[::-1]


def r(n: int):
    n: list = int_to_base(n)
    res = sorted((n[0]+n[1], n[1]+n[2]))
    return lst_to_int(res)


"""Автомат получает на вход
трёхзначное число.
По этому числу строится новое
число по следующим правилам.

1.  Складываются первая и вторая,
а также вторая и третья цифры исходного числа.

2.  Полученные два числа записываются друг
за другом в порядке возрастания (без разделителей).

Пример. Исходное число: 348.
Суммы: 3+4 = 7; 4+8 = 12. Результат: 712.

Укажите наименьшее число,
в результате обработки которого автомат
выдаст число 1115.
"""

if __name__ == '__main__':
    n = 100
    while r(n) != 1115:
        n += 1
    else:
        print(n)
