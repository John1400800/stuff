def return_path(start_pos: tuple[int, int],
                end_pos: tuple[int, int],
                field: list[list[int]]):
    steps = ((0, -1), (-1, 0), (0, 1), (1, 0))
    width, height = len(field[0])-1, len(field)-1
    # проверяет возможно ли дойти до конца
    if ((0 > end_pos[0] or end_pos[0] > width) or
            (0 > end_pos[1] or end_pos[1] > height) or
            start_pos == end_pos or field[end_pos[1]][end_pos[0]] == -1):
        return False
    for step_x, step_y in steps:
        new_x, new_y = start_pos[0]+step_x, start_pos[1]+step_y
        if (new_x, new_y) == end_pos:
            return (start_pos, end_pos)

    fild_weights = [row.copy() for row in field]
    weight_now = 1
    past_cells = [end_pos]
    # итоговый покозатель можно ли дойти до конца
    found = False

    # вес каждой клетки относительно конца пути
    while len(past_cells) and not found:
        new_cells = []
        for past_x, past_y in past_cells:
            for step_x, step_y in steps:
                new_x, new_y = past_x+step_x, past_y+step_y
                if (0 <= new_x <= width and
                    0 <= new_y <= height and
                    fild_weights[new_y][new_x] == 0 and
                        (new_x, new_y) != end_pos):
                    new_cells.append((new_x, new_y))
                    fild_weights[new_y][new_x] = weight_now
                    if (new_x, new_y) == start_pos:
                        found = True
        weight_now += 1
        past_cells = new_cells.copy()

    # кординаты пути если он есть
    if found:
        path = [start_pos]
        while path[-1] != end_pos:
            past_x, past_y = path[-1]
            for step_x, step_y in steps:
                new_x, new_y = past_x+step_x, past_y+step_y
                if (0 <= new_x <= width and
                        0 <= new_y <= height):
                    past_cell, new_cell = (fild_weights[past_y][past_x],
                                           fild_weights[new_y][new_x])
                    if new_cell != -1 and new_cell == past_cell-1:
                        path.append((new_x, new_y))
                        break
        return path
    else:
        return False

if __name__ == '__main__':
    field = [[-1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1],
            [-1, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0],
            [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0],
            [0, -1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
            [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1, 0],
            [0, -1, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0],
            [0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0, 0]]

    print(*return_path((0, 3), (10, 2), field), sep='\n')
    print(*field, sep='\n')
