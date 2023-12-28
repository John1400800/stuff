# шаги в пространстве
steps = ((0, -1), (-1, 0), (0, 1), (1, 0))
# поле -1 стенка 0 клетка
field = [[-1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1],
         [0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0],
         [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0],
         [0, -1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
         [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1, 0],
         [0, -1, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0],
         [0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0, 0]]
# позиция старта
start_pos = (0, 3)
# позиция финиша
end_pos = (10, 2)

weight = 1
last_cords = [start_pos]
found = False

# вычисляем вес ячеек
while not found:
    new_cords = []
    for last_x, last_y in last_cords:
        for step_x, step_y in steps:
            new_x, new_y = last_x+step_x, last_y+step_y
            if (0 <= new_x < len(field[0]) and
                0 <= new_y < len(field) and
                field[new_y][new_x] != -1 and
                (new_x, new_y) != start_pos and
                    field[new_y][new_x] == 0):
                field[new_y][new_x] = weight
                new_cords.append((new_x, new_y))
                if (new_x, new_y) == end_pos:
                    found = True
    if len(new_cords) == 0:
        break
    else:
        last_cords = new_cords.copy()
        weight += 1

# строим путь по весу ячеек
path = [end_pos]
if found:
    while path[-1] != start_pos:
        last_x, last_y = path[-1]
        for step_x, step_y in steps:
            new_x, new_y = last_x+step_x, last_y+step_y
            if (0 <= new_x < len(field[0]) and
                0 <= new_y < len(field) and
                    field[new_y][new_x] == field[last_y][last_x]-1):
                path.append((new_x, new_y))
                break
path = path[::-1]
# высвечиваем путь
if found:
    print(*path, sep='\n')

# рисуем дорожку на field
# если пути нет то рисуем звездочку на начале
if found:
    for x, y in path:
        field[y][x] = -2
else:
    field[start_pos[1]][start_pos[0]] = -2


# функция для отрисовки что в ячейке
def print_cell(v):
    '''отбражение стенок и человечка'''
    if v == -1:
        return '#'
    elif v == -2:
        return '*'
    else:
        return ' '


# вывод
print('',
      *['| '+' | '.join([print_cell(v) for v in row]) +
        ' |\n' for row in field], '', sep=f'{"  — "*len(field[0])}\n')

# звездочка это путь # это стенка
