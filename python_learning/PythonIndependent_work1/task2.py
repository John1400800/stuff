f1_name = input()
f2_name = input()
# f1_name = r'Independent_work1\f1.txt'
# f2_name = r'Independent_work1\f2.txt'

with (open(f1_name, 'r') as f1,
      open(f2_name, 'r') as f2,
      open(r'Independent_work1\lucky.txt', 'w') as fres):
    # номер координатной четверти
    cord_quart = float(f1.readline().rstrip())
    # максимальное расстояние до подходящих точек
    max_distance = float(f1.readline().rstrip())

    res = []
    for s in f2:
        cord = tuple([float(n) for n in s.split()])

        if '-' in str(cord[0]):  # 2 3
            if '-' in str(cord[1]):  # 3
                my_cord_quart = 3
            else:  # 2
                my_cord_quart = 2
        else:  # 1 4
            if '-' in str(cord[1]):  # 4
                my_cord_quart = 4
            else:  # 1
                my_cord_quart = 1

        if ((cord[0]**2 + cord[1]**2) ** (1 / 2) <= max_distance):
            if my_cord_quart == cord_quart:
                res.append(cord)

    res = sorted(res, key=lambda tpl: (tpl[0]**2 + tpl[1]**2)**(1 / 2))[::-1]
    res = '\n'.join([f'({el[0]}, {el[1]})' for el in res])
    # print(res)
    fres.write(res)
