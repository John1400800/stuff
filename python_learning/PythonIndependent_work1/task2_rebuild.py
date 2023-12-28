def true_coord(tpl: tuple[float, float], quarter: str, maxx: str) -> bool:
    '''Возвращяет True если точка лежит в четверти quarter\n
    И если линия проведённая к точке tpl[x; y] не больше maxx'''
    if (straight(tpl[0], tpl[1]) <= float(maxx) and
            func_quarter(tpl[0], tpl[1]) == int(quarter)):
        return True
    return False


def func_quarter(x: float, y: float) -> int:
    '''Определяет в какой четверти лежит точка (x, y)'''
    if x == 0 or y == 0:
        return 0
    if x > 0:  # I IV
        if y > 0:  # I
            return 1
        else:  # IV
            return 4
    else:  # II III
        if y > 0:  # II
            return 2
        return 3


def straight(a: float, b: float) -> float:
    '''Вычисление длину между координатами (0, 0) и (a, b)'''
    return (a**2 + b**2)**(1 / 2)


def main_func(name_f1: str, name_f2: str, name_fres: str) -> None:
    with (open(name_f1, 'r') as f_1,
          open(name_f2, 'r') as f_2,
          open(name_fres, 'w') as f_res):
        required_quarter, max_distance = f_1.read().split('\n')
        coords = tuple(
            [(float(line.split()[0]), float(line.split()[1]))
             for line in f_2])

        results = [coord for coord in coords
                   if true_coord(coord, required_quarter, max_distance)]

        results = '\n'.join([f'({tpl[0]}, {tpl[1]})' for tpl in sorted(
            results, key=lambda tpl: straight(tpl[0], tpl[1]), reverse=True)])

        if results:
            f_res.write(results)
        else:
            f_res.write('None')


f1_name = r'Independent_work1\f1.txt'
f2_name = r'Independent_work1\f2.txt'
fres_name = r'Independent_work1\lucky.txt'
main_func(f1_name, f2_name, fres_name)
